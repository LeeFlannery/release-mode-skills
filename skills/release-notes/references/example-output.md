# Example output

> Illustrative sample. **Hooklet is a fictional SDK** — in a real run every line traces to a commit or PR in the actual diff.

---

# @hooklet/sdk v2.0.0

Signature verification is now async-first and the retry API got the overhaul the issue tracker has been asking for. One breaking change — budget ten minutes for the migration.

## Breaking changes

### `verifySignature()` now returns a Promise

Synchronous verification blocked the event loop on large payloads (#412). The method is now async; the sync variant is gone.

```js
// before (v1.x)
const ok = client.verifySignature(payload, header);

// after (v2.0)
const ok = await client.verifySignature(payload, header);
```

If you can't go async at the call site, `verifySignatureSync()` remains available but logs a deprecation warning and will be removed in v3.

## New

- **`client.deliveries.replay(id)`** — replay any stored delivery from code; previously dashboard-only (#388)
- **Configurable backoff** — `new Client({ retry: { attempts, strategy } })` accepts `"exponential"` or `"linear"` (#395)
- **TypeScript: `DeliveryEvent` is now generic** — `DeliveryEvent<MyPayload>` types your handler payloads end to end

## Fixed

- Crash when `HOOKLET_TIMEOUT_MS` was set but empty (#401)
- Retry counter reset on process restart, causing infinite retry loops against dead endpoints (#407)
- `hooklet listen` tunnel URLs now survive laptop sleep (#391)

## Upgrade

```bash
npm install @hooklet/sdk@2
```
