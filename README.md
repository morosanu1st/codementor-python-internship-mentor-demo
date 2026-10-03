# Python Internship Mentoring Demo

A small Codementor-style sample showing how I mentor Python learners toward **internship-ready habits**: clean structure, deliberate practice, and code review that teaches.

## What this repo demonstrates

- Tiny project layout (`scripts/`, `exercises/`) instead of one-off scripts
- Sample exercise outline covering lists, dicts, functions, and OOP
- A mentoring plan you can expect in a weekly 1:1

## Mentoring plan (typical 4–6 weeks)

| Week | Focus | Outcome |
|------|--------|---------|
| 1 | Core types + control flow | Comfortable with lists/dicts; write small pure functions |
| 2 | Functions, modules, testing basics | Split logic into modules; add 1–2 simple tests |
| 3 | OOP + file/CLI I/O | Small class design; run a CLI end-to-end |
| 4 | Debugging + code review habits | Reproduce bugs; explain trade-offs; clean PRs |
| 5–6 | Mini project + internship polish | README, git hygiene, talk through your design |

### Weekly goals (example)

1. **Ship something small every week** — one script or exercise set, committed with a clear message.
2. **Explain before you code** — 2–3 sentences on inputs, outputs, and edge cases.
3. **One refactor per session** — rename, extract function, or simplify a branch.

### Code review style

- Start with **what works**, then one **high-impact** improvement, then optional nits.
- Prefer questions (“What happens if the list is empty?”) over dumping fixes.
- Leave concrete next steps you can finish before the next call.
- Point at patterns you’ll see in internships: clear naming, small functions, tests for the happy path + one edge case.

### Internship-ready habits we build

- Readable git history and a short project README
- Asking clarifying questions before coding
- Debugging with prints/`pdb` and reproducing failures
- Knowing when a list, dict, or class is the right tool

## How a live session usually goes

1. Quick check-in on last week’s goals (5 min)
2. Live coding or review of your exercise/PR (30–40 min)
3. Agree next week’s target + optional homework (5 min)

## Run the sample CLI

```bash
python scripts/todo_cli.py add "Finish exercise 2"
python scripts/todo_cli.py list
python scripts/todo_cli.py done 1
```

## Exercises outline

See [`exercises/OUTLINE.md`](exercises/OUTLINE.md) for progressive practice (lists → dicts → functions → OOP).

---

*Demo for Codementor mentoring offers — topic/skill focused, not client-specific.*
