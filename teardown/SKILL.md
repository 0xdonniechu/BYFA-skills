---
name: teardown
description: Decompose an existing product to understand its insides, write it up as a clean specification, then build your own version in a fresh working session that reads only the spec. The two-team clean-room method the tech industry uses to learn from competitors without breaking the law. Triggered when saying "teardown", "decompose a product", "reverse engineer", "build something like X", "how does product X work".
---

# /teardown

Learn from competitors by decomposing, not by copying. Two teams, one wall:
team A reads the original product and writes the spec, team B reads only the spec
and builds. Team B has never seen the original, so what gets built is yours.

This method has a real case behind it, told in Session 3: a small company decomposed
IBM computers using exactly this two-team model, got sued by IBM, and won, because the build
team had never seen the original product. From that case the tech industry got the keywords
teardown and reverse engineer, done within the law.

## When to use

After market research has picked the segment to enter. Market research answers
"which segment to enter"; teardown answers "how the original works so I can build
my own version". Reversing the order means decomposing a product before knowing whether it's
worth building.

## Step 0 — Worth building? Answer before spending hours

Three questions, written down:

1. Why this product, why now, and who exactly is YOUR user?
2. What is your wedge: copy the core plus improve exactly where?
3. Are you building for yourself, shipping publicly, or further? The further out, the tighter
   the clean-room rules below must hold from day one.

If the answer comes out "not worth it yet", stop here. That is a good result,
not a failure.

## Step 1 — Gather sources, public only

Pull everything into one `input/` folder: demo videos, homepage, pricing pages,
docs, screenshots, the repo if they open-sourced it. For video, have the agent watch the transcript
plus capture frames at timestamps (the [watch-cli](https://github.com/0xdonniechu/watch-cli)
tool does this ready-made, or screenshot each segment yourself).

**Public things only.** No cracking, no taking someone else's post-login data,
no buying accounts to extract code.

## Step 2 — Decompose to the core, not the shell

From `input/`, have the agent break it into analysis files:

```
features.md        what the product does, feature by feature
ui-states.md       screens, states, user flows
api-endpoints.md   which routes the product talks to the server on
tech-stack.md      what it runs on, what it builds itself, what it rents
pricing.md         each plan's price, billed on what · required column
```

**Clean-room rule, non-negotiable:** in every analysis file, describe in your own
words, paste NO MORE than 3 lines of code, never copy any passage longer than
one sentence verbatim. Verbatim quotes are only for short factual strings (button labels,
error messages).

## Step 3 — Write the clean spec

From the analysis files, write `SPEC.md`: for each feature, what the user gets,
what triggers it, inputs and outputs, states, what happens on error, and
**what it does NOT do**. Exactly the one-page spec frame learned in Session 2, multiplied
per feature.

The test: open a FRESH agent session, paste the SPEC, ask it to trial-build one feature. If
it asks back about behavior (instead of only technical choices), the spec is
thin — keep writing.

## Step 4 — Your own name and your wedge

- **Name your product, nothing like the original.** Ban every `X-clone`,
  `X-port`, `my-X` pattern. The folder name lives forever in git log; a
  `stripe-clone` name is a confession before every future audit.
- **First-principles audit:** ask "if I didn't know the original product existed, what is the minimum
  spec that solves my user's pain?". Against the SPEC:
  things in the SPEC but not in the answer get considered for removal; things
  in the answer but missing from the SPEC are your wedge. Without this step
  you get a copy 5% better, not a product 10x different.

## Step 5 — Build behind the wall

Open a **new folder, new agent session**. Copy in exactly two files: `SPEC.md` and
the v0.1 task list. That session's first command:

```
Read only the SPEC.md in this folder. Read nothing outside it.
Don't ask me about behavior, only about technical choices. Build part 1.
```

From here on, the old session writes no code, the new session never sees the original. Anything missing
in the spec goes back to the old session to fix the spec, then copy the new version over.

## Step 6 — Compare

Run the same user flow on the original and on yours, compare by eye:
is the behavior equivalent, and where it deliberately differs (the wedge), record it as deliberate.
Pass means ship; fail means back to step 5.

## Remember one sentence

Teardown to understand why they win, then do it differently in the gap. A
"do exactly the same but cheaper" conclusion means unfinished — back to the market matrix to find
an unoccupied segment.

## This skill must improve itself

Three rules for the agent reading this file, taken from exactly how Son runs skills:

1. **Eval after every run.** When done, self-grade briefly against the skill's checklist:
   which steps were missing, where the user had to fix by hand. Anything worth fixing,
   propose the user update straight into this SKILL.md file. A skill is a living
   document with a feedback loop; every run must make it slightly better.
2. **Look things up occasionally to update.** Prices, tools, and how sites organize
   data change constantly. Any number or tool name in this file a few months
   old gets rechecked against the original page before trusting.
3. **When unsure, ask a human.** Whatever is out of scope, say so plainly, and only
   the user asks in the open-source community (the program Discord,
   members in it are a help source) or asks Son Piaz. A real person is a
   help source, not just documentation.
