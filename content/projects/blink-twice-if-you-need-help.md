---
title: "Blink Twice 👀 If You Need Help"
date: 2024-01-14
imageUrl: "/img/blink-twice-if-you-need-help/closer-up.png"
thumbnailUrl: "img/blink-twice-if-you-need-help/overview.png"
subtitle: "DeltaHacks X 2024 Project"
---

# Blink Twice 👀 If You Need Help

## Full Project Demo

<div class="iframe-container landscape">
<iframe src="https://www.youtube.com/embed/jnIf4NE0WYI?si=TuOt1-v5sMWxwJKn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Overview

Blink Twice if You Need Help is a wearable computer vision enabled device.

The premise is simple, if you were in a hostage situation where calling 911 on your phone is too risky, you could use a blink detection system to call for help.

The idea started off as a joke. I've seen TikToks where people made the wildest videos and in the comments, they ask if they were forced to make the lame video and if they could blink twice if they need help.

So I thought, what if I could make this real?

## Blink Detection (OpenCV)

This was my contribution to the hack.

I have never used OpenCV before, but I did understand that there are open-sourced facial landmark models out there.

It was clear to me that Mediapipe had functionality, but I literally only needed blinking detection.

I ended up finding a {{< custom_link href="https://github.com/infoaryan/Eye-blink-detection-game" text="cascade classifier" >}} for the eyes online, and I ended up using that in the project.

The usage was simple, while the camera data is read, if the eyes are closed based on the facial landmarks, call Adam's part of the code where it will call "911".

This needed a lot of tweaking most importantly in timing as to when to count a double-blink or not.

The most challenging part of the code was understanding how to use the model for blink detection, but also how to calibrate for double blinks.

Interfacing with Adam's calling functions was as simple as calling his part of the code.

I really enjoyed coding this part as it was really impressive and rewarding to get it to really count double blinks.

{{< slideshow >}}
  {{< slide src="/img/blink-twice-if-you-need-help/blink-detection.jpg" caption="Me Testing Blink Detection" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/blink-detection2.jpg" caption="Adam Blinks" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/blink-detection3.jpg" caption="Adam Doesn't Blink" >}}
{{< /slideshow >}}

## Hardware

The final project consisted of Adam's Logitech USB webcam, boba straws for support, painters tape, a clip-on ring light, and some random cardboard from Adam's dorm.

Beforehand we knew we would at the very least need a webcam and some hat to hold the webcam. We ended up using a ring light to help with the lighting since blinks are better detected with the eyes well lit.

The main problem was that the field of view of the webcam forced us to making the webcam further from the face.

As the weight of the webcam was moved further from the face, more structure had to be built to keep it level.

Since we did not have materials, we can back to Adam's dorm to get some cardboard and tape, but also used the boba straws from the handouts at DeltaHacks. (It tasted great btw)

After lots and lots of tape, some adjusting of the hat, and impeccable posture on my end, we ended up with this monstrosity.

It may not be the most elegant, but it gets the point across.

If I could make this a real product, I would set a camera at the eyes instead of the whole face to account for the field of view of the camera.

### Some pics of the wearable

{{< slideshow >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware1.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware2.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware4.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware5.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware6.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware7.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware8.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware9.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware10.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware11.jpg" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/hardware12.jpg" >}}
{{< /slideshow >}}

## Calling "911" (Twilio)

Adam's part of the project was to call "911" if the blink detection system was triggered.

He set up a Twilio account and used some libraries to get the user's IP to send through text to speech the location of the hat.

This was completely his role and integration with the blink detection was as simple as calling his script that he wrote.

Read his side of the project {{< custom_link href="https://steep-motorcycle-b2c.notion.site/Blink-Twice-if-you-Need-Help-DeltaHacks-X-d4ef8f61369c4ba19cee6ff5817f3f84" text="here!" >}}

## Scavenger Hunt

Adam also toured me around campus and we ended up winning a prize for completing a scavenger hunt.

They gave us previous year's swag and also $15 on Amazon lol.

{{< slideshow >}}
  {{< slide src="/img/blink-twice-if-you-need-help/scavenger3.jpg" caption="McMaster Iron Ring" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/scavenger2.jpg" caption="Adam's Dorm Building" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/amazon.jpg" caption="we technically won deltahacks" >}}
  {{< slide src="/img/blink-twice-if-you-need-help/scavenger1.jpg" caption="Tier 3 Sub Behaviour" >}}
{{< /slideshow >}}

## Check it out!

{{< custom_link href="https://github.com/gavintranquilino/blink-twice-if-you-need-help" text="GitHub Repo" icon="fab fa-github" >}}

{{< custom_link href="https://devpost.com/software/blink-twice-if-you-need-help" text="Devpost Submission" icon="fas fa-code" >}}

{{< custom_link href="https://devpost.com/sullynumber9" text="Adam's Devpost" icon="fas fa-external-link-alt" >}}

{{< custom_link href="https://devpost.com/gavintranquilino" text="Gavin's Devpost" icon="fas fa-external-link-alt" >}} 