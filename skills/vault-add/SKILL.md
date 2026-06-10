---
name: vault-add
description: >
  Dispatcher for adding an entry to the user's personal vaults. Trigger when the
  user says "add X to the vault", "track this", "add this", "look it up and add
  it", or names a tool/package/company/role/lead to record without making the
  target vault obvious. Figure out which of the four vaults it belongs to, then
  hand off to the matching sub-skill: vault-add-saas, vault-add-stack,
  vault-add-job, or vault-add-client. If the vault is already obvious from how
  the user phrased it, the specific sub-skill triggers directly and this
  dispatcher is not needed.
---

# vault-add (dispatcher)

The user keeps a personal knowledge base of markdown vaults (root path is
user-configurable; default `~/vaults/`). This skill routes an "add this" request
to the right per-vault sub-skill. Each sub-skill owns its own research,
classification, schema, and file template.

Read `references/conventions.md` for the shared rules (file location, naming,
no-em-dashes, git). If a vault folder contains a `schema.py`, that file is the
authoritative frontmatter contract.

## Routing

Decide which vault the thing belongs to, then invoke that sub-skill:

| If it is... | Vault | Sub-skill |
|-------------|-------|-----------|
| A paid SaaS, freemium product, paid software, or course/community | `tools-services/` | **vault-add-saas** |
| A package, library, CLI, framework, runtime, or free/open-source tool | `stack/` | **vault-add-stack** |
| A job, role, recruiter outreach, or application | `job-search/` | **vault-add-job** |
| A freelance / consulting lead or potential client | `potential-clients/` | **vault-add-client** |

### Disambiguation

- Has a pricing page and charges money, used as a product -> **vault-add-saas**.
- Installable via a package manager / it is code you import or run -> **vault-add-stack**.
  (Bun is a runtime -> stack. Linear is a paid SaaS -> tools-services.)
- A company reached out about a W2/contract role, or the user is applying -> **vault-add-job**.
- A company or person who might pay the user for freelance/consulting work -> **vault-add-client**.

If the user already said the vault ("add X to stack", "track this client"), skip
straight to that sub-skill. If it is genuinely ambiguous between two vaults,
ask the user one short question before handing off.

## Handoff

Once the vault is decided, load and follow the matching sub-skill. Do not write
the file from this dispatcher; the sub-skill owns the schema and template.
