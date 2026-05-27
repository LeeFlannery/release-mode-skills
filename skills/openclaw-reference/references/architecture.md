# OpenClaw Architecture Reference

## The Gateway

The Gateway is the control plane for all OpenClaw activity. It is a single long-lived Node.js process that:
- Listens on WebSocket at `ws://127.0.0.1:18789` (default)
- Manages all channel connections (WhatsApp, Telegram, Slack, Discord, etc.)
- Maintains session state and routing
- Runs the Command Queue

On Linux it runs as a systemd service. On macOS as a LaunchAgent. It should never be exposed directly to the internet — use Tailscale, a reverse proxy, or another secure tunnel for remote access.

## Channel Adapters

Each messaging platform has an adapter that normalizes incoming messages into a consistent internal format before anything reaches the model. WhatsApp uses Baileys, Telegram uses grammY. Voice notes are transcribed before reaching the model. The model always sees clean, structured input regardless of source.

## Session Model and the Command Queue

The Gateway supports multi-agent routing — different agents can handle different channels, contacts, or groups. Each agent maintains its own session: a stateful representation of an ongoing conversation with a unique ID, message history, and serialized execution queue.

The Command Queue processes messages within a session one at a time. This is deliberate: concurrent execution within a session would produce tool conflicts and corrupt history. Concurrency across different sessions is fine.

## The Agentic Loop

Per the official docs, one full agent run is:

> intake → context assembly → model inference → tool execution → streaming replies → persistence

### Context Assembly

Before the model sees anything, the agent runtime assembles a system prompt from:
1. OpenClaw's base instructions
2. A compact skills index (names, descriptions, paths only — not full skill content)
3. Bootstrap workspace files (SOUL.md, AGENTS.md, TOOLS.md)
4. Any per-run overrides

The model reads the skills index and loads full SKILL.md content on demand when it determines a skill is relevant. This keeps base prompts lean regardless of how many skills are installed.

### Model Inference

Context is sent to the configured provider (Anthropic, OpenAI, Google, Ollama, or any OpenAI-compatible endpoint). OpenClaw enforces model-specific context limits and maintains a compaction reserve — a buffer of tokens kept free for the model's response.

### Tool Execution: The ReAct Loop

The model responds with one of two things:
1. A text reply → turn ends, reply is sent
2. A tool call request → runtime executes it, result is fed back into context, loop continues

This Reason + Act cycle continues until the model produces a text reply. Responses stream in real time — tool calls, results, and model reasoning are visible as they happen.

Pseudocode:
```python
while True:
    response = llm.call(context)
    if response.is_text():
        send_reply(response.text)
        break
    if response.is_tool_call():
        result = execute_tool(response.tool_name, response.tool_params)
        context.add_message("tool_result", result)
        # loop continues
```

## Skills Architecture

A skill is a directory containing a `SKILL.md` file with YAML frontmatter and natural language instructions. Optional subdirectories:
- `references/` — detail docs loaded on demand
- `scripts/` — executable code for deterministic tasks
- `assets/` — templates, icons, other static files

The agent never loads all skills into context. It loads a compact index (name + description only) and reads full skill content on demand. This is why the description frontmatter is the primary triggering mechanism.

Skills install from ClawHub (community registry) or from scratch. Security warning: Snyk audits of community skills have found prompt injection, malware, and credential theft in a meaningful fraction. Review all community skills before installing, especially anything touching email, browser, or credentials.

## MCP Integration

OpenClaw supports MCP (Model Context Protocol) servers as a standardized external tool layer. Instead of hardcoding integrations, an MCP server exposes tools with defined schemas. The agent discovers tools, calls them via standard request format, receives structured results. This gives tool portability across any MCP-compatible runtime.

Native MCP support is actively evolving. Community adapters exist today.

## Memory System

Memory lives in plain Markdown files — not a database or vector store.

```
~/.openclaw/workspace/
├── SOUL.md          — personality, name, tone
├── AGENTS.md        — agent role and config
├── TOOLS.md         — available tools and capabilities
├── MEMORY.md        — durable long-term facts
├── HEARTBEAT.md     — proactive task checklist
└── memory/
    ├── 2026-05-17.md  — daily ephemeral log (append-only)
    └── 2026-05-18.md
```

Daily logs are NOT automatically injected into every prompt. The agent loads them on demand via memory tools when relevant. MEMORY.md stores durable facts ("user prefers TypeScript", "never schedule meetings on Fridays"). SOUL.md defines the agent's personality and communication style.

When context would be exceeded, OpenClaw runs compaction: older conversation turns are summarized into compressed entries, preserving semantic content while reducing token count.

## Version Notes (as of May 2026)

- **2.23**: HSTS headers, SSRF policy hardening
- **2.26**: External secrets management, cron reliability fixes (duplicate/hung executions resolved), multi-lingual memory embeddings
- Recent releases: multi-model routing, thread-bound agents
