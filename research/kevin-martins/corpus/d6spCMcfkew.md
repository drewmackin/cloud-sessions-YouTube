# Dear Higgsfield, I reverse engineered you in 12 hours

- URL: https://www.youtube.com/watch?v=d6spCMcfkew
- Windows: 17 (first timestamps 20s … 1011s)
- Source: verbatim Perplexity search results (YouTube auto-captions), machine-extracted from agent logs

Metadata lines seen:
  ## Sirio
  ##### Oct 09, 2026 (0:21:46)
  ...
  07:07 – 08:18 API Key Setup
  08:18 – 09:38 Draft Mode Explained
  09:38 – 11:02 First Test
  1. Why Seedance 2.5 blocks your video and the exact two things that trigger it (face + music)
  11:02 – 13:32 Two Fixes
  13:47 – 15:04 My 11 Steps Workflow
  15:04 – 15:47 Get the Workflow for FREE
  15:47 – 18:23 Workflow Live Demo
  18:23 – 20:37 Face Mesh Workflow

---
We hit the face, we hit the music, we
described the room, and then we laid the people over the real video.

[…]

You have to
upload, review, draft and export or save.

[…]

say, hey, use the draft mode for this generation.

[…]

movements, the movements are still there.

[…]

what actually happens when you try to do it the normal way.
I'm uploading that same
template video into Seedance 2.5 and asking
{ts:20} you to swap me in.
Blocked.
But apps
like Higgsfield's Genjutsu do this exact thing all day, every day
with these exact videos.

[…]

Today we're
going to reverse engineer Higgsfield's Genjutsu and we're going to get around the
IP blocks in Seedance 2.5 so that you guys can put yourself into pretty much any movie
scene or talking head you want without
{ts:52} any special software.

[…]

And the way that it works is that you upload
a photo of yourself and then you pick a
{ts:130} template video and then it just swaps you
in for the person that is in that template video.

[…]

{ts:184} This is the template.
And all I did
here was I head over to CDense 2.5.
I uploaded this exact video and I typed
replace the character in the video with the picture that I uploaded.
And it got blocked
for IP, which I mean, sure, it makes
{ts:198} sense.
These people are famous.
But like I said, this exact video
works totally fine in Genjutsu.
But before we actually build anything,
I think that it is important for us to
{ts:207} understand why because if you get this part,
the rest of the video is basically just just details.
There are really only
two things that get you blocked here.
The first one is the face.
The second one is the music.
{ts:218} And the way that I like to think about
this is that the video is really carrying these two things at the same time.

[…]

So the whole idea here is that
you keep the how, the movement and you
{ts:242} throw away the who, the IP and everything
that we're going to do from here on out is really just hide one of those two things,
obviously without losing the movement.
So the first thing that we're going to
have to do is turn this template into
{ts:255} something where the AI cannot tell who
the people are, but he can still see how they move.
And for that, we're going to use
something that is called depth anything.
You can find it on hugging
phase or replicate or foul.
{ts:268} And all you have to do is that you upload
your video, you click generate, and then you get something like this.
So this
is what's called the depth mask.
And what I mean by this is that it throws
away what everything looks like and it
{ts:282} keeps how close or how far
things are from the camera.

[…]

If we want the lips to match
the song, then the audio has to go through as well.
Now, the first thing
that most people would say is just muted,
{ts:327} but we cannot do that.
And the reason
why is that AI actually needs to hear the voice in order for it to move the mouth.
So instead of muting it, we're going to
keep the voice, but get rid of everything
{ts:340} else.
Keep the actual words, remove the
soundtrack, remove the background music.
So what I'm going to do is that I'm going
to take this depth mask and bring it into cap cut.

[…]

So one way to fix this
is to have the agent describe
{ts:666} the studio.
And the reason why is like I
said earlier, the depth mask has no idea what the place looks like.
And if this was
your reference video, this is why you got back.

[…]

{ts:680} And what I'm going to do is I'm going to
take a screenshot of the original video and I'm going to drop it into the agent.
And I'm going to say, Hey, describe this
place for me, but do not describe the
{ts:690} people and then update the prompt with
that and send the same request again.

[…]

{ts:740} So this time, I'm going to grab the original
video and then our depth mask with the changed audio, I'm going to drop the original
clip into cap cut, and then I'm going to put in the depth
mask right on top of it.
{ts:753} I'm going to mute the original clip.
So the only audio left
is our pitched vocals.
And I'm going to click on the depth mask
and go over to the video tab, then the
{ts:764} background removal, then click on customer
removal, and just highlight the people.
Basically, what this is doing is that it's
cutting out just the people and then it's laying them on top of the original video.

[…]

{ts:798} Then I'm going to send it back to the agent
and say, Hey, swap the old sorts video for this new one and make another draft.
And look at that.
That
worked.

[…]

But but you can do all of it with
one click the same way Higgsfield does with the workflow.
So I had the
agent turn everything we just did into one.
All you need is a replicate
account and I'm giving you a skill that sets
{ts:838} everything up.
Hugging face is also
optional, just a backup choice.
So really quickly it is 11 steps.
One, we upload the original video.
{ts:847} We keep the original video for
also the final audio to demicus on replicate splits the
vocals from the music.
Three rubber band pitches the
vocals up by three semitones.
{ts:861} Four, we have depth anything video, which
makes the collared depth video that we talked about.
Five, we have Sam three
cutting out all the people on every frame.
Six, it puts those depth people
over the original background.
{ts:874} Seven, the pitched vocals go
right inside of that video.
Eight, you check
everything before it sends.
Nine, C dense makes a draft
through enhancer in the edit mode.
{ts:884} Ten, it throws away C dense audio and puts
in the whole original soundtrack back.

[…]

The first one is you just drop in the
video that you want to change and then the photos that you want to be placed in
the video are like swapped and you say,
{ts:963} Hey, run the workflow as simple as that.
The second one you do it yourself in the

[…]

And then it's making the depth video,
cutting the people with Sam three laying them
{ts:1011} over the original background and cleaning
