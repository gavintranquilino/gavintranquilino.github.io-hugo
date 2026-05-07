---
title: "IoT Light Switch Bot/Mount"
date: "2023-03-15"
imageUrl: "light-switch/light-switch.png"
subtitle: "remotely controllable via web interface"
bulletPoints:
  - "Designed a <strong>3D-printed</strong> servo mount that physically actuates a rocker switch without rewiring mains voltage"
  - "Built a remote control interface backed by an <strong>Ubuntu</strong>-hosted <strong>HTTP</strong> service"
  - "Combined mechanical design and web control to deliver safer, globally accessible room-light automation"
---

## Overview

3D printed, servo actuated, Raspberry Pi webserver, Discord API integration.

I wanted to create a device that can manually click the rocker switch of my room light on and off. I did not want to have to mess with any of the electrical circuits of the light switch system underneath the cover.

{{< my_video_embed src="https://www.youtube.com/embed/videoseries?list=PL2zKq55_kXLd6ajXMeEt_8hbf1B00W04K" title="YouTube video player" >}}

## 3D Printed Bracket

The bracket I designed for the servo motor was modelled in Fusion360.

[{{< img src="light-switch/light-switch6.png" alt="3D model of the servo bracket" >}}](https://youtube.com/playlist?list=PL2zKq55_kXLd6ajXMeEt_8hbf1B00W04K)

After learning the basics of CAD software, I was comfortable modelling the bracket on my own with precise measurements. Alongside the 3D printer, I used digital calipers for accurate prototyping.

Below is the finished bracket mount. I contemplated white vs. black filament, settling on black for contrast (Panda-themed).

{{< slideshow >}}
  {{< slide src="light-switch/light-switch4.png" caption="3D printed bracket" >}}
  {{< slide src="light-switch/light-switch5.png" caption="3D printed bracket with servo" >}}
{{< /slideshow >}}

Messing with 3D printer settings, I plan to enable ironing for smoother prints. I also intend to add modular connectors so sensors and mounts can be swapped like Legos. 