---
name: devrel-metrics
description: >
  Design a metrics framework for a DevRel program or developer product. Trigger when the user asks "how do we measure DevRel", "build a metrics sheet", "define developer activation", "what KPIs should developer relations have", or needs to defend devrel work with numbers. Anchored on developer activation and time to first value, with explicit anti-vanity-metric rules.
---

# DevRel Metrics

Design a metrics framework that ties developer-facing work to outcomes a business actually cares about. The anchor metrics are **developer activation** and **time to first value** — everything else hangs off those.

## Process

### 1. Define the activation moment

Work with the user to define, for their specific product, the moment a developer stops evaluating and starts succeeding. Good activation definitions are:
- **Observable** in product data (an API call, a deploy, a second session)
- **Meaningful** — correlated with sticking around, not just clicking around
- **Close to value** — "made first successful API call with their own data", not "created an account"

Then define **time to first value**: wall-clock time from first touch (docs visit, signup) to the activation moment.

### 2. Map the funnel

```
Aware → Curious → Trying → Activated → Building → Advocating
```

For each stage: what marks entry, what's measurable today, what's not instrumented yet. Most devrel funnels leak worst between Trying and Activated — that's where `dx-audit` findings convert into metric improvements.

### 3. Separate leading from lagging

- **Lagging** (what the business reports): activated developers, retention, developer-sourced revenue/expansion
- **Leading** (what devrel can move this quarter): TTFV, quickstart completion rate, docs-search success, support deflection, sample-app clones-to-keys ratio

Every leading metric must have a stated hypothesis about which lagging metric it feeds. If nobody can say what a metric leads to, it doesn't make the sheet.

### 4. Produce the metrics sheet

```markdown
# DevRel Metrics Sheet: [program/product]

**Activation definition:** [one sentence]
**Time to first value:** [definition + current baseline if known + target]

## Funnel

| Stage | Entry marker | Metric | Instrumented? | Current | Target |
|---|---|---|---|---|---|

## Leading indicators

| Metric | Definition | Feeds which outcome | Owner | Cadence |
|---|---|---|---|---|

## Lagging outcomes

| Metric | Definition | Reported to | Cadence |
|---|---|---|---|

## Instrumentation gaps

[What can't be measured today and the cheapest way to start:
docs analytics, key-issuance events, funnel events, UTM discipline]

## What we deliberately don't count

[The vanity metrics this program refuses, and why — see rules below]
```

## Anti-vanity rules

- **Reach without a next step is not a metric.** Views, impressions, and follower counts only count as inputs to a funnel stage, never as outcomes.
- **Activity is not impact.** "Published 12 posts, gave 4 talks" is a work log, not a metrics sheet.
- **GitHub stars measure attention, not adoption.** Pair them with clones, dependents, or key issuance or leave them out.
- **Attendance is not activation.** Workshop signups count when paired with what attendees did afterward.
- If a metric can be moved without any developer being better off, it's vanity. Cut it.

## Rules

- Fewer metrics, defended harder: a sheet with 6 metrics someone checks beats 25 nobody does.
- Every metric gets an owner and a cadence or it's deleted.
- Be honest about attribution limits. DevRel influence is often directional, not causal — say so in the sheet rather than overclaiming.

## Example

A complete sample of this skill's output: [references/example-output.md](references/example-output.md).

## Scope

This skill designs the measurement framework. It does not:
- Implement analytics or dashboards
- Run the DX audit that improves the numbers (that's `dx-audit`)
- Write the report narrative for stakeholders (it gives you the numbers' structure; the story is yours)
