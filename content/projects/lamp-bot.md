---
title: "Automated Lamp"
date: "2021-11-15"
imageUrl: "lamp-bot/lamp-bot.png"
subtitle: "laziness 100"
bulletPoints:
  - "Simple <strong>LED lamp</strong> with automation capabilities"
  - "<strong>Breadboard</strong> prototype transitioned to <strong>perfboard</strong> design"
  - "<strong>Arduino</strong>-based control system for smart lighting"
---

## Overview

A simple LED lamp. Automated.

{{< slideshow >}}
  {{< slide src="lamp-bot/lamp-bot2.png" caption="Lamp Bot Breadboard Setup" >}}
  {{< slide src="lamp-bot/lamp-bot.png" caption="Lamp Bot Perfboard Setup" >}}
{{< /slideshow >}}

## How Did I Do It?

FYI: If you don't already know, you can click the images to be redirected to either code or a video.

I am very proud of this project, mostly because I find it to be the most useful, despite its simplicity.

{{< my_video_embed src="https://www.youtube.com/embed/videoseries?list=PL2zKq55_kXLfjpb5t2CUzVKcb67IvNmML" title="YouTube video player" >}}

I rewired the lamp to a separate transistor switch circuit. From there, it connects one of my Raspberry Pis to a Discord Bot.

This was done on purpose in order to not have to port forward, and also so that my friends and I could turn the lamp on and off whenever we please.

## Conclusion

The lamp bot was initially assembled on a small breadboard, then upgraded to its own perfboard. It may be further improved in the future. Curious to see where this goes next! 