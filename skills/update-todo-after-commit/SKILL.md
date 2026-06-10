---
name: update-todo-after-commit
description: Keep TODO.md synchronized with repository work after commits. Use when the user asks to commit changes, asks what changed after a commit, asks to keep TODO/checklists current, or when a commit has just been created and the repository contains a TODO.md, roadmap, or project task list that may need updates.
---

# Update TODO After Commit

## Workflow

After a successful commit, inspect the committed diff and update the project task list when the commit changes planned work, completes planned work, creates new follow-up work, or invalidates an existing TODO item.

1. Identify the committed range:
   - Prefer `git show --stat --oneline --name-only HEAD` for the latest commit.
   - Use `git show --name-only --format=fuller HEAD` if the commit message or touched files are ambiguous.
   - If the user committed a different revision, inspect that revision instead of `HEAD`.

2. Find task-list files:
   - Prefer repo-root `TODO.md` when present.
   - Also check obvious roadmap files only if the commit touched docs or the user asks broadly: `README.md`, `CLAUDE.md`, `AGENTS.md`, `ROADMAP.md`, `DATA_CAPABILITIES.md`.
   - Do not invent a TODO file if none exists unless the user asks.

3. Decide whether to edit `TODO.md`:
   - Mark an item complete when the commit clearly implemented it.
   - Add follow-up items when the commit intentionally leaves known next steps, partial implementations, OAuth gaps, manual work, or validation gaps.
   - Revise stale wording when implementation details changed.
   - Leave TODO unchanged when the commit is unrelated to planned work or the existing TODO is already accurate.

4. Keep edits small and factual:
   - Preserve the file's existing sections and checklist style.
   - Use concrete task names and implementation nouns from the repo.
   - Do not add AI attribution, generated-by text, or co-author trailers.
   - Avoid turning TODO into a changelog. Completed items can remain checked if useful, but long historical detail belongs elsewhere.

5. Validate and commit TODO updates:
   - Run a quick read of the edited TODO section.
   - If only docs/TODO changed, no build is required unless the docs are generated or tested by the project.
   - Commit the TODO update separately with a terse conventional message such as `docs: update todo after commit`.
   - If the user asked for a single combined commit and the original commit has not happened yet, update TODO before committing the combined changes.

## Guardrails

- Never modify ignored local files such as `.env` while doing this workflow.
- Never rewrite, amend, or reset the user's commit unless explicitly asked.
- Do not mark work complete just because files were touched; the diff must show the task was actually delivered.
- If unsure whether an item is complete, add or preserve a follow-up item instead of checking it off.
- If a commit introduces a stub, scaffold, or partial implementation, record the remaining real-data or productionization step.

## Useful Commands

```bash
git show --stat --oneline --name-only HEAD
sed -n '1,220p' TODO.md
git diff -- TODO.md
git add TODO.md
git commit -m "docs: update todo after commit"
```
