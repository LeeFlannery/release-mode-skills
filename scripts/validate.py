#!/usr/bin/env python3
"""Validate skill frontmatter and README links. Stdlib only.

Checks:
- every skills/*/ contains a SKILL.md
- frontmatter is delimited by --- lines and contains name: and description:
- name: matches the folder name
- every relative link in README.md resolves to an existing path
- every skill folder is linked from README.md
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"

errors: list[str] = []


def check_skill(folder: Path) -> None:
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{folder.name}: missing SKILL.md")
        return
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{folder.name}: SKILL.md does not start with ---")
        return
    try:
        end = next(i for i, l in enumerate(lines[1:], start=1) if l.strip() == "---")
    except StopIteration:
        errors.append(f"{folder.name}: frontmatter never closes")
        return
    fm = lines[1:end]
    name = next((l.split(":", 1)[1].strip() for l in fm if l.startswith("name:")), None)
    if name is None:
        errors.append(f"{folder.name}: frontmatter missing name:")
    elif name != folder.name:
        errors.append(f"{folder.name}: frontmatter name '{name}' != folder name")
    has_desc = any(l.startswith("description:") for l in fm)
    desc_body = [l for l in fm if l.startswith("  ") or (l.startswith("description:") and l.split(":", 1)[1].strip(" >|"))]
    if not has_desc or not desc_body:
        errors.append(f"{folder.name}: frontmatter missing or empty description:")


def check_readme() -> None:
    text = README.read_text(encoding="utf-8")
    linked: set[str] = set()
    for target in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
        path = (ROOT / target).resolve()
        if not path.exists():
            errors.append(f"README: broken link '{target}'")
        if target.startswith("skills/"):
            linked.add(target.strip("/").split("/")[1])
    for folder in sorted(SKILLS.iterdir()):
        if folder.is_dir() and folder.name not in linked:
            errors.append(f"README: skill '{folder.name}' is not listed")


def main() -> int:
    folders = [f for f in sorted(SKILLS.iterdir()) if f.is_dir()]
    if not folders:
        errors.append("no skill folders found")
    for folder in folders:
        check_skill(folder)
    check_readme()
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(folders)} skills validated, README links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
