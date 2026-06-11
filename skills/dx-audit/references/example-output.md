# Example output

> This one is real: the skill run against **this repo's own install experience**, June 2026. The blocker below is why the README's clone URL got fixed and CI got added.

---

# DX Audit: release-mode-skills (install experience)

**Date:** 2026-06-10
**First-value moment:** a skill from this repo triggers correctly inside the user's agent
**Time to first value:** 1m 40s via `npx skills` (target for this category: CLI tool, under 5 minutes)
**Steps to first value:** 3 (1 of which is a context switch — restarting the agent)

## Summary

Install via `npx skills add` is well inside the CLI benchmark. The manual path had a blocker: the README's clone URL pointed at a GitHub org that doesn't host the repo, so the documented copy-paste path failed at step one. Fixed; CI now link-checks the README on every push to prevent regression.

## Findings

### blocker — README clone URL pointed at the wrong org
- **Where:** README.md, Install section (`git clone https://github.com/releasemodellc/...`)
- **What happened:** clone returned `repository not found`; the repo lives under `LeeFlannery/`
- **Expected:** the first command in the install docs works as pasted
- **Fix:** correct the URL; add a CI link check so the README can't drift again *(both shipped)*

### minor — agent restart requirement is easy to miss
- **Where:** README.md, single line after the install commands
- **What happened:** a skill installed mid-session doesn't trigger until restart; the note is one unemphasized sentence
- **Expected:** the docs call out the one step that makes installs look broken
- **Fix:** keep the note adjacent to every install path, not just the last one

### polish — no per-skill install verification step
- **Where:** README.md, Install section
- **What happened:** nothing tells the user how to confirm a skill is active
- **Expected:** a "say this to your agent and X should happen" checkpoint
- **Fix:** add a one-line trigger test, e.g. paste a changelog and expect `release-notes` to activate

## Quick wins

1. Fix the clone URL *(shipped)*
2. CI link check on the README *(shipped)*
3. Add a trigger-test checkpoint to the Install section
