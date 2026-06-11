# Example output

> Illustrative sample of a written vault file, `tools-services/Hooklet.md`. Hooklet is fictional. Note the conventions: PascalCase filename, domain without protocol, no em dashes in content.

---

```markdown
---
company: Hooklet
website: hooklet.dev
category: freemium
status: evaluating
subscribed: "Free tier"
pricing: "Free: 1k deliveries/mo. Pro: $29/mo, 50k deliveries. Enterprise: contact sales."
offerings: "Webhook delivery infrastructure: signed deliveries, automatic retries, replay API, local tunnel CLI"
last_contact: 2026-06-10
tags: [webhooks, api-infrastructure, developer-tools, freemium]
---

# Hooklet

**What they do:** Managed webhook delivery with signing, retries, and one-click replay so teams stop building their own delivery queues.

## Analysis

Strongest feature is the replay API, which competitors gate behind enterprise plans. Free tier is enough for development and small production loads. Main tradeoff: deliveries route through their infrastructure, so latency-sensitive or compliance-bound teams may need the self-hosted option, which is enterprise-only. Alternatives: Svix (closest, more mature), building on SQS, or raw provider webhooks with hand-rolled retries.

## Notes

Evaluating for the webhook-debugger sample app. Free tier covered the whole build.
```

*Confirmation the skill gives the user:* Written: `~/vaults/tools-services/Hooklet.md`
