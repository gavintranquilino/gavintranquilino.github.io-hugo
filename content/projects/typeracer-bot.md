---
title: "Typeracer <strong>Python Bot</strong>"
date: "2020-09-28"
imageUrl: "typeracer-bot/logo.jpg"
subtitle: "170+ WPM on TypeRacer"
bulletPoints:
  - "Developed automated typing bot using <strong>Python Selenium</strong> and <strong>PyAutoGUI</strong> libraries to achieve 170+ WPM performance on TypeRacer platform"
  - "Implemented <strong>web scraping</strong> techniques to extract plaintext from <strong>HTML DOM</strong> and convert into automated keyboard input sequences"
  - "Discovered <strong>rate limiting mechanisms</strong> in web automated interactions"
---

# Typeracer Bot
This project was one of my first Python projects, where I created a Selenium bot in Python to play TypeRacer for me. 

Back in 2020, the plaintext of the TypeRacer game was not obfuscated and made available on the HTML, so I was able to scrape the text and use it to type out the words at a speed of over 170 WPM. I found that this was the upper limit to the typing speed as the game would not allow you to type any faster than that.

I used the `pyautogui` library to simulate keyboard input and the `selenium` library to control the browser. 

Here's a YouTube short of the bot in action (somehow the only video I took was a phone recording of my computer screen):

{{< my_video_embed src="https://www.youtube.com/embed/b-bPyzhUCyA" title="YouTube video player" >}}