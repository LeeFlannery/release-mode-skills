# release-mode-skills

Agent skills following the open [SKILL.md spec](https://github.com/anthropics/claude-code/blob/main/docs/skills.md), portable across Claude Code, Codex CLI, and OpenClaw. Authored by [Release Mode LLC](https://releasemode.co).

## Skills

A full DevRel-agency skill suite organized by pipeline stage, plus tracking, workflow, and reference skills.

### Win clients

| Skill | Description |
|-------|-------------|
| [company-research](skills/company-research/) | Deep research brief: org structure, where DevRel reports, product feedback loop signals |
| [jd-analyzer](skills/jd-analyzer/) | Score a job description against a configurable rubric |
| [proposal-writer](skills/proposal-writer/) | Turn discovery-call notes into a consulting proposal or SOW |

### Do the work

| Skill | Description |
|-------|-------------|
| [dx-audit](skills/dx-audit/) | Walk an API/SDK onboarding as a new developer; friction report with time-to-first-value |
| [docs-sync](skills/docs-sync/) | Audit and update project docs to match the actual source code |
| [sample-app-planner](skills/sample-app-planner/) | Spec a weekend-sized reference implementation against a target API |
| [tutorial-writer](skills/tutorial-writer/) | Turn working code into a step-by-step tutorial with verified commands |
| [demo-script](skills/demo-script/) | Two-column demo video script: talk track + screen actions, timestamped |
| [release-notes](skills/release-notes/) | Turn a git log or changelog into developer-facing release notes |

### Prove it

| Skill | Description |
|-------|-------------|
| [devrel-metrics](skills/devrel-metrics/) | Design a metrics framework: activation, time-to-first-value, anti-vanity rules |
| [case-study-writer](skills/case-study-writer/) | Turn engagement notes into a client case study — real metrics only |

### Market yourself

| Skill | Description |
|-------|-------------|
| [content-repurpose](skills/content-repurpose/) | One source piece → platform-native cuts (YouTube, LinkedIn, X, TikTok, blog) |
| [hermes-tweet-launch-monitor](skills/hermes-tweet-launch-monitor/) | Read-first X/Twitter launch monitoring with Hermes Tweet |
| [cfp-writer](skills/cfp-writer/) | Conference talk proposals: titles, abstract, outline, bio |

### Track & organize

| Skill | Description |
|-------|-------------|
| [opportunity-tracker](skills/opportunity-tracker/) | Track job and contract opportunities through your pipeline |
| [vault-add](skills/vault-add/) | Dispatcher: route an "add this" request to the right vault sub-skill |
| [vault-add-saas](skills/vault-add-saas/) | Add a paid SaaS / freemium / paid tool to the tools-services vault |
| [vault-add-stack](skills/vault-add-stack/) | Add a package / library / CLI / framework / runtime to the stack vault |
| [vault-add-job](skills/vault-add-job/) | Add a job / role / application to the job-search vault |
| [vault-add-client](skills/vault-add-client/) | Add a freelance / consulting lead to the potential-clients vault |

### Workflow & safety

| Skill | Description |
|-------|-------------|
| [guardrails-enforcer](skills/guardrails-enforcer/) | The Four Laws of Agent Safety — read before edit, stay in scope, verify, halt when uncertain |
| [env-separator](skills/env-separator/) | Enforce strict test/production environment separation |
| [commit-validator](skills/commit-validator/) | Validate commits: single focus, no secrets, clean messages |
| [update-todo-after-commit](skills/update-todo-after-commit/) | Keep TODO.md synchronized with repository work after commits |

### Reference

| Skill | Description |
|-------|-------------|
| [openclaw-reference](skills/openclaw-reference/) | Reference for the OpenClaw agentic runtime |
| [ghostty-terminfo](skills/ghostty-terminfo/) | Fix "unknown terminal" errors when SSHing from Ghostty |

## Install

The fastest way is [`npx skills`](https://github.com/vercel-labs/skills), which works across 40+ agents (Claude Code, Codex CLI, Cursor, Gemini CLI, ...):

```bash
# pick skills interactively
npx skills add LeeFlannery/release-mode-skills

# or install specific skills, or everything
npx skills add LeeFlannery/release-mode-skills --skill dx-audit -g -y
npx skills add LeeFlannery/release-mode-skills --all
```

Or clone and copy whichever skills you want:

```bash
git clone https://github.com/LeeFlannery/release-mode-skills.git
cp -r release-mode-skills/skills/dx-audit ~/.claude/skills/
```

Restart your agent after installing so it rescans skill metadata.

### Install paths by agent

| Agent | User-level | Repo-level |
|-------|-----------|------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex CLI | `~/.codex/skills/` | `.codex/skills/` or `.agents/skills/` |
| OpenClaw | `~/.openclaw/skills/` | n/a |

## Quality standards

Every skill in this repo meets a bar most skill collections don't state, let alone enforce:

- **Trigger-rich descriptions.** Every `description:` lists the concrete phrases that should activate the skill, so agents trigger it reliably instead of guessing from a one-liner.
- **Scope fences.** Every skill says what it does *not* do, so it doesn't bleed into neighboring tasks or take actions you didn't ask for.
- **Prompt-injection guards.** Skills that consume pasted content (emails, job descriptions, changelogs, discovery notes) explicitly treat that input as data, never as instructions.
- **Example outputs.** Deliverable-producing skills ship a `references/example-output.md` showing a real, complete sample of what they produce — instructions you can verify, not just trust.
- **CI-validated.** Every push checks that frontmatter is well-formed, skill names match their folders, and README links resolve.

## SKILL.md format

Every skill is a folder containing a `SKILL.md` file:

```yaml
---
name: my-skill
description: When to trigger this skill and what it does.
---

# My Skill

Instructions in natural language.
```

Skills can include optional subdirectories:
- `references/` — supporting docs loaded on demand
- `scripts/` — executable helpers for deterministic tasks

## License

MIT
