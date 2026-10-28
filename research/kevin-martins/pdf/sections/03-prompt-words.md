---
number: 3
title: How they talk to the AI
subtitle: The exact words, the patterns behind them, and the eight rules every image and video prompt follows
---

## The pattern in one paragraph

They never write the final image or video prompt themselves. They **talk to Claude in plain, bossy, conversational English**: “Hey, listen…”, one job per message, the reference images attached. **Claude writes the technical prompt**, and they paste that into Higgsfield. The skill lies in (1) loading Claude with a **context prompt** first, (2) telling it the **format** (“Tik Tok style”, “static shot”, “9x16”, “phone camera”), and (3) always adding **strict negatives**. In Kevin's words:

> {{q:hK2Os3wSPI8|I'm just kind of giving it a framework|what I've seen from other competitors, right?}}

## The exact phrases (word for word, by purpose)

| Purpose | What they actually say | Who / where |
|---|---|---|
| Open every request | “Hey, listen, …” / “Listen, …” (used in P5, P6, P8, P10, P11) | Kevin, throughout the tutorial |
| Set up Claude once | {{q:hK2Os3wSPI8|All right, based off of this information,|for my video creation.}} | Kevin · P3 |
| Hand over the product | {{q:GfhpQLqF658|Hey, listen. Here's the product|style of video.}} | Kevin · P4 |
| Make a look-alike avatar | {{q:hK2Os3wSPI8|Hey, listen, give me a prompt to recreate|as hers.}} | Kevin · P5 |
| Stay legally clear of the real person | {{q:hK2Os3wSPI8|Listen, I want you to change it up a bit,|We don't want to go to jail.}} | Kevin · P5 |
| Freeze the scene | {{q:hK2Os3wSPI8|hey, listen, I want you to lock the environment|of the master frame.}} | Kevin · P6 |
| Ask for shots in bulk | {{q:GfhpQLqF658|Listen, I want five, maybe eight|this, and that.}} | Kevin · P7 |
| Describe the set | {{q:hK2Os3wSPI8|Listen, lock the environment, right?|watch designer's workbench,}} | Kevin · P8 |
| Kill the “AI look” | {{q:hK2Os3wSPI8|Listen, no cinematic, no studio, no DSLR|none of that stuff.}} | Kevin · P8 |
| Force phone-native framing | {{q:hK2Os3wSPI8|keep that 9x16 vertical close-up photography|modern smartphone rear camera.}} | Kevin · P8 |
| Place the camera | {{q:hK2Os3wSPI8|Listen, do a side angle third-person view|eye level, yada yada yada.}} | Kevin · P8 |
| Animate stills | {{q:hK2Os3wSPI8|here are three more images|realistic process action.}} | Kevin · P9 |
| Lock the camera | {{q:hK2Os3wSPI8|just remind it all the images are static shots.|does not move at all}} | Kevin · P9 |
| Ban the glitches | {{q:hK2Os3wSPI8|Listen, do not move the camera,|no other people.}} | Kevin · P10 |
| Fake a handheld selfie | {{q:hK2Os3wSPI8|you want to ask Claude to add a subtle camera shake|realism.}} | Kevin |
| Build the hook | {{q:hK2Os3wSPI8|Hey, listen, I want you to write me a prompt|first frame of the hook.}} | Kevin · P11 |
| Clone a viral video's setup | {{q:hK2Os3wSPI8|you could even tell Claude to copy a video|by just literally sending it a}} screenshot | Kevin |
| Refresh a tired hook word | {{q:kmy9uOj0ve0|give me other words for tonitis.|used for this?}} | Gus ($60K month) · P13 |
| Background for a product | {{q:S9COXhnjijY|I tell Claude to make|type of background to match it}} | Charlie ($110K month) |

## The house language of the Seedance brief (coach Elias, P12)

Elias's document is the most “engineered” prompt in the group. These lines are fixed and must appear in every Seedance prompt it produces (quoted from the document, unchanged):

- {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|This is a recreation of my own original ~[X]-second vertical iPhone UGC video. I own @video_1 and all rights to it.}}
- {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|@video_1 is the full reference for everything in the output}}
- {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|Keep the entire foreground absolutely identical to @video_1.}}
- {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|The ONLY changes:}} then a numbered list: (1) the new environment, (2) {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|NO text, NO captions, NO subtitles, NO emoji, NO graphic overlays}}, (3) {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|NO audio of any kind}}
- {{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|Ultra-realistic iPhone UGC look throughout, completely silent output with zero text.}}

Its design rule is the opposite of how most people prompt: **don't re-describe what's already in the reference video** ({{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|re-describing what is already in the source video creates semantic conflict with the visual reference and degrades output fidelity. Trust the reference.}}). Describe only the change, and describe it densely ({{d:1donrcdIengXaQfiWBqkFAbImxE02thkgzt1uNZAaDV4|deep walnut wood paneled wall with brass accents}}, not “luxurious room”).

## The eight rules behind every prompt (Kevin's framework)

**Image prompts** (he says there are four; captions confirm three, and the fourth is the depth-of-field ban he stresses right after):

1. **Nail the environment first.** {{q:hK2Os3wSPI8|It's basically describing your master frame in detail,|Set the scene before anything else.}}
2. **Precise framing and camera placement.** {{q:hK2Os3wSPI8|spell out exactly where the camera sits|Never let the image tool guess for you}}
3. **Strict negatives.** {{q:hK2Os3wSPI8|no studio lighting, no professional setup, strip out every cinematic element.|looks like it was shot on a phone,}}
4. **No depth of field, ever.** {{q:hK2Os3wSPI8|depth of field is the number one mistake|it makes them too cinematic.}}

**Video prompts:**

5. **Match the camera to the shot.** {{q:hK2Os3wSPI8|fixed shots equals static camera locked to the input frame.|I mean the master frame.}}
6. **Time every action.** {{q:hK2Os3wSPI8|break the motion into second-by-second beats,|right?}}
7. **Lock the scene.** {{q:hK2Os3wSPI8|Everything from the input image, environment, lighting, props, hands, clothing stays identical,|Only the described motion happens. Nothing else moves.}}
8. **Say what you don't want.** {{q:hK2Os3wSPI8|no camera movement, no warping, no extra fingers, no morphing, no overlays,|right?}}

<div class="note"><b>Why this works (our read).</b> Image and video models fill gaps with “stock-photo” defaults: studio light, shallow depth of field, a smooth gimbal camera. Those defaults are exactly what makes viewers say “AI”. Each rule above removes one default, so the result reads as a phone video from a normal person. That's also why the negatives matter more than the description.</div>
