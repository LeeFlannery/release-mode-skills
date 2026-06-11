---
name: vault-add-saas
description: >
  Add a paid SaaS, freemium product, paid software, or course/community to the
  user's tools-services vault. Trigger on "add X to tools-services", "track this
  SaaS / subscription / paid tool", "add this product", or when the user names a
  hosted/paid product they use or evaluated and want recorded. For packages,
  libraries, and CLIs use vault-add-stack instead.
---

# vault-add-saas

Adds an entry to the `tools-services/` vault (default
`~/vaults/tools-services/`). If the vault contains a `schema.py`, that file is
the authoritative frontmatter contract; otherwise the template below is.

## Step 1: Research

Web search the product before writing anything. Gather: one-sentence summary,
website, pricing tiers (free / freemium / paid / contact-sales), key offerings,
and notable alternatives. The file should be accurate, not a stub.

## Step 2: Classify

`category` (pick one): `saas` (cloud-hosted subscription product) |
`freemium` (meaningful free tier + paid upgrade) | `paid-tool` (one-time or
licensed desktop/CLI) | `course-community` (paid learning platform / community).

`status` (default `evaluating` unless the user says otherwise):
`active-use` | `evaluating` | `dropped` | `watching` | `want-to-try`.

## Step 3: Write the file

File: `tools-services/<CompanyName>.md` -- PascalCase, no spaces.
Frontmatter:

```
---
company: <Name>
website: <domain only, no https://>
category: <saas|freemium|paid-tool|course-community>
status: <status>
subscribed: "No"          # Yes | No | Free tier | <plan name>
pricing: "<free tier info, paid tier info>"
offerings: "<what it does, key features>"
last_contact: <today YYYY-MM-DD>
tags: [<3-6 kebab-case tags>]
---

# <Name>

**What they do:** <one sentence>

## Analysis
<Why someone uses this. Key tradeoffs. Alternatives.>

## Notes

```

## Step 4: Confirm

Tell the user the file is written, one line, show the path. Do not recap the
content.

## Conventions

- **No em dashes** in file content. Use ` -- `, colon, comma, or rewrite.
- If the file already exists, stop and ask the user whether to update it instead.
- The user handles git. Do not commit or push.
- If a tool cannot be found, tell the user what is missing and ask them to fill
  the gaps before writing.

## Example

A complete sample of this skill's output: [references/example-output.md](references/example-output.md).
