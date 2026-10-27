#!/usr/bin/env bash
# Build Chat Analytics' interactive HTML report from DiscordChatExporter JSON files.
#
#   bash tools/discord/report.sh <export-folder> <output.html>
#
# Runs entirely offline (https://github.com/mlomb/chat-analytics, AGPL-3.0); chat data never leaves this machine.
# The HTML is self-contained: open it in a browser, or publish it as a private artifact.
set -euo pipefail

[[ $# -eq 2 ]] || { sed -n '2,7p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 2; }
input="$1"
output="$2"
[[ -d "$input" ]] || { echo "Not a folder: $input" >&2; exit 2; }
mkdir -p "$(dirname "$output")"
npx --yes chat-analytics@1.1.2 --platform discord --inputs "$input/**/*.json" --output "$output"
