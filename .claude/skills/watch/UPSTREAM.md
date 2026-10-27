# Upstream

Vendored from https://github.com/bradautomates/claude-video (MIT, see LICENSE)
- Upstream commit: `03ceb42f7fa2c4439aca01752118044baabffb8f` (release 0.3.2, committed 2026-09-25)
- Copied: `skills/watch/` unchanged, minus the packaging-only `scripts/build-skill.sh`.
- Not copied: the plugin's SessionStart hook (this repo's `tools/bootstrap.sh` covers setup).

To update: re-copy `skills/watch/` from a newer upstream commit and update the hash above.
