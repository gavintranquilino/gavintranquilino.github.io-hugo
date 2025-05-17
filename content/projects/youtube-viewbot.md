---
title: "YouTube Viewbot"
date: "2021-01-09"
imageUrl: "/img/youtube-py.png"
subtitle: "Free Views?"
---

This YouTube Viewbot uses Selenium for Python to view a Youtube video multiple times. This bot is not inteded to be used to gain thousands of views, but instead will aid in getting your first 100 views on a YouTube video.

## How Does it Work?

Once you run the program, the application will need user input to run. It asks for the video link, how many tabs to open, how long to watch the video for, and how many times it will watch the videos. Once it has gathered the data, the bot will open up a new Firefox window and open the amount of tabs listed. It will cycle through each tab and simultaneously play and refresh the video as needed.

After many attempts, I learned that the maximum amount of views that it does reach in one sitting is around 100. I assume that YouTube has a system which tracks suspicious view counts that come from the same IP Address, or a system that flags a video if it gets too much traffic from one source. I will experiment with using a proxy in order to bypass their system.

[GitHub Repository](https://github.com/gavintranquilino/YouTube-view-bot) 