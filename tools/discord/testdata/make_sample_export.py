#!/usr/bin/env python3
"""Write a fictional Discord server export in DiscordChatExporter's JSON format.

Used to self-test the pipeline without touching real data. Every person, server
and message here is invented. Field names follow DCE's JsonMessageWriter
(DiscordChatExporter v2.48). Usage: make_sample_export.py OUTPUT_DIR
"""
from __future__ import annotations

import json
import random
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

GUILD = {"id": "900000000000000001", "name": "Hale Capital Community (SAMPLE)", "iconUrl": None}
TARGET = {"id": "500000000000000001", "name": "marcus.hale", "nickname": "Marcus | Hale Capital",
          "roles": [{"id": "1", "name": "Founder", "color": "#E67E22", "position": 10}]}
MEMBERS = [
    {"id": f"50000000000000010{i}", "name": n, "nickname": d, "roles": [{"id": "2", "name": r, "color": None, "position": 1}]}
    for i, (n, d, r) in enumerate([
        ("jen_flips", "Jen", "Member"), ("dlee", "Danny Lee", "Member"), ("rosa.capital", "Rosa", "Pro Member"),
        ("tk_builds", "TK", "Member"), ("ana.m", "Ana M", "Moderator"), ("quietinvestor", "QI", "Member"),
    ])
]
BOT = {"id": "500000000000000999", "name": "WelcomeBot", "nickname": "WelcomeBot", "roles": [], "isBot": True}
CHANNELS = [
    {"id": "700000000000000001", "type": "GuildNews", "category": "INFO", "name": "announcements"},
    {"id": "700000000000000002", "type": "GuildTextChat", "category": "COMMUNITY", "name": "general"},
    {"id": "700000000000000003", "type": "GuildTextChat", "category": "DEALS", "name": "deal-analysis"},
    {"id": "700000000000000004", "type": "GuildTextChat", "category": "DEALS", "name": "ask-marcus"},
    {"id": "700000000000000005", "type": "GuildPublicThread", "category": "general", "name": "Q3 market update"},
]
QUESTIONS = [
    "What cap rate do you need before you'd buy a duplex right now?",
    "Do you still use the 70% rule when rates are this high?",
    "How do you find off-market sellers without cold calling?",
    "Is a DSCR loan worth it for a first rental?",
    "Would you house hack or BRRRR in a market like Columbus?",
    "How much reserve do you keep per door?",
]
ANSWERS = [
    "I want at least a 7.5 cap on a duplex at today's rates, otherwise the debt eats the cash flow.",
    "Yes, but I use 65% now. The 70% rule assumed cheaper money.",
    "Probate lists and driving for dollars. Direct mail still works if you follow up 6+ times.",
    "DSCR is fine for a second or third door. For the first, an FHA house hack is cheaper.",
    "House hack first. BRRRR only works when you can refinance, and appraisals are tight.",
    "Six months of PITI per door, minimum. I broke this rule once and regretted it.",
]
TEACHINGS = [
    "Rule I repeat: buy cash flow, get appreciation as a bonus. Never the other way round.",
    "Full breakdown of last week's deal is on the channel: https://www.youtube.com/watch?v=AAAAAAAAAAA",
    "My underwriting sheet is here: https://docs.google.com/spreadsheets/d/sample-sheet-id/edit?utm_source=discord",
    "New video on finding motivated sellers: https://youtu.be/BBBBBBBBBBB?si=trackingcode",
    "Interest rates will be under 6% by spring. Plan your refis around that.",
    "If you can't explain your exit strategy in one sentence, you don't have one.",
    "Live Q&A recording: https://www.youtube.com/live/CCCCCCCCCCC",
    "Book I recommend to everyone starting out: https://www.biggerpockets.com/store/sample-book",
]
CHAT = ["anyone in the Midwest?", "just closed my first deal!", "thanks, that helped a lot", "lol same",
        "what software do you all use for comps?", "great call on that one"]


def user(u: dict) -> dict:
    return {"id": u["id"], "name": u["name"], "discriminator": "0000", "nickname": u["nickname"],
            "color": None, "isBot": u.get("isBot", False), "roles": u["roles"],
            "avatarUrl": "https://cdn.discordapp.com/embed/avatars/0.png"}


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)
    start = datetime(2025, 1, 6, 14, 0, tzinfo=timezone.utc)
    next_id = iter(range(800000000000000001, 800000000000999999))
    per_channel: dict[str, list[dict]] = {c["id"]: [] for c in CHANNELS}

    def post(channel: dict, author: dict, when: datetime, content: str, **extra) -> dict:
        msg = {"id": str(next(next_id)), "type": extra.pop("type", "Default"), "timestamp": when.isoformat(),
               "timestampEdited": extra.pop("edited", None), "callEndedTimestamp": None,
               "isPinned": extra.pop("pinned", False), "content": content, "author": user(author),
               "attachments": extra.pop("attachments", []), "embeds": extra.pop("embeds", []), "stickers": [],
               "reactions": extra.pop("reactions", []), "mentions": [user(m) for m in extra.pop("mentions", [])],
               "inlineEmojis": []}
        if (ref := extra.pop("reply_to", None)) is not None:
            msg["type"] = "Reply"
            msg["reference"] = {"type": "Default", "messageId": ref["id"], "channelId": channel["id"], "guildId": GUILD["id"]}
        per_channel[channel["id"]].append(msg)
        return msg

    def reactions(n: int) -> list[dict]:
        return [{"emoji": {"id": None, "name": "🔥", "code": "fire", "isAnimated": False, "imageUrl": ""},
                 "count": n, "users": []}] if n else []

    announcements, general, deals, ask, thread = CHANNELS
    t = start
    post(announcements, TARGET, t, "Welcome! Read the rules, then introduce yourself in #general.", pinned=True,
         reactions=reactions(41))
    post(general, BOT, t + timedelta(minutes=5), "Jen joined the server.", type="GuildMemberJoin")
    for week in range(80):
        t = start + timedelta(days=7 * week, hours=rng.randint(0, 6))
        q_author = rng.choice(MEMBERS)
        qi = week % len(QUESTIONS)
        q = post(ask, q_author, t, QUESTIONS[qi], mentions=[TARGET] if week % 3 == 0 else [])
        a = post(ask, TARGET, t + timedelta(minutes=rng.randint(5, 90)), ANSWERS[qi], reply_to=q,
                 reactions=reactions(rng.randint(0, 25)), mentions=[q_author])
        if week % 5 == 0:
            post(ask, q_author, t + timedelta(hours=2), "Thanks, that changes how I'm running my numbers.", reply_to=a)
        if week % 2 == 0:
            post(general, TARGET, t + timedelta(hours=3), TEACHINGS[(week // 2) % len(TEACHINGS)],
                 reactions=reactions(rng.randint(3, 60)), pinned=(week == 10),
                 edited=(t + timedelta(hours=4)).isoformat() if week == 12 else None)
        for k in range(rng.randint(1, 3)):
            post(general, rng.choice(MEMBERS), t + timedelta(hours=4, minutes=10 * k), rng.choice(CHAT))
        if week % 4 == 1:
            deal_post = post(deals, rng.choice(MEMBERS), t + timedelta(days=1),
                             "Deal review please: 3-unit, asking $310k, rents $3,900/mo total.",
                             attachments=[{"id": str(next(next_id)), "url": "https://cdn.discordapp.com/attachments/sample/deal.pdf",
                                           "fileName": "deal.pdf", "fileSizeBytes": 48211}])
            post(deals, TARGET, t + timedelta(days=1, hours=1),
                 "Pass at that price. Run it at 65% and offer $255k. Taxes are underestimated.",
                 reply_to=deal_post, reactions=reactions(rng.randint(2, 15)))
        if week % 13 == 5:
            post(announcements, TARGET, t + timedelta(days=2),
                 f"Monthly call this Thursday. Replay will be on YouTube: https://www.youtube.com/watch?v=DDDDDDDDDD{week % 10}",
                 reactions=reactions(rng.randint(10, 30)))
    tq = post(thread, MEMBERS[2], start + timedelta(days=250), "Marcus, where do you think prices go in Q3?")
    post(thread, TARGET, start + timedelta(days=250, hours=2),
         "Flat to slightly down nationally, up in Midwest metros. I'm buying in Indianapolis.", reply_to=tq,
         reactions=reactions(19))
    post(thread, TARGET, start + timedelta(days=251), "", attachments=[
        {"id": str(next(next_id)), "url": "https://cdn.discordapp.com/attachments/sample/q3-chart.png",
         "fileName": "q3-chart.png", "fileSizeBytes": 91822}])

    for ch in CHANNELS:
        msgs = sorted(per_channel[ch["id"]], key=lambda m: m["timestamp"])
        doc = {"guild": GUILD, "channel": {**ch, "categoryId": None, "topic": None},
               "dateRange": {"after": None, "before": None},
               "exportedAt": datetime(2026, 10, 27, tzinfo=timezone.utc).isoformat(),
               "messages": msgs, "messageCount": len(msgs)}
        name = f"{GUILD['name']} - {ch['category']} - {ch['name']} [{ch['id']}].json"
        (out / name).write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    total = sum(len(v) for v in per_channel.values())
    print(f"Wrote {len(CHANNELS)} channel exports, {total} messages → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
