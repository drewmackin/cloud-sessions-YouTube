#!/usr/bin/env python3
"""Report which research capabilities work in this session, and what's missing for the rest.

  python3 tools/doctor.py

Checks local programs, keys (presence only, never values), network reach and Discord exports.
Connectors (Perplexity, Supadata) live in Claude's tool list, not the shell, so it can't see them:
Claude checks those itself.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
HOSTS = {
    "gemini": "https://generativelanguage.googleapis.com/v1beta/models",
    "youtube_api": "https://www.googleapis.com/youtube/v3/videos",
    "youtube_site": "https://www.youtube.com/robots.txt",
    "discord": "https://discord.com/api/v10/gateway",
    "supadata_api": "https://api.supadata.ai/v1/",
}


def reachable(url: str) -> bool:
    try:
        with urlopen(Request(url, method="GET"), timeout=8):
            return True
    except HTTPError:
        return True  # the server answered, so the network path is open
    except (URLError, TimeoutError, OSError):
        return False


def has_key(name: str) -> bool:
    if os.environ.get(name, "").strip():
        return True
    if name == "GEMINI_API_KEY":
        config = Path.home() / ".config" / "watch" / ".env"
        if config.is_file():
            return any(line.startswith("GEMINI_API_KEY=") and line.split("=", 1)[1].strip()
                       for line in config.read_text().splitlines())
    return False


def docker_state() -> tuple[bool, list[str]]:
    if not shutil.which("docker"):
        return False, []
    info = subprocess.run(["docker", "image", "ls", "--format", "{{.Repository}}:{{.Tag}}"],
                          capture_output=True, text=True, timeout=20)
    return info.returncode == 0, info.stdout.split()


def main() -> int:
    tools = {name: bool(shutil.which(name)) for name in ["ffmpeg", "yt-dlp", "deno", "npx", "docker"]}
    keys = {name: has_key(name) for name in ["GEMINI_API_KEY", "YOUTUBE_API_KEY", "DISCORD_TOKEN", "DISCORD_BOT_TOKEN"]}
    net = {name: reachable(url) for name, url in HOSTS.items()}
    docker_up, images = docker_state()
    exports = [p for p in (ROOT / "data" / "discord").rglob("*.json")] if (ROOT / "data" / "discord").is_dir() else []
    def status(ok: bool, needs: list[str]) -> tuple[str, str]:
        return ("✅ ready", "") if ok else ("❌ blocked", "; ".join(needs))

    rows = [
        ("Deep-watch YouTube videos (watch + Gemini)", *status(
            keys["GEMINI_API_KEY"] and net["gemini"],
            [m for m, bad in [("add GEMINI_API_KEY", not keys["GEMINI_API_KEY"]),
                              ("allow generativelanguage.googleapis.com", not net["gemini"])] if bad])),
        ("Watch local video files (frames + captions)", *status(tools["ffmpeg"], ["install ffmpeg"])),
        ("Download YouTube directly (watch local engine)", *status(
            tools["yt-dlp"] and net["youtube_site"],
            [m for m, bad in [("install yt-dlp", not tools["yt-dlp"]),
                              ("allow youtube.com + googlevideo.com (YouTube may still block cloud IPs)",
                               not net["youtube_site"])] if bad])),
        ("YouTube channel inventory (tools/youtube/channel.py)", *status(
            keys["YOUTUBE_API_KEY"] and net["youtube_api"],
            [m for m, bad in [("add YOUTUBE_API_KEY", not keys["YOUTUBE_API_KEY"]),
                              ("allow www.googleapis.com", not net["youtube_api"])] if bad])),
        ("Transcripts via Supadata", "↪ connector", "Claude checks for supadata tools in-session"),
        ("Web research via Perplexity", "↪ connector", "Claude checks for perplexity tools in-session"),
        ("Analyse Discord exports (intel.py, report.sh)", *status(
            bool(exports), ["put DiscordChatExporter JSON files in data/discord/<server>/"])),
        ("Export Discord from this session (export.sh)", *status(
            keys["DISCORD_TOKEN"] and net["discord"] and tools["docker"],
            [m for m, bad in [("add DISCORD_TOKEN", not keys["DISCORD_TOKEN"]),
                              ("allow discord.com, gateway.discord.gg, cdn.discordapp.com", not net["discord"])] if bad])),
        ("Live Discord via MCP (bot)", *status(
            keys["DISCORD_BOT_TOKEN"] and net["discord"],
            [m for m, bad in [("server owner invites your bot; add DISCORD_BOT_TOKEN", not keys["DISCORD_BOT_TOKEN"]),
                              ("allow discord.com, gateway.discord.gg", not net["discord"])] if bad])),
        ("Browse exports in DCE-frontend (viewer.sh)", *status(tools["docker"], ["install Docker"])),
    ]
    print("# Research toolkit status\n")
    print("| capability | status | what's missing |\n|---|---|---|")
    for name, state, missing in rows:
        print(f"| {name} | {state} | {missing} |")
    print("\nDetails: programs " + ", ".join(f"{k} {'✓' if v else '✗'}" for k, v in tools.items())
          + f"; Docker daemon {'running' if docker_up else 'stopped'}"
          + f"; images {', '.join(i for i in images if 'discord' in i or 'dcef' in i) or 'none pulled'}"
          + f"; Discord export files {len(exports)}"
          + "; keys " + ", ".join(f"{k} {'✓' if v else '✗'}" for k, v in keys.items())
          + "; network " + ", ".join(f"{k} {'✓' if v else '✗'}" for k, v in net.items()) + ".")
    return 0


if __name__ == "__main__":
    sys.exit(main())
