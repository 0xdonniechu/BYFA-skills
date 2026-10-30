# Installing Agent Workflows skills (wave 2)

This document is for users who have **never installed a skill**. This repo's skills cover eleven workflows: ten `byfa-*` skills and one shared skill named `market-research`.

Repo: [github.com/0xdonniechu/BYFA-skills](https://github.com/0xdonniechu/BYFA-skills)

---

## What is a skill?

A skill is a `SKILL.md` file — a procedure set the agent **reads itself** when you hand it the right kind of work. You don't memorize steps; the agent sees the right context, opens the guide, and follows it.

Skill names are always **English**, prefixed with `byfa-`. Guide content in the files is English.

---

## Seven new skills, when to use them

| Skill | Session | Use when | Don't use when | Example invocation |
|---|---|---|---|---|
| **byfa-sdlc** | 2, 4 | New feature, large refactor, need spec before code | One-line fix, quick question, one-off ops work | *"Write the intent for the dark mode feature"* · *"Follow the SDLC chain, approve the plan before coding"* |
| **byfa-agent-team** | 7 | Multi-part change (backend + frontend…), want one approval then the agent runs to done | One file, one small bug | *"Split waves for the dashboard ticket, write the brief then spawn roles"* · *"One approval, run build → review → merge"* |
| **byfa-whats-next** | 7 | End of session, unsure what to do next; need to sweep unfinished work | Mid-task, want the agent to just do it | *"What next?"* · *"Summarize what is still unfinished this session?"* |
| **byfa-page-quality** | 5, 8 | Slow page, Core Web Vitals, measure before/after deploy, post-launch analytics | Pure backend, no live site yet | *"What is the landing page LCP?"* · *"Measure page quality before launch"* |
| **byfa-optimize-mac** | — (utility) | Mac disk full, high RAM, many agents/builds at once | Windows/Linux machine (this skill is for macOS) | *"How many GB are left on disk, clean up safely for me"* · *"Machine is slow, measure RAM then propose cleanup"* |
| **byfa-event-review** | — (utility) | Back from a conference or meetup with a recording or transcript plus slide images, want to reread each full talk | Only need a short summary, or a social media post | *"Event review for yesterday's 3 talks, here is the transcript and the slide image folder"* · *"Rewrite this talk in full in English"* |
| **byfa-posthog** | — (utility) | Product has a real live site, want to know where users go, what they click, whether events arrive | No live site yet, or only asking for one stray number | *"Audit the landing page PostHog, events are not arriving"* · *"Build an overview dashboard so opening the project shows the numbers"* |

**Note:** `byfa-whats-next` only **recommends**, never acts by itself. `byfa-agent-team` requires you to approve the brief before running waves.

**`/byfa-optimize-mac`:** this skill may **delete regenerable caches** (e.g. `rm -rf` on npm/bun/Xcode DerivedData folders inside the skill) — **never** personal files (photos, transcripts, project data), and **never use `sudo`**.

---

## Create your own skill (0.0.9)

| Skill | Use when | Don't use when | Example invocation |
|---|---|---|---|
| **byfa-create-skill** | A multi-step job you have done 2+ times and want the agent to always remember | One-off work (a prompt is enough), or machine-blockable errors (make a hook or script) | *"Turn what I just did into a skill"* · *"Create a release-note skill for this repo"* |

The skill asks you five questions, writes `SKILL.md` from the [one-page template](byfa-create-skill/TEMPLATE.md), trials it on a real case in a fresh session, then installs it on your machine.

---

## Install — Claude Code (recommended)

### Method A: Install the whole repo (all skills, one command)

Open **Claude Code**, paste this entire line:

> Install byfa-skills: run `git clone https://github.com/0xdonniechu/BYFA-skills.git ~/.claude/skills/byfa-skills && ~/.claude/skills/byfa-skills/setup` then confirm all eleven skills are picked up (ten `byfa-*` names and `market-research`).

Or run it yourself in Terminal:

```bash
git clone https://github.com/0xdonniechu/BYFA-skills.git ~/.claude/skills/byfa-skills
~/.claude/skills/byfa-skills/setup
```

The `setup` script creates **symlinks** from the repo into `~/.claude/skills/<skill-name>/` and removes the legacy `byfa-researchmarket` symlink only when it points exactly at the removed skill folder. Re-running is safe.

### Method B: A single skill

Example with just `byfa-sdlc` (single-file skill):

```bash
mkdir -p ~/.claude/skills/byfa-sdlc
curl -o ~/.claude/skills/byfa-sdlc/SKILL.md \
  https://raw.githubusercontent.com/0xdonniechu/BYFA-skills/main/byfa-sdlc/SKILL.md
```

Swap `byfa-sdlc` for the skill name you need.

`market-research` ships with a playbook, chart guide, and scripts/assets; install that skill alone with the full commands in **Installation → Claude Code** in [README.md](README.md). Downloading only `SKILL.md` will miss the referenced docs and tools.

### Verify the install (Claude Code)

1. **Close the old session, open a new Claude Code session** (skills only load at start).
2. Ask something like:

```
I'm about to build a new feature. Is there a spec-before-code procedure?
```

The agent mentions `intent/`, plan, approval before code → **byfa-sdlc** is live.

3. Or check the file:

```bash
ls ~/.claude/skills/byfa-sdlc/SKILL.md
# or if installed via setup:
readlink ~/.claude/skills/byfa-sdlc
```

---

## Install — Cursor

Cursor reads skills from `~/.cursor/skills/` (personal) or `.cursor/skills/` (inside a project repo).

### Method A: Symlink the whole repo (like Claude Code)

```bash
git clone https://github.com/0xdonniechu/BYFA-skills.git ~/.cursor/skills/byfa-skills
mkdir -p ~/.cursor/skills
for d in ~/.cursor/skills/byfa-skills/*/; do
  [ -f "$d/SKILL.md" ] || continue
  name=$(basename "$d")
  ln -sfn "$d" ~/.cursor/skills/"$name"
done
legacy="$HOME/.cursor/skills/byfa-researchmarket"
if [ -L "$legacy" ] && [ "$(readlink "$legacy")" = "$HOME/.cursor/skills/byfa-skills/byfa-researchmarket" ]; then
  rm "$legacy"
fi
```

To install only `market-research` for Cursor, clone the repo and link the whole skill folder so references and chart assets come along:

```bash
git clone https://github.com/0xdonniechu/BYFA-skills.git ~/.cursor/skills/byfa-skills
ln -s ~/.cursor/skills/byfa-skills/market-research ~/.cursor/skills/market-research
```

### Method B: A single skill

```bash
mkdir -p ~/.cursor/skills/byfa-whats-next
curl -o ~/.cursor/skills/byfa-whats-next/SKILL.md \
  https://raw.githubusercontent.com/0xdonniechu/BYFA-skills/main/byfa-whats-next/SKILL.md
```

### Verify the install (Cursor)

1. Open a **new Agent** in Cursor (agent chat, not a regular edit tab).
2. Type: *"What should I do next in this session?"* — the agent should sweep PRs/unfinished work, **not** run code by itself.
3. Check the file:

```bash
ls ~/.cursor/skills/byfa-whats-next/SKILL.md
```

In Cursor: **Settings → Rules / Skills** (depending on version) may list discovered skills.

---

## Updating skills later

```bash
cd ~/.claude/skills/byfa-skills   # or ~/.cursor/skills/byfa-skills
git pull
~/.claude/skills/byfa-skills/setup   # Claude Code: refresh symlinks
```

Open a **new** agent session after pulling.

---

## Common errors

| Symptom | Cause | Fix |
|---|---|---|
| Agent never mentions the skill workflow | Session opened **before** installing | Close it, open a new session |
| `setup` reports "skipping … already exists" | You already have a skill folder with the same name (self-written) | Rename the old folder, or curl a single SKILL.md file |
| `git clone` reports the folder exists | Second clone | `cd ~/.claude/skills/byfa-skills && git pull` |
| Cursor doesn't see the skill | Placed in the wrong spot | Link the skill folder from `~/.cursor/skills/byfa-skills/`, including `market-research/` |
| Broken symlink after deleting the repo | Accidentally deleted the clone folder | Clone again + run `setup` |
| Agent answers in an unexpected language | Request language unclear | Normal; phrase the request in the language you want answered |

---

## Need help

- Program community channel for Q&A
- Email / learning platform: the program coordinator will send the repo link + this file
- Skill feedback: [CONTRIBUTING.md](CONTRIBUTING.md) — fork, fix, open a PR

---

*Updated: 09/28/2026, added byfa-create-skill and byfa-posthog (11 skills), byfa-event-review. 09/15/2026, wave 2: byfa-sdlc, byfa-agent-team, byfa-whats-next, byfa-page-quality, byfa-optimize-mac.*
