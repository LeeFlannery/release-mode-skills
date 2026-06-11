# Example output

> Illustrative sample. **Hooklet is a fictional company**; every fact, person, and source below is invented to show the format. A real brief cites real URLs.

---

# Research Brief: Hooklet

**Date:** 2026-05-12
**Context:** consulting pitch (DX audit + onboarding overhaul)

## TL;DR

Hooklet is a Series B webhook-delivery platform whose product is loved and whose onboarding is visibly losing them developers — their own community forum's top thread is a setup complaint. DevRel reports to marketing, which explains the content-heavy, product-light output. The winning angle: arrive with evidence (a timed walkthrough of their quickstart) rather than a pitch deck, and frame the engagement as moving a number they already report (trial-to-paid conversion).

## Org

- DevRel sits under VP Marketing (source: two LinkedIn profiles list "Developer Relations — Marketing org"). No DevRel presence in engineering RFCs. *(inference: weak product loop)*
- Team of 3: one lead (ex-Stripe docs), two advocates. Lead posted in March about "finally getting eng buy-in for docs fixes" — friction confirmed. *(source: personal blog)*

## Product and developer strategy

- Shipped in last 12 months: Go SDK, Terraform provider, usage-based pricing tier *(source: changelog)*
- Public roadmap lists "redesigned onboarding" under "exploring" for two consecutive quarters — stalled internally *(source: public roadmap board)*
- Quickstart requires dashboard signup, two API keys, and a CLI install before the first delivered webhook — 11 steps total *(source: docs walkthrough, 2026-05-11)*

## Feedback loop

**Verdict: walled-off, with one bridge.** DevRel doesn't appear in issues or RFCs, but the docs lead personally triages the `documentation` label on GitHub — that person is the entry point.

## People

- **Maya Trent, DevRel lead** — ex-Stripe, speaks at API World, writes about docs-as-product. Connection point: shared opinion that quickstarts should be timed in CI.
- **Dev Okafor, VP Marketing** — owns the budget; public OKR mentions "developer signups" *(source: podcast interview)*.

## Signals and risks

- $30M Series B nine months ago; hiring across eng, not DevRel — consulting budget plausible, headcount unlikely.
- Community sentiment: product praised, onboarding criticized in 4 of the top 10 forum threads.

## Angles

1. Bring a timed TTFV measurement of their own quickstart to the first call (supports: 11-step finding).
2. Frame around "developer signups" — the VP's stated OKR — not docs quality.
3. Offer Maya the CI-timed-quickstart idea as a shared artifact; she's championed it publicly.
4. Anchor scope to the stalled "redesigned onboarding" roadmap item — budget already wants this.

## Open questions

- Who owns trial-to-paid conversion as a number? (Ask: "When onboarding improves, whose dashboard moves?")
- Is the Terraform provider strategic or a one-off? (Ask Maya directly.)
