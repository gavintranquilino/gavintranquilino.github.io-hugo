---
title: "FlexiTrack: <strong>Health Tech <br> Innovation Challenge</strong>"
date: "2025-02-05"
imageUrl: "/img/flexitrack/square.jpg"
subtitle: "get your patients moving"
---

# FlexiTrack: Combating Hospital Delirium

We were awarded the <strong>Grand River Hospital's Most Innovative Project</strong> for this, and it was a team effort with my friends from the University of Waterloo.

{{< my_video_embed src="https://www.youtube.com/embed/AVHAPjYH-AA/" title="YouTube video player" >}}

{{< custom_link href="https://youtu.be/2dW5qCMDXIY" text="Shorter demo video to save you on time :)" >}}

So here's the deal - Grand River Hospital had this massive problem with their long-term senior patients. These folks were stuck in bed dealing with inactivity and boredom because of physical constraints and limited tech familiarity. 

The worst part? Many of them stay bedridden which cranks up the risk of hospital-induced delirium - basically when your mental state gets all confused and disoriented. Not fun.

We asked ourselves: how do we get these patients moving?

## Our Solution

Enter FlexiTrack - a mobile app that lets hospital volunteers and nurses host exercise sessions right in the ward. 

Here's the cool part: we built a computer vision system that tracks patient movement during sessions and awards them points based on their physical activity. Those points? They can redeem them for games and recreational activities to keep them motivated.

### App Features
{{< slideshow >}}
  {{< slide src="/img/flexitrack/dashboard.jpg" caption="FlexiTrack Main Interface" >}}
  {{< slide src="/img/flexitrack/mediapipe.jpg" caption="Points Tracking System" >}}
  {{< slide src="/img/flexitrack/awards.jpg" caption="Redeeming Prizes" >}}
{{< /slideshow >}}

## How It Works

The volunteer enters the patient's name (let's say John), selects their activity group, and picks from allowed exercises like arm yoga, stretching, or simple hand movements.

Once everything's set up with the cameras, the session starts. Our system tracks the distance traveled by their wrists (we focus on upper body exercises) and monitors their speed. All that movement data gets converted into points they can actually use.

After the session ends, John might have scored 6 points to add to his existing total, and boom - he can claim some cards, board games, or magazines.

## The Tech Stack

FlexiTrack is built on a robust tech stack that includes:

- **Frontend**: <u>SwiftUI</u> and <u>XCode</u> for the iOS app, providing a user-friendly interface for staff
- **Backend**: <u>Python</u> with <u>Flask</u> to handle requests and manage the points system
- **Database**: <u>SQLite</u> to store points per patient locally - just points, no personal data
- **Computer Vision**: <u>Mediapipe</u> for real-time pose detection and tracking
- **3D Model**: <u>Solidworks</u> for designing the adjustable camera mount and the hospital beds

{{< slideshow >}}
  {{< slide src="/img/flexitrack/camera-mount.jpg" caption="Camera Mount in CAD" >}}
  {{< slide src="/img/flexitrack/CAD.gif" caption="Full CAD Animation" >}}
  {{< slide src="/img/flexitrack/swift-development.jpg" caption="XCode Environment" >}}
{{< /slideshow >}}

## Impact

This isn't just about getting people to move - it's about preventing hospital-induced delirium and keeping patients engaged during their stay. By gamifying physical activity and making it accessible regardless of mobility level, FlexiTrack creates a win-win for patients and healthcare staff.

The adjustable camera mount means we can accommodate patients whether they're in bed, sitting up, or standing. It's all about meeting them where they are and giving them something to look forward to.

## Contributors
This project was a collaborative effort with my friends from the University of Waterloo, including:
- **[Gavin Tranquilino](https://linkedin.com/in/gavintranquilino)** | University of Waterloo Mechatronics Engineering | Class of 2028
    - Project Lead, Computer Vision, 3D Model Design
- **[Tito Ngo](https://linkedin.com/in/tito-ngo)** | University of Waterloo Mechatronics Engineering | Class of 2028
    - Computer Vision, Backend Development, Points System
- **[Michael Chan](https://www.linkedin.com/in/michaelchanwh8/)** | University of Waterloo Biomedical Engineering | Class of 2029
    - Frontend Development, User Interface Design
- **[Soyoon (Emma) Lee](https://www.linkedin.com/in/soyoon-emma-lee-619b83301/)** | University of Waterloo Biomedical Engineering | Class of 2029
    - Frontend Development, Patient Interaction Design
- **[Nina Yu](https://www.linkedin.com/in/nina-yu-3281a4300/)** | University of Waterloo Biomedical Engineering | Class of 2029
    - Frontend Development, User Testing, Documentation

{{< slideshow >}}
  {{< slide src="/img/flexitrack/team-photo1.jpg" caption="Team Photo" >}}
  {{< slide src="/img/flexitrack/team-photo2.jpg" caption="Awarded Most Impact" >}}
  {{< slide src="/img/flexitrack/judging.jpg" caption="Judging POV" >}}
{{< /slideshow >}}

{{< custom_link href="https://github.com/gavintranquilino/HealthInnovationChallenge" text="GitHub Repository" >}}

