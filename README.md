# cloud-sessions-YouTube: person research toolkit

Give Claude a name, and it researches that person across the web, their YouTube channel and their Discord
server, then writes a sourced dossier in `research/<person>/`. Built for Claude Code cloud sessions; it
also works in Claude Code on your own computer.

## What's installed

| Part | Role | Source |
|---|---|---|
| **watch** skill | Actually watches videos: Gemini views the whole video, or frames + captions locally | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) (MIT), vendored in `.claude/skills/watch` |
| **Supadata** connector | Cheap transcripts for many videos (YouTube, TikTok, Instagram, X) | [supadata-ai/mcp](https://github.com/supadata-ai/mcp), hosted; you add it on claude.ai |
| **DiscordChatExporter** | Exports a Discord server to JSON | [Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) (MIT), Docker image, `tools/discord/export.sh` |
| **Chat Analytics** | Interactive community report (activity, sentiment, who talks to whom) | [mlomb/chat-analytics](https://github.com/mlomb/chat-analytics) (AGPL-3.0), `tools/discord/report.sh` |
| **DiscordChatExporter-frontend** | Browse and search an export in a Discord-like UI (Windows/Linux) | [slatinsky/DiscordChatExporter-frontend](https://github.com/slatinsky/DiscordChatExporter-frontend) (GPL-3.0), `tools/discord/viewer.sh` |
| **Discord MCP** | Lets Claude read a server live through a bot | [SaseQ/discord-mcp](https://github.com/SaseQ/discord-mcp) (MIT), `.mcp.json` → `tools/discord/discord-mcp.sh` |
| Glue | Person-focused Discord evidence pack, YouTube channel inventory, health check, research playbook | `tools/discord/intel.py`, `tools/youtube/channel.py`, `tools/doctor.py`, `.claude/skills/research-person` |

Already connected on your account: **Perplexity** (web research).

## How it fits together

```
name ─► identity & footprint (Perplexity + web search)
          │
          ├─► YouTube: channel.py inventory ─► Supadata transcripts (breadth) ─► watch/Gemini deep-watch (depth)
          │                                         ▲
          ├─► Discord: export ─► intel.py evidence pack ─► youtube_links.txt ┘   + Chat Analytics report
          │
          └─► cross-check (track record, public vs private message, money, claims vs records)
                    └─► research/<person>/dossier.md  (every claim tagged and sourced)
```

## Setup checklist

Do these once. Each one unlocks a lane, and the toolkit runs whatever is ready.

1. **Merge this branch** (`research-toolkit`) into `main`, so every new cloud session picks the toolkit up.
2. **Supadata connector.** claude.ai → Settings → Connectors → *Add custom connector* → URL
   `https://api.supadata.ai/mcp`, then sign in. Free plan: 100 transcripts a month.
3. **Keys and settings.** Add these as environment variables on your cloud environment: click the
   environment name in a cloud session's title bar → Edit → Environment variables:
   - `GEMINI_API_KEY`: free at https://aistudio.google.com/apikey. Lets `watch` view whole YouTube videos,
     free up to 8 hours a day for public videos.
   - `YOUTUBE_API_KEY` (optional): a Google Cloud API key with *YouTube Data API v3* enabled. Lists every
     video on a channel with view counts.
   - Anyone who can use the environment can read its variables. It's your personal environment, but don't
     share it.
4. **Discord access.** Pick one:
   - **Export on your computer (recommended).** See `data/discord/README.md`. Your Discord login never
     touches the cloud.
   - **Export from the cloud.** Add `DISCORD_TOKEN`, and allow `discord.com`, `gateway.discord.gg` and
     `cdn.discordapp.com` under the environment's Network access (Custom).
   - **Live bot.** If the server owner invites your bot, add `DISCORD_BOT_TOKEN` (plus the same network
     domains), and the `discord` MCP server starts with the session.
   - Using a personal account token breaks Discord's Terms of Service and risks a ban. DiscordChatExporter's
     own README says so.

Check progress anytime by asking Claude to run `python3 tools/doctor.py`.

## Verified on 2026-10-27 (cloud session, default "Trusted" network)

- `watch`: extracted frames from a test video and Claude read the on-screen text; Gemini API reachable
  (fails only without a key).
- DiscordChatExporter v2.48.0 container runs; it stops cleanly with a network message until discord.com is
  allowed.
- `intel.py` and Chat Analytics produced full reports from a fictional sample server
  (`tools/discord/testdata`); DiscordChatExporter-frontend loaded the same sample and rendered its channels.
- Discord MCP container starts and reports it can't reach Discord until the network allows it.
- `python3 -m unittest discover tools/tests`: 8 offline tests pass.
