# Changelog

## 0.0.13 · 2026-11-10

- `sdlc`: replaced with the newer version. Adds `clarify` (an intent cannot reach `approved` while an open point remains), a `## Tasks` section in the plan that feeds each builder's contract, and `converge` (lists changed files outside the plan's tasks, tasks left untouched and Proof items without a result). The skill now ships `sdlc/scripts/` (`sdlc-check.py`, `dispatch.py`, `contract.py`, standard library only), so it is no longer a single-file skill; the old `sdlc/SKILL.md` is gone.

## 0.0.12 · 2026-10-26

- `market-research`: substantial research now defaults to a browser-viewable HTML report with a verified direct URL using existing authorized hosting; keeps sensitive research private and does not create hosting accounts.

## 0.0.11 · 2026-10-26

- Merged the existing `market-research` skill with the `byfa-researchmarket` workflow; added sourcing, review, market sizing, finance, and investor/vendor diligence playbooks while preserving the existing chart workflow.
- Removed the `byfa-researchmarket` directory, updated README/install/contributing; `setup` removes the old symlink only when it points exactly at the removed skill.
- Preserved the SVG chart tool; clarified when to use matrix, sizing, and valuation methods; added Eval and feedback based on the Native research case.

## 0.0.10 · 2026-09-28

- Added `byfa-create-skill`, the skill-creation skill: first ask whether this should be a skill at all (one-off work gets a prompt; machine-blockable errors get a hook or script), then ask five questions, write `SKILL.md`, trial it on a real case in a fresh session, add a countable eval and a feedback log, and install into Claude Code or Cursor. Ships with `byfa-create-skill/TEMPLATE.md`, a one-page `SKILL.md` template with guiding notes. If installed via `setup`, re-run `git pull` and `setup` to receive the new skill.

## 0.0.9 · 2026-09-28

- Added `byfa-posthog`: audits your product's PostHog against a complete standard (project setup, SDK per site type, identify/reset, key events, reverse proxy), builds an overview dashboard set as the Home page, then re-measures to confirm numbers land in the right project. Ships with a dashboard layout example and a one-page checklist. If installed via `setup`, run `git pull` then `setup` to receive the new skill.

## 0.0.8 · 2026-09-28

- Member guide: count all nine skills correctly (install command and Method A heading still said eight), added `byfa-event-review` to the when-to-use table. README has been correct since 0.0.6.

## 0.0.7 · 2026-09-28

- Switched the `description` of `byfa-event-review` and `byfa-optimize-mac` to Vietnamese to match the other seven skills. Skill names stay English while descriptions stay Vietnamese so you know at a glance when to invoke them. Also fixed the `byfa-event-review` frontmatter bug (the old description contained a colon that broke YAML parsing). Names and invocation unchanged, no reinstall needed.

## 0.0.6 · 2026-09-27

- `byfa-event-review`: from a talk's recording or video plus slide images, rewrites each talk in full (no summarizing), with independent agent review and a completeness-measurement script. Example output: https://homus.dev. Original: https://github.com/0xdonniechu/event-review

## 0.0.5 · 2026-09-15

Fixed per the public security/content review (Grok, 09-15):

- Member guide: removed personal names; added `byfa-optimize-mac` warnings (`rm -rf` cache, no personal files, no `sudo`).
- Removed `CLAUDE.md` — internal notes, not shipped to users.

## 0.0.4 · 2026-09-15

Five wave-2 skills for users (Sessions 4–8):

- `byfa-sdlc` — artifact chain intent → plan → build → verify → ship
- `byfa-agent-team` — single approval, multiple agent roles, run to done
- `byfa-whats-next` — session triage, next-step recommendations (read-only)
- `byfa-page-quality` — page quality measurement, Core Web Vitals, post-launch
- `byfa-optimize-mac` — safe macOS RAM/disk cleanup

Added the member guide: install Claude Code + Cursor, verify skills, common errors.
README updated with the 8-skill table.

## 0.0.1 · 2026-08-30

First three skills, distributed for releases after Session 3:

- `giu-khoa` — keep API keys safe when delegating work to agents
- `research-market` — agent-driven market research, sourced numbers, TAM SAM SOM
- `teardown` — decompose products and rebuild under clean-room rules

## 0.0.2 · 2026-08-30

Renamed all three skills under Son's two new rules: the `byfa-`
brand prefix (following the OMC product-name-prefix pattern) and an English name part.

- `giu-khoa` → `byfa-secrets`
- `research-market` → `byfa-researchmarket`
- `teardown` → `byfa-teardown`

README gained a program intro, pointing to github.com/0xdonniechu/BYFA-skills.

## 0.0.3 · 2026-08-30

Four requirements from Son after Session 3, plus cross-checked content from the real transcript:

- Each skill gains a "When to use" section and a "This skill must improve itself" section:
  eval after each run, occasional lookups to update, ask the
  open-source community or Son Piaz when unsure
- `byfa-researchmarket` adds the 1-star/2-star review filtering technique and three validation
  methods (landing plus waitlist, talking to 5 real customers, preselling), exactly as taught
  live in Session 3
- `byfa-teardown` adds the IBM clean-room case told in Session 3
- Added CONTRIBUTING.md: fork, clone, open PRs, contribution rules, where to ask when stuck
