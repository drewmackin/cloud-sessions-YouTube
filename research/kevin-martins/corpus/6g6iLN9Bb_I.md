# 秒単位で流れを決められる、新しい動画生成モデル【Kling 4.0】

- URL: https://www.youtube.com/watch?v=6g6iLN9Bb_I
- Windows: 10 (first timestamps 5s … 329s)
- Source: verbatim Perplexity search results (YouTube auto-captions), machine-extracted from agent logs

Metadata lines seen:
  ## HIROCODE.
  Date: 2026-10-23

---
It's now possible to specify what happens and when within a 30-second timeframe using images and timestamps . So, my impression after trying it out is that image generation has moved closer to a visual presentation than a simple gacha system.

[…]

I'll register this car image I just generated as a reference image and create several shots of the same car but with different angles,

[…]

The part where the captain turns around and speaks after the cannon fire is also exactly as written in seconds.

[…]

The prompts are the same as with the car, divided by seconds, and

[…]

{ts:5} We'll be using Kling 4.0 with Artlist, and its key features include the ability to generate up to 30 seconds of video in a single run , support for 21:9 ultrawide aspect ratios, and
{ts:15} most importantly , the ability to specify what happens at each second within the 30 seconds.
Previously, you would provide the first and last images and leave the rest to the model, but
{ts:25} with Kling 4.0, you can place up to 8 images in between and specify prompts by time, such as "0-5 seconds: this," "5-10 seconds: this," and so
{ts:35} on.

[…]

Now I'll move on to generating the video and select Kling 4.0 from the model list.
The configurable items are video length ratio, resolution, and audio on/off.
{ts:100} From the Image Reference in the prompt box, open My Library.
All the images I just generated are in here, so I'll select the cuts I want to use in the video and add them.
Once
{ts:110} added, the images will be listed in the prompt box with @ tags, so I'll write which image composition will be used for each second, like this image for 0-3 seconds, this image for 3-6 seconds, and so on.

[…]

As you can see, the images specified in the reference are used and it
{ts:141} 's finished as a single video.
However, to be precise, there is a delay of about 1-2 seconds from the specified time, so it doesn't seem to be generated at the exact specified time.

[…]

This time, instead of a car, we'll try a subject where only the camera moves.
Similarly, using Nano Banana Pro, we 'll generate a latte on a cafe table and create shots from directly above, the woman picking up the cup, and the woman drinking.
{ts:166} The Kling 4.0 Video screen has three sections: Start Frame, Middle Frame, and End Frame.
Previously, we used the @ symbol to place images within prompts, but
{ts:176} this time we'll try placing images within frames.
The start frame will have the latte on the table, the middle frame will show the camera picking it up, and the end frame will show the woman drinking it.
The middle frame allows for multiple frames, so
{ts:187} if there are many passing points, we'll add them here.
For the prompt, we'll set it to "the latte on the cafe table, the woman drinking it."
Since you don't need to write detailed instructions using the @ symbol like before,
{ts:200} this is definitely easier if you want to generate it quickly.

[…]

It 's not just subjects with moving parts like cars; even with quiet subjects like this, where the camera and hand only move towards a stationary object,
{ts:228} you can place images at the passing points and the movement will be accurate.

[…]

So, you can
{ts:329} specify the number of seconds when you want to make fine adjustments, and leave it to the system when you just want the atmosphere.
