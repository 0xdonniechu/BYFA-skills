# Contributing to byfa-skills

A skill is a living document. You use it, find something missing or wrong, fix it, and the
next person avoids tripping where you tripped. That is the entire lifecycle of this repo.

## How to contribute, four steps

```bash
# 1. Fork this repo on GitHub (Fork button, top right), then clone your fork
git clone https://github.com/<your-name>/BYFA-skills.git
cd BYFA-skills

# 2. Create a branch, edit the relevant SKILL.md file
git checkout -b fix/short-name

# 3. Commit describing WHY you fixed it, not just what you changed
git add <file> && git commit -m "fix: ..."
git push -u origin fix/short-name

# 4. Open a pull request to 0xdonniechu/BYFA-skills, describe it in English
```

New to git? Open an issue retelling what happened to you — that counts as a contribution too.
Or tell your agent: "fork 0xdonniechu/BYFA-skills, fix X, open a PR for me".

## Rules for an accepted contribution

1. **Every new rule must come with a real failure story.** Where you tripped, how long
   it cost, how you fixed it. A rule with no story behind it is theory and will not
   be accepted. This entire repo is written on that principle.
2. **Write in English, keep technical terms as-is.** A `webhook` is a webhook.
3. **No keys, no secrets, no real-person data, no personal machine paths** in any file.
4. **New skill names are English kebab-case with no prefix** (the existing shared exception is `market-research`), one folder
   per `SKILL.md`, runnable right after symlinking.
5. To propose replacing an entire workflow, open an issue to discuss first — don't send
   a PR rewriting a whole file outright.

## Where to ask when stuck

- **developer community**: the `q-and-a` channel; program members are
  the fastest source of help — someone has tripped over most issues before you.
- **GitHub Issues** of this repo: for bugs inside the skills themselves.
- **Son Piaz**: [github.com/0xdonniechu](https://github.com/0xdonniechu), the original
  author of these skills.

Not in the program but want to learn the full method behind the skills:
[github.com/0xdonniechu/BYFA-skills](https://github.com/0xdonniechu/BYFA-skills).
