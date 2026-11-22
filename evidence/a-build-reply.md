# Build A (Ponytail off): Claude Code's reply when it finished

Copied from the Claude Code session on Nov 21, 2026, as pasted into chat at the time. Added to the repo Nov 22, 2026. The table was pasted from the app as plain text, so its columns are tab-separated.

---

All checks pass in the logic. Next I'll look at the layout and check the console for failed self-check asserts.

Everything passes except a 45-letter word that still gets cut off on phones; I'm switching the shrink to measure the input box's real width instead of estimating from letter count.

I built the app in index.html, and it passes all nine acceptance checks. I ran them in the browser pane and got the expected result each time:

Type this	Result
(nothing)	"Type a word to test the table."
banana	Fully spellable · Ba · Na · Na
kiro	Fully spellable · K · Ir · O
BaCoN / ba-con!	Same as bacon: Ba · Co · N
periodic	1 letter could not be placed (P · Er · I · O · D? · I · C)
quiz	2 letters could not be placed (Q? · U · I · Z?)
jazz	4 letters could not be placed, page still works
10,200-letter word	Shows results right away, no freeze

How to check it yourself:

Double-click index.html to open it in a browser. There's no build step.
Type each word from the table into the box. Results update as you type.
For the long-word check, paste in a very long string, such as a paragraph with the spaces left in.
Optional: open the browser's developer tools (F12) and look at the Console. The page checks the acceptance table against itself when it loads and prints a failure message there if anything is wrong. It's silent right now.
To check the phone layout, narrow the window or use phone view in the developer tools. Tiles wrap onto new lines and nothing scrolls sideways.
To check the keyboard, press Tab to move from the input to each example button and Enter to pick one. The focus ring is visible.

When a word can be spelled more than one way, the app shows the one with the fewest tiles. That's why bacon gives Ba · Co · N, which matches the example in the PRD.

Two things I couldn't check:

Screen reader: I gave each tile a label like "Ba, Barium, atomic number 56", but I haven't tried it with an actual screen reader.
Fonts: the preview here may not have internet access, so I couldn't confirm the Google Fonts load. Without them, the page falls back to standard system fonts.
