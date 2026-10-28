# Create the Viral Fall Through Social Media Effect

- URL: https://www.youtube.com/watch?v=crgRBYNcFXM
- Windows: 8 (first timestamps 15s … 321s)
- Source: verbatim Perplexity search results (YouTube auto-captions), machine-extracted from agent logs

Metadata lines seen:
  ## ElevenLabs
  ##### Aug 27, 2026 (0:10:23)
  ...
  Copy those keyframes across every clip, leave an even gap between them for the UI to slide into, and the cuts disappear.
  Date: 2026-08-27
  Each style frame goes into Seedance 2.0 with a prompt that has the character fall in from the top of the frame and out of the bottom, which is what makes the scroll read properly.
  Finally, the edit.
  From there we build style frames in GPT Image 2, using a prompt structure that splits into three parts: an identity section that tags your reference image, a pose section you reuse across every frame for consistency, and a style section that changes per scene.
  Retro 90s anime is the example, but the same structure works for any look you want.
  Screenshot the Instagram UI on your phone, drop everything into Premiere Pro, and animate position keyframes so each clip and each UI element travels up the frame at the same speed.
  Then we animate.
  This tutorial builds the whole thing inside ElevenCreative Flows, from a single reference photo through to the final edit in Premiere Pro.

---
And to do this, I'm simply going to drag a connector from the last frame and use it as the end

[…]

Once we've done that, we then want ahead and choose the duration.

[…]

{ts:15} So, the first step is you need to take at least one picture where you can see your full body.
If you don't have one,
{ts:19} here inside of 11 Labs Creative, I'm simply going to take a reference image of myself and then use a prompt to turn
{ts:24} that into a full body shot.
All we have to do is click on new flow and to get started you can click the first link in
{ts:29} the description down below.
And here you want to upload a picture of yourself.

[…]

To do this, we simply drag a
{ts:42} connector from the node and then click edit image and here we want to use this simple prompt.
With this prompt, we just
{ts:49} want to make sure that we tag the original reference asset to keep the facial likeness as much as possible.
{ts:54} Here, we then want to change the aspect ratio to 9 by 16 and we can change the model to Nano Banana 2, just like
{ts:61} [music] this.
Now we want to change the resolution to at least 2K and we can simply click run.

[…]

And so here what I'm going to do is drag a connector, choose edit image node and
{ts:77} paste [music] in this prompt.

[…]

And so, now we've got our three style frames, we can go
{ts:224} ahead and turn these [music] into videos.
And to do this, we simply want to drag a connector and choose a video
{ts:229} generation [music] from our style frame.

[…]

And so here, we paste in the prompt, and then we simply
{ts:271} want to make sure that we've selected SeedOuts 2.0, the aspect ratio is 9 by 16.

[…]

So, what we need to do is drag a connector from the style frame all the way into
{ts:321} the image reference section.
