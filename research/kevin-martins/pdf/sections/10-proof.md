---
number: 10
title: Proof & sources
subtitle: Who said what, the revenue behind them, how each document was verified, and what is still missing
---

## The people behind the claims

All revenue figures are what the person (or Kevin, introducing them) says on camera, usually alongside a Shopify dashboard. Nobody has audited them; the two mismatches we found are flagged.

| Person | Role | Revenue claim (exact caption) | What it backs in this report |
|---|---|---|---|
| **Kevin Martins** | Founder, FSC | {{q:hK2Os3wSPI8|I've done multiple six figures|with AI organic drop shipping}} · {{q:WVzIUxovPdA|I've done over $600,000|with AI organic.}} | The whole workflow; P1–P11, R1 |
| **Elias** | Coach | {{q:8zsX4RwrN84|He just hit a $91,000 month,|and 10k day,}} | P12 (author); the 321 prompt; split-testing routine |
| **Harper** | “Advanced coach” | {{q:XNu-o5bXTkk|he was actually able to make $65,000 in 4 days|with that AI influencer.}} | Taught the first AI group call; resin products |
| **John / Jhon** | Member, now a coach | {{q:6o0llGgVRrg|how he did $140,000 with me in the last 30 days.|in the last 30 days.}} | Seedance B-roll with Elias's method (P12) |
| **Adam** | Member | {{q:mA7lA-40Nu0|he just hit a $220,000 month.|$220,000 month.}} | Run two / burner method (his store totals as spoken don't add up exactly) |
| **Tim** | Member | {{q:rIiUPh3Jx8c|he was able to make $118,000 with AI Organic.|with AI Organic.}} | Claude/Higgsfield training from Kevin and Elias |
| **Charlie** (18) | Member | {{q:S9COXhnjijY|He just got off a $110,000 month|last month.}} | Virtual run twos; Claude for backgrounds |
| **Ivan** (19) | Member | {{q:7yKY90-ekTw|Now you just got off of 70K a month.|70K a month.}} | Claude niche-research prompt structures; Pinterest rooms |
| **Trajan** | Member | {{q:0oUpuHm5YK8|how he hit a $66,000 month|with AI organic drop shipping.}} | Swap method; reused showcase with new hooks |
| **Gus** | Member | {{q:kmy9uOj0ve0|Gus just got off a $60,000 month|in July.}} | P13; Pinterest avatars; prompts handed out on calls |
| **Omar** | Member | {{q:putfs1jofwo|He just got off a $41,000 month|drop shipping.}} The dashboard reads 37.3K | Pinterest “doctor” avatar; ICP example (P1, P2) |
| **Vitaly** | Member | {{q:AXjonWCPVCI|He just did a $33,000 month|with me.}} | Hybrid filming plus AI |
| **Theo & Lennon** | Members | {{q:3Uj3cu5MFVw|They just got done doing a 37k month,|back-to-back 7k days}} | Joined with Higgsfield experience |
| **Pedro** (17) | Member | {{q:N0l2H4-_anA|he did $30,000 in a singular month|which we}} will be leaking | Higgsfield ad for a local business |

## The three documents and how they were verified

| Document | Verification (Google Drive metadata) | Where it came from |
|---|---|---|
| **Niche Research Prompt** (P1) | Owner: Kevin's Google account · created 2026-07-30 | Linked free in his Aug 8 video description |
| **FSE SEEDANCE BACKGROUND PROMPT** (P12) | Owner: Kevin's Google account · created 2026-08-05 · last edited 2026-09-12 · **shared with you 2026-10-25** | Shared from inside the group; header credits coach Elias |
| **Brandable Product Research Rubric** (R1) | Owner: Kevin's Google account · created 2026-01-18 · last edited 2026-10-17 | Linked in his video descriptions |

## Method

1. Listed every upload on both of Kevin's channels from April 27 to October 27, 2026 (about 35 videos), and prioritised tutorials, group-call segments and case studies with revenue.
2. Pulled each video's transcript through Perplexity's search index, which holds YouTube captions with timestamps. Direct access to YouTube is blocked from this cloud environment, and I didn't try to get around that.
3. Rebuilt the transcripts by script from the raw search results, exactly as returned (4,000+ caption windows), never retyped.
4. Cut every quote and prompt in this PDF from those windows by script; the build fails if any word differs. Exported documents straight from Google Drive.
5. Checked platform and legal claims (section 7) against primary sources: TikTok, Meta and the FTC.

## What we could not get (and where it is)

- **The FSC Discord itself.** No export was available, so internal chat, files and call recordings posted only in the Discord are not covered. A DiscordChatExporter export would let the toolkit in your repo fill this in (see `data/discord/README.md`).
- **Kevin's context prompt.** It's linked in his Jun 14 and Jun 19 descriptions, but neither the link nor the text is in any index I could reach. If you open it, save it to your Drive; it can then be added verbatim the same way as P12.
- **Prompts shown only on screen** (the Kling prompt structure, full image prompts, Elias's 321 prompt, John's run-two prompts). Captions only record speech.
- **Transcript coverage** ran from about 25% (the 3.5-hour course) to near-complete (short videos). The gaps are listed in the research notes in your repo.
- **Speaker labels** in group calls are inferred from context, not captioned.

## All videos quoted

{{sources}}

## Outside sources (section 7)

- TikTok, AI-generated content labels: support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content · Community Guidelines, Integrity & Authenticity: tiktok.com/community-guidelines/en/integrity-authenticity
- FTC, final rule banning fake reviews and testimonials (16 CFR Part 465, effective Oct 21, 2024): ftc.gov press release (Aug 14, 2024) and the rule's Q&A page
- Meta, combating unoriginal content: creators.facebook.com/blog/combating-unoriginal-content · Rewarding original creators (Mar 2026): about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/
