---
name: commit-validator
description: >
  Validates git commits for quality and safety. Trigger before any commit operation to check for: AI attribution, single-focus commits, secrets in the diff, and conventional commit message format. Also trigger when the user asks to review commit hygiene or clean up commit history.
---

# Commit Validator

Validate git commits for quality, safety, and consistency.

## Validation Rules

### 1. Single Focus

- One commit = one logical change.
- No unrelated changes in the same commit.
- Commit message describes a single, focused purpose.

Good: `feat: add user authentication middleware`
Bad: `feat: add auth and fix bugs and update docs`

### 2. No Secrets in Diff

Before committing, scan for:

- API keys or tokens
- Passwords or credentials
- Private keys (RSA, SSH, etc.)
- `.env` file contents
- Database connection strings with passwords
- Cloud provider credentials (AWS, Azure, GCP)

If found: block the commit immediately and alert the user.

### 3. Commit Message Format

```
<type>: <description>

[optional body with details]
```

Types:

| Type | Use for |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Test additions/changes |
| `chore` | Maintenance tasks |

### 4. Pre-Commit Requirements

- All relevant tests should pass.
- No linting or formatting errors.
- Code has been reviewed (at minimum, self-reviewed).

## On Validation Failure

1. Block the commit.
2. Explain which rule was broken.
3. Provide specific steps to fix.
4. Require user confirmation before proceeding.
