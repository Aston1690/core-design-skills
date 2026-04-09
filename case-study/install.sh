#!/bin/bash
set -e

SKILL_DIR="$HOME/.claude/skills/case-study"
REPO="https://raw.githubusercontent.com/Aston1690/core-design-skills/main/case-study"

echo "Installing case-study skill..."
mkdir -p "$SKILL_DIR/scripts"
curl -fsSL "$REPO/SKILL.md" -o "$SKILL_DIR/SKILL.md"
curl -fsSL "$REPO/scripts/generate_images.py" -o "$SKILL_DIR/scripts/generate_images.py"
echo "Done — case-study skill installed to $SKILL_DIR"
