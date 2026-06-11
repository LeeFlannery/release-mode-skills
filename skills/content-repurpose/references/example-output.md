# Example output

> Illustrative sample: a fictional tutorial ("Receive and Verify Hooklet Webhooks in Node.js") cut for three platforms. A real batch covers every platform in `platform-specs.md` unless the source is weak somewhere — note the skipped TikTok cut at the bottom.

---

# Repurpose batch: Receive and Verify Hooklet Webhooks in Node.js

**Source:** blog tutorial, 1,800 words
**Core claim:** webhook signature verification fails silently for most people because JSON parsing runs before verification — middleware order is the whole bug.
**CTA:** read the full tutorial

## LinkedIn

Your webhook signature verification is probably broken, and your tests won't tell you.

Here's the bug I see in almost every Express codebase: `express.json()` runs before the verification middleware. Parsing rewrites the body, the signature no longer matches the bytes that were signed, and verification fails — or worse, someone "fixes" it by skipping verification entirely.

The fix is one line of middleware ordering. The raw body parser goes first, on the webhook route only:

app.post("/webhooks", express.raw({ type: "application/json" }), handler)

I wrote up the full pattern — verification, rejection, and idempotent retry handling — in a step-by-step tutorial. Link in the comments.

*Notes: link goes in first comment per spec; no hashtags; post text verified under 1,300 chars.*

## X thread

1/ Most webhook signature verification bugs are the same bug: middleware order.

2/ express.json() parses the body BEFORE your verification runs. The signature was computed over raw bytes. Parsed-then-restringified JSON ≠ those bytes. Verification fails forever.

3/ The fix is one line — raw parser, webhook route only:
app.post("/webhooks", express.raw({ type: "application/json" }), handler)

4/ The dangerous failure mode isn't the error. It's the dev who "fixes" the error by deleting verification. Now every forged payload is a valid request.

5/ Full walkthrough — verify, reject with a 401, handle retries idempotently: [link]

*Notes: 5 tweets, each under 280 chars verified; code tweet renders without wrapping on mobile.*

## YouTube description

Webhook signature verification keeps failing? It's almost always middleware order. In this walkthrough we build an Express endpoint that receives Hooklet webhooks, verifies signatures against the raw body, and rejects forgeries — then handle retries without double-processing.

00:00 The bug: parsed body vs signed bytes
02:10 Raw-body middleware, the right way
05:30 Verifying with the SDK
09:00 Rejecting forgeries with a 401
11:45 Idempotent retry handling

Full written tutorial: [link]
Sample code: [link]

*Notes: chapters assume the existing video edit; update stamps after final cut.*

## Skipped: TikTok/Shorts

No visual moment in this source — the payoff is a middleware ordering concept, not something that reads on a phone screen in 3 seconds. Forcing a cut here would produce a talking-head explainer that underperforms. Suggest instead: screen-record the 401-rejection demo from the tutorial's step 4 as the visual hook if a Short is required.
