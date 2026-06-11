# Example output

> Illustrative sample. **Hooklet is a fictional product**; baselines and targets are invented to show the format.

---

# DevRel Metrics Sheet: Hooklet developer program

**Activation definition:** a developer delivers a webhook to their own endpoint (not the dashboard test button) within 7 days of signup.
**Time to first value:** signup → first delivered webhook. Baseline 38 min (audit, 2026-05). Target: under 5 min.

## Funnel

| Stage | Entry marker | Metric | Instrumented? | Current | Target |
|---|---|---|---|---|---|
| Curious | docs visit | unique docs visitors/wk | yes | 4,200 | — |
| Trying | API key issued | keys issued/wk | yes | 310 | 350 |
| Activated | first own-endpoint delivery | activation rate (7d) | **no** | est. 22% | 40% |
| Building | 100+ deliveries/wk | active integrations | yes | 410 | 500 |
| Advocating | public repo / talk / referral | tracked manually | partial | 6/qtr | 10/qtr |

## Leading indicators

| Metric | Definition | Feeds which outcome | Owner | Cadence |
|---|---|---|---|---|
| TTFV | signup → first own-endpoint delivery, median | activation rate | DevRel lead | weekly |
| Quickstart completion | % of key-issuers who reach step 5 | activation rate | DevRel lead | weekly |
| Docs search dead-ends | top queries returning no result | TTFV | docs eng | monthly |
| Sample clones → keys | debugger-repo clones that issue a key in 48h | trying → activated | advocate | monthly |

## Lagging outcomes

| Metric | Definition | Reported to | Cadence |
|---|---|---|---|
| Activation rate | % of new signups activated in 7d | VP Product | monthly |
| Activated → paid conversion | activated devs on paid plan in 90d | CEO | quarterly |

## Instrumentation gaps

Activation isn't measurable today: deliveries aren't joined to signup cohorts. Cheapest start: emit one `first_delivery` event keyed to account age — one sprint, unlocks the whole sheet.

## What we deliberately don't count

- **GitHub stars** — attention, not adoption; clones→keys covers the real question
- **Blog pageviews / social impressions** — inputs to Curious, never reported as outcomes
- **Webinar attendance** — counted only as "attendees who issued a key within 7 days"
