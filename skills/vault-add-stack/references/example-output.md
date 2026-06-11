# Example output

> Illustrative sample of a written vault file, `stack/drizzle-orm.md`. Note the conventions: kebab-case filename matching the package, no em dashes in content.

---

```markdown
---
name: drizzle-orm
type: package
ecosystem: [typescript, node, bun]
install: "bun add drizzle-orm"
repo: https://github.com/drizzle-team/drizzle-orm
docs: https://orm.drizzle.team
status: active
use_case: "Typed SQL access for sample apps; SQLite persistence without infra"
maturity: stable
marketshare: moderate
added: 2026-06-10
last_reviewed: 2026-06-10
tags: [orm, sql, typescript, sqlite, postgres]
---

# drizzle-orm

**What it does:** TypeScript ORM that stays close to SQL, with schema-as-code and zero runtime dependencies.

## Analysis

Picked over Prisma for sample apps: no codegen step, no separate schema language, and the query builder reads like SQL so tutorials stay teachable. Tradeoff: migrations tooling is younger than Prisma Migrate, and the docs assume comfort with SQL. Reach for it when the database is part of what you are demonstrating; reach for Prisma when the team wants guardrails over control.

## Market Position

Fast-growing since 2023, now a default in the Bun and serverless crowd. Prisma still dominates job postings and enterprise use. Notable alternatives: Prisma, Kysely (query builder only), plain better-sqlite3.

## Notes

Used in the webhook-debugger sample for delivery-log persistence.
```

*Confirmation the skill gives the user:* Written: `~/vaults/stack/drizzle-orm.md`
