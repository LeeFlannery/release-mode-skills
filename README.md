# release-mode-skills

Agent skills following the open [SKILL.md spec](https://github.com/anthropics/claude-code/blob/main/docs/skills.md), portable across Claude Code, Codex CLI, and OpenClaw. Authored by [Release Mode LLC](https://releasemode.co).

## Skills

| Skill | Description |
|-------|-------------|
| [company-vet](skills/company-vet/) | Pre-call due diligence brief on a company (coming) |
| [jd-analyzer](skills/jd-analyzer/) | Score a job description against a configurable rubric |
| [opportunity-tracker](skills/opportunity-tracker/) | Track job and contract opportunities through your pipeline |
| [openclaw-reference](skills/openclaw-reference/) | Reference for the OpenClaw agentic runtime |
| [ghostty-terminfo](skills/ghostty-terminfo/) | Fix "unknown terminal" errors when SSHing from Ghostty |
| [env-separator](skills/env-separator/) | Enforce strict test/production environment separation |
| [guardrails-enforcer](skills/guardrails-enforcer/) | The Four Laws of Agent Safety — read before edit, stay in scope, verify, halt when uncertain |
| [commit-validator](skills/commit-validator/) | Validate commits: single focus, no secrets, clean messages |

## Install

Clone and copy whichever skills you want:

```bash
git clone https://github.com/releasemodellc/release-mode-skills.git
cp -r release-mode-skills/skills/company-vet ~/.claude/skills/
```

Or install all of them:

```bash
cp -r release-mode-skills/skills/* ~/.claude/skills/
```

Restart your agent after installing so it rescans skill metadata.

### Install paths by agent

| Agent | User-level | Repo-level |
|-------|-----------|------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex CLI | `~/.codex/skills/` | `.codex/skills/` or `.agents/skills/` |
| OpenClaw | `~/.openclaw/skills/` | n/a |

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
