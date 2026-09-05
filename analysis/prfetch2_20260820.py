"""Resolve the advance-PR link out of each feed, then print its date/timing
sentences. LULU / TTC / CIEN -- feeds found on the round-2 host rotation."""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "*/*"}
FEEDS = {
 "LULU": ("https://corporate.lululemon.com/rss/press-releases", r"second quarter fiscal 2026 earnings conference call"),
 "TTC":  ("https://www.thetorocompany.com/rss/news-releases.xml", r"Announce Fiscal 2026 Third Quarter Results"),
 "CIEN": ("https://investor.ciena.com/rss/pressrelease.aspx", r"Reporting Date and Web Broadcast for Fiscal Third Quarter 2026"),
}
ITEM = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
LINK = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)
KEY = re.compile(r"before|after|market|close|open|a\.m\.|p\.m\.|ET\b|PT\b|CT\b|"
                 r"conference call|webcast|September|Sept|August|202[67]", re.I)

def get(url):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def strip(h):
    h = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    for a, b in [("&nbsp;", " "), ("&amp;", "&"), ("&#39;", "'"), ("&rsquo;", "'"),
                 ("&quot;", '"'), ("&ldquo;", '"'), ("&rdquo;", '"'), ("&mdash;", "--")]:
        h = h.replace(a, b)
    return re.sub(r"\s+", " ", h)

def go(kv):
    sym, (feed, pat) = kv
    try:
        body = get(feed)
    except Exception as e:
        return sym, feed, f"FEED ERR {e}", []
    link = None
    for it in ITEM.findall(body):
        if re.search(pat, it, re.I):
            m = LINK.search(it)
            if m:
                link = m.group(1).strip(); break
    if not link:
        return sym, feed, "no matching item", []
    try:
        txt = strip(get(link))
    except Exception as e:
        return sym, link, f"PR ERR {type(e).__name__}: {e}", []
    sents = re.split(r"(?<=[.!?])\s+", txt)
    seen, out = set(), []
    for s in sents:
        s = s.strip()
        if KEY.search(s) and 30 < len(s) < 500 and s not in seen:
            seen.add(s); out.append(s)
    return sym, link, f"OK {len(txt)}B", out[:12]

with ThreadPoolExecutor(max_workers=3) as ex:
    for sym, url, st, hits in ex.map(go, FEEDS.items()):
        print(f"\n{'='*72}\n{sym}  {st}\n  {url}")
        for s in hits:
            print(f"   . {s[:320]}")
