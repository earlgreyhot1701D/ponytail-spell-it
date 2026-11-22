"""Re-run the Spell It acceptance checks and the long-word timing on all three builds.

Added Nov 22, 2026, after the experiment. This is the same logic Claude used on
Nov 21 to score the builds, cleaned up so anyone can rerun it.

Usage (from the repo root):
    pip install playwright
    python -m playwright install chromium
    python tools/check_builds.py

Each build names its input box and result areas differently, so the selectors
for each one are listed in BUILDS below.
"""
import pathlib
import time

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent

BUILDS = {
    "original": {"file": "spell-it-original/index.html", "input": "#word-input", "verdict": "#verdict",
                 "symbols": "#sequence", "tile": ".tile", "missing": ".tile.missing"},
    "a-ponytail-off": {"file": "spell-it-a/index.html", "input": "#word", "verdict": "#verdict",
                       "symbols": "#symbols", "tile": ".tile", "missing": ".tile.missing"},
    "b-ponytail-full": {"file": "spell-it-b/index.html", "input": "#word", "verdict": "#verdict",
                        "symbols": "#symbols", "tile": ".tile", "missing": ".tile.none"},
}

# The PRD's acceptance table (section 6), as (input, what must be true).
CHECKS = [
    ("", lambda v, s, m: "type a word to test the table." in v.lower()),
    ("banana", lambda v, s, m: "fully spellable" in v.lower() and s.replace(" ", "") == "Ba·Na·Na"),
    ("kiro", lambda v, s, m: "fully spellable" in v.lower() and s.replace(" ", "") == "K·Ir·O"),
    ("BaCoN", lambda v, s, m: "fully spellable" in v.lower()),
    ("ba-con!", lambda v, s, m: "fully spellable" in v.lower()),
    ("periodic", lambda v, s, m: m == 1),
    ("quiz", lambda v, s, m: m == 2),
    ("jazz", lambda v, s, m: m == 4),
]

LONG_WORD = ("supercalifragilisticexpialidocious" * 400)[:10_200]
FREEZE_SECONDS = 1.0  # set after the Nov 21 test, see ADDENDUM.md


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, b in BUILDS.items():
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.goto((ROOT / b["file"]).as_uri())
            passed = 0
            for word, ok in CHECKS:
                page.fill(b["input"], word)
                verdict = page.inner_text(b["verdict"]).strip()  # compared lowercased: the original shows it in capitals via CSS
                symbols = page.inner_text(b["symbols"]).strip()
                missing = page.locator(b["missing"]).count()
                passed += bool(ok(verdict, symbols, missing))
            # Long-word check: paste 10,200 letters, then time three single keystrokes.
            page.fill(b["input"], LONG_WORD)
            page.wait_for_timeout(300)
            letters_kept = len(page.input_value(b["input"]))
            times = []
            for _ in range(3):
                page.focus(b["input"])
                page.keyboard.press("End")
                start = time.time()
                page.keyboard.type("a")
                page.evaluate("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
                times.append(time.time() - start)
            froze = max(times) > FREEZE_SECONDS
            passed += not froze
            print(f"{name:16} checks {passed}/9   letters kept {letters_kept:>6}   "
                  f"seconds per keystroke {min(times):.2f} to {max(times):.2f}   "
                  f"{'FREEZE' if froze else 'ok'}")
        browser.close()


if __name__ == "__main__":
    main()
