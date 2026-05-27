---
name: openclaw-reference
description: Apply this skill whenever the user mentions OpenClaw, the OpenClaw Gateway, OpenClaw skills, SOUL.md, AGENTS.md, HEARTBEAT.md, MEMORY.md, ClawHub, or any task involving configuring, running, debugging, or extending an OpenClaw installation. Use it when the user asks about OpenClaw workspace files, systemd service setup for OpenClaw, MCP integration with OpenClaw, or anything related to the OpenClaw agentic runtime — even if they don't say "OpenClaw" explicitly and the context makes it clear that's what they're working with.
---

# OpenClaw Reference

OpenClaw is an open-source, self-hosted AI agent runtime. It runs as a persistent background process, connects to messaging platforms (WhatsApp, Telegram, Slack, Discord, and others), and takes real actions: reading and writing files, running shell commands, sending email, browsing the web, managing calendars. It is not a chatbot — it is a local orchestration platform with an LLM as the reasoning layer.

Created by Peter Steinberger. Launched January 2026. MIT licensed. Now governed by an independent open-source foundation. Node.js 22+ required.

For full architectural detail, read `references/architecture.md`. For workspace file reference, read `references/workspace.md`.

---

## Key facts to always apply

**The Gateway is the central process.** Everything routes through it. It runs as a systemd service on Linux (or a LaunchAgent on macOS), listening on WebSocket at `ws://127.0.0.1:18789` by default. Do not expose this port directly to the internet.

**Config and state live under `~/.openclaw/`.** The agent workspace lives at `~/.openclaw/workspace/`. Skills install into `~/.openclaw/skills/` by default.

**Memory is plain Markdown files.** Not a database, not a vector store. MEMORY.md, SOUL.md, AGENTS.md, HEARTBEAT.md, and daily logs under `memory/`. Agents load these on demand — they are not injected into every prompt automatically.

**Skills are Markdown folders, not code packages.** A skill is a directory containing a `SKILL.md` with YAML frontmatter and natural language instructions. The agent reads a compact index of installed skills and loads the full `SKILL.md` on demand when relevant. Skills can also contain scripts and reference files.

**Messages within a session are serialized.** The Command Queue processes one message per session at a time. This is intentional — it prevents tool conflicts and keeps session history consistent.

**MCP is the external tool integration layer.** OpenClaw supports MCP servers for connecting to external services. The agent discovers tools via standard MCP schemas and calls them through a standard interface.

**Onboarding installs the daemon.** `openclaw onboard --install-daemon` sets up the systemd service. Manual unit files are not needed for a standard install.

---

## When editing OpenClaw workspace files

The five core workspace files and what they control:

| File | Purpose |
|------|---------|
| `SOUL.md` | Agent personality, name, tone, communication style |
| `AGENTS.md` | Agent configuration, role definition |
| `TOOLS.md` | What tools and capabilities the agent can use |
| `MEMORY.md` | Durable long-term facts about the user |
| `HEARTBEAT.md` | Proactive task checklist, cron-driven actions |

Daily logs live at `~/.openclaw/workspace/memory/YYYY-MM-DD.md`. These are append-only.

When editing these files, preserve existing content unless explicitly replacing it. They are append-friendly by design.

---

## When writing OpenClaw skills

A skill directory looks like this:

```
my-skill/
├── SKILL.md          (required)
└── references/       (optional)
    └── detail.md
```

Minimal valid `SKILL.md`:

```markdown
---
name: my-skill
description: When to trigger this skill and what it does. Be specific.
---

# My Skill

Instructions here in natural language.
```

Key rules:
- Keep SKILL.md under 500 lines. Use reference files for detail.
- The `description` frontmatter is the triggering mechanism — it must clearly state when and why to use the skill.
- Skills are loaded on demand by the agent, not injected wholesale. Write descriptions that are specific enough to trigger correctly.
- Community skills from ClawHub carry security risk (prompt injection, credential theft have been found in the wild). Always review before installing.

---

## When configuring systemd for OpenClaw

The standard install creates a systemd user or system service via `openclaw onboard --install-daemon`. Check service status with:

```bash
systemctl status openclaw-gateway
journalctl -u openclaw-gateway -f
```

If writing Ansible to manage the service, the correct approach is ensuring the service is enabled and running — not writing a new unit file, since the onboarding wizard creates it.

---

## Read these reference files for more detail

- `references/architecture.md` — Full Gateway architecture, agentic loop, channel adapters, session model, compaction
- `references/workspace.md` — Complete workspace file reference with examples
