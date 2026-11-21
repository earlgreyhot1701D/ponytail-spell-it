# Spell It: PRD

Shared PRD for the Ponytail comparison. Every build gets this exact file and the exact same first prompt. Nothing else.

## 1. What it is

A single web page. You type a word, and it shows that word built from periodic table element symbols, as tiles. If the word can't be fully built, it shows the closest it can get and flags the letters that don't fit.

## 2. Who it's for

Anyone who likes word play. It's a toy, not a tool. It should feel instant and a little delightful.

## 3. Features

### MUST

- **M1. Word input.** One text box. Results update as you type, with no submit button.
- **M2. Cleaning.** Ignore case, spaces, numbers, and punctuation. "Ba-Con!" is treated as "bacon".
- **M3. Full spelling.** If the word can be spelled entirely with element symbols, say so ("Fully spellable") and show one valid spelling.
- **M4. Best partial.** If it can't, show the spelling that places the most letters, and flag each letter that couldn't be placed. Say how many letters couldn't be placed ("1 letter could not be placed" / "2 letters could not be placed").
- **M5. Tiles.** Each element shows as a tile with its atomic number, symbol, and full name. Flagged letters show as a visibly different tile marked "No element".
- **M6. Symbol line.** Under the verdict, show the plain sequence, like `Ba · Co · N`. Flagged letters show as the letter plus a question mark, like `D?`.
- **M7. Examples.** Six clickable example words: banana, brain, nacho, irony, bacon, periodic. Clicking one fills the box and shows the result.
- **M8. Empty state.** With nothing typed, show: "Type a word to test the table."
- **M9. All 118 elements**, with correct symbols, names, and atomic numbers.
- **M10. Deterministic.** The same word always gives the same result. No randomness.
- **M11. Errors never blank the page.** If something fails, show a short plain message instead.
- **M12. Accessible.** Each tile is readable by a screen reader (symbol, name, and atomic number). Keyboard works for the input and examples.
- **M13. Footer line:** "Real element symbols · deterministic · no randomness · nothing stored or sent"

### STUB (comment only, do not build)

- **S1. Share a word.** A link that opens the page with a word already filled in.
- **S2. Show every possible spelling**, not just one.

### NEVER

- **N1.** No accounts, no saving, no history, no storage of any kind.
- **N2.** Nothing is sent anywhere. No network calls, no analytics, no APIs. The one exception is the Google Fonts link in section 4.
- **N3.** No dictionary check. Any string of letters is allowed, real word or not.
- **N4.** No AI or LLM calls.
- **N5.** No `innerHTML`, no `eval()`. Put text on the page with `textContent`.

## 4. UI

One screen, top to bottom, centered column:

1. **Header.** App name "Spell It" and the line "Build words from the elements."
2. **Input.** One large text box labeled "Type a word." It's the focus of the page. Long words shrink to fit instead of overflowing.
3. **Examples.** A row of six small buttons (M7). The one that matches the current word looks pressed.
4. **Verdict.** One line, big enough to read at a glance:
   - Empty: "Type a word to test the table."
   - Full: "Fully spellable", styled as a success.
   - Partial: "N letters could not be placed", styled as a warning.
   - Error: a short plain message (M11).
5. **Symbol line.** The plain sequence (M6), smaller, under the verdict.
6. **Tiles.** A row that wraps onto new lines. Each tile looks like a periodic table square: atomic number small in the top corner, symbol large in the middle, name small at the bottom. Each element gets its own color, and the same element is always the same color. "No element" tiles are clearly different (for example, dashed and gray).
7. **Footer.** The M13 line.

Layout rules:

- Works on a phone and a laptop. Tiles wrap, nothing scrolls sideways.
- Readable contrast. Visible keyboard focus.
- No UI libraries or frameworks.

### Theme: "Specimen instrument"

The page looks like an old brass lab instrument in a dark room. Use these exact tokens.

**Colors**

| Token | Hex | Used for |
|---|---|---|
| background | `#080a09` | Page |
| panel | `#111514` | Input and verdict panels |
| ink | `#f0e6d2` | Main text (warm cream) |
| muted | `#a99d89` | Small labels, footer |
| brass | `#b48345` | Borders, frame lines |
| brass-bright | `#d2a668` | Headings, highlights |
| green | `#9bc879` | "Fully spellable" verdict |
| amber | `#e0ad58` | Partial verdict, "No element" tiles |
| focus | `#f0c77d` | Keyboard focus ring |

**Fonts** (from Google Fonts, one `<link>` tag, with system fallbacks)

| Font | Used for |
|---|---|
| Oswald | The "Spell It" title |
| Space Grotesk | Body text |
| IBM Plex Mono | Labels, verdict, symbol line, tiles |

**Look and feel**

- A thin brass frame around the whole page, like an instrument case.
- A small mono label above the title: "Specimen instrument 118".
- Rounded corners kept small (3 to 5px).
- Tile color: each element's hue is `(atomic number × 17) mod 360`, used for the tile's border and symbol color on a dark background.
- Dark theme only.

## 5. Constraints

- One HTML file. Opens by double-clicking it. No build step.
- Design gets scored in its own row, separate from code size.

## 6. Acceptance checks

| Type this | Expect |
|---|---|
| (nothing) | "Type a word to test the table." |
| `banana` | Fully spellable: Ba · Na · Na |
| `kiro` | Fully spellable: K · Ir · O |
| `BaCoN` | Same result as `bacon` (fully spellable) |
| `ba-con!` | Same result as `bacon` |
| `periodic` | Partial, 1 letter could not be placed |
| `quiz` | Partial, 2 letters could not be placed |
| `jazz` | Partial, no letters placed, nothing breaks |
| a very long word | Still works, page doesn't freeze |
