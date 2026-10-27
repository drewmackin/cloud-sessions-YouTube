#!/usr/bin/env bash
# Browse DiscordChatExporter JSON exports in a Discord-like interface with search (DiscordChatExporter-frontend).
#
#   bash tools/discord/viewer.sh start <export-folder>   # serves http://localhost:21011
#   bash tools/discord/viewer.sh stop
#
# Meant for your own Linux computer (Windows users: use the project's Windows release instead; macOS isn't
# supported upstream). In a cloud session it still runs, but only Claude can reach the port.
# Project: https://github.com/slatinsky/DiscordChatExporter-frontend (GPL-3.0). The image is about 1.9 GB.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/tools/lib/docker.sh"
IMAGE="slada/dcef:main"
NAME="dcef"

case "${1:-}" in
  start)
    [[ -d "${2:-}" ]] || { echo "Usage: $0 start <export-folder>" >&2; exit 2; }
    folder="$(cd "$2" && pwd)"
    ensure_docker
    ensure_image "$IMAGE"
    docker rm -f "$NAME" >/dev/null 2>&1 || true
    docker run -d --name "$NAME" -p 21011:21011 -v "$folder:/dcef/exports" "$IMAGE" >/dev/null
    echo "Starting viewer for $folder …"
    for _ in $(seq 1 90); do
      if curl -fsS -o /dev/null http://localhost:21011/ 2>/dev/null; then
        echo "Viewer ready: http://localhost:21011"
        exit 0
      fi
      sleep 2
    done
    echo "Viewer did not answer within 3 minutes. Logs: docker logs $NAME" >&2
    exit 1 ;;
  stop)
    docker rm -f "$NAME" >/dev/null 2>&1 && echo "Viewer stopped." ;;
  *)
    sed -n '2,9p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 2 ;;
esac
