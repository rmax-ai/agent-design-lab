#!/bin/bash
#
# Lock Run Script
#
# Marks a run as immutable after completion.
#

set -e

usage() {
    echo "Usage: $0 <manifest.json>"
    echo "  Marks a run as immutable"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
fi

MANIFEST="$1"

if [ ! -f "$MANIFEST" ]; then
    echo "Error: Manifest not found: $MANIFEST"
    exit 1
fi

# Check if already locked
LOCKED=$(jq -r '.immutability.locked // false' "$MANIFEST")
if [ "$LOCKED" = "true" ]; then
    echo "Warning: Run already locked"
    exit 0
fi

# Update manifest with lock information
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")

jq --arg timestamp "$TIMESTAMP" '
  .immutability.locked = true |
  .immutability.locked_at = $timestamp |
  .immutability.lock_reason = "run_completed"
' "$MANIFEST" > "$MANIFEST.tmp"

mv "$MANIFEST.tmp" "$MANIFEST"

echo "✓ Run locked at $TIMESTAMP"
echo "  Manifest: $MANIFEST"

exit 0
