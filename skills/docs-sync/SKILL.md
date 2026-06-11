---
name: docs-sync
description: >
  Audit and update project documentation so it matches the actual source code. Trigger when the user says docs are stale, asks to "sync the docs", "update the README", "audit documentation", or after a session of changes that likely outdated the docs. Reads the real codebase first — never guesses — then rewrites README and docs files to match reality.
---

# Docs Sync

Audit all project documentation against the actual source, then update every doc that has drifted. No guessing — read the real code.

## Step 1: Discover the doc surface

Find what documentation exists:

- `README.md` at the repo root
- A `docs/` directory
- A doc generator config: `mkdocs.yml`, `docusaurus.config.*`, `astro.config.*` with Starlight, `book.toml`, etc.
- Other common docs: `CONTRIBUTING.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `AGENTS.md`/`CLAUDE.md`

## Step 2: Read the source

Read the parts of the codebase the docs describe:

- Entry points, public APIs, exported functions
- Route/endpoint definitions (pull request/response shapes from the actual handlers, not from memory)
- Data models and schemas
- Config files, environment variables, CLI flags
- Build/run scripts (`package.json` scripts, `Makefile`, `justfile`)

## Step 3: Audit and sync

For each doc file, compare claims against the source. Fix anything that's wrong, stale, or missing:

- Commands that no longer work or have changed flags
- API endpoints, parameters, or response shapes that drifted
- Architecture descriptions that no longer match the layout
- Setup steps missing new prerequisites
- Features that shipped but aren't documented
- Features documented but removed

Keep the README short: what it is, the stack, a quickstart, a link to full docs.

## Step 4: Verify

- If a doc generator exists, build it and fix breakage before finishing (e.g. `mkdocs build --strict`, `npm run docs:build`)
- Check that internal doc links resolve
- Check that every command in a quickstart actually runs

## Style defaults

Unless the project has its own style guide:

- Short sentences
- Code blocks for every command and schema snippet
- No filler phrases ("In order to...", "It is worth noting...")
- No "simply" or "just" in instructions

## Rules

- Read the source before editing any doc. Never document from assumption.
- Preserve the project's existing doc structure and voice unless asked to restructure.
- Do not commit or push — leave that to the user.

## Example

A complete sample of this skill's output: [references/example-output.md](references/example-output.md).

## Scope

This skill syncs existing documentation to match the code. It does not:
- Write tutorials or blog posts (that's `tutorial-writer`)
- Generate release notes (that's `release-notes`)
- Create a docs site from scratch (it can recommend one, but ask first)
