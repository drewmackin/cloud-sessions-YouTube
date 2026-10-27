#!/usr/bin/env bash
# Prepare a fresh cloud container for the research toolkit. The research-person skill runs it first;
# it is fast once done and safe to rerun. On your own computer it does nothing unless you
# pass --force, so it never changes your local watch settings or starts Docker for you.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="${TMPDIR:-/tmp}/research-bootstrap.log"
[[ -n "${CLAUDE_CODE_REMOTE:-}" || "${1:-}" == "--force" ]] || exit 0

{
  echo "== bootstrap $(date -u +%FT%TZ)"
  command -v yt-dlp >/dev/null || uv tool install "yt-dlp[default,curl-cffi]" \
    || python3 -m pip install --user "yt-dlp[default,curl-cffi]"
  command -v deno >/dev/null || npm install --global --silent deno
  # Skip the watch skill's interactive first-run questions: Gemini when GEMINI_API_KEY is set, otherwise
  # local frames + captions, with no paid speech-to-text fallback.
  python3 "$ROOT/.claude/skills/watch/scripts/setup.py" --engine auto --backend none --detail balanced
} >>"$LOG" 2>&1

# Docker images for the Discord exporter are pulled in the background so the session starts at once.
(
  source "$ROOT/tools/lib/docker.sh"
  ensure_docker && ensure_image tyrrrz/discordchatexporter:stable
) >>"$LOG" 2>&1 &

echo "Research toolkit ready (log: $LOG). Run 'python3 tools/doctor.py' to see which capabilities are live."
