# Example output

> Illustrative samples of the two things this skill produces: a pipeline view (read-only) and a record after a stage update. Companies are fictional.

---

## Sample pipeline view ("what needs follow-up")

| Company | Role | Stage | Next action | Due |
|---|---|---|---|---|
| Hooklet | Senior Developer Advocate | interviewing | send panel thank-you notes | 2026-06-11 |
| Quillbase | DX Engineer (contract) | applied | follow up with recruiter | 2026-06-09 ⚠ overdue |
| Ferrostack | Developer Educator | screening | prep for recruiter call | 2026-06-13 |

2 active records omitted (no pending action). 1 closed this month: Driftwave (rejected after onsite).

## Sample record after a stage update

*(Analysis half above the tracking section is untouched — written by `jd-analyzer`, never modified here.)*

```markdown
### Tracking

- **Applied:** yes
- **Date applied:** 2026-05-20
- **Stage:** interviewing
- **Last contact date:** 2026-06-08
- **Next action:** send panel thank-you notes
- **Next action date:** 2026-06-11
- **Outcome:**
- **Notes:**
  - [2026-05-20] Stage changed: not applied → applied
  - [2026-05-28] Stage changed: applied → screening
  - [2026-06-08] Stage changed: screening → interviewing
  - [2026-06-08] Panel was 3 people; demo of webhook-debugger sample landed well. Comp range confirmed verbally.
```
