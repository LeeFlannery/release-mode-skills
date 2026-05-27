---
name: env-separator
description: >
  Enforces strict separation between test and production environments. Trigger when creating test infrastructure, writing test configuration, setting up database connections in tests, or any operation where test and production environments could mix. Also trigger on review of CI/CD pipelines, Docker configs, or environment variable files.
---

# Environment Separator

Enforce strict separation between test and production environments.

## The Three Laws of Environment Separation

1. **Production Code First** — Production code MUST be created before test code.
2. **Separate Instances** — Test and production MUST use separate service instances.
3. **No Data Mixing** — Test data must NEVER contaminate production databases.

## Pre-Flight Checklist

Before creating test code or running tests:

- [ ] Production implementation exists and is functional
- [ ] Test environment uses separate database/service instances
- [ ] Test data will not leak to production
- [ ] Separate user accounts for test vs production
- [ ] Test credentials are isolated from production

## Forbidden Patterns

1. **Tests writing to production databases** — Database connection strings in test files pointing to prod.
2. **Test fixtures in production code paths** — Mock data or test fixtures imported in production code.
3. **Shared database instances** — Same host/database name for test and prod, even with different schemas.
4. **Test credentials in production configs** — Test keys or passwords in production configuration files.
5. **Production data in tests without sanitization** — Real user data or PII in test fixtures.
6. **Same service instance for test and production** — Shared URLs, shared containers, shared VMs.

## Detection Patterns

Watch for these red flags:

```
DATABASE_URL=postgresql://prod-host/...  # In test files
API_ENDPOINT=https://api.production.com  # In test config
api_key = "sk-live-..."                  # Live keys in tests
users = fetch_real_users()               # Real data in tests
```

## When Uncertain

If you cannot verify environment separation:

1. HALT the operation immediately.
2. Ask the user to confirm environment boundaries.
3. Request explicit confirmation of test database location, production database location, and service instance separation.
4. Do NOT proceed until separation is guaranteed.

## Acceptable Test Patterns

- Separate database server or container
- In-memory databases (SQLite, H2)
- Ephemeral test databases (created/destroyed per run)
- Mock/stub services instead of real services
- Environment variables for test configuration
