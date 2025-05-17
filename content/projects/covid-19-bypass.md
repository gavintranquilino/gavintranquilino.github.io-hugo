---
title: "<strong>COVID-19</strong> Screening Bypass"
date: "2021-03-01"
imageUrl: "/img/covid-19.png"
subtitle: "Not Intended for Malicious Intent"
---

## What does it do?

This program is a project I designed to quickly fill out the COVID-19 Screening Tool. Every time I went to school, I had to fill out the COVID-19 Screening Form as a proof that I can enter the building. The questions on the form are very straightforward and common sense. While this program is not intended to lie on the form, this was created to speed up the process of having to fill out a valid form every day. I designed this program using Python and the selenium library.

## Video Demonstration

{{< my_video_embed src="https://www.youtube.com/embed/UZwzyrAIt7A" title="YouTube video player" >}}

If you can\'t already tell, this is satire. I\'m not actually sick nor did I get anyone sick. Though, the Python script is pretty sick tbh.

## Try it out yourself! (NOT WORKING 2023)

You can try the demo on Replit, but note that it\'s no longer working as of 2023:

[Try on Replit](https://replit.com/@GuhBean/ontario-covid19-screening-bypass)

## How does it work?

This program uses Python and a few third-party libraries such as, selenium, smtplib, and email. The selenium library is a web testing tool to run scripts and commands on a browser. This library is used in this program to handle the actions on the screening tool like opening the website, pressing buttons, etc. The smtplib and email libraries are both used together to handle sending automated emails to the users that are listed in the config files.

On startup, the program opens a "webdriver", which is just fancy for "broswer for robots" as it allows commands and scripts to be ran on specific elements of a website. The next step is to open the website of the screening tool. Once the tool has opened, the program follows a series of steps to fill out the screening form. The program looks for buttons to click via their respective xpath values. These xpaths are just names of certain elements of a website like buttons, text, containers, etc. Once a valid form has been filled, the program then takes a screenshot of the final page and closes the webdriver.

After the webdriver has been closed, the program then connects to an email address of the user\'s choice. Then, an SMTP connection to the email address will be created. After the connection, the program reads the email template and contacts list in order to find all the email addresses to send the screenshot to. The program, one by one, sends an email to all the contacts in the contacts list. While this email feature is not available in the web version above, this program is open sourced on GitHub, ready for you to use.

[GitHub Repository](https://github.com/gavintranquilino/ontario-covid19-screening-bypass)

## TAS WORLD RECORD??
{{< my_video_embed src="https://www.youtube.com/embed/ZsbxI7mqVh0" title="YouTube video player" >}} 