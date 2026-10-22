#!/bin/bash
# Run from IAA/Slides (Dropbox or Mac sync path)
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
cat "$DIR/slides_9.4.1.part1.md" "$DIR/slides_9.4.1.part2.md" "$DIR/slides_9.4.1.part3.md" > "$DIR/slides_9.4.1.md"
echo "Restored slides_9.4.1.md ($(wc -c < "$DIR/slides_9.4.1.md") bytes)"
