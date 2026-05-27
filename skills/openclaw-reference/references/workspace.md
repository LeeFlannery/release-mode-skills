# OpenClaw Workspace File Reference

All workspace files live at `~/.openclaw/workspace/`. They are plain Markdown. Agents load them on demand — not injected automatically into every prompt.

---

## SOUL.md

Defines the agent's identity. What makes it feel like your assistant rather than a generic bot.

Typical contents:
- Agent name
- Personality and tone
- Communication style preferences
- Things the agent should always or never do
- User-specific context the agent should internalize

Example:
```markdown
# Soul

You are Cleo, a direct and capable assistant running on surfer-rosa.

Tone: concise, technical, no filler. Assume the user is an engineer.
Never apologize for doing your job.
Prefer action over asking for clarification when intent is clear.
```

---

## AGENTS.md

Defines agent roles, routing rules, and configuration. In a multi-agent setup, this file describes which agent handles which channels or contact groups.

Typical contents:
- Agent definitions (name, channel, scope)
- Routing rules
- Per-agent capability grants

---

## TOOLS.md

Governs what tools and capabilities the agent can use. Controls the tool surface the agent is allowed to call.

Typical contents:
- Enabled/disabled tool categories
- Tool-specific configuration
- Permission scopes

---

## MEMORY.md

Long-term facts the agent has learned and should remember across all conversations. Written by the agent during compaction or explicitly by the user.

Typical contents:
- User preferences ("prefers TypeScript over JavaScript")
- Recurring constraints ("never schedule meetings before 9am")
- Stack and environment facts ("primary machine is surfer-rosa, Arch Linux")
- Project context that should always be available

This file grows over time. The agent appends to it; it is not a log. Edit directly to correct or remove facts.

---

## HEARTBEAT.md

The proactive task checklist. OpenClaw wakes on a configurable heartbeat interval and works through this file without being prompted.

Typical contents:
- Scheduled checks ("every morning, summarize unread email")
- Recurring automations ("every Sunday, review the week's calendar")
- Watchdog tasks ("if surfer-rosa disk usage exceeds 80%, send Telegram alert")

Format is flexible — natural language instructions the agent can follow. Be specific about triggers and frequency.

Note: version 2.26 fixed serious cron reliability issues (duplicate and hung executions). On older versions, heartbeat tasks may have run multiple times or not at all.

---

## memory/YYYY-MM-DD.md

Daily ephemeral logs. Append-only. One file per day.

The agent writes to these during runs — what it did, what it decided, what it observed. They are NOT injected into every prompt. The agent retrieves them on demand via memory tools when the current task makes past context relevant.

Do not edit these manually unless correcting an error. Let the agent maintain them.

---

## File editing guidelines

When modifying workspace files programmatically:
- Preserve existing content unless explicitly replacing a section
- Append new facts to MEMORY.md rather than rewriting
- HEARTBEAT.md entries should be self-contained — each task should make sense without requiring the agent to read the others
- SOUL.md changes take effect on the next agent run — no restart needed
- The Gateway does not need to be restarted when workspace files change
