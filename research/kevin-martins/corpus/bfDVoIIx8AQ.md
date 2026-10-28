# ElevenLabs Flow: Create 30 second Product Video Ads with Seedance 2.5

- URL: https://www.youtube.com/watch?v=bfDVoIIx8AQ
- Windows: 16 (first timestamps 16s … 396s)
- Source: verbatim Perplexity search results (YouTube auto-captions), machine-extracted from agent logs

Metadata lines seen:
  ## The AI Hustle
  ##### Sep 05, 2026 (0:06:55)
  ...
  00:00 Create Cinematic AI Ads with ElevenLabs Flow
  00:24 ElevenLabs Flow Workflow Setup
  00:58 Generate Luxury Product Images with GPT Image 2
  01:34 Generate AI Model Images & Upscale to 4K
  01:58 Create Cinematic Ad Shots with AI
  03:18 Generate Videos with Seedance 2.5
  03:56 Combine AI Video Shots in Flow
  04:14 Add AI Voiceover with ElevenLabs
  05:01 Generate Background Music with AI

---
The model image has also been generated, and she actually looks

[…]

So, make sure you follow each step carefully and use

[…]

So, I'll disconnect it and generate the first shot.

[…]

From generating the product and model images to animating every shot, adding a
{ts:16} professional voiceover, and creating background music, all inside ElevenLabs Flow.

[…]

After
{ts:26} signing up, just go to Flow and then create a new flow.
Okay.

[…]

So, let's add our first node.
Just press
{ts:38} N and add the image generation node.
As you can see, the image generation node has been added.

[…]

Now, if you already have a product image, simply
{ts:60} create a media node and then connect that media node to an image generation node like this.
But, since I don't
{ts:65} already have a product image, I'm going to generate one directly using this image generation node.
So, let's enter
{ts:71} this prompt here.
Then, choose the GPT image 2 model, select your aspect ratio, and then choose the resolution.
You can
{ts:78} set the resolution all the way up to 4K, but for now, I'm going to keep it at 2K.
Later, we can easily upscale the image.

[…]

{ts:96} Now, we need a female model.
So, I'll drag in another image generation node and enter this prompt here.
I'll keep
{ts:101} the settings the same as before and run the node.

[…]

Now, we need to generate different shots such as the model with the perfume, the model walking, and
{ts:125} more.
For that, you need to have a clear story in mind.
So, let's generate the first shot where I want to create a wide
{ts:131} shot of the model.
The prompt will look something like this.
Then, add an image generation node like this.
Paste the
{ts:136} prompt here, then press at and select the image as a reference like this.

[…]

So, I'll simply drag
{ts:153} an image generation node from the perfume image, enter the prompt, and generate the image.

[…]

So, I'll drag an image generation node using both the
{ts:171} perfume image and the model image.
Then, press at again and select both the model and perfume as references and generate

[…]

{ts:195} So, let's rename all the shots first.
Okay, now let's drag a video generation node from the first shot.
Then, enter
{ts:201} this motion prompt, select seedance 2.5 as the video model, and set the video quality to 720p for now.
I'm going to
{ts:209} set the duration to 4 seconds because each of our shots will be 4 seconds long.
Then, simply generate the video.

[…]

In the same way, I'll
{ts:226} convert each image into a video one by one.

[…]

All right, so we've generated a total of eight 4-second shots.
Now, we need to combine all of them together and
{ts:238} create our final video.
But, you don't need to use any external software for this.
Just press M, search for the
{ts:244} composition node, and add it.
Then, connect all of the videos to the composition node like this.
As you can
{ts:250} see, a timeline has been created inside the composition node, but we're not done yet.

[…]

We also need to add a voiceover and background music to this video ad, which will make the final
{ts:261} video feel much more polished.
So, for that, simply add a text-to-speech node and select a voice from the 11 Labs
{ts:267} voice library.
However, I would recommend designing your own voice instead, because you may not find the
{ts:272} exact voice you need for this specific type of video in the library.
So, simply go to the 11 Labs home tab, then go to
{ts:278} voices, click on create voice, and select voice design.
Here, enter a prompt describing exactly what you want
{ts:285} your voiceover to sound like.
Adjust the settings if needed, and generate the voice.
Once the voice is ready, I'll
{ts:290} simply save it to my library.
Then, come back to flow.
I'll add my 30-second script here, select the voice I just
{ts:296} designed, and run the node.
As you can see, the voiceover has been generated.
Now, connect this node to the
{ts:301} composition node.
Boom!
You can see that the voiceover has been added to the timeline.
Now, I'll do the same thing
{ts:307} with the background music.
I'll add a music generation node, choose the V2 music model for better audio quality,
{ts:313} turn off lyrics, then add your 30-second script, and generate the audio.
Once the music has been generated, connect this
{ts:319} node to the composition node as well.
You can also adjust the volume of the voiceover and background music directly
{ts:325} from here.
Once everything sounds good, simply run the composition node.
And this node doesn't use any credits, so
{ts:331} you don't need to worry about that.
Okay, as you can see, the final ad video is ready to download.
But, if you're not
{ts:336} satisfied with the video quality, you can simply add a video upscaler node, choose the Topaz upscaler model, set the
{ts:342} resolution to 4K, and upscale the video.

[…]

The voiceover and the visuals are also aligned really
{ts:396} well with each other, which makes the final ad feel much more polished.
