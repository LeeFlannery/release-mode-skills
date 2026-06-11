---
name: cfp-writer
description: >
  Write a conference talk proposal from a topic and the speaker's background. Trigger when the user asks to "write a CFP", "submit a talk to X", "draft a conference proposal", or "turn this project/post into a talk". Asks for the CFP's actual constraints before drafting, then produces title options, abstract, outline, and bio.
---

# CFP Writer

Turn a topic and a speaker's real experience into a talk proposal reviewers accept.

## Step 1: Get the CFP's actual constraints

Before drafting, ask for (or read from a provided CFP link/text):
- Abstract length limit and any separate fields (elevator pitch, talk details, audience takeaways)
- Talk formats and lengths offered
- The conference's audience and selection bent (intro-friendly? hard-technical? case-study-driven?)
- Submission deadline and whether it's anonymized review (anonymized = no self-references in the abstract)

Drafting to imaginary constraints wastes the work. If the user has no CFP yet, draft to a generic 200-word abstract and flag it.

## Step 2: Find the talk inside the topic

A topic is not a talk. Work with the user to sharpen:
- **The claim:** what will the audience believe after that they didn't before?
- **The evidence:** what real experience backs it — a project shipped, a failure survived, data gathered? Talks built on the speaker's actual scars beat surveys of a topic.
- **The takeaway:** what can attendees *do* Monday morning?

If the user's material is thin, say so and identify what experience they do have that's talk-worthy.

## Step 3: Draft

```markdown
# CFP: [conference]

**Format:** [chosen format/length]
**Deadline:** [date]

## Title options

1. [specific + outcome or tension: "We Cut Onboarding From 14 Steps to 6.
   Here's What Fought Back."]
2. [alternate angle]
3. [safer/conventional option]

## Abstract ([X words / limit Y])

[Hook sentence — the tension or claim. What the talk covers, concretely.
Who it's for. What they leave with. Written to the reviewer AND the
attendee scanning a schedule.]

## Audience takeaways

- [3, each actionable]

## Outline (for the details field / reviewer notes)

- [minute-budgeted beats: problem (5) → story/demo (15) → lessons (8) → Q&A (2)]

## Bio ([X words])

[Relevant credibility for THIS talk, not a resume. Why is this person
the right one to give it?]

## Reviewer notes (if the CFP has the field)

[Why this conference, why now, what's new vs. existing talks on the topic.
Mention prior speaking honestly — including "first-time speaker" if true;
many conferences actively want them.]
```

## Writing rules

- Specific beats comprehensive. "How we measured developer activation at a 12-person startup" outranks "The State of DevRel Metrics" in every review pile.
- No clickbait the talk can't pay off. Reviewers have seen everything.
- Promise only what fits the time slot. A 30-minute talk holds one claim well.
- Never invent the speaker's experience, credentials, or war stories. The bio and evidence come from what the user actually did.
- Match abstract length limits exactly — overlong abstracts get truncated or binned.

## Example

A complete sample of this skill's output: [references/example-output.md](references/example-output.md).

## Scope

This skill writes the proposal. It does not:
- Write the talk or slides (script the demo portion with `demo-script` later)
- Submit anything
- Find conferences to submit to (it can suggest fit criteria if asked, but no scanning)
