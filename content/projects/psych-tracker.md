---
title: "HackTheNorth 2023 <strong>Psych Tracker</strong>"
date: "2023-09-17"
imageUrl: "/img/psych-tracker.png"
subtitle: "a project over a single weekend?"
---

## HackTheNorth 2023

I had an incredible experience at HackTheNorth, Canada's largest hackathon. The event at the University of Waterloo brought together 1,000 hackers from Canada and around the world. The HTN team did an amazing job, celebrating their 10th anniversary with custom stickers and unique digital tickets.

[![All the stickers I got](/img/psych-tracker2.png)](/img/psych-tracker2.png)

On top of trying to collect all the swag from the sponsors, I attended workshops and activities, including OpenAI, Intro to Embedded Systems, and Hacking the Brain workshops. With the help of lots of snacks, a couple cups of coffee, and maybe an energy drink or two, the 36 hours of hacking flew by. This was an experience I will never forget — meeting countless people who wanted to grow their network, build a project over a weekend, collect some swag, or a little bit of everything.

## Inspiration

Have you ever wished you could log how you're feeling, especially when dealing with mental health challenges? Mental well-being can be a complex journey, and finding the right tools to navigate it can be tough. But what if a simple metric could help you gain clarity on difficult days?

{{< my_video_embed src="https://www.youtube.com/embed/OE9ZMTe3uAk?si=8g-ZbvRVMlW_WIw0" title="YouTube video player" >}}

Introducing Psyche Tracker: a personal companion for managing emotions, stress, and focus. Like a trusted friend, it records your moods and facial expressions, helping you understand your mental well-being.

{{< my_video_embed src="https://www.youtube.com/embed/i6kFMdbqREE" title="YouTube video player" >}}

## What it does

This device records your mood whenever you feel like checking in. There are three mood options: high, neutral, and low. While coarse, this allows quick input without overthinking or distractions. The device also tracks focus with two buttons, letting you log periods of concentration with a tap.

Mounted on the front is a camera trained to assess mood via facial expressions, and a temperature sensor captures skin temperature during mood logging. Mood, temperature, and facial data feed into a larger algorithm, stored in MongoDB and prepared for neural network analysis. Correlating noninvasive temperature measurements with mood could offer valuable insights over time.

[![Psych Tracker Image](/img/psych-tracker3.png)](/img/psych-tracker3.png)

## How we built it

We used open source hardware and software to focus on integration. The system runs on a Raspberry Pi 3 and an Arduino Leonardo, with a TensorFlow-based vision model. The housing combines laser-cut parts with 3D-printed accents.

The camera mounts on a spring for a "bobble head" effect, LEDs shaped like hearts light up when moods are low, and robot arms respond to neutral moods and focus mode.

## Challenges we ran into

Time was our biggest challenge. Integration steps sometimes took longer than anticipated, and training the vision model required significant compute time, leading to tradeoffs in model complexity and accuracy.

## My contribution

I focused on robust electrical connections and circuitry for the buttons, integrated the temperature sensor, and helped the three-person team complete the build and machine learning integration within 36 hours.

[![Psych Tracker Image 4](/img/psych-tracker4.png)](/img/psych-tracker4.png)

## Accomplishments we're proud of

We delivered a functional prototype with insights for passive mental health tracking, and our teamwork, communication, and rapid prototyping under time constraints were exceptional.

[![Psych Tracker Image 5](/img/psych-tracker5.png)](/img/psych-tracker5.png)

## What we learned

We learned rapid hardware integration, model training under time pressure, and the value of laser cutting for quick mechanical parts alongside 3D printing and gets creative with limited resources.

## What's next for Psych Tracker

We plan further design iterations, additional sensors, and deeper data analysis to map physical metrics to mental health over time.

## Try it out!

{{< custom_link href="https://github.com/and-hans/PsychTracker" text="GitHub Repo" >}}

{{< custom_link href="https://devpost.com/software/psyche-tracker" text="Devpost Submission" >}} 