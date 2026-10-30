---
name: posthog
description: Audit and upgrade your product's PostHog against a complete standard — project setup, SDK wiring per site type, identify and reset on sign-in/sign-out, key events, reverse proxy, and an overview dashboard set as the Home page so opening the project shows all numbers. Use when saying "posthog", "add tracking", "analytics", "audit tracking", "events not arriving", "overview dashboard", "open posthog and see numbers", or when about to launch a site that needs user measurement. Not for page speed and deep Core Web Vitals (use `page-quality`), or when asking for one stray number inside PostHog.
---

# /posthog

Wiring PostHog is easy — paste one snippet and numbers appear. The hard part is three months later:
numbers mixed with dev-machine traffic, no idea who is who because identify used email,
half the events blocked by adblock, and every viewing session costs five page clicks.
This skill walks you through a complete standard, distilled from auditing seven real
running PostHog projects, then applies that standard to your product.

Four parts: **audit** (read-only) · **apply the standard** to project and code · **build
the Home dashboard** · **re-measure** to confirm numbers land in the right place.

## Prerequisites
- One PostHog project (Cloud US or EU). **One product per project**: don't
  merge unrelated domains into one project, because funnels, retention, and
  filters all compute per project.
- Agent access to PostHog: PostHog MCP (recommended) or a personal API key
  in `.env`, never pasted into chat. See `secrets`.
- The site repo, if you want to edit code.

## Step 1 — Audit (read-only, change nothing)

1. **Project settings.** Read settings and compare against the Step 2 table.
   Note: the project-read command also returns the project token; don't copy the token into the
   report file.
2. **30-day traffic by host and SDK**, one SQL query:
   ```sql
   SELECT properties.$host, properties.$lib, max(properties.$lib_version),
          count(), countIf(event = '$pageview'), uniq(person_id)
   FROM events
   WHERE timestamp > now() - INTERVAL 30 DAY
   GROUP BY 1, 2 ORDER BY 4 DESC
   ```
   Seeing `localhost`, `*.vercel.app`, `*.pages.dev`, or a strange domain is
   a finding: either the filters are insufficient, or another site is using the wrong key.
3. **30-day event list** (`GROUP BY event`), compared against the Step 4 event table.
4. **Current Home dashboard**: which tiles exist, whether tiles enable test
   account filtering. PostHog's sample dashboard usually leaves it off.
5. **Code**: find `posthog` in the repo with fixed strings (`grep -rnFi`),
   skipping `node_modules`, `.git`, `dist`. Record: key from env or hardcoded,
   proxy or not, identify by what, `reset()` on logout or not.

Result: a "standard vs reality" table and a fix list.

## Step 2 — Apply the standard to the project

| Setting | Standard value | Why |
|---|---|---|
| Product name + description | name + one sentence | PostHog's AI and future people understand the project |
| Authorized URLs (`app_urls`) | every production domain | toolbar and heatmaps open from PostHog |
| Test account filters | internal-people cohort + host filters `localhost`, `127.0.0.1`, `vercel.app`, `pages.dev`, `web.app` | previews and dev machines skew numbers |
| Default test account filtering | on | new insights auto-exclude internal traffic |
| Timezone | one zone for all your projects (or your primary users' zone) | cross-comparison doesn't shift days |
| Autocapture, web vitals, heatmaps, dead clicks | on | click and page-speed data with no code |
| Exception autocapture | on | JS errors are the cheapest signal for "user is broken" |
| Session replay | on, mask all inputs (privacy-first sites turn it off) | replay where users get stuck |

Privacy-first sites (no cookies, hidden IPs): keep replay off,
no browser-side identify. That is a deliberate choice — record it in
the report rather than "fixing" it.

## Step 3 — Apply the standard to code

```js
posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY, { // key from env, never hardcoded
  api_host: '/_ph',                   // same-domain reverse proxy
  ui_host: 'https://us.posthog.com',  // switch to eu if the project is in EU
  defaults: '<latest defaults in the PostHog docs>',
  person_profiles: 'identified_only',
  capture_pageview: 'history_change', // SPA
  capture_pageleave: true,
  autocapture: true,
  capture_exceptions: true,
  session_recording: { maskAllInputs: true },
})
```

- **Key from env var; missing env means send nothing.** Don't let code fall back to another
  project's key: that's how a site quietly sends numbers into the wrong
  project for months.
- **Reverse proxy** to dodge adblock. Next.js/Vercel: rewrite
  `/_ph/static/:path*` → `https://us-assets.i.posthog.com/static/:path*` and
  `/_ph/:path*` → `https://us.i.posthog.com/:path*`. Static sites on Vercel:
  same rewrites in `vercel.json`. Cloudflare Pages: `_redirects` or one
  Function as proxy.
- **Identify by internal id, not email**: after sign-in completes,
  `posthog.identify(user.id, { email, name, plan })`. On sign-out:
  `posthog.reset()`. Changing email must not split one person into two.
- **Money events from the server** (payment webhooks), same distinct_id as the
  browser. Person-less events (API hits, bots) ship with
  `$process_person_profile: false` to avoid creating phantom people.
- **Pin the SDK version** in the lockfile, update deliberately.
- Add one test: "no env means no `posthog.init`".

## Step 4 — Key events by site type

Event names in `snake_case`, form `object_action`, one name one meaning.

| Site type | Required | Nice to have |
|---|---|---|
| Landing / marketing | `$pageview`, `cta_clicked {cta, location}`, `signup_started`, `waitlist_joined` or `checkout_started` | `outbound_click` |
| SaaS dashboard | `user_signed_up`, `user_signed_in`, `onboarding_completed`, one core-action event, `checkout_started`, `payment_succeeded` (server) | `feature_used {feature}` |
| Docs | `$pageview`, `docs_search`, `docs_copy_code`, `docs_cta_click` | a "was this page helpful?" button |
| Course | `lesson_viewed`, `lesson_completed`, `checkout_started`, `purchase_completed` (server) | `assignment_submitted` |
| Desktop app | `app_launched {version}`, `onboarding_completed`, core action, `signed_in` + identify, `signed_out` + reset | data-sending kill switch; never send user content |

## Step 5 — Home dashboard: opening the project shows the numbers

One dashboard named `Home — <product> overview`, set as the project's
primary dashboard (`primary_dashboard`). Every tile enables test account filtering. If a dashboard is
nearly there, add tiles to it instead of cloning.

Example layout for a small SaaS:

```
┌─────────────────┬─────────────────┬─────────────────┐
│ Active users 30d│ Sessions 7d     │ Pageviews 7d    │   big numbers
├─────────────────┴────────┬────────┴─────────────────┤
│ DAU / WAU (line)         │ Traffic by channel 30d   │
├──────────────────────────┼──────────────────────────┤
│ Top pages 7d             │ Top referrers            │
├──────────────────────────┴──────────────────────────┤
│ Main funnel: signup → core action → payment        │
├──────────────────────────┬──────────────────────────┤
│ Key events 30d           │ Web vitals p75 (LCP/INP) │
├──────────────────────────┼──────────────────────────┤
│ Errors ($exception)+rage │ Weekly retention         │
└──────────────────────────┴──────────────────────────┘
```

Multiple domains in one project means adding a "visitors by host" tile.

## Step 6 — Re-measure, don't trust "fixed"

1. In the target project: `SELECT properties.$host, count() FROM events WHERE
   timestamp > now() - INTERVAL 1 HOUR GROUP BY 1` shows the real domain.
2. After a project split: the old project drops to 0 events for that domain after deploy time.
3. New events (`$identify`, custom events, `$exception`) appear in the
   event list.
4. Opening the project: the Home page is the newly built dashboard, every tile returns numbers.

Report with before-and-after numbers.

## One-page checklist

- [ ] One product per project, no strange domains mixed in
- [ ] `app_urls` covers every production domain
- [ ] Test account filtering: cohort + 5 hosts, on by default
- [ ] Exception autocapture, dead clicks, web vitals, heatmaps on
- [ ] Key read from env; missing env means no sending
- [ ] Reverse proxy `/_ph`
- [ ] Fresh `defaults`, SDK version pinned in lockfile
- [ ] `identify(user.id)` after sign-in, `reset()` on sign-out
- [ ] Money events sent from the server
- [ ] Required events per site type (Step 4)
- [ ] Home dashboard set as primary, every tile filters test accounts
- [ ] Re-measured after deploy (Step 6)

## Don't
- Never paste API keys or project tokens into chat, report files, or commits.
- Never delete old dashboards, insights, cohorts, or data while cleaning up.
- Never enable replay or identify on a site you chose to keep private.
- Never deploy tracking changes to production without reading the diff.

## This skill must improve itself

Three rules for the agent reading this file:

1. **Eval after every run.** Grade against the checklist above: how many items passed
   before and after, what the user still had to fix by hand. Anything worth fixing,
   propose the user update straight into this SKILL.md file.
2. **Look things up occasionally to update.** PostHog moves fast: the `defaults` build, setting
   names, tool names in the MCP. Anything in this file a few months
   old gets rechecked against PostHog docs before trusting.
3. **When unsure, ask a human.** Whatever is out of scope, say so plainly, and only
   the user asks in the open-source community (the program Discord) or asks
   Son Piaz.
