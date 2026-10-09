"""Measure stocktitan's rate limit: how many requests pass at a given spacing, and how long a block lasts.

Usage (from the workspace root, e.g. E:/options_scanner/agents/earnings_researcher):
    python analysis/helpers/stocktitan_probe.py --spacing 20 --cycles 3
    python analysis/helpers/stocktitan_probe.py --spacing 10 --cycles 2 --probe-schedule 30,60,120,240,300

Each cycle has two phases, using the same curl shape and headers as spine.py:
  BURST    one request every --spacing seconds until the first non-200 (or --max-burst requests).
           Records how many passed before the block.
  RECOVERY after the block, one request at each interval of --probe-schedule (seconds; the last
           interval repeats) until a request returns a full page again, or --max-recovery seconds pass.
           Records the time from the first 429 to the first 200 (a bracket, not an exact moment: the
           true recovery is somewhere between the last failed probe and the first good one).
The next cycle's BURST then starts immediately, so its pass-count shows whether the budget fully
refilled on recovery or only partly.

SIDE PROBES (cycle 1 only, once, right after the first block): a few one-off requests that show
what the block covers: the site root, robots.txt, a listing page with spine's headers, the same
listing page with bare curl headers (the 403-vs-429 question), and an article page. They are
logged with phase "side". They add a handful of requests during a block, which is why they run in
one cycle only.

Every request is appended to --log (CSV) as it happens, so a Ctrl+C or a crash loses nothing.
Run it when no research session is using stocktitan: the probes deliberately provoke blocks.
Caveat: probing during a block may itself extend it. To test that, run once with a sparse schedule
(--probe-schedule 300) and once with a dense one (--probe-schedule 30), and compare recovery times.
"""
import argparse, csv, itertools, os, subprocess, sys, tempfile, time
from datetime import datetime

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
# Rotate through real symbol pages so each request resembles a spine run (and isn't one cached URL).
SYMBOLS = ["AAPL", "MSFT", "KO", "PEP", "XOM", "CVX", "JNJ", "PFE", "WMT", "HD", "MCD", "NKE",
           "DIS", "INTC", "CSCO", "ORCL", "ADBE", "CRM", "BA", "CAT", "GS", "MS", "V", "MA"]


SIDE = [
    ("root", "https://www.stocktitan.net/", False),
    ("robots.txt", "https://www.stocktitan.net/robots.txt", False),
    ("listing-spine-headers", "https://www.stocktitan.net/news/AAPL/", False),
    ("listing-bare-curl", "https://www.stocktitan.net/news/AAPL/", True),
    ("article", "https://www.stocktitan.net/news/FAF/first-american-financial-announces-third-quarter-2026-earnings-uyn3yoxy52mx.html", False),
]


def fetch(symbol, url=None, bare=False):
    """One request. Returns (http_code, bytes, retry_after, ok, curl_err).
    url overrides the listing page; bare=True drops spine's headers (plain curl).
    http_code 000 means curl got no HTTP response (connection refused/reset/timeout, DNS, local
    network); curl_err then holds curl's exit code and message so it can be told apart from a 429."""
    url = url or f"https://www.stocktitan.net/news/{symbol}/"
    with tempfile.TemporaryDirectory() as d:
        body, hdr = os.path.join(d, "b.html"), os.path.join(d, "h.txt")
        cmd = ["curl", "-s", "-m", "40", "-D", hdr, url, "-o", body,
               "-w", "%{http_code}|%{exitcode}|%{errormsg}"]
        if not bare:
            cmd[2:2] = ["--compressed", "-A", UA, "-H", "Accept: text/html",
                        "-H", "Accept-Language: en-US,en;q=0.9"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        parts = (r.stdout.strip() or "000||").split("|", 2) + ["", ""]
        code = parts[0] or "000"
        err = f"exit{parts[1]}:{parts[2]}".strip(":") if parts[1] not in ("", "0") else ""
        text = open(body, encoding="utf-8", errors="replace").read() if os.path.exists(body) else ""
        headers = open(hdr, encoding="utf-8", errors="replace").read() if os.path.exists(hdr) else ""
    retry = next((l.split(":", 1)[1].strip() for l in headers.splitlines()
                  if l.lower().startswith("retry-after")), "")
    ok = code == "200" and len(text) >= (5000 if not url.endswith("robots.txt") else 1)         and "Too Many Requests" not in text
    return code, len(text), retry, ok, err


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spacing", type=float, default=20, help="seconds between burst requests")
    ap.add_argument("--cycles", type=int, default=2)
    ap.add_argument("--max-burst", type=int, default=60, help="stop a burst after this many passes")
    ap.add_argument("--probe-schedule", default="30,60,120,180,300",
                    help="comma list of seconds between recovery probes; the last value repeats")
    ap.add_argument("--max-recovery", type=int, default=3600, help="give up after this many seconds")
    ap.add_argument("--log", default="inbox/fetch/stocktitan_probe_log_v2.csv")
    a = ap.parse_args()
    schedule = [float(x) for x in a.probe_schedule.split(",")]
    os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
    new = not os.path.exists(a.log)
    f = open(a.log, "a", newline="", encoding="utf-8")
    w = csv.writer(f)
    if new:
        w.writerow(["time", "cycle", "phase", "n", "symbol", "http", "bytes", "retry_after", "ok", "curl_err"])
    syms = itertools.cycle(SYMBOLS)
    summary = []

    def verdict(code, ok, err):
        """ok / BLOCKED (an HTTP answer that is not a full page: 429, 403...) / NETFAIL (no HTTP answer at all)."""
        return "ok" if ok else ("NETFAIL" if code == "000" else "BLOCKED")

    def control(cycle, phase):
        """Fetch a different site. True = our own network works, so a stocktitan failure is stocktitan's doing."""
        code, size, _, ok, err = fetch("", url="https://www.google.com/robots.txt")
        w.writerow([datetime.now().strftime("%H:%M:%S"), cycle, "control", phase, "google", code, size, "", int(ok), err])
        f.flush()
        print(f"[{datetime.now():%H:%M:%S}] control google robots.txt http={code} "
              f"{'ok' if ok else 'FAILED (local network down?) ' + err}", flush=True)
        return ok

    def wait_for_network(cycle, max_wait=1800):
        """Local outage: poll the control every 15s until it works. Returns outage length in seconds."""
        t0 = time.time()
        print(f"[{datetime.now():%H:%M:%S}] LOCAL NETWORK DOWN - pausing the test until it is back", flush=True)
        while time.time() - t0 < max_wait:
            time.sleep(15)
            if control(cycle, "outage-poll"):
                break
        secs = time.time() - t0
        print(f"[{datetime.now():%H:%M:%S}] network back after {secs:.0f}s (request retried, not counted)", flush=True)
        return secs

    def req(cycle, phase, n):
        """One counted request. A no-response failure with a dead control is a local outage: wait it out and
        retry; it is NOT recorded as a stocktitan block. No-response with a live control IS a stocktitan-side drop."""
        s = next(syms)
        for attempt in range(5):
            code, size, retry, ok, err = fetch(s)
            w.writerow([datetime.now().strftime("%H:%M:%S"), cycle, phase, n, s, code, size, retry, int(ok), err])
            f.flush()
            print(f"[{datetime.now():%H:%M:%S}] c{cycle} {phase:8s} #{n:<3d} {s:5s} http={code} bytes={size}"
                  f"{' retry-after=' + retry if retry else ''}{' curl=' + err if err else ''} {verdict(code, ok, err)}", flush=True)
            if code != "000":
                return ok
            if control(cycle, phase):
                print("  -> control works, so this is a stocktitan-side connection drop (counts as a block)", flush=True)
                return False
            wait_for_network(cycle)
        return False

    for c in range(1, a.cycles + 1):
        passed, n = 0, 0
        t_burst = time.time()
        while n < a.max_burst:
            n += 1
            if not req(c, "burst", n):
                break
            passed += 1
            time.sleep(a.spacing)
        else:
            summary.append((c, passed, None, "no block within max-burst"))
            print(f"cycle {c}: {passed} passed, never blocked at {a.spacing}s spacing", flush=True)
            continue
        t_block = time.time()
        if c == 1:
            print("side probes (what does the block cover?)", flush=True)
            for label, url, bare in SIDE:
                code, size, retry, ok, err = fetch("", url=url, bare=bare)
                w.writerow([datetime.now().strftime("%H:%M:%S"), c, "side", label, "", code, size, retry, int(ok), err])
                f.flush()
                print(f"[{datetime.now():%H:%M:%S}] side {label:22s} http={code} bytes={size}"
                      f"{' retry-after=' + retry if retry else ''}{' curl=' + err if err else ''} {verdict(code, ok, err)}", flush=True)
                time.sleep(5)
        print(f"cycle {c}: blocked after {passed} passes in {t_block - t_burst:.0f}s "
              f"(spacing {a.spacing}s). Probing recovery...", flush=True)
        probes, recovered, last_fail = 0, None, 0.0
        while time.time() - t_block < a.max_recovery:
            wait = schedule[min(probes, len(schedule) - 1)]
            time.sleep(wait)
            probes += 1
            if req(c, "recovery", probes):
                recovered = time.time() - t_block
                break
            last_fail = time.time() - t_block
        if recovered is None:
            summary.append((c, passed, None, f"not recovered after {a.max_recovery}s"))
            print(f"cycle {c}: still blocked after {a.max_recovery}s; stopping.", flush=True)
            break
        summary.append((c, passed, recovered, f"recovered between {last_fail:.0f}s and {recovered:.0f}s"))
        print(f"cycle {c}: recovered; first 200 at {recovered:.0f}s after the block "
              f"(last failure at {last_fail:.0f}s).", flush=True)

    print("\n== SUMMARY ==")
    for c, passed, rec, note in summary:
        print(f"cycle {c}: {passed} requests passed at {a.spacing}s spacing; {note}")
    print(f"log: {a.log}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted; partial results are in the log.")
        sys.exit(1)
