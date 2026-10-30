---
name: master-winning-product
description: Find winning products — products already proven to work and already paid for — by industry, niche, keywords and time window. Starts from TrustMRR, YC and a16z Speedrun, then Product Hunt and Hacker News; ranks by verified revenue, then funding raised, then traffic; enriches each entry with website, founder, X and other social; scores fit against the user's own profile (strengths, resources, customers); exports to a spreadsheet or Notion and writes a debrief for the team. Runs weekly. Triggers on "find winning product", "winning product", "scan winning products this week", "Master week 1 assignment" (also Vietnamese: "tìm winning product", "sản phẩm win", "quét sản phẩm win tuần này", "bài tập tuần 1 Master").
metadata:
  category: product
  scope: master
  owner: Sơn Piaz
  executor: internal agent
  version: "0.0.3"
---

# /master-winning-product

## Goal

Find **all** products that have been proven to work and that other people already pay for, within the exact industry, niche, keywords and time window the user chooses. The skill does one thing: produce that output, complete and sourced.

> "A product that someone has invested in has already passed the idea stage."
> "Don't read with your eyes. Put the AI on the web."
>
> Sơn, Master session 1, 25/10/2026

## Division of work: agent vs. you

| Agent does | You do |
|---|---|
| Reads sources, filters, ranks, enriches | Picks industry, niche, keywords, time window |
| Scores fit against your profile | Answers the 3 profile questions (strengths, resources, customers) |
| Exports tables, writes the debrief | Provides keys if you have them (Kyma, TrustMRR), into `.env` |
| | No TrustMRR key: opens the niche category page on TrustMRR yourself and gives the links to the agent |
| | Tries the products, adds a card if needed, fills in Weaknesses and Own angle |

Before running, the agent checks which tools it has (browser, Google or Notion connection, which keys are in `.env`) and says briefly: what it can run, what is missing, what you need to do. Do your part first; when a step needs you, stop and say exactly what is needed, do not guess. Scheduled runs do not stop: skip the missing step and record it under Blockers in the debrief.

## Inputs

On the first run, the agent asks, saves the answers to `winning-product.config.md` in the working folder, and prints the full path of that file:
1. **Industry** (for example Marketing, Sales, CRM, AI agent, e-commerce, healthcare).
2. **Niche** within that industry (for example scheduling posts across multiple social media channels).
3. **Keywords** to search.
4. **Time window** (for example 2025 to 2026). Default: most recent first, "filter by most recent".
5. **Where the output goes**: Google Sheet, Drive, Notion, or a local file. Depends on the user.
6. **Where the weekly report goes**: email, Telegram, iMessage, or opened in the browser.

**My profile.** Your product sits at the intersection of: your strengths, the resources you have, and a market that already pays. "Follow your strengths and what you enjoy, because once you enjoy it you can keep doing it for a long time." The skill finds the third circle; the agent asks you for the first two:

7. **Strengths and expertise**: what you have done, in which industry, for how long.
8. **Resources you have**: past customers, community, relationships in the industry.
9. **Your customers**, if you already have them.

If the machine already holds context about you (CLAUDE.md, the agent's memory, the product repo you are working on), the agent asks permission to read it first and only asks for what is missing. The profile is saved with the config file and can be edited at any time.

There is no fixed count: if 40 products match, record 40. The week 1 assignment needs at least 10; that is the assignment, not a limit of the skill.

Scheduled run: open the agent in the folder that contains `winning-product.config.md`, read the file and run immediately, without asking again.

## Steps

### 1. Go to the right places, in priority order

"You only need to search the right places. Not many. Few, but good quality." Few places, but at each one take **all** products that match the input.

| # | Source | Why |
|---|---|---|
| 1 | **TrustMRR** (trustmrr.com) | Monthly recurring revenue (MRR) is verified, because the product is tied directly to a payment provider |
| 2 | **Y Combinator** (ycombinator.com/companies), by batch year | Already funded by YC, already passed the idea stage |
| 3 | **a16z Speedrun** (speedrun.a16z.com/companies), by year | Already funded by a16z Speedrun |
| 4 | **Product Hunt** | Newly launched products, not verified |
| 5 | **Hacker News** (Show HN section) | Newly launched products, not verified |

Prioritise 2026, then go back in time. Sources 4 and 5 are broader and give more ideas, but are unproven: always rank them below sources 1 to 3 and mark them "not verified". To look further, check acquire.com, Flippa, Empire Flippers and Microns.

Two ways to get data from TrustMRR:
- **With an API key** (`TRUSTMRR_API_KEY`, created at trustmrr.com/dashboard-dev): call their API or MCP, filter by category and revenue. Amounts come back in USD cents; divide by 100.
- **Without a key**: the user opens the TrustMRR category page closest to the niche and gives the agent the links to the products; the agent reads `trustmrr.com/startup/<slug>.md` for each product and saves these links to the config so the next run can read them again.

### 2. Filter by industry first, then by product

"Filter by industry group first, then filter by product." On YC and Speedrun, use the industry filters (B2B, Marketing, Sales, Engineering, ...) and the batch-year filter. Compare this year with the previous one (for example 2024 with 2025) to see where the market is moving.

### 3. Rank

In this exact order:
1. **Verified revenue**, highest to lowest.
2. **Funding raised.** Only record the figure when the source states it clearly.
3. **Traffic.**

Ties: rank by traffic, then by the more recent funding round.

### 4. Enrich the list

"Fill in this list for me. That is what Enrich means." For each product:
- website link, what it does (one sentence: which problem, for whom);
- founder, the founder's X account, and their other social profiles;
- lowest plan price and how it is charged (per channel, per brand, per user);
- trial: how many days, whether a card is required;
- monthly traffic and main market (if a traffic API is available);
- tech stack (if visible).

### 5. Score fit with me

For each product, the agent compares it with your profile and records **Fit for me** (high, medium, low) with one sentence **Why** (which strength, which resource, which customer it relies on). This column does not change the ranking in step 3 and does not remove any row: the list stays complete, it only adds your own point of view.

### 6. Export the output

Put everything in the location the user chose (Sheet, Drive, Notion, file). Read back to the user the top 3 products by rank and the top 3 that fit them best, each with its reason.

### 7. Debrief

At the end of each run, the agent writes `debrief-<date>.md` next to the config file, written for someone who was not watching the run:
1. Where it searched, and how many products each source gave.
2. Top 3 by rank, and top 3 that fit me, each with one sentence of reason.
3. Blockers (blocked pages, missing keys, missing figures) and how each was handled.
4. What to do differently next time.

Write the debrief in the language the user works in (Vietnamese by default). This is the winning-product part of the 15-minute opening talk in the team session (the customer-profile part comes from assignment 2): "this past week I found a winning product, here is the customer profile, here is what I chose and why". When submitting the assignment on Campus, attach the debrief. Scheduled runs send the debrief to the report channel.

## Output

Two tables:
- **List:** every product found in the latest run, ranked.
- **History:** each run adds new rows with the date, marks products that newly appeared and products whose revenue changed. Old rows are never deleted.

Columns: Rank · Product · Industry · Niche · What it does · Verified revenue (MRR) · Funding · Traffic · Lowest price · Trial · Website · Founder · Founder X · Source · Date fetched · Fit for me · Why. The last two columns are for the user to fill in after trying the product: **Weaknesses** · **Own angle**. Leave a cell blank if it cannot be read. For rows from Product Hunt and Hacker News, the revenue column says "not verified", because that is a known status, not an unreadable cell.

**Quick view:** besides the Sheet or Notion, the agent builds an HTML table page next to this skill with `render-table.py` (`python3 render-table.py <file.csv> <file.html> "<title>" "<description>"`): Be Vietnam Pro font, numbers right-aligned, one colour per source group, empty cells left empty.

## Tools

"I give it the tools and equipment to do the work." Use what is already available first; add what is missing.

| Task | Use | Notes |
|---|---|---|
| Read the web, pages that load JavaScript (YC, Speedrun) | the agent's browser | built into Claude Code |
| **Cited web search, enrich founders and their X** | **Kyma API, model `sonar`**; if X is not found, retry with `sonar-pro` | realtime web search; source links are in `choices[0].message.annotations`, not in the answer text. Base URL `https://kymaapi.com/v1`, key `KYMA_API_KEY`, created at kymaapi.com/keys. Each `sonar` call costs about $0.007 for the search plus tokens; default to `sonar`, use `sonar-pro` only when needed |
| Lowest plan price, trial | the agent opens `<domain>/pricing` directly | `sonar` does not open pricing pages, so it cannot get prices |
| Summarise, classify the industry, write the "What it does" column, score "Fit for me" | Kyma API, any chat model | one key, many models |
| Read product screenshots (onboarding, pricing tables) | Kyma API, a vision-capable model | |
| Verified revenue by category | TrustMRR API or MCP | optional, see step 1 |
| Traffic, main market | Similarweb API | optional, external |
| Put the table into Sheet, Drive, Notion | the agent's Google or Notion connection | |

Keys are stored in environment variables or a `.env` file on the machine (`.env` is in `.gitignore`). Never paste keys into the chat, and never write keys into the config or the spreadsheet.

## Schedule

"Every Saturday and Sunday it will automatically crawl pages like these." Schedule the agent to run this skill every week, on a machine that is on (a MacBook or a Mac mini running 24/7); the report goes to the channel saved in the config. How to set up the schedule (cron job) is covered in the technical session.

## Do not

- Do not invent revenue, funding, traffic or founder names. If it cannot be read, leave that cell blank.
- Do not rank unverified products above verified ones.
- Do not crawl the whole TrustMRR site; go through the API, the MCP, or each product's own page.
- Do not sign up for trials or enter a card on the user's behalf.
- Do not print API keys to the screen.

## Eval

| # | Metric | Target |
|---|---|---|
| E1 | Every product matches the industry, niche, keywords and time window (spot-check 5 random rows) | 100% |
| E2 | Rows with a revenue or funding figure all have a source link | 100% |
| E3 | Ranking is correct: verified revenue, then funding, then traffic | 100% |
| E4 | Rows that have both a website and a founder | ≥ 90% |
| E5 | Invented or wrong-unit figures (check 3 rows against the original page) | 0 |
| E6 | Scheduled runs do not ask the user any question | 100% |
| E7 | No omissions: pick one YC filter that matches the input, every company matching the niche is in the table | 100% |
| E8 | Every row with "Fit for me" has a "Why" that refers to exactly one point in the profile | ≥ 90% |
| E9 | The debrief has all 4 parts | 100% |

How to measure: E1 to E5 on the tables submitted to Campus after session 2. E6 from the log of one scheduled run. E7 by reopening that YC filter yourself and counting. E8 and E9 on the debrief and the table submitted with it on Campus.

## Feedback log

| Date | Feedback | What was changed |
|---|---|---|
| 22/10/2026 | first version `bto-product-diagnosis`, diagnosis of four boxes | |
| 25/10/2026 | renamed to winning product; rewritten to match the skill description from session 1 | sources, ranking, enrich, spreadsheet, weekly run |
| 25/10/2026 | Sơn: "sounds like what I already said"; needs a sample output with images; use the Kyma API first; 10 is the assignment, not a limit; find everything by industry, niche, keywords, time; output location is up to the user; do not talk about copying | rewritten in Sơn's words from the session 1 recording, added a sample output, Tools section prefers Kyma, removed the count limit |
| 25/10/2026 | review round 5 | the line "Few, but good quality" about where to search moved to step 1; Y Combinator naming; Kyma fee and key location; E7 no omissions |
| 25/10/2026 | Sơn chose A, C, E (learned from MEGA HQ Challenges); Kyma `sonar` test: founder 6/6, X 1/3 (`sonar-pro` 2/3), price 0/6 | added My profile + the Fit for me step; division-of-work table; Debrief tied to the opening 15 minutes; prices taken from the pricing page |
| 25/10/2026 | Sơn: put Goal first; key link is kymaapi.com/keys; leave blank if unreadable; sample table must look good: aligned, spaced, font adjusted | Goal moved to the top, key link fixed, "unknown" removed, `render-table.py` added |

## Self-improvement

After each use: note which sources returned little or wrong data in the Feedback log. If a source changes its page structure, fix the Steps section right away. Feedback that repeats twice or more means the skill must be changed. When a stronger model is available, re-run the same niche and compare the tables.
