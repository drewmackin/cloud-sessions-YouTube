# Discord exports go here

Put DiscordChatExporter **JSON** files in a folder per server: `data/discord/<server-name>/*.json`.

**Easiest route (keeps your Discord token off the cloud):**

1. Download DiscordChatExporter from https://github.com/Tyrrrz/DiscordChatExporter/releases. Use the
   desktop app for your system, for example `DiscordChatExporter.win-x64.zip` for Windows.
2. Follow its built-in guide to sign in, pick the server, and export with **Format: JSON** and
   **Threads: All**. For very large channels, set a partition limit such as `10mb`.
3. Upload the files here. On github.com, open this folder, choose *Add file → Upload files* and drag them
   in (25 MB per file on the website). Or attach them in a Claude chat and ask Claude to save them here.

Read first: DiscordChatExporter's README warns that automating a user account is against Discord's Terms
of Service and may get the account banned. A bot invited by the server owner is the compliant route.

These files contain other members' messages too. This repo is private; keep it that way, and keep raw
exports out of anything you publish.
