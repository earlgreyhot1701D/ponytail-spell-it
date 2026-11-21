# Scorecard

All three builds were tested the same way in headless Chrome, plus by hand.

| Group | Metric | Original | A: Ponytail off | B: Ponytail full |
|---|---|---|---|---|
| Size | JavaScript lines | 319 | 151 | 109 |
| Size | CSS lines | 595 | 227 | 61 |
| Size | Total lines | 989 | 416 | 206 |
| Size | Files | 1 | 1 | 1 |
| Size | Dependencies | 0 | 0 | 0 |
| Size | Outside requests | 1 (Google Fonts) | 1 (Google Fonts) | 1 (Google Fonts) |
| Behavior | Acceptance checks passed | 9 of 9 | 8 of 9 | 9 of 9 |
| Behavior | MUST features met | 13 of 13 | 13 of 13 | 13 of 13 |
| Behavior | STUBs left as comments | n/a | 2 of 2 | 2 of 2 |
| Rules | NEVER rules kept | 5 of 5 | 5 of 5 | 5 of 5 |
| Rules | innerHTML or eval() | 0 | 0 | 0 |
| Ponytail | Self-tests written | 0 | 7 | 8 |
| Ponytail | `shortcut:` comments | 0 | 0 | 0 |
| Ponytail | Audit findings | 7 (1 must-fix) | 5 (1 must-fix) | 5 (0 must-fix) |
| Process | Build time | n/a | 1m 49s | 1m 29s |
| Process | Follow-up prompts | n/a | 0 | 0 |
| Process | Build cost | n/a | $0.85 | $0.73 |
| Design | UI parts from the PRD | 7 of 7 | 7 of 7 | 7 of 7 |
| Design | Gut score (1 to 5) | 5 | 4 | 4 |

## Notes

- **The failed check.** A pasted 10,200-letter word froze Build A for 1.1 to 1.8 seconds per keystroke. Build B paused for about 0.3 seconds. The original caps input at 80 letters, so it never gets that long.
- **Audits.** A and B were audited in the same session that built them. The original was audited in a fresh session. Full output is in [`/audits`](../audits).
- **The auditor made mistakes too.** It called the "Powered by NLP" tagline a false claim, described the project as college-affiliated, and suggested a test where "banana" spells as B·A·Na·Na. A is not an element symbol.
- **Spellings.** Build B uses the international names "Aluminium" and "Caesium." The others use "Aluminum" and "Cesium."
