"""Background poll for PVH's Q2-2026 advance PR, 2026-08-17 (Monday).

Why today: PVH's advance PR is 7 days past due for the DB's 08-25 release, and
today is exactly when it would be due for the live 09-01 alternative (15d lead).
Both observed advance PRs landed on a MONDAY MORNING -- Q1-26 at 09:00:00 ET
(feed pubDate), Q2-25 on Monday 2025-08-11 via BusinessWire. Today is Monday and
this session starts at 07:2x, before that window.

Same shape as the 2026-08-04 BR confirm: polling a known publication minute is a
valid confirmation route when the channel is deterministic. Here the channel is
the formulaic slug (404 => not issued) plus the IR feed.

Writes every observation to analysis/pvh_poll_20260817.out so tomorrow's session
can read the outcome even if this session has ended. Stops on first hit or at
09:30 ET.
"""
import re, time, urllib.error, urllib.request
from datetime import datetime, timedelta, timezone

ET = timezone(timedelta(hours=-4))  # EDT
STOP = datetime.now(ET).replace(hour=9, minute=30, second=0, microsecond=0)
OUT = r"E:\options_scanner\agents\earnings_researcher\analysis\pvh_poll_20260817.out"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

SLUG = ("https://www.pvh.com/news/press-releases/pvh-corp-to-host-conference-"
        "call-to-discuss-second-quarter-2026-earnings-results")
FEED = "https://pvh.gcs-web.com/rss/news-releases.xml"
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)


def say(msg):
    line = f"[{datetime.now(ET):%Y-%m-%d %H:%M:%S} ET] {msg}"
    print(line, flush=True)
    with open(OUT, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


say("poll start -- watching PVH Q2-2026 advance PR (slug + IR feed) until 09:30 ET")
while datetime.now(ET) < STOP:
    code, _ = get(SLUG)
    if code == 200:
        say("*** HIT: slug returns 200 -- PVH Q2-2026 advance PR IS ISSUED ***")
        say(SLUG)
        break

    code_f, body = get(FEED)
    newest = "?"
    hit = False
    if code_f == 200:
        items = ITEM_RE.findall(body)
        if items:
            t = TITLE_RE.search(items[0])
            d = DATE_RE.search(items[0])
            newest = f"{d.group(1).strip() if d else '?'} | {t.group(1).strip() if t else '?'}"
        for it in items[:5]:
            t = TITLE_RE.search(it)
            title = t.group(1).strip() if t else ""
            if re.search(r"second quarter 2026|conference call", title, re.I):
                say(f"*** HIT in feed: {title}")
                hit = True
    say(f"slug={code}  feed={code_f}  newest: {newest}")
    if hit:
        break
    time.sleep(300)
else:
    say("poll window closed at 09:30 ET with no PR -- Q2 advance PR still not issued")
