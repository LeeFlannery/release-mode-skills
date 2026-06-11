# Example output

> Illustrative excerpt (first two steps of five). **Hooklet is a fictional API** — in a real run every command is executed before delivery, and anything unverifiable is marked.

---

# Receive and Verify Hooklet Webhooks in Node.js

You'll build an Express endpoint that receives Hooklet webhook deliveries, verifies their signatures, and rejects forgeries. By the end you'll see a real delivery logged with a verified signature. Finished code: `github.com/example/hooklet-webhook-tutorial`.

## Prerequisites

- Node.js 22+ (`node --version`)
- A free Hooklet account and one API key from **Dashboard → Keys** (free tier covers this entire tutorial)
- `hooklet` CLI v1.4+ for local tunneling: `npm install -g @hooklet/cli`

## Step 1: Create the endpoint

You need a route that accepts Hooklet's POST deliveries with the **raw** body — signature verification breaks on parsed JSON, so the raw middleware comes first.

```js
// src/server.js
import express from "express";

const app = express();

app.post("/webhooks", express.raw({ type: "application/json" }), (req, res) => {
  console.log("delivery received:", req.headers["hooklet-delivery-id"]);
  res.sendStatus(200);
});

app.listen(3000, () => console.log("listening on :3000"));
```

Run it:

```bash
node src/server.js
```

**Checkpoint:** the terminal prints `listening on :3000`.

## Step 2: Tunnel deliveries to localhost

Hooklet can't reach your laptop, so the CLI opens a tunnel and registers it as a temporary endpoint.

```bash
hooklet listen --forward http://localhost:3000/webhooks
```

**Checkpoint:** the CLI prints a `https://*.hooklet.dev` URL and `forwarding to localhost:3000`. Send a test delivery from **Dashboard → Endpoints → Send test** — your server logs a `delivery received:` line with an ID.

*(Steps 3–5 in the full tutorial: verify signatures with the SDK, reject bad signatures with a 401, handle retries idempotently.)*
