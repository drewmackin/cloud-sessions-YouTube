#!/usr/bin/env bash
# Launch the Discord MCP server (https://github.com/SaseQ/discord-mcp, MIT) over stdio for Claude Code.
# Registered in .mcp.json as "discord". It only works with a bot that the server's owner has invited:
# needs DISCORD_BOT_TOKEN (and optionally DISCORD_GUILD_ID) in the environment, plus network access to
# discord.com and gateway.discord.gg. Without a token it exits at once, so /mcp lists it as failed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/tools/lib/docker.sh"
IMAGE="saseq/discord-mcp:latest"

if [[ -z "${DISCORD_BOT_TOKEN:-}" ]]; then
  echo "discord-mcp: DISCORD_BOT_TOKEN is not set; see README.md, 'Discord access'." >&2
  exit 3
fi
ensure_docker >&2
ensure_image "$IMAGE" >&2
proxy_args
exec docker run --rm -i "${PROXY_ARGS[@]}" -e DISCORD_TOKEN="$DISCORD_BOT_TOKEN" \
  -e DISCORD_GUILD_ID="${DISCORD_GUILD_ID:-}" "$IMAGE"
