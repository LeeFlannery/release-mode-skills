# Example output

> Illustrative sample. **Hooklet is a fictional webhook-delivery API**; the spec shows the shape and sizing the skill produces.

---

# Sample App Spec: webhook-debugger

**Target product:** Hooklet API
**One-liner:** A local dashboard that receives, inspects, and replays your Hooklet webhook deliveries in real time.
**Why this use case:** Hooklet's core value is reliable delivery with replay — this app makes replay *visible*, which their own demos don't.
**Context:** interview artifact for Hooklet's Senior Developer Advocate role

## Stack

- **Next.js + TypeScript** — what Hooklet's own samples use; zero stack friction for their reviewers
- **SQLite via Drizzle** — delivery log persistence without infra
- **Hooklet Node SDK** — exercises the SDK, not just raw HTTP (SDK gaps become interview material)

## Scope

In:
- Receive deliveries on a local tunnel endpoint and list them live
- Inspect payload, headers, signature verification result per delivery
- One-click replay of any delivery via the Hooklet replay API
- Failure simulation toggle (return 500s) to show retry behavior

Out (explicitly):
- Auth/multi-user, deploy story, payload editing, metrics dashboards

## Build plan

1. Endpoint + tunnel receiving real deliveries, logged to console — *runnable*
2. SQLite persistence + live list UI — *runnable*
3. Detail view with signature verification — *runnable*
4. Replay button + failure-simulation toggle — *runnable, demo-ready*

**Timebox:** ~1.5 days. Replay API is the only unknown; it's on the free tier (verified — no quota gate).

## README outline

What it is (one line + gif) → Quickstart (under 5 min, two commands) → How it uses Hooklet (signature verification, replay API, retry semantics) → What I'd add next

## What this proves

- Can ship against their API on their stack without hand-holding
- Found and exercised the replay API their own samples skip
- Understands what *their* buyers struggle with (delivery debugging), not just what's easy to demo
