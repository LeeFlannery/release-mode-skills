# Example output

> Illustrative sample, 2-minute feature demo. **Hooklet is a fictional product.**

---

# Demo Script: Replay any webhook in one click

**Length target:** 2:00
**Audience:** developers evaluating Hooklet who currently debug webhooks with log archaeology
**Money shot:** a failed delivery replayed and succeeding live, 1:10
**CTA:** free account + the webhook-debugger sample repo

| Time | Talk track | Screen |
|------|-----------|--------|
| 0:00 | A webhook fails at 2 a.m. and your only evidence is a log line. Here's the part that should be illegal: you can't run it again. | terminal showing a 500 in server logs, frozen |
| 0:10 | This is Hooklet. Every delivery it makes is stored, inspectable, and replayable. Let me break something on purpose. | dashboard: Deliveries list, live |
| 0:22 | My endpoint's now returning 500s — watch the retries land. | terminal: flip `SIMULATE_FAILURE=true`, restart; dashboard shows delivery going red, retry counter ticking |
| 0:45 | Each attempt is right here: payload, headers, signature check, response body. No grepping. | click the failed delivery, scroll the attempt detail |
| 1:05 | Now I fix my endpoint... and this is the whole pitch: | terminal: flip the flag back, restart |
| 1:10 | ...one click. Same payload, same headers, delivered. | click **Replay** — delivery row turns green |
| 1:25 | That replay came through the API, which means your support team can do it from a script, not a dashboard. | editor: 6-line replay snippet using the SDK |
| 1:45 | Free tier covers all of this. Grab a key, clone the debugger sample below, and break things on purpose. | end card: signup URL + repo URL |

## Prep checklist

- Terminal font 18pt+, dark theme, single window; editor with only the snippet file open
- Dashboard pre-logged-in, Deliveries page, seeded with ~10 green deliveries
- `SIMULATE_FAILURE` flag tested both directions twice before recording
- Notifications off, menu bar hidden, browser bookmarks bar hidden
- Word count: ~210 words ≈ 1:37 spoken — fits 2:00 with demo pauses
