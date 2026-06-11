---
name: sample-app-planner
description: >
  Spec a reference implementation or sample app against a target API or developer product. Trigger when the user says "plan a sample app for X", "what should I build against this API", "spec a reference implementation", or wants a portfolio/interview artifact that demonstrates a specific company's product. Produces a build spec, not the code itself.
---

# Sample App Planner

Given a target API, SDK, or developer product, produce a spec for a small reference implementation that demonstrates the product's core value — sized to actually get built.

## Why this exists

A working sample app against a company's API is the strongest artifact you can bring to a DevRel interview or a consulting pitch. It proves you can do the job before anyone asks. This skill turns "I should build something against X" into a concrete weekend-sized plan.

## Process

### 1. Understand the target

Research the product enough to answer:
- What is the product's **core value proposition** — the one thing it does that competitors don't?
- What does the company showcase in its own docs and demos?
- What do existing community samples already cover? (Don't duplicate the obvious one.)
- What's the auth model and pricing — can this be built on a free tier?

### 2. Pick the use case

The use case must:
- Exercise the product's core value, not a peripheral feature
- Be explainable in one sentence
- Produce something visibly working (a screen, an output, a deployed URL)
- Avoid needing real production data or paid quotas

Offer the user 2-3 candidate use cases with a recommendation, then spec the chosen one.

### 3. Write the spec

```markdown
# Sample App Spec: [name]

**Target product:** [API/SDK]
**One-liner:** [what it does in one sentence]
**Why this use case:** [what core value it demonstrates]
**Context:** [interview artifact for X | sales demo | content source]

## Stack

[Choices with one-line reasons. Default to boring, mainstream choices —
the sample should showcase the target product, not your stack taste.]

## Example

A complete sample of this skill's output: [references/example-output.md](references/example-output.md).

## Scope

In:
- [3-6 features maximum]

Out (explicitly):
- [the tempting extras that would blow the timebox]

## Build plan

1. [milestone — each one ends with something runnable]
2. ...

**Timebox:** [total honest estimate; if it exceeds ~2 days, cut scope]

## README outline

[Sections the finished repo's README needs: what it is, demo gif/link,
quickstart, how it uses the target API, what you'd add next]

## What this proves

[2-3 bullets: the specific competence signals this artifact sends]
```

## Rules

- Weekend-sized or smaller. If the spec can't be built in roughly two days, cut features until it can.
- Every milestone ends runnable. No "big bang at the end" plans.
- The stack serves the demo. Pick what the target company's developers would recognize.
- Flag any cost, quota, or approval gate (API access waitlists, paid tiers) up front.

## Scope

This skill produces the spec. It does not:
- Build the app (do that in a normal coding session with the spec as input)
- Write the tutorial about the app (that's `tutorial-writer`)
- Research the company's org or hiring (that's `company-research`)
