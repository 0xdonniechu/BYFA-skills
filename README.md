# Agent Skills

**Production-grade AI agent skills for Claude Code, Cursor, and autonomous agent workflows.**

A skill is a structured instruction set that an agent autonomously loads and executes when encountering a specific operational domain. You do not need to memorize workflows or repeatedly paste prompts — the agent detects context, loads the guidelines, and executes with precision.

All principles are distilled from production engineering experience: secrets management, rigorous market research with multi-tier source verification, clean-room product teardowns, structured software development life cycles (SDLC), and multi-agent coordination.

## Research

- [Native.no competitive landscape (26 Oct 2026)](research/native-competitive-2026-10-26.html) — competitor matrix, TrustMRR snapshots, funding/valuation evidence, and a clearly caveated TAM/SAM/SOM scenario.

---

## Skills Directory

| Skill | Core Capability & Usage Context |
|---|---|
| `/bto-researchmarket` | In-depth market research: 3-tier fact tagging (`[CONFIRMED]`, `[SECONDARY]`, `[VENDOR-CLAIMED]`), 1★/2★ review mining for content wedges, TAM/SAM/SOM arithmetic chains, Sales Competitor Battlecards, and proof-based Marketing Case Study packaging. |
| `/bto-teardown` | Clean-room competitor teardowns: core features, monetization models, tech stack analysis, and end-to-end user experience flows. |
| `/bto-secrets` | Guard sensitive credentials: scan API keys, `.env` files, auth tokens, and secrets prior to commit or push. |
| `/bto-sdlc` | Structured software development: specification before code, discrete implementation phases, and verified testing gates. |
| `/bto-agent-team` | Multi-agent orchestration: single-approval pipelines (build → independent review → fix → merge → verify) across execution waves. |
| `/bto-whats-next` | Session wrap-up: audit pending work items, recommend next steps, and log progress. |
| `/bto-page-quality` | Post-launch site audits: page load performance, Core Web Vitals, and UI layout stability. |
| `/bto-optimize-mac` | Safe disk reclamation, RAM inspection, and developer environment hygiene for macOS. |
| `/bto-event-review` | Conference and meetup synthesis: reconstruct complete talks from slide decks and transcripts. |
| `/bto-posthog` | Production analytics with PostHog: event tracking setup, proxy configuration, and executive dashboards. |
| `/bto-create-skill` | Standard template and workflow for building and customizing agent skills. |

---

## Installation

### Claude Code

Install all skills with a single command:

```bash
git clone https://github.com/0xdonniechu/bto-skills.git ~/.claude/skills/bto-skills
~/.claude/skills/bto-skills/setup
```

Or install a specific skill (e.g. `bto-researchmarket`):

```bash
mkdir -p ~/.claude/skills/bto-researchmarket
curl -o ~/.claude/skills/bto-researchmarket/SKILL.md \
  https://raw.githubusercontent.com/0xdonniechu/bto-skills/main/bto-researchmarket/SKILL.md
```

### Cursor & Other Agents

See the complete guide in [INSTALL.md](INSTALL.md).

---

## Verification

Open a new agent session and test with prompts such as:

```
I need to research this market and evaluate competitors — which framework should we follow?
I am about to build a new feature — do we have a spec-before-code procedure?
What are our next steps for this session?
```

When the agent autonomously references the respective framework, the skills are active and ready.

---

## Core Principles

1. **Empirical Evidence Over Assumptions**: Every metric must be cited with primary sources or calculated with transparent math.
2. **Agent Assistance, Human Authority**: Skills keep agents disciplined; final approval and irreversible actions remain strictly with the user.
3. **Continuous Optimization**: Skills improve with each operational cycle and real-world deployment. See [CONTRIBUTING.md](CONTRIBUTING.md).
