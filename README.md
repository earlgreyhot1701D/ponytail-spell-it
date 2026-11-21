# Ponytail x Spell It

**Same PRD. Same model. Same prompt. One build with the [Ponytail](https://github.com/DietrichGebert/ponytail) ruleset off, one with it on, both compared against the version I made last summer.**

Short version: Ponytail made the app smaller (half the lines, about a quarter less by file size), a little cheaper and faster, with no must-fix bugs. It also took out the parts I liked.

**Read the full write-up on [dev.to](https://dev.to/earlgreyhot1701d).**

![Ponytail x Spell It case study card. Same PRD, same model, same prompt. Line counts: original 989, Ponytail off 416, Ponytail full 206. A tile row spells banana as Ba, Na, Na.](assets/article/cover.webp)

---

## The problem

AI coding agents tend to build more than you asked for. Extra abstractions, extra files, a library where the browser already has the feature. The code works, but it's bigger than it needs to be, and bigger code is harder to read, review, and trust.

[Ponytail](https://github.com/DietrichGebert/ponytail) is an open source ruleset that tries to fix that. It tells the agent to act like "the laziest senior dev in the room" and climb a ladder before writing anything:

1. Does this need to exist?
2. Is it already in this codebase?
3. Does the standard library handle it?
4. Is there a native platform feature?
5. Is there an installed dependency?
6. Can it be one line?
7. Only then, the minimum code that works, plus one small test if the logic is non-trivial.

Its own benchmark reports about 53% less code, 41% less time, and 26% lower cost. I wanted to see what that looks like on one small app of mine, and what it costs in ways a line count doesn't show.

## How this tests it

I picked **Spell It**, one of my [Hot AR Summer 2026](https://github.com/earlgreyhot1701D/hot-ar-summer-2026) daily builds. You type a word and it builds that word out of periodic table symbols, like `Ba · Na · Na` for banana. Letters no element covers get flagged.

It's a good test case because it has:

- **Real logic.** Finding the spelling that places the most letters is a small search problem, so Ponytail's "add a test" rule has something to bite on.
- **Room to over-build.** A solver framework, a dictionary API, settings, history.
- **A finished original to compare against.** I already shipped it last summer, with a deliberate design.

Then I wrote one [PRD](PRD.md) from the original's behavior, with MUST, STUB, and NEVER labels, acceptance checks, and the original's visual theme. Both builds got that PRD and nothing else.

## See it

All three run the same demo: type "banana", click "periodic", type "jazz".

### Original (summer 2026)

![Original build](gifs/spell-it-original.gif)

### A: Claude Code, Ponytail off

![Build A, Ponytail off](gifs/spell-it-a-ponytail-off.gif)

### B: Claude Code, Ponytail full

![Build B, Ponytail full](gifs/spell-it-b-ponytail-full.gif)

## The setup

![One spec, three builds. The original was built last summer. Builds A and B were made by Claude Code on Opus 5.5, with Ponytail off for A and full for B. Both got the PRD and one prompt.](assets/article/one-spec-three-builds.webp)

| | Original | A | B |
|---|---|---|---|
| Built | Summer 2026, directed by me | Claude Code (desktop) | Claude Code (desktop) |
| Model | n/a | Opus 5.5 | Opus 5.5 |
| Ponytail | n/a | `/ponytail off` | `/ponytail full` |
| Input | n/a | [PRD.md](PRD.md) + one prompt | [PRD.md](PRD.md) + one prompt |
| Folder | `spell-it-original/` | `spell-it-a/` | `spell-it-b/` |

Each build ran in a fresh session, in an empty folder holding only the PRD, with no personal rules files (`CLAUDE.md` or `AGENTS.md`). Both got this exact prompt:

```
Build the app described in PRD.md. Put it in one index.html in this folder. When you're done, tell me how to check it against the acceptance checks.
```

I didn't help with code. I was ready to send a one-line follow-up for any failed check, but neither build needed one.

## Results

### Size

| | Original | A: off | B: full |
|---|---|---|---|
| JavaScript lines (logic) | 319 | 151 | 109 |
| CSS lines (the look) | 595 | 227 | 61 |
| **Total lines** | **989** | **416** | **206** |
| **File size** | **28.9 KB** | **14.1 KB** | **10.8 KB** |
| Files | 1 | 1 | 1 |
| Dependencies | 0 | 0 | 0 |

![Size comparison by lines. JavaScript: original 319, A 151, B 109. CSS: original 595, A 227, B 61. Total: 989, 416, 206. Acceptance checks: 9, 8 and 9 of 9. Build cost: $0.85 for A, $0.73 for B. Build time: 1 minute 49 seconds for A, 1 minute 29 seconds for B.](assets/article/size-comparison.webp)

### Does it work?

| | Original | A: off | B: full |
|---|---|---|---|
| Acceptance checks | 9 of 9 | 8 of 9 | 9 of 9 |
| MUST features | 13 of 13 | 13 of 13 | 13 of 13 |
| NEVER rules kept | 5 of 5 | 5 of 5 | 5 of 5 |
| STUBs left as comments, not code | n/a | 2 of 2 | 2 of 2 |
| Self-tests written | 0 | 7 | 8 |

The one failed check: pasting a 10,200-letter word froze Build A for 1.1 to 1.8 seconds per keystroke. Build B paused for about 0.3 seconds. The original caps input at 80 letters, so it never gets that long.

![The long-word freeze test, time per keystroke with a 10,200-letter word. Original: 0.03 seconds. A, Ponytail off: 1.1 to 1.8 seconds. B, Ponytail full: about 0.3 seconds.](assets/article/freeze-test.webp)

### Cost and time

| | A: off | B: full |
|---|---|---|
| Build cost | $0.85 | $0.73 |
| Build time | 1m 49s | 1m 29s |
| Follow-up prompts | 0 | 0 |
| Review + audit cost | $0.33 | $0.32 |

The three sessions together, builds plus all reviews and audits, cost **$2.95** ($1.18 + $1.05 + $0.72).

### Compared with Ponytail's own benchmark

| | Ponytail's benchmark | This test (B vs A) |
|---|---|---|
| Less code | about 53% | 50% by lines, about 24% by file size |
| Less time | about 41% | about 18% (20 seconds) |
| Lower cost | about 26% | about 14% (12 cents) |

By lines, the savings matched their claim. By file size, they were about half as big, because B packs more onto each line. Time and cost savings were real but smaller on an app this size. One app is context, not a rebuttal of a 39-task benchmark.

### What the Ponytail audits found

| | Original | A: off | B: full |
|---|---|---|---|
| Must-fix | 1 | 1 | 0 |
| Should-fix | 4 | 1 | 2 |
| Nice to have | 2 | 3 | 3 |
| **Total** | **7** | **5** | **5** |

![Ponytail audit findings. Must-fix: original 1, A 1, B 0. Should-fix: 4, 1, 2. Nice to have: 2, 3, 3. A note reads: check the judge too.](assets/article/audit.webp)

- **Original:** a leftover placeholder for the social share image.
- **A:** the long-paste freeze.
- **All three:** screen readers read too much on every keystroke. That one is on my PRD, not on any builder.

Full output is in [audits/](audits).

### My gut score (would I ship it as is?)

| Original | A: off | B: full |
|---|---|---|
| 5 | 4 | 4 |

![Would I ship it? Gut score from 1 to 5: original 5, A 4, B 4. A and B would get there with a few UI tweaks.](assets/article/would-i-ship-it.webp)

All three work the same. The original wins on detail: the background, the frame, the big title. A and B are one-shots that would need small UI tweaks.

## What I learned

1. **Ponytail does what it says.** Smaller than the plain build by every measure, same behavior, and the only build with no must-fix bugs.
2. **Most of the cut came from the design.** B has about a tenth of the original's styling by lines and about a quarter by file size. My PRD named the colors, fonts and frame but not the texture or the details, and design that isn't written down disappears. Lean code and good design are different goals.
3. **Line count overstates the gap.** Half the lines, but only about a quarter less by file size. Formatting moves the number.
4. **A good PRD did a lot of the work.** The plain build was already less than half the size of my original. Clear MUST, STUB, and NEVER labels kept both agents in scope.
5. **The one real bug went to the build without Ponytail.** Build A froze on a huge paste. Build A also told me it showed results "right away"; its own review later admitted it had only checked that it worked, not how fast.
6. **Summer me already had the fix.** The audit's fix for that freeze was to cap the input length. My original has done that since July.
7. **Check the judge too.** The audits found real bugs, and also called my "Powered by NLP" tagline a false claim, described the project as college-affiliated, and suggested a test where "banana" spells as B·A·Na·Na. A is not an element symbol.

## Limits

- One small app, one run per build. This is a case study, not a benchmark, and AI builds vary from run to run.
- Ponytail was installed for both builds and switched off for A with `/ponytail off`, not uninstalled.
- The PRD was written from the original, so the original had a head start on matching it.
- A and B were audited in the same session that built them. The original was audited in a fresh one.
- Not tested with a real screen reader or on a real phone.

## Run it yourself

**Try the apps:** download any `index.html` and double-click it. No build step.

**Repeat the experiment:**

1. Install Ponytail in Claude Code (see the [Ponytail README](https://github.com/DietrichGebert/ponytail)).
2. Make two empty folders and put [PRD.md](PRD.md) in each.
3. In a new session in the first folder, send `/ponytail off`, then the prompt above.
4. In a new session in the second folder, send `/ponytail full`, then the same prompt.
5. Score both against the acceptance checks in the PRD.

## What's in here

```
PRD.md               the spec both builds got
spell-it-original/   my summer 2026 version
spell-it-a/          Claude Code, Ponytail off
spell-it-b/          Claude Code, Ponytail full
gifs/                same demo on each build
assets/article/      graphics from the write-up
results/             full scorecard
audits/              raw Ponytail review and audit output
```

## Credits

- [Ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert, MIT.
- Article graphics generated with ChatGPT from my own numbers.
- Spell It and this experiment by [L. Cordero](https://github.com/earlgreyhot1701D).

## License

MIT. See [LICENSE](LICENSE).

---

AI assisted. Human approved. Powered by NLP.
