---
name: bto-sdlc
description: The intent → plan → build → verify → ship artifact chain for any repo work big enough. Use when starting a new feature, a large refactor, or saying "write the intent", "follow the plan", "/bto-sdlc". Not for one-line fixes, quick diagnosis, or one-off ops work.
---

# /bto-sdlc

Each phase ends with an artifact committed to the repo. The next session (or another agent) only needs to read that file — no chat history required.

You are both the requester and the builder — all approval gates collapse into: **you approve the artifact before the next phase runs.**

The chain lives in the repo's `intent/` folder:

```
intent/
  2026-09-01-dark-mode.md        # WHY + WHAT (intent, approved)
  2026-09-01-dark-mode.plan.md   # HOW (plan, self-explanatory)
```

Matches Sessions 2 and 4: spec before code; verify per layer instead of reading every line.

---

## Phase 1 — Intent (why + what)

When you describe a feature or problem: the agent asks a few sharp questions (3–6) until scope is clear — technical constraints, affected systems, what is **not** being done. Then it writes `intent/<yyyy-mm-dd>-<slug>.md`:

```markdown
---
status: draft   # draft → approved → planned → building → verified → shipped (PR #n)
---
# <Title>
**Problem** — what hurts, in your words.
**Outcome** — what exists when done; success criteria (measurable).
**Constraints** — tech, budget, policy (lean, no new dependency, …).
**Out of scope** — what this deliberately does NOT do.
**Open questions** — undecided (empty = ready to approve).
```

You edit → `status: approved`, commit. **No plan before the intent is approved.**

For a new product: the intent must state the money path (who pays, paying for what).

---

## Phase 2 — Plan (how)

Feed only the intent file into plan mode. Large or architectural work: split product review and technical review before finalizing. Ask: "what could break?" Output `intent/<slug>.plan.md`:

- **Files** — every file to touch, in work order.
- **Risks** — what could break, and which check catches it.
- **Proof** — commands/evidence proving done (test, build, screenshot, curl). "Done" is defined here, before any code is typed.

You accept the plan → `status: planned`, commit. The plan is the handoff contract: the implementing agent reads only the plan, not the chat.

---

## Phase 3 — Build

Normal repo rules (one logical unit at a time; worktrees if parallel). Plus:

- Deviated from the plan → **update plan.md in the same commit**. Diff must match plan.
- Starting code → `status: building`.

---

## Phase 4 — Verify

Run exactly the plan's **Proof** section. The writer does **not** self-approve: pass an independent review (`code-reviewer` or another review agent) with intent + plan as the contract. Green proof → `status: verified`.

Any error repeating a second time in any repo → record immediately in that repo's `CLAUDE.md` or `lessons.md`.

---

## Phase 5 — Ship

Merge per repo flow (feature branch → PR → main; or uat → main if your repo does that). After merge: `status: shipped (PR #n)` in the intent — chain closed, git history is the audit trail.

---

## Phase 6 — Maintain (the loop)

Health checks, cron, and alert emails may auto-flag issues. Convention: a worthwhile issue bigger than a one-line fix → starts with a new intent file in the owning repo. Small bounded fixes → straight PR, skip the chain.

---

## Evals — regression for the process

An `evals/` folder per repo: one file per case — **Task** (a real prompt) + **Expect** (a checkable result). Every production incident and every "agent did it wrong" → one permanent case.

Run evals **before merging** changes to `CLAUDE.md`, skills, or hooks — config that drops the pass rate doesn't merge. 5 cases beats 0.

---

## When NOT to use

One-line fixes, diagnosis, one-off ops — the chain is overhead. Rule of thumb: if it deserves a feature branch, it deserves an intent file.
