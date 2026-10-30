---
name: byfa-page-quality
description: Measure and improve web page quality — speed, Core Web Vitals, per-country experience, search visibility, edge cache. Use when asking "slow page", LCP/INP/CLS, per-country bounce, Lighthouse scores, or before/after frontend changes. Matches Session 5 (logs, alerts) and Session 8 (post-launch measurement).
---

# /byfa-page-quality

One question: **is the site good, and for whom?** Answer it from multiple sources — never one tab alone.

---

## Four traps that once caused wrong conclusions

**1. Headless browsers dominate low-traffic page p75.** PostHog/Web Vitals may report LCP of 20–30s while mobile PageSpeed reads ~99. The sample has two clusters: fast or >10s, nothing between — usually Linux-desktop bots (FCP = LCP). Filter LCP ≥ 10s before trusting the raw RUM tab.

**2. The operator is not the market.** `/admin` with a few dozen samples may be one person. Exclude admin/internal paths from public reports.

**3. One mobile Lighthouse run is not a measurement.** Same code, same day, deltas of hundreds of ms are normal. Mobile: median of ≥3 runs; only a spread smaller than the delta counts as a delta. Spread = 0 may be PSI cache — compare across reports, not within one report.

**4. Missing CrUX country ≠ "fine there".** Only enough real Chrome traffic gets published. No row = not enough data yet, not fast.

---

## Five sources — each answers one question

| Source | The one question | How to get it (generic) |
|---|---|---|
| **field** — CrUX | What real Chrome users measure; the numbers Google ranks on | CrUX API or BigQuery `chrome-ux-report` |
| **lab** — PageSpeed | Fixed input → which deploy caused the change | PageSpeed Insights API |
| **rum** — analytics | Country × path; where exactly the page is *only* slow | PostHog, Plausible, GA4 BigQuery, … |
| **search** — Search Console | What Google **shows**; what the market sees without clicking | GSC API |
| **edge** — headers | Whether HTML comes from cache near the user or flies far | `curl -I` production |

The CrUX API has no country split; BigQuery `country_summary` does — ~1.5 GB/scan, ~2-month lag. Use for reach sizing, not just speed.

---

## In-repo measurement script (recommended)

Create one command (e.g. `npm run quality:page` or a script in `scripts/`) gathering the sources:

```bash
# Example shape — adapt to your repo
bun run quality:page                  # full (~ minutes if PSI included)
bun run quality:page --skip=lab       # skip Lighthouse
bun run quality:page --only=rum
bun run quality:page --json
bun run quality:page --days=7
```

Secrets come from env (`CRUX_API_KEY`, analytics key, GSC service account JSON). The script **fails loudly** on missing sources — never prints fake zeros.

---

## Fix what the script finds

**The logged-in page matters more than landing** if paying customers use the dashboard daily. Both on the list means prioritizing app/authenticated over marketing.

**Edge-cached HTML + App Router RSC** breaks easily: one URL, two bodies (`vary: rsc`). A mismatched cache rule → client navigation receives an HTML document. Before caching HTML: verify RSC still bypasses; keep a rollback snapshot; never overwrite the rollback snapshot.

**Good rank, low CTR → look at the QUERY before the title.** Brand queries (`your name + api`) naturally CTR low on sub-pages. Only edit titles for non-brand-intent queries. `site:` searches self-generate impressions.

**Byte weight is the lever you control.** Image budgets (KB, max width), SSR payload guards in CI.

---

## Common gaps (prioritized by value/hour)

| Gap | Consequence | Fix |
|---|---|---|
| No third-party uptime monitor | "Not broken" has no witness | UptimeRobot/Better Stack free tier |
| Crash emails filtered | Production dies silently | Remove the filter or route to Telegram |
| Node/runtime EOL | Sudden build failure | Follow platform deadlines |
| New RLS/table missing policy | Data leak flag | Audit + CI guard |
| No CWV gate in CI | Deploys regress LCP silently | `quality:page --json` + threshold |

Weekly workflow: a GitHub Actions cron runs the report into the summary; needs secrets in repo settings.

---

## Email / alerts worth skimming monthly

Search Console (indexing, structured data), analytics weekly digest, platform deploy failures, host crashes, DB security advisor, DMARC XML — add back whatever the APIs don't expose.

---

## Extending the skill

Add a source only when it answers a question the five sources above cannot. When thresholds change, change them in the script with a measured reason.

**Rule of three:** the third time you write an ad-hoc CWV/GSC query for the same question → put it in the script/skill.
