# Ponytail review and audit: b-ponytail-full

Run with `/ponytail full` in the same Claude Code session that built this version. Output pasted as-is.

/ponytail:ponytail-review

What this change does: It adds one new file, index.html, which is the whole Spell It app. When you type, it strips out everything except letters and uses dynamic programming (it works from the end of the word backward, remembering the best score at each position) to find the spelling that places the most letters. It then draws the verdict, the symbol line and the tiles with textContent only. At the bottom, a self-check runs the PRD's acceptance table through console.assert each time the page loads.

I judged it as a toy for one person in one browser tab. I measured instead of guessing: a pasted word of about 102,000 letters takes about 360 ms to process and draw, so the page pauses briefly but doesn't freeze. On a 375 px phone screen, the page doesn't scroll sideways.

Should fix

Long words don't actually shrink to fit (index.html:208)
What this is: The PRD says long words in the input box should shrink instead of overflowing.
Problem: The font size is set to 600 / length, which ignores how wide the box is. With pneumonoultramicroscopic, the text was 334 px wide in a box that shows 153 px, so the start of the word scrolled out of view.
Fix: Base it on the box's real width: Math.max(16, Math.min(40, input.clientWidth / (0.62 * Math.max(raw.length, 1)))). Here 0.62 is about the width of one monospace character compared with its height. It's a one-line change.
If we skip it: We fail a PRD layout rule. It's most visible on phones.
The tile list breaks list semantics for screen readers (index.html:142, index.html:183)
What this is: The tiles are <li> items inside a <ul>. Each <li> is given role="img" so a screen reader can read its label.
Problem: role="img" replaces the list-item role, so the list contains no list items. Accessibility checkers such as axe flag this, and some screen readers announce "list, 0 items" before the tiles.
Fix: Use <div id="tiles"> and make each tile a <div> instead of an <li>. Keep role="img" and the aria-label. That changes two tag names and nothing else.
If we skip it: M12 (each tile readable by a screen reader) is only partly met, and accessibility checks fail.

Nice to have

Screen readers re-read the whole symbol line on every keystroke (index.html:137)
What this is: aria-live="polite" sits on the section that holds both the verdict and the symbol line. A live region is an area whose changes get read aloud automatically.
Problem: Each keystroke queues the full sequence (P · Er · I · O · D? · …) to be read. With a pasted long word, that's thousands of symbols.
Fix: Move aria-live="polite" from the <section> to <p id="verdict">.
If we skip it: Screen-reader users hear a lot of noise while typing.
Dead condition in the spelling search (index.html:162)
What this is: This line decides whether to use a two-letter symbol.
Problem: && two > 0 never changes the result. two is either -1 or at least 2, and score is never negative, so two >= score already fails whenever two is -1.
Fix: Delete && two > 0.
If we skip it: Nothing breaks. It's just one more thing for the next reader to puzzle over.

Verdict: fix 1 and 2 first.
Lean: about 0 lines possible. Finding 4 shortens a line but doesn't remove one.
Not checked: a real screen reader and real phone hardware. Element names fitting inside tiles was checked with fallback fonts only, because Google Fonts may not load in the preview.

/ponytail:ponytail-audit

What this repo does: The repo holds two files. PRD.md describes Spell It, a one-page toy that spells a typed word out of periodic table symbols. index.html is the whole app: the HTML, CSS and JavaScript plus a self-check for the PRD's acceptance table. There's no build step, no dependencies and no tests outside that self-check.

I judged it as a toy for one person in one browser tab, with nothing stored and no server.

I checked every MUST and NEVER item in the PRD against the code. Every acceptance check passes, there are no network calls besides the fonts, there's no innerHTML or eval, and nothing is stored. All 118 elements match their atomic numbers. The theme tokens and footer text are exact.

Should fix

Long words don't actually shrink to fit (index.html:208)
What this is: The PRD (section 4.2) says long words in the input box should shrink instead of overflowing.
Problem: The font size is set to 600 / length, which ignores how wide the box is. I measured pneumonoultramicroscopic at 334 px wide in a 153 px box, so the start of the word scrolls out of view.
Fix: Base it on the box's real width: Math.max(16, Math.min(40, input.clientWidth / (0.62 * Math.max(raw.length, 1)))). Here 0.62 is about the width of one monospace character compared with its height. It's a one-line change.
If we skip it: We fail a PRD layout rule. It's most visible on phones.
The tile list breaks list semantics for screen readers (index.html:142, index.html:183)
What this is: The tiles are <li> items inside a <ul>. Each <li> is given role="img" so a screen reader can read its label.
Problem: role="img" replaces the list-item role, so the list contains no list items. Accessibility checkers such as axe flag this, and some screen readers announce "list, 0 items".
Fix: Use <div id="tiles"> and make each tile a <div> instead of an <li>. Keep role="img" and the aria-label. That changes two tag names.
If we skip it: M12 (each tile readable by a screen reader) is only partly met, and accessibility checks fail.

Nice to have

Screen readers re-read the whole symbol line on every keystroke (index.html:137)
What this is: aria-live="polite" wraps both the verdict and the symbol line. A live region is an area whose changes get read aloud automatically.
Problem: Each keystroke queues the full sequence to be read. With a pasted long word, that's thousands of symbols.
Fix: Move aria-live="polite" from the <section> to <p id="verdict">.
If we skip it: Screen-reader users hear a lot of noise while typing.
The example buttons and the speller clean the word differently (index.html:206)
What this is: An example button looks pressed when it matches the typed word.
Problem: The button check only trims spaces and lowercases. The speller also drops punctuation and digits. If you type ba-con!, the result is exactly bacon's, but the "bacon" button doesn't look pressed.
Fix: Clean the word the same way in both places: raw.toLowerCase().replace(/[^a-z]/g, "").
If we skip it: The pressed state doesn't match what the PRD promises (M2: "Ba-Con!" counts as "bacon").
Dead condition in the spelling search (index.html:162)
What this is: This line decides whether to use a two-letter symbol.
Problem: && two > 0 never changes the result. two is either -1 or at least 2, and score is never negative.
Fix: Delete && two > 0.
If we skip it: Nothing breaks. It's just one more thing for the next reader to puzzle over.

Verdict: fix 1 and 2 first. Everything else is polish.
Lean: -0 lines, -0 dependencies possible. The app has no dependencies, and finding 5 shortens a line but doesn't remove one.
Not checked: a real screen reader, real phone hardware, and how tiles look with the Google Fonts loaded (the preview may have used fallback fonts). There's no git history to audit, because this folder isn't a git repository.