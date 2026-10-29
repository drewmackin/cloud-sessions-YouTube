#!/bin/bash
# Print every session and subagent log of this research session (old and new project dirs).
ls /root/.claude/projects/-home-user/69af9fed-564f-5f37-9ac0-5ff41e97bcd0.jsonl \
   /root/.claude/projects/-home-user/69af9fed-564f-5f37-9ac0-5ff41e97bcd0/subagents/*.jsonl \
   /root/.claude/projects/-home-user-cloud-sessions-youtube/69af9fed-564f-5f37-9ac0-5ff41e97bcd0.jsonl \
   /root/.claude/projects/-home-user-cloud-sessions-youtube/69af9fed-564f-5f37-9ac0-5ff41e97bcd0/subagents/*.jsonl 2>/dev/null
