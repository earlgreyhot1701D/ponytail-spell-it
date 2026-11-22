# Addendum: added after the experiment

**Added Nov 22, 2026.** Everything in this file, and in the `tools/` and `evidence/` folders, was added after the experiment ran.

The experiment itself is frozen at commit `c3cf74e` (tag `experiment-2026-11-21`). Nothing from that snapshot was edited: the three builds, `PRD.md`, `audits/`, and `results/scorecard.md` are exactly as they were on Nov 21. The only later changes to an existing file are in the README: a pointer to this addendum, and the dev.to link once the post is live.

## Why this exists

Before publishing, I had the experiment reviewed for gaps in its evidence. The review found that some numbers in the write-up came from scripts and screenshots that weren't in the repo, and that two terms were never defined. This addendum fills those gaps without changing the snapshot.

## Two definitions I should have written down first

**What counts as a freeze.** The PRD said a very long word must not freeze the page, but it never set a number. I didn't set one before testing either. After seeing the results, I counted **more than 1 second per keystroke** as a freeze. The gap between builds was wide enough that any line from about 0.5 to 1 second gives the same verdict.

**What counts as a self-test.** The scorecard's "self-tests written" is the number of `console.assert` lines in each file: 0 in the original, 7 in A, 8 in B.

## Rerun the numbers yourself

| Script | What it does |
|---|---|
| `tools/count_size.sh` | Recounts lines, bytes, and `console.assert` lines for all three builds |
| `tools/check_builds.py` | Runs the PRD's acceptance checks in a headless browser and times the 10,200-letter keystroke test |

Timings move a little from run to run. Here are the two runs side by side:

| Seconds per keystroke | Nov 21 | Nov 22 rerun |
|---|---|---|
| Original (input capped at 80 letters) | 0.03 | 0.03 to 0.04 |
| A: Ponytail off | 1.1 to 1.8 | 0.98 to 1.68 |
| B: Ponytail full | about 0.3 | 0.28 to 0.37 |

Verdicts were the same both days: A froze, the other two didn't.

## Receipts

| File | What it shows |
|---|---|
| `evidence/a-build-reply.md` | Build A's reply when it finished, including its claim that a 10,200-letter word "shows results right away" |
| `evidence/b-build-reply.md` | Build B's reply when it finished |
| `evidence/a-build-cost-band.png` | Build A session: $0.85, 1m 49s |
| `evidence/b-build-cost-band.png` | Build B session: $0.73, 1m 29s |
| `evidence/a-after-review-audit-band.png` | Build A session after review and audit: $1.18 total |
| `evidence/b-after-review-audit-band.png` | Build B session after review and audit: $1.05 total |
| `evidence/original-audit-session-start-band.png` | Original's audit session after switching Ponytail on, before any work: $0.30 |
| `evidence/original-after-audit-band.png` | Original's audit session after the audit: $0.72 total |

The cost screenshots come from Ponytail's status band in the Claude desktop app.
