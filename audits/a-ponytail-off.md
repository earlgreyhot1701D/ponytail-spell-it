# Ponytail review and audit: a-ponytail-off

Run with `/ponytail full` in the same Claude Code session that built this version. Output pasted as-is.

/ponytail:ponytail-review

What this change does: It adds one file, index.html, which holds the whole Spell It toy. A small table of all 118 elements feeds a function, spell(), that finds the spelling which places the most letters. render() then draws the verdict, the symbol line and the tiles each time you type. I assumed the load is one person in one browser tab, with no server.

Must fix

A very long word freezes the page on every keystroke (index.html render(), and the input at L248)
What this is: Each keystroke throws away every tile and builds them all again, each with its own animation.
Problem: I timed it with a 10,200-letter word. That word makes 7,500 tiles, and one extra keystroke took about 1.7 seconds. That fails the "page doesn't freeze" acceptance check. In my last message I said it showed results "right away", but I had only checked that it worked, not how fast. That claim was wrong.
Fix: Add maxlength="300" to the <input>. That's one attribute. 300 letters gives a few hundred tiles, which draw instantly.
If we skip it: Someone who pastes a big block of text gets a frozen page, which looks like a crash.

Should fix

Some screen readers may read the tiles as silent (index.html makeTile())
What this is: Each tile hides its visible number, symbol and name from screen readers (aria-hidden) and puts the spoken text in an aria-label on the <li> instead. aria-label is a hidden text label that only screen readers use.
Problem: Some screen readers ignore aria-label on a plain list item when you read the page line by line. For example, NVDA in browse mode may skip it. With the visible text hidden too, that reader says nothing for the tile, which breaks M12. The file already has a .sr-only class for screen-reader-only text, but nothing uses it.
Fix: Drop the aria-label and put a <span class="sr-only"> with the same sentence inside each tile, so the label is real text.
If we skip it: For some blind users the tiles, which are the main result, may be silent.

Nice to have

The screen reader reads the whole symbol line after every keystroke (index.html, the <section aria-live="polite">)
What this is: aria-live tells a screen reader to read out a region whenever it changes. Here that region holds both the verdict and the symbol line.
Problem: With a 30-letter word, every keystroke reads out "P middle dot Ne middle dot U…" in full.
Fix: Move aria-live="polite" from the <section> onto the #verdict paragraph.
If we skip it: It's noisy but still usable.
The input doesn't shrink again when the window changes size (index.html render())
What this is: The input's text size is only fitted while you type.
Problem: If you type a long word in a wide window and then narrow the window or turn the phone, the word gets cut off until your next keystroke.
Fix: window.addEventListener("resize", render); That's one line.
If we skip it: The text is clipped now and then, and nothing breaks.
The code that builds the symbol line exists twice (index.html selfCheck and render())
What this is: The parts.map(p => p.el ? p.el.symbol : p.letter.toUpperCase() + "?").join(" · ") expression appears in both places.
Problem: If someone changes the format in render(), the self-check still tests the old format and passes.
Fix: Make one symbolLine(parts) function and call it from both places.
If we skip it: The two copies can drift apart with no warning.

Verdict: fix 1 and 2 first.
Lean: -2 lines possible.
Not checked: whether Firefox and Safari report the input's text width the same way Chrome does (the fit-to-width code depends on it), and how a real screen reader behaves. I only tested in the Chromium browser pane.

/ponytail:ponytail-audit

What this repo does: It holds two files. PRD.md describes Spell It, a toy page that spells a typed word with periodic-table symbols. index.html builds the whole app in one file, with no server, no build step and no dependencies. I assumed the load is one person in one browser tab.

I checked the PRD's hard rules first, and they all hold. The only network request is the one Google Fonts <link> (N2). Nothing is saved: no localStorage or cookies (N1). There's no innerHTML or eval (N5) and no randomness (M10). The acceptance table passes, apart from the speed problem in finding 1.

Must fix

A very long word freezes the page on every keystroke (index.html render() and the <input id="word">)
What this is: Each keystroke throws away every tile and draws them all again, each with a small drop-in animation.
Problem: A 10,200-letter word makes 7,500 tiles. I timed one extra keystroke at about 1.7 seconds. That fails the PRD check "a very long word: still works, page doesn't freeze".
Fix: Add maxlength="300" to the input. That's one attribute, and a few hundred tiles draw instantly.
If we skip it: Pasting a big block of text makes the page look frozen.

Should fix

Some screen readers may read the tiles as silent (index.html makeTile())
What this is: Each tile hides its visible text from screen readers and puts the spoken text only in an aria-label, a hidden text label that only screen readers use, on the <li>.
Problem: Some screen readers ignore aria-label on a plain list item when reading line by line. For example, NVDA in browse mode may skip it. That reader would then say nothing for the tile, which breaks M12. The .sr-only CSS class for screen-reader-only text is in the file but unused (nothing else in the folder references it).
Fix: Replace the aria-label with a <span class="sr-only"> holding the same sentence, such as "Ba, Barium, atomic number 56".
If we skip it: For some blind users the main result may be silent.

Nice to have

The screen reader reads the whole symbol line after every keystroke (index.html, the <section aria-live="polite">)
What this is: aria-live makes a screen reader read a region out loud whenever it changes. That region holds the verdict and the symbol line.
Problem: With a long word, every keystroke reads out "P middle dot Ne middle dot U…" in full.
Fix: Move aria-live="polite" from the <section> onto the #verdict paragraph.
If we skip it: It's noisy but still usable.
The input doesn't shrink again when the window changes size (index.html render())
What this is: The input's text size is only fitted while you type.
Problem: If you type a long word in a wide window and then narrow the window or turn the phone, the word stays cut off until your next keystroke.
Fix: window.addEventListener("resize", render); That's one line.
If we skip it: The text is clipped now and then, and nothing breaks.
The code that builds the symbol line exists twice (index.html selfCheck and render())
What this is: The same parts.map(...).join(" · ") expression builds the symbol line in both places.
Problem: If someone changes the format in render(), the self-check keeps testing the old copy and still passes.
Fix: Make one symbolLine(parts) function and call it from both places.
If we skip it: The test can pass while the page shows something different.

Verdict: fix 1 first (it fails an acceptance check), then 2.
Lean: -2 lines, -0 dependencies possible.
Not checked: a real screen reader, and Firefox and Safari. The fit-to-width code depends on how the browser reports the input's text width, and I only tested in the Chromium browser pane.