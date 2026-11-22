# Build B (Ponytail full): Claude Code's reply when it finished

Copied from the Claude Code session on Nov 21, 2026, as pasted into chat at the time. Added to the repo Nov 22, 2026. The table was pasted from the app as plain text, so its columns are tab-separated.

---

All the checks pass. Let me look at the page and the console assertions.

I built the app as a single file: index.html. It opens by double-clicking, with no build step. It uses no frameworks or innerHTML, stores nothing, and the only network request is the Google Fonts link the PRD allows. I ran every row of the acceptance table in the in-app browser and all of them pass.

How to check it yourself

Double-click index.html.
Type each word from the PRD's table into the box and compare the result:
Type	You should see
(nothing)	"Type a word to test the table."
banana	Fully spellable · Ba · Na · Na
kiro	Fully spellable · K · Ir · O
BaCoN, ba-con!	Fully spellable · Ba · Co · N, the same as bacon
periodic	1 letter could not be placed · P · Er · I · O · D? · I · C
quiz	2 letters could not be placed · Q? · U · I · Z?
jazz	4 letters could not be placed, all four shown as dashed "No element" tiles
a very long word	Still responsive. I tested a word of about 102,000 letters.
Quick check: open DevTools (F12) and look at the Console. The file checks the whole table against itself when it loads. A failed check shows up there as an "Assertion failed" line, and I got none.
Keyboard: press Tab to move from the input through the six example buttons. A gold focus ring shows where you are, and Enter fills the box with that word. The button matching the current word looks pressed.

Choices I made

When two spellings place the same number of letters, the app picks one with a fixed rule, so the result never changes. bacon always comes out as Ba · Co · N rather than B · Ac · O · N.
"Share a word" and "show every possible spelling" are comments in the script only, as the PRD asks.

I haven't tested with a real screen reader or on a real phone. Each tile has a spoken label (for example "Ba, Barium, atomic number 56") and the tiles wrap at phone width, but neither has been checked on a device. Without internet the page falls back to system fonts.
