"""stocktitan news spine: last 10 headlines per symbol from the page's JSON-LD.

Usage (from the workspace root):
    python analysis/helpers/spine.py SYM [SYM ...]             # waits out the rate-limit window as needed
    python analysis/helpers/spine.py --no-wait SYM [SYM ...]   # stop when the window's budget is spent

Pass the most urgent symbols first. See memory/reference_stocktitan_jsonld_discovery.md for the request
shape and its traps. Promoted from inbox/fetch/spine.py (10-01 session) at the 2026-10-04 maintenance;
rate-limit policy rewritten 2026-10-09 after the experiment below.

RATE LIMIT (measured 2026-10-09; analysis/stocktitan_ratelimit_test_plan.md has the full log)
  Observed, from this machine's IP, with this request shape (browser UA, listing pages):
  * Blocked responses are HTTP 429 with a `Retry-After` header. Body ~2.5 KB "Too Many Requests".
    The block covers the whole site (root, listing pages, article pages); only /robots.txt stayed
    reachable. A bare `curl` with no User-Agent gets 403 even when not blocked (header filtering).
  * 4 of 4 blocks (runs 1 and 3) fit one rule: a window opens at the first request and lasts 300 s
    (window-open to block-end was 299-300 s every time); the 11th request inside it is refused.
    Cold bursts passed 10 requests; cycles that opened with a recovery probe passed 9 more (the probe
    was request 1). `Retry-After` counts down to that window end, and the first 200 came back inside
    the bracket it predicted every time.
  * It is a count per window, not a rate: 10 requests passed at 20 s spacing and at 10 s spacing,
    then the 11th was refused. Probing during a block did not extend it.
  * 40 requests at 40 s spacing (about 8 per 300 s) all returned 200, over 26 minutes (run 4c).
  Inferred (not separately tested): the limit is per client IP (WebFetch, which egresses elsewhere,
  read a listing page while curl was blocked; one fetch); the window is fixed, not sliding.
  Run 5 (this file's own policy, below) is the test of the rule; its result is in the plan file.

POLICY
  * At most BUDGET (9) requests per WINDOW (300 s) + PAD, one below the observed limit of 10 as margin
    for any other traffic from this IP. The window state is saved in inbox/fetch/.stocktitan_window.json,
    so separate spine invocations in one session share the budget.
  * When the budget is spent: sleep until the window has closed (unless --no-wait, which lists the
    unread symbols and the seconds to wait). 9 requests per ~305 s is about 34 s per symbol.
    A foreground Bash call is capped at 10 minutes (~17 symbols); for a longer list use
    run_in_background and read the output file.
  * A 429 is never an absence: sleep Retry-After + 2 s and retry the same symbol (twice at most),
    then flag it UNREAD.
  * curl got no HTTP answer (http 000): ask a different site (google robots.txt). If that also fails
    the local network is down, so wait for it and retry; if it works, stocktitan dropped us, so back
    off 60 s once and retry before flagging UNREAD.
"""
import json, os, re, subprocess, sys, tempfile, time
from datetime import date

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
PAT = re.compile(r'"headline":\s*"([^"]+)",\s*"url":\s*"([^"]+)",\s*"datePublished":\s*"([^"]+)"')
KEY = re.compile(r'(?i)quarter|Q[1-4]|earnings|results|call|webcast|announce')
WINDOW, BUDGET, PAD, SPACING = 300, 9, 5, 5
STATE = "inbox/fetch/.stocktitan_window.json"

since = date.today().replace(day=1)
since = since.replace(month=since.month - 1) if since.month > 1 else since.replace(year=since.year - 1, month=12)


def load_state():
    try:
        return json.load(open(STATE))
    except Exception:
        return None


def save_state(st):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(st, open(STATE, "w"))


def take_slot(no_wait):
    """Reserve one request in the current window. Returns (ok, seconds_to_wait_if_not_ok)."""
    st = load_state()
    now = time.time()
    if st and now >= st["start"] + WINDOW + PAD:
        st = None
    if st and st["count"] >= BUDGET:
        wait = st["start"] + WINDOW + PAD - now
        if no_wait:
            return False, wait
        print(f"  (budget {BUDGET} per {WINDOW}s spent; sleeping {wait:.0f}s for the window to close)", flush=True)
        time.sleep(max(wait, 0))
        st = None
    if not st:
        st = {"start": time.time(), "count": 0}
    st["count"] += 1
    save_state(st)
    return True, 0


def fetch(s):
    """One request. Returns (http, text, retry_after_seconds_or_None, curl_exit)."""
    out = f"inbox/fetch/st_{s}.html"
    with tempfile.TemporaryDirectory() as d:
        hdr = os.path.join(d, "h.txt")
        r = subprocess.run(["curl", "-s", "--compressed", "-m", "40", "-A", UA,
                            "-H", "Accept: text/html", "-H", "Accept-Language: en-US,en;q=0.9",
                            "-D", hdr, f"https://www.stocktitan.net/news/{s}/", "-o", out,
                            "-w", "%{http_code}|%{exitcode}"], capture_output=True, text=True)
        headers = open(hdr, encoding="utf-8", errors="replace").read() if os.path.exists(hdr) else ""
    code, _, ex = (r.stdout.strip() or "000|-1").partition("|")
    text = open(out, encoding="utf-8", errors="replace").read() if os.path.exists(out) else ""
    ra = None
    for line in headers.splitlines():
        if line.lower().startswith("retry-after"):
            try:
                ra = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
    return code, text, ra, ex


def network_up():
    r = subprocess.run(["curl", "-s", "-m", "15", "-o", os.devnull, "-w", "%{http_code}",
                        "https://www.google.com/robots.txt"], capture_output=True, text=True)
    return r.stdout.strip() == "200"


def read_symbol(s, no_wait):
    """Returns (code, text, note). code None = budget spent under --no-wait (note = seconds to wait)."""
    drop_retried = False
    for attempt in range(6):
        ok, wait = take_slot(no_wait)
        if not ok:
            return None, "", f"{wait:.0f}"
        code, text, ra, ex = fetch(s)
        if code == "200" and len(text) >= 5000 and "Too Many Requests" not in text:
            return code, text, ""
        if code == "429" and ra is not None and attempt < 2:
            print(f"  429 on {s}: sleeping Retry-After {ra}+2 s, then retrying", flush=True)
            if no_wait:
                return code, text, f"429, Retry-After {ra}s"
            time.sleep(ra + 2)
            save_state(None)  # the server's window ended; the retry opens a new one
            continue
        if code == "000":
            if not network_up():
                print("  local network down: waiting for it (15 s polls, 10 min cap)", flush=True)
                t0 = time.time()
                while time.time() - t0 < 600 and not network_up():
                    time.sleep(15)
                continue
            if not drop_retried:
                drop_retried = True
                print(f"  stocktitan gave no answer (curl exit {ex}) but the network is up: backing off 60 s", flush=True)
                time.sleep(60)
                continue
        return code, text, ""
    return code, text, ""


def main():
    args = sys.argv[1:]
    no_wait = "--no-wait" in args
    syms = [a for a in args if not a.startswith("--")]
    unread, first = [], True
    for s in syms:
        if not first:
            time.sleep(SPACING)
        first = False
        code, t, note = read_symbol(s, no_wait)
        if code is None:
            unread.append(s)
            continue
        items = PAT.findall(t)
        flag = ""
        if code != "200" or len(t) < 5000 or "Too Many Requests" in t:
            flag = "  <-- UNREAD (429/blocked): not an absence"
            unread.append(s)
        elif not items:
            flag = "  <-- full page but 0 items: check the regex before reading absence"
        print(f"== {s} http={code} bytes={len(t)} items={len(items)}{flag}", flush=True)
        for h, u, d in items:
            if d[:10] >= since.isoformat() and KEY.search(h):
                print("  ", d[:16], h[:110], "|", u)
    if unread:
        st = load_state()
        wait = f" The window closes in ~{st['start'] + WINDOW + PAD - time.time():.0f}s." if st else ""
        print(f"\nUNREAD ({len(unread)}): {' '.join(unread)}.{wait} Re-run these; 'unread' is not 'absent'.")


if __name__ == "__main__":
    main()
