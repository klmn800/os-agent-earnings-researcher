---
name: reference-q4-event-feed
description: Q4 Inc. IR calendars that render as JS-only pages have a readable JSON feed at /feed/Event.svc/GetEventList — lists every scheduled earnings event; returns OLDEST first (sortDirection ignored) so use pageSize=100 and sort client-side; found via AMX 2026-09-22
metadata:
  type: reference
---

**Q4 Inc.-hosted IR "events / calendar" pages (`…/investors/events/calendar/default.aspx`, `…/events-and-presentations`) are SPA shells to curl and WebFetch, but the widget behind them reads a plain JSON service that fetches fine with a browser User-Agent:**

```
https://<ir-host>/feed/Event.svc/GetEventList?languageId=1&eventSelection=0&includeFinancialReports=true&includePresentations=true&includePressReleases=true&pageSize=100&pageNumber=0&sortOrder=EventDate
```

- Response: `{"GetEventListResult":[{"StartDate":"10/15/2025 11:00:00","Title":"AMX will report 3Q25 Financial and Operating Results on October 14th after the market close. The conference call…","TimeZone":"ET","LinkToDetailPage":…}, …]}`.
- ⚠⚠ **`sortDirection` is ignored (corrected 2026-09-24; this note said the opposite until 09-27).** The feed returns **oldest first**, so a small `pageSize` shows only 2014-era events and looks like "no upcoming event". That is what the 09-25 AMX read got and logged as a "quirk?". Use `pageSize=100`, page with `pageNumber` (0, 1, 2 …) until a page comes back empty, **sort by `StartDate` in Python**, and dedupe by `EventId` (each event came back **twice** on AMX). `eventDateFilter=FutureOnly` is also ignored.
- Open the response as **utf-8** (`json.loads(raw.decode('utf-8'))`): the AMX JSON carries a 0x81 byte that the Windows default cp1252 codec rejects.
- Companion feeds on the same hosts: `/feed/PressRelease.svc/GetPressReleaseList?…` (same parameter style) and the RSS at `/rss/pressrelease.aspx` ([[reference-ir-rss-feeds]]).
- Send a browser UA (`Mozilla/5.0 …Chrome/128…`) with `--compressed`; the project UA gets tarpitted on most Q4 hosts.
- First use: **AMX 2026-09-22** — the feed listed every quarterly call since 2014 and settled AMX's Tuesday-amc cadence in one fetch, where the calendar page had been "JS-only" in the cadence table for months. Candidates to try next: GTLB and WSM events pages (recorded as "200 but JS-only" in [[reference-source-probe-failure-modes]]), macysinc.com events, ir.kroger.com.

**Why:** "200 but JS-only" has been treated as a dead end (stop trying paths). For Q4 sites specifically it is not — the data sits one URL away, and an events feed can carry a date **before** any wire PR exists (AMX has no advance PR at all).

**How to apply:** when an IR events page is a Q4 shell, hit `Event.svc/GetEventList` before declaring the channel unreadable; cache the feed URL as the IR URL so the next session doesn't rediscover it.
