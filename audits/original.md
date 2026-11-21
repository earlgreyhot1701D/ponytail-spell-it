# Ponytail audit: original

Run with `/ponytail full` in a fresh Claude Code session. Output pasted as-is.

/ponytail:ponytail-audit

What this repo does: It is one static web page, index.html. You type a word and it tries to spell that word with chemical element symbols, like B·A·Na·Na. Letters no symbol covers show up as grey "missing" tiles. Load assumed: one person at a time in their own browser, with no server and no stored data.

Must fix
Social preview image is a placeholder (index.html:10, index.html:16)
What this is: The og:image and twitter:image tags pick the picture shown when someone shares the link on social media or in chat apps.
Problem: Both still say SITE_URL/og-spellit.png, and there is no og-spellit.png in the folder. Every shared link will show a broken image or none.
Fix: Put the real full URL in both tags and add the 1200×630 image. If you don't have the image yet, delete lines 10–12 and 16.
If we skip it: Shared links look broken, and that is the first thing new visitors see.
Should fix
Screen readers read the whole result on every key press (index.html:656)
What this is: aria-live makes a screen reader read a region aloud when it changes. aria-atomic="true" makes it read the whole region, not just the change.
Problem: The live region holds the verdict, the symbol line and every tile, and each tile is an <article> with its own label. Typing "periodic" reads out about eight tiles per letter typed, and the reading starts over with each new key.
Fix: Move aria-live="polite" from #readout onto #verdict and #sequence only, drop aria-atomic, and add aria-hidden="true" to #tiles, because the sequence line already says the same thing.
If we skip it: The tool is close to unusable with a screen reader.
The footer says "Powered by NLP", which isn't true (index.html:666)
What this is: NLP (natural language processing) means software that understands language.
Problem: The page does no language processing. It is a plain search over element symbols. Line 665 even says "deterministic · no randomness", which is accurate.
Fix: Delete "Powered by NLP." from the line.
If we skip it: A false claim on a college-affiliated project, and anyone technical will notice.
Two search functions do the same job (index.html:738-776, used at index.html:930)
What this is: findFullSpelling looks for a perfect spelling. findBestPartial looks for the best spelling with gaps allowed.
Problem: When a perfect spelling exists, findBestPartial already finds it and reports missing: 0. I ran both on 200,000 random spellable words, and they returned the same answer every time. So the first function is about 40 lines that add nothing.
Fix: Delete findFullSpelling. In render(), call findBestPartial once and choose "Fully spellable" when result.missing === 0.
If we skip it: Two copies of the rules that must be kept in sync by hand.
The spelling logic has no test (index.html:798-862)
What this is: findBestPartial is the only real logic in the app: a search that remembers results it has already worked out.
Problem: If a change breaks it, for example by flipping a check in isBetter, nothing fails. You only find out by trying words by hand.
Fix: Add three console.assert lines after makeElementMap(): "banana" spells fully as B·A·Na·Na, "j" gives 1 missing letter, and "" gives no pieces.
If we skip it: The next edit to the search can quietly show wrong spellings.
Nice to have
Accented and non-letter input is dropped without telling the user (index.html:734-736)
What this is: cleanWord keeps only the letters a–z.
Problem: "José" is checked as "jos" and shows J?·Os, so the é just disappears. Typing "42" removes everything and shows "Type a word to test the table." even though the user did type something.
Fix: Run value.normalize("NFD") before the filter, so é becomes e. One call.
If we skip it: Names with accents, which the placeholder text invites, give confusing results.
Error catches that can't trigger and hide real errors (index.html:965-974, index.html:955-961)
What this is: try/catch blocks around setting the input value and around drawing the result.
Problem: Setting input.value can't fail. If drawing ever does fail, the catch shows a generic message and never logs the error, so you can't debug it. The overlap check at index.html:787 is also dead, because covered + missing always equals the word length.
Fix: Delete the chooseExample try/catch and the missing check in isBetter. Add console.error(error) to the catch in render().
If we skip it: About 10 extra lines, and silent failures.

Verdict: Healthy small app. Fix the placeholder image tags (1) and the screen-reader live region (2) first.

Lean: about -50 lines possible, and there are no dependencies to remove.

Not checked: I didn't open the page in a browser or test it with a real screen reader. I didn't check how it looks on phones, the color contrast of the muted grey text, or where it is (or will be) deployed.

The audit of spell-it-original is finished. The whole app is one 990-line index.html. I found 7 issues: a broken social-preview image link, screen-reader noise, a footer claim that isn't true, and about 50 lines of duplicate or dead code. I changed no code.

Which findings should I fix?