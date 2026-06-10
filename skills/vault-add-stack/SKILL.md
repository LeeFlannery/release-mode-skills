---
name: vault-add-stack
description: >
  Add a package, library, CLI, framework, runtime, or free/open-source tool to
  the user's stack vault. Trigger on "add X to stack", "track this package /
  library / CLI / framework", "add this dependency", or when the user names
  something installable via a package manager or imported as code. For paid
  hosted products use vault-add-saas instead.
---

# vault-add-stack

Adds an entry to the `stack/` vault (default `~/vaults/stack/`). If the vault
contains a `schema.py`, that file is the authoritative frontmatter contract;
otherwise the template below is.

## Step 1: Research

Web search before writing. Gather: one-sentence summary, repo URL, docs URL,
install command, ecosystem/languages, and maturity/marketshare signals (GitHub
stars, age, release cadence, notable alternatives, adoption).

## Step 2: Classify

`type`: `package` (installable via package manager) | `cli` (command-line tool) |
`library` (vendored/embedded, no package manager) | `framework` (opinionated
full-stack or layer) | `runtime` (execution environment) | `tool` (utility that
fits none of the above).

`status` (default `evaluating`): `active` | `evaluating` | `dropped` |
`watching` | `want-to-try`.

`maturity`: `experimental` | `growing` | `stable` | `legacy` | `abandoned`.

`marketshare`: `niche` | `moderate` | `dominant`.

## Step 3: Write the file

File: `stack/<package-name>.md` -- kebab-case matching the package name. Drop the
scope for scoped packages unless ambiguous (`@tanstack/react-router` ->
`react-router.md`). Frontmatter:

```
---
name: <package-name>
type: <package|cli|library|framework|runtime|tool>
ecosystem: [<language/runtime list>]
install: "<install command>"
repo: <repo URL>
docs: <docs URL>
status: <status>
use_case: "<what problem it solves for the user>"
maturity: <experimental|growing|stable|legacy|abandoned>
marketshare: <niche|moderate|dominant>
added: <today YYYY-MM-DD>
last_reviewed: <today YYYY-MM-DD>
tags: [<3-6 kebab-case tags>]
---

# <name>

**What it does:** <one sentence>

## Analysis
<Why this vs alternatives. Tradeoffs. When you would reach for it.>

## Market Position
<Stars, downloads, notable alternatives, adoption context.>

## Notes

```

## Step 4: Confirm

Tell the user the file is written, one line, show the path. Do not recap the
content.

## Conventions

- **No em dashes** in file content. Use ` -- `, colon, comma, or rewrite.
- If the file already exists, stop and ask the user whether to update it instead.
- The user handles git. Do not commit or push.
- If extra context is given ("I'm using it for X"), put it in `use_case` and Notes.
