#!/usr/bin/env bash
# Export a Discord server (or a few channels) to JSON with DiscordChatExporter, via its official Docker image.
#
#   bash tools/discord/export.sh guilds                      # servers the token can see
#   bash tools/discord/export.sh channels <server-id>        # channels in one server
#   bash tools/discord/export.sh server <server-id> [--after 2025-01-01]
#   bash tools/discord/export.sh channel <channel-id> [<channel-id> ...] [--after DATE]
#
# Output goes to data/discord/<server-or-channel-id>/ as DCE JSON, which tools/discord/intel.py reads.
# Needs DISCORD_TOKEN in the environment and network access to discord.com. The token is passed to the
# container through the environment and never printed.
#
# Read before using a personal account token: DiscordChatExporter's README warns that automating a user
# account is against Discord's Terms of Service and can get the account banned. A bot token that the
# server owner invited is the compliant route. Exporting on your own computer with DCE's desktop app,
# then copying the JSON files into data/discord/, keeps your token out of the cloud entirely.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/tools/lib/docker.sh"
IMAGE="tyrrrz/discordchatexporter:stable"

usage() { sed -n '2,8p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 2; }
[[ $# -ge 1 ]] || usage
if [[ -z "${DISCORD_TOKEN:-}" ]]; then
  echo "DISCORD_TOKEN is not set. Add it to the environment (see README.md, 'Discord access')." >&2
  exit 3
fi

if ! curl -sS -o /dev/null --max-time 15 https://discord.com/api/v10/gateway 2>/dev/null; then
  echo "Can't reach discord.com from here. In a cloud session, allow discord.com, gateway.discord.gg and" >&2
  echo "cdn.discordapp.com under the environment's network access, or export on your own computer instead." >&2
  exit 4
fi
ensure_docker
ensure_image "$IMAGE"

run_dce() {
  local out="$1"; shift
  mkdir -p "$out"
  proxy_args
  docker run --rm "${PROXY_ARGS[@]}" -e DISCORD_TOKEN -e FUCK_RUSSIA=true -v "$out:/out" "$IMAGE" "$@"
}

command="$1"; shift
case "$command" in
  guilds)
    run_dce "$(mktemp -d)" guilds ;;
  channels)
    [[ $# -ge 1 ]] || usage
    run_dce "$(mktemp -d)" channels --guild "$1" --include-threads All ;;
  server)
    [[ $# -ge 1 ]] || usage
    id="$1"; shift
    out="$ROOT/data/discord/$id"
    run_dce "$out" exportguild --guild "$id" --format Json --include-threads All --utc \
      --output "/out/%G - %P - %C [%c].json" --parallel 2 "$@"
    echo "Exported to $out" ;;
  channel)
    [[ $# -ge 1 ]] || usage
    ids=()
    while [[ $# -gt 0 && "$1" != --* ]]; do ids+=("$1"); shift; done
    out="$ROOT/data/discord/channels"
    run_dce "$out" export --channel "${ids[@]}" --format Json --utc --output "/out/%G - %P - %C [%c].json" "$@"
    echo "Exported to $out" ;;
  *)
    usage ;;
esac
