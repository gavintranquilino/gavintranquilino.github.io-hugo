---
title: "<strong>Custom Tamagotchi</strong>"
date: "2024-06-23"
imageUrl: "/img/circle-display/kumi.gif"
thumbnailUrl: "/img/circle-display/panda_square.png"
subtitle: "work in progress"
---

## The Goal

Make a portable handheld virtual pet that can support higher quality images on a round display.

My current plan is to turn my stuffed animals into virtual pets I can take around with me as if it were a Tamagotchi.

I am also a fan of the idea to introduce various sensors and an IMU to increase possible interactions with my pets.

I think this is really cool to carry around as a wearable and fun to showcase to others as well.

## 3D Models

### Mobile Scanner

I think it's cool to be able to interact with actual 3D pets, so I started with a scan of my panda stuffed animal.

I used [Polycam](https://poly.cam/) — a [photogrammetry](https://en.wikipedia.org/wiki/Photogrammetry) 3D scanner for mobile — to scan my panda Kumi.

Polycam gives, IIRC, about 15 free scans, so this was just enough for my purposes if I wanted to scan more.

My Pixel 6a does not support LiDAR like the iOS counterparts, so I used photogrammetry, which is a method of using images and stitching them together to create a 3D model of an object.

This is the same technology that Google uses for [Google Earth](https://www.youtube.com/watch?v=suo_aUTUpps).

Of course this comes with its limitations as it has trouble scanning dark, shiny, or clear areas.

My solution to this was to ensure good lighting by having a lamp overhead and just go around my desk for each scan.

{{< my_video_embed src="https://www.youtube.com/embed/ZL2r2g9Ic80?si=XMe3BL3qVwEh4" title="YouTube video player" >}}

## Round Display

I wanted a circular display for my virtual pet.

It's like a little portal to view my pet.

I opted for the [GC9A01](https://dronebotworkshop.com/gc9a01/) 1.28" TFT LCD display module (240 × 240 px).

I chose this LCD since it's not power hungry, and also a small size good enough for handheld.

For now, I got the display with pin headers for debugging, but in the future I plan to get one with either JST connectors or ribbon connectors.

I used the [AnimatedGIF](https://github.com/bitbank2/AnimatedGIF) library to play GIFs from flash memory. I plan to read GIFs from storage like a microSD card in the future.

{{< my_video_embed src="https://www.youtube.com/embed/gWcwKqVwEh4?si=3NyFOf1sR5x6y12_" title="YouTube video player" >}}

## Current Goals

With the current configuration, I have an IMU setup; I hope to move the panda model freely as I rotate the device.

I am also exploring other graphics libraries such as [LVGL](https://lvgl.io) for 2D content.

Another plan is using a rotary encoder around the display to interact with the circular nature of the screen.

Battery management is also a concern: I have various LiPo cells to tinker with, and I'm researching BMS usage on ESP32-based handheld devices.

Stay tuned for future updates to this project! 