#!/usr/bin/env bash
# Recount the size numbers in the scorecard. Added Nov 22, 2026.
# Usage (from the repo root): bash tools/count_size.sh
for f in spell-it-original spell-it-a spell-it-b; do
  h="$f/index.html"
  echo "$f: total lines $(wc -l <"$h"), JS lines $(awk '/<script/,/<\/script>/' "$h" | wc -l), CSS lines $(awk '/<style/,/<\/style>/' "$h" | wc -l), bytes $(wc -c <"$h"), console.assert lines $(grep -c 'console.assert' "$h")"
done
