# Example output

> Illustrative sample of the report a docs-sync run delivers alongside its edits. The project ("hooklet-go") is fictional.

---

# Docs sync report: hooklet-go

**Audited:** README.md, docs/ (4 files), CONTRIBUTING.md — against source at commit `a3f91c2`

## Drift found and fixed

| Doc | Claim | Reality in source | Fix applied |
|---|---|---|---|
| README quickstart | `hooklet init --key` | flag renamed to `--api-key` in v0.9 (`cmd/init.go:34`) | command updated |
| README | "requires Go 1.21+" | `go.mod` says `go 1.23` | prerequisite bumped |
| docs/retries.md | default backoff "3 attempts" | `retry.go:18` defaults to 5 | corrected, linked to source |
| docs/api.md | documents `DeliverSync()` | removed in v0.9, no deprecation note existed | section deleted, changelog pointer added |
| CONTRIBUTING.md | `make test` | Makefile target renamed to `make check` | command updated |

## Undocumented surface (added)

- `HOOKLET_TIMEOUT_MS` env var (read in `config.go:41`) — added to docs/configuration.md
- `--dry-run` flag on `hooklet send` — added to README quickstart

## Verification

- `mkdocs build --strict`: pass (was failing on two dead internal links, now fixed)
- Every README quickstart command run in a clean container: all exit 0

## Not changed (needs a human call)

- docs/architecture.md describes the queue as "Redis-backed"; source now supports Redis **or** NATS. Both are documented as options now, but the diagram still shows Redis only — needs a redrawn asset.
