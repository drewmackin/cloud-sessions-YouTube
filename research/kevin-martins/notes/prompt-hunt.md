# Prompt hunt: spoken prompts in Kevin Martins videos (2026-10-28)

Method: `perplexity_search`, `search_domain_filter: ["youtube.com"]`, `max_results: 3`, `max_tokens_per_page: 2048`.
Windows below are copied character for character from the search results (YouTube auto-captions, caption
errors kept: "cloud"/"CL" = Claude, "Higsfield"/"Hicksfield"/"Higgs Field" = Higgsfield, "C dance"/"Sea Dance" =
Seedance, "cling" = Kling). `{ts:N}` = seconds into the video. A window ends where the search result's excerpt
ends; nothing is stitched across a "..." gap. Descriptions outside the code blocks are my own words.

Already in the report (not re-hunted): the 13 prompts starting "Now based off this information," / "All right,
based off of this information," / "Hey, listen. Here's the product" / "Please give me a prompt to recreate" /
"hey, listen, I want you to lock the environment" / "Listen, I want five, maybe eight" / "Listen, lock the
environment, right?" / "here are three more images" / "Listen, do not move the camera," / "Hey, listen, I want
you to write me a prompt" / "give me other words for tonitis." plus the two documents.

---

## Candidate prompts

### C1. Seedance background swap: what to tell Claude about the clip (Hgc13jXWm_c, ts 990)

- **Video:** Hgc13jXWm_c "How To Print $50k/mo With Seedance Background Swapping (Step by Step)" (Kevin Martins, 2026-08-13)
- **Starts:** {ts:990} (the quoted words begin on the caption line stamped 990; the lead-in "So," sits just before it)
- **Who says it:** Kevin Martins, quoting what he typed to Claude ("basically what I said was").
- **What it is for:** step 2 of his four-step Seedance background swap. Step 1 is pasting the free "instruction
  prompt" (the FSE Seedance Background Prompt document, P12 in the report) into a new Claude chat. Then you download a
  competitor clip (SnapTik on desktop), mute it, drop it into the same chat and "clearly say what you want changed",
  kept simple. These are the two messages he sent for a car-enthusiast version, asking for two prompt versions. Claude's
  output goes into Seedance inside Higgsfield (max 15 s, 720p, two variations), then gets upscaled in Topaz (1K, 60 fps).
  It is in the existing corpus but not quoted in the report. It came back again in this hunt (search 3), so it is in this log.
- **Verbatim window** (search 3, query "How To Print $50k/mo With Seedance Background Swapping (Step by Step) Kevin
  Martins Claude prompt background swap 720p 1080p scam Topaz"):

```
Link in the description.
All right.
Step number
{ts:952} two is going to be downloading the clip that you want to use.
So, for example, let's say you want to, I don't know,
{ts:958} steal a random clip from a TikTok competitor.
You're going to go ahead and download it to your camera roll.
In this
{ts:963} case, if you're going to be on your computer, use something like SnapTik.
All right.
And you want to remove all
{ts:968} the copyrighted sound.
So, let's say the competitor was using, you know, a sound from Lil Baby.
You're better off
{ts:974} just muting the video so Claude doesn't start tripping about copyright.
All right.
So, you're going to drop it You
{ts:979} want to drop it into Claude and clearly say what you want changed, right?
Just be super simple.
Don't over
{ts:984} overcomplicate the prompt, right?
So, in this scenario, I went ahead and stole the clip from my competitor.
So,
{ts:990} basically what I said was, "For this video, don't forget to remove the text and build me a super niche and stylish
{ts:996} background, the way you know how to do them, right?"
Because again, we already instructed Claude, so it already knows
{ts:1002} what, you know, what we need.
Um and I said, "For a car enthusiast, add lots of props, incredible details, or maybe
{ts:1008} change the wall color in the back.
Make it super clean.
Give me two versions of the prompt, please, and don't forget the
{ts:1014} method that we use every single time."
And so, again, remind it to use the instruction prompt that you went ahead
{ts:1019} and fed it before telling it what to do.
```

- **The prompt itself, two quotes:** "For this video, don't forget to remove the text and build me a super niche and stylish
  background, the way you know how to do them, right?" and "For a car enthusiast, add lots of props, incredible details,
  or maybe change the wall color in the back. Make it super clean. Give me two versions of the prompt, please, and
  don't forget the method that we use every single time." (Each quote crosses caption line breaks inside one window.
  Nothing is joined across a gap.)

### C2. Ask Claude for the creation-process steps (hK2Os3wSPI8, ts 884; also GfhpQLqF658 at about 5345)

- **Video:** hK2Os3wSPI8 "How I Make AI Organic Videos That Print $100k/m (Step by Step)" (2026-06-19). The same
  footage is in GfhpQLqF658 "Leaking My $1M AI Organic Dropshipping Blueprint (FULL COURSE)" (2026-06-14), where the
  window starts just before {ts:5350}.
- **Starts:** on the line stamped {ts:884}, which reads "If you're having trouble getting ideas for creation process, just
  ask Claude." The prompt words start right after it and run past {ts:889}.
- **Who says it:** Kevin Martins.
- **What it is for:** brainstorming B-roll shots. It sits between the "lock the environment" step (P6) and the bulk
  B-roll step (P7). If you don't know what the making of your product looks like, ask Claude for the steps. Then use
  them as the list of shots for "five, maybe eight different shots of my avatar doing this, this, this, and that". This
  fills part of the 860-914 gap that earlier gap-fill rounds could not get.
- **Verbatim window, hK2Os3wSPI8** (search 13, query "Kevin Martins AI organic videos step by step first b-roll image of my
  shorty holding the design sketches laid out on her desk I told Claude make her sketching drawing the watch design"):

```
{ts:884} If you're having trouble getting ideas for creation process, just ask Claude.
Be like, "Listen, what would the
{ts:889} creation process of a watch look like step by step?"
And boom, there you go.
You'll take your uh you'll you'll you'll
{ts:896} take that as inspiration, right?
And so, as you can see, this was my first b-roll image, right?
Of my shorty holding uh
{ts:902} you know, the design.
As you can see, it kept everything consistent.
We have all these other sketches laid out on her
{ts:908} desk.
You could even see that she was locking in hard, sipping on some coffee.
And bro, look at the attention to
{ts:913} detail, okay?
Even like the lighting, bro, on the car, man.
Crazy.
Crazy.
Now, step number two, this
{ts:920} is when it gets a little bit crazy, right?
You want to start making the first batch of your B-rolls in bulk,
{ts:925} right?
You can generate up to 10 to 15 and yes, you can reuse them across your videos as long as you make new hooks
{ts:932} every single time.
For this example, I made six different B-roll images that essentially
{ts:938} shows progression, right?
From start to finish, all right?
And again, if you want an idea of what to say to Claude,
{ts:945} you want to go ahead and give it your master frame and you're going to be like, "Listen, I want
{ts:951} five, maybe eight different shots of my avatar doing this, this, this, and that."
```

- **Same moment in the full course, GfhpQLqF658** (search 13, same result set):

```
Be like, "Listen, what would the creation process of a watch look like step by
{ts:5350} step?"
And boom, there you go.
You'll take your uh you'll you'll take that as inspiration, right?
And so, as you can
{ts:5355} see, this was my first B-roll image, right, of my shorty holding uh you know, the design.
```

- **The prompt itself:** "Listen, what would the creation process of a watch look like step by step?" (Swap "a watch" for
  your product.)

### C3. Follow-up to P7: one shot per step (GfhpQLqF658, ts 5421)

- **Video:** GfhpQLqF658 (full course), module 4. Kevin Martins.
- **Starts:** on the line stamped {ts:5421}, which reads "And then based off those steps, like, now I want 10 different shots
  of her actually, you know, doing those uh those".
- **What it is for:** a borderline item, not a separate prompt. It is the next sentence after P7 in the same window.
  After Claude lists the steps (C2), you ask for one shot per step. It is in the existing corpus but the report does not
  quote it. Use it as a P7 note if at all.
- **Verbatim window** (search 13):

```
Now, step number two.
This is when it gets a little bit crazy, right?
You want to start making the
{ts:5380} first batch of your B-rolls in bulk, right?
You can generate up to 10 to 15.
And yes, you can reuse them across your
{ts:5386} videos as long as you make new hooks every single time.
For this example, I made six uh different B-roll images that
{ts:5395} essentially shows progression right from start to finish.
All right.
And again, if you want an idea of what to say to
{ts:5402} Claude, you want to go ahead and give it your master frame.
And you're going to be like, "Listen, I want five, maybe
{ts:5409} eight different shots of my avatar doing this, this, this, and that."
And so, again, like I mentioned before, if you
{ts:5416} ask Claude what's the step-by-step process of making a watch, it'll probably spit out 10 different steps.
{ts:5421} And then based off those steps, like, now I want 10 different shots of her actually, you know, doing those uh those
{ts:5428} steps.
```

- **The words:** "now I want 10 different shots of her actually, you know, doing those uh those steps." (Paraphrased
  instruction. Kevin does not frame it as an exact quote.)

### C4. Translate a proven winner for a new market (FAtJ50Kh5-8, ts 1089-1096)

- **Video:** FAtJ50Kh5-8 "From Uber Driver To $65K/Month With AI Organic Dropshipping" (Kevin Martins channel, 2026-06-16).
  Case study with student John (spelled "Jhon" in later videos).
- **Starts:** the prompt words are on the line stamped {ts:1096}. The lead-in starts at {ts:1089}.
- **Who says it:** probably John, answering Kevin's "all I got to do is just translate to that language and then boom,
  right?". The captions do not mark speaker turns, so the attribution is **unverified**. The words after it, "Or at least
  I'm making money in that way", fit John, who runs the same product in the US, Spanish and European markets.
- **What it is for:** running an already-proven product in another language market (France, Italy, Spain). You ask
  Claude or ChatGPT to translate the hook/caption text naturally instead of word for word. Short and generic, but it is
  an instruction spoken to an AI tool. It is in the existing corpus but not in the report. It came back in search 16.
- **Verbatim window** (search 16, query "From Uber Driver To $65K/Month With AI Organic Dropshipping Kevin Martins John
  translate this in a natural way I don't know Italian French Elias prompt split testing markets Spanish"):

```
{ts:1067} to post more content, but you know, why not just, you know, run an already proven uh winner from the states into,
{ts:1073} you know, France or another country that is also high converting, you know, because it's like you have so much more
{ts:1078} confidence into what you're doing because like I I know this prints, all I got to do is just translate to that
{ts:1082} language and then boom, right?
Um yeah, exactly.
And sometimes you guys are thinking like, okay, I don't know
{ts:1089} the language.
I don't know uh Italian, I don't know French, so I cannot.
Bro, you have chat GPD, you have cloud, you can
{ts:1096} just say to cloud or shad translate this in a natural way and that's it, right?
{ts:1102} Or at least I'm making money in that way.
If you don't want to believe it, it's your your problem.
```

- **The prompt itself:** "translate this in a natural way" ("cloud or shad" = Claude or ChatGPT, as captioned).
- **Related, not a prompt:** in the same video John says {ts:766} "I uh started this product with one of the prompts that
  Elias gave us in one of the calls." and {ts:779} "Because with your with your with your prompt, I have made around
  10K." The Elias prompt's text is not spoken in any window retrieved.

---

## Out-of-scope leads (not Kevin's channels; listed so nobody re-hunts them)

### L1. "Omar" channel: voice prompt that turns a viral video into a Claude skill (IYUWNumtxHc, ts 199-226 and 323-330)

- **Video:** IYUWNumtxHc "How I Get Claude to Do 90% of the Work for My Organic Dropshipping Products", channel header
  "## Omar", dated 2026-08-25. **Unverified** whether this is Kevin's student Omar (Red Light Therapy, FSC). Nothing in
  the result links it to Kevin.
- **What it is for:** you attach the clip links and their first and last frames, then dictate (Claude's voice feature) how
  the concept should be saved as a reusable skill. Later you change single elements by telling Claude, e.g. the avatar's
  hair or the background.
- **Verbatim windows** (search 26, query "Leaking My $1M AI Organic Dropshipping Blueprint FULL COURSE Omar red light
  therapy doctor avatar Pinterest before and after rat monkeys hook prompt Claude how do you make your videos"):

```
When it comes to
{ts:199} saving this concept, you're going to use the voice feature and listen to the following what I'm
{ts:205} saying.
So, for example, for the first attached link, if you use a specific prompt for it,
{ts:211} still keep it, use it the same, and do it with the adjustments I tell you.
For example, if I tell you to change the
{ts:218} avatar to an avatar image I send you in the chat, then you should change it, but keep everything exactly, literally, the
{ts:226} same.
```

```
And if you need any adjustments, if you want to
{ts:323} change the avatar, you want to change the background, you just tell it.
Just simple.
Change the girl to a girl
{ts:330} who is blonde.
Change the app Change the background to this background I attached in the in the chat.
```

### L2. es2hnNDl8K4 "Claude + Higgsfield = $30k/mo on tiktok shop": confirmed not Kevin's

- Search 24 returned it with channel header "## David Margaryan" and "Date: 2026-06-20" (the corpus metadata says the same).
  The video is about his client Tyler's faceless TikTok Shop account (Kalodata, then Nano Banana Pro, then Kling 2.6).
- No spoken prompt. Both prompts are only shown on screen: "And give it this exact prompt. So, you can Feel free to
  pause this video, copy and paste this prompt" (around {ts:506}-{ts:513}) and "And you're going to give it the this new
  prompt right here. Again, go ahead, pause the video, copy and paste this prompt." (around {ts:551}-{ts:556}).

---

## Near-misses (already in the corpus or course notes, or no prompt text spoken)

- hK2Os3wSPI8 {ts:1741} / GfhpQLqF658 about {ts:6197}-{ts:6205}: "you could even tell Claude to copy a video from um you
  know, your For You page by just literally sending it a screenshot". He describes a method (send a screenshot and
  Claude breaks it down into locked environment, camera framing, hands and action), not prompt wording. It came back
  again in search 21. It is already in the corpus and in notes/course.md, but not in the report.
- GfhpQLqF658 {ts:6363} (also hK2Os3wSPI8 {ts:1907}): "just ask clot to add a camera shake to add realism". A
  variant of the camera-shake line the report already quotes (section 03). Came back in search 27.
- GfhpQLqF658 {ts:8866}-{ts:8879} (Elias and Kevin): "Uh that's pretty crazy because people use my prompt until now." and
  "You were the one that found the prompt to do the 321." In search 2 the next words are "Yeah, there was a concept,
  bro." The 321 prompt is never read out.
- FAtJ50Kh5-8 {ts:766} (John): his first product came from "one of the prompts that Elias gave us in one of the calls".
  The text is not spoken.
- kmy9uOj0ve0 {ts:802} (Gus): "Immediately right after the call he gives us the prompts. I copy paste the prom, make my
  own." The prompts themselves are not read.
- b3xKO_MABXg {ts:2183} (Money Bash): "if you guys want, I can send in my like avatar prompt." and then "It's It's long
  and deep." He does not read it (search 27).
- S9COXhnjijY {ts:563} (Charlie): "Just got to prompt it correctly." No wording. His {ts:1210}-{ts:1217} line about telling
  Claude to make a matching background is already in the report (section 03).
- Hgc13jXWm_c {ts:385} and {ts:315}: descriptions of the swaps he made ("I removed the text. I added this person like in like
  this very mysterious looking place with some Rolexes"; "I added some chrome jeans"). These describe results, not
  messages to Claude.
- T6-LXSu0qHw {ts:222}: "at the end you say, "Just kidding, we sell them link in our bio". This is on-screen or spoken
  video text for run-twos, not an AI prompt.
- OTRP8hk1wr4 {ts:675}: "Using, "Hey, hi. This is fantastic."". Probably audio from the screen recording. Not a prompt.

## Videos where this hunt found no new prompt

- **GfhpQLqF658** (full course): no prompt outside the tutorial footage. C2 and C3 sit in its module 4, which is the same
  footage as hK2Os3wSPI8. Module 2 (Atlas AI store build) only pastes an AliExpress link, with no typed prompt (search 8).
  Modules 3, 5 and 6 returned no prompt text.
- **OTRP8hk1wr4**: only P1/P2, which are already in the report (searches 20, 38).
- **b3xKO_MABXg**: none (searches 27 and incidental hits).
- **T6-LXSu0qHw**: none. Run-twos and 321s are described as concepts only, with no prompt wording (searches 7, 19, 34, 41).
- **kmy9uOj0ve0** (Gus): nothing beyond P13 (search 11).
- **6o0llGgVRrg** (Jhon $140K): none (searches 17, 36).
- **S9COXhnjijY** (Charlie): none new (search 25).
- **7yKY90-ekTw** (Ivan): none ("niche research with Claude, building like prompt structures", with no wording) (search 28).
- **XNu-o5bXTkk**: none (search 30). **mq4PgXJAw8s**: not searched on its own. Its text is the same script as XNu-o5bXTkk
  (earlier gap-fill: offset about +31 s), and the existing corpus covers 0-337 s except about 120-139, 250-269 and 286-308.
- **es2hnNDl8K4**: not Kevin's video (David Margaryan, 2026-06-20). Its prompts are only on screen (search 24).
- **pjprEGW89-U** (plushies): none. It is a brand-history video. The AI part is only "this part is all AI" (search 15).
- **0EwzL3Etidg**: none (search 35). **WVzIUxovPdA**: none (search 32).
- New prompts found only in: **Hgc13jXWm_c** (C1), **hK2Os3wSPI8 / GfhpQLqF658** (C2, C3) and **FAtJ50Kh5-8** (C4).

## Still not retrievable (gaps that every query skipped)

- hK2Os3wSPI8 about 1100-1129 (GfhpQLqF658 about 5558-5591): between "get your prompt from Claude" and "spit out the
  prompt for Kling 3.0". If Kevin read the Kling prompt aloud anywhere, it is here. Searches 9, 14, 31 and 40 did not
  reach it.
- hK2Os3wSPI8 about 865-884, 1019-1032 and 1946-2063 (the outro).
- Hgc13jXWm_c about 10-231, 326-385, 390-472, 479-659, 740-843 and after 1124. The "saucy" copyright workaround Kevin
  promises is never reached (searches 18, 22).
- T6-LXSu0qHw about 1159-1372 and 1591-1662. pjprEGW89-U is mostly unretrieved (1:00:57 long).

## Search log (all 41 perplexity_search calls; youtube.com filter, max_results 3, max_tokens_per_page 2048)

1. Kevin Martins Leaking My $1M AI Organic Dropshipping Blueprint FULL COURSE 11 Labs voices voiceover script Claude write me a script
2. Leaking My $1M AI Organic Dropshipping Blueprint FULL COURSE Elias first one to do the 3 to one with AI people use my prompt there was a prompt going viral over and over again
3. How To Print $50k/mo With Seedance Background Swapping (Step by Step) Kevin Martins Claude prompt background swap 720p 1080p scam Topaz
4. Kevin Martins Seedance background swapping step by step C dance post twice the volume same video different background student Elias example copyright mute
5. Seedance background swap Kevin Martins lightsaber chrome jeans changed the whole entire vibe what did I do I told Claude add props niche background gamer room
6. How I Make AI Organic Videos That Print $100k/m (Step by Step) Kevin Martins don't move her still hold the product every prompt you generate from now on first B-roll props workbench result
7. how to SPEEDRUN to your first winning product with AI Organic Dropshipping Kevin Martins ripping affiliate clips TikTok shop then Claude prompt avatar walking into Costco run two 321 make with AI
8. Kevin Martins FULL COURSE Atlas AI Store Builder full store neck product AliExpress link import branding colors prompt AI conducting market research copy reviews
9. Kevin Martins pasting the prompt into Kling with your image reference get your prompt from Claude this exact prompt structure seconds 0 to 2 static camera she paints the watch brush
10. "How I Make AI Organic Videos That Print $100k/m" Kevin Martins first frame test our props paints sketches she is painting the watch boom look what came out even the lighting on the car
11. How He Made $60K In 30 days With AI Organic Dropshipping (Product Revealed) Gus Claude prompt I told Claude make me an image avatar Costco run two tinnitus Higgsfield prompt
12. Leaking My $1M AI Organic Dropshipping Blueprint (FULL COURSE) "hey listen" "I want you to" give me make me Claude
13. Kevin Martins AI organic videos step by step first b-roll image of my shorty holding the design sketches laid out on her desk I told Claude make her sketching drawing the watch design
14. Kevin Martins AI organic videos step by step it went ahead and spit out the prompt for Kling 3.0 we're going to be using this exact prompt structure copy it start frame her pouring it
15. how I made $250K selling $9 plushies with branded organic dropshipping Kevin Martins this part is all AI me grabbing the product putting it in the cart prompt Claude Higgsfield
16. From Uber Driver To $65K/Month With AI Organic Dropshipping Kevin Martins John translate this in a natural way I don't know Italian French Elias prompt split testing markets Spanish
17. How He Made $140K in 30 days With AI Organic Dropshipping (Product Revealed) Jhon B-rolls Seedance background swap prompt I ask Claude I tell Claude make the avatar run two hook
18. Kevin Martins Seedance background swapping saucy copyright workaround I own the video and all rights to it Higgs Field blocks the generation tell Claude
19. Kevin Martins speedrun first winning product run two concept first person POV grabbing the box off the shelf how to make it with AI tell Claude prompt store collaboration grand opening 321 employees
20. "healthmaxxing" is the fastest way to $35k/mo with AI organic dropshipping Kevin Martins talking to Claude hyper specific build your ICP prompt red light therapy hat Omar content plan hooks
21. Kevin Martins AI organic videos step by step you could even tell Claude to copy a video from your For You page by literally sending it a screenshot break down the camera angle lighting action everything use it for yourself
22. Kevin Martins Seedance background swapping 1080p is an absolute scam I'll show you why credits comparison Topaz upscale must have reference video tip end of video apply FSE
23. C dance background swapping literally changing the whole organic space Kevin Martins Elias Jhon $140K showcase clips creation process reactions there's really no example needed
24. "Claude + Higgsfield = $30k/mo on tiktok shop" youtube faceless AI TikTok shop Tyler Kalodata Nano Banana Pro Kling 2.6 prompt
25. How He Made $110K In 30 days With AI Organic Dropshipping Charlie mold your avatar to your ICP just got to prompt it correctly theme to whatever your product is custom products Claude
26. Leaking My $1M AI Organic Dropshipping Blueprint FULL COURSE Omar red light therapy doctor avatar Pinterest before and after rat monkeys hook prompt Claude how do you make your videos
27. How To Split Test In AI Organic Dropshipping Money Bash how did you find your avatar Whimsical Realm Claude detail prompts I can send in my avatar prompt it's long and deep
28. How He Made $70K in 30 Days With AI Organic Dropshipping Ivan niche research with Claude prompt structures deep research Kimmy Pinterest perfect room Zelda bags background swapping run two
29. Kevin Martins How I Make AI Organic Videos editing on CapCut I added my text hook transition sound where I got the text hook mix real clips showcase from a competitor rent a video
30. Step by Step Guide to Making AI Avatars in 2026 ($65k in 4 days) Kevin Martins build an AI influencer goth niche Zelda niche healthcare product this is exactly how I go about it Claude prompt
31. Leaking My $1M AI Organic Dropshipping Blueprint Kevin Martins step number four pasting the prompt into cling with your image reference get your prompt from Claude I sent it the image of her pouring the paint
32. $0 vs $100k/Month Ai Videos for Organic Dropshipping Kevin Martins Amish lady voiceover script Claude prompt hook realism Elias resin lamps $1,000 a month video tracker
33. Kevin Martins AI organic dropshipping voiceover video Claude write me a script for my AI avatar 11 Labs voice text hooks give me 10 hooks
34. Kevin Martins speedrun winning product 321 employees doing it instead of the avatar gifting concept alarm clock honorable mention how to make this with AI prompt Seedance Kling
35. how to make "f*ck you" money with AI organic dropshipping in Q4 Kevin Martins Google calendar routine leverage AI platforms Claude Code automate tell Claude
36. How He Made $140K in 30 days John book nook even the B-rolls I made them with CDN I changed the background nobody had them classic split test changed the music clips shorter
37. "How to make video ads that PRINT for organic dropshipping" Kevin Martins Extended Claude prompt hook text hook video hook
38. healthmaxxing $35k/mo Kevin Martins recap at least 50% margin under $100 Claude prompt ICP then go watch my video creation tutorial apply to work with me Omar outro
39. Leaking My $1M AI Organic Dropshipping Blueprint Elias resin lamp Lord of the Rings my method is to first replicate the most viral content took the videos from Harper creation process with just the hands AI prompt
40. "How I Make AI Organic Videos That Print $100k/m" essentially how this looks like you want to go ahead and get your prompt from Claude I sent it this image and it went ahead and spit out the prompt for Kling
41. how to SPEEDRUN to your first winning product Kevin Martins make multiple variations of each concept longevity delegate scary embarrassing process to AI when I was filming run twos myself different stores
