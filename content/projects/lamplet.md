---
title: "4DoF Robot <br> Lamp "
date: "2026-04-30"
imageUrl: "lamplet/lamplet-concept.gif"
thumbnailUrl: "lamplet/logo.png"
subtitle: "a pet lamp for the desk"
bulletPoints:
  - "Designed and built a <strong>4-DOF robotic lamp</strong> in <strong>48 hours</strong> with integrated <strong>mechanical, actuation, and control</strong> systems"
  - "Validated <strong>physical assembly</strong> through complete <strong>wiring, joint motion, and component-layout</strong> checks"
  - "Produced full build documentation (BOM, wiring, and assembly instructions) for reproducibility"
---

## Overview

{{< custom_link href="https://devpost.com/software/other-handhttps://drive.google.com/drive/folders/1EtLfewJRqqHDpUmPZ3ipvWLY57L6Xh9u?" text="Full Project Page (Models)" >}}

### Concept Video - Movement 
{{< my_video_embed src="https://www.youtube.com/embed/bx00OwmyYRo" title="YouTube video player" >}}

### Swinging Legs and Kicking Feet
{{< my_video_embed src="https://www.youtube.com/embed/N3JcIAdKeUc" title="YouTube video player" >}}

## Concept

This robotic desk lamp responds to touch through motion, light, and physical feedback. The goal is to create an object that feels expressive without relying on screens or facial features. Instead, posture, movement, and light direction act as the primary communication channels.

### Real-World Inspiration

The motion language is inspired by Luxo Jr., where simple joint movements convey intent. Small changes in pose and timing are enough to make the lamp feel alive.

{{< slideshow >}}
  {{< slide src="lamplet/luxo.jpeg" caption="Luxo Jr. Inspiration" >}}
  {{< slide src="lamplet/luxo.jpg" caption="Luxo image" >}}
{{< /slideshow >}}

There are many kinds of lampshades/lampheads that exist. Two main kinds of lampshades are categorized here: a drum vs desk lampshade. The drum shaped lampshades refer to those that diffuse light in all directions. The desk lampshades refer to those that direct a light, typically in a conical or tapered out opening to cast light into a direction. Traditional desk lamps focus light directionally, while drum shades diffuse light more broadly. This design sits somewhere in between: directional enough to suggest "attention," but soft enough to feel ambient.

There's also influence from camera-headed characters where direction replaces facial expression. In this case, the lamp's "gaze" is defined entirely by where the light points.

### Lowlight Character

This design builds on my earlier “<a href="https://gavintranquilino.com/lowlight">Lowlight</a>” project, which explored expressive lighting through posture and movement. That version emphasized a subdued tone, with slouched posture and downward lighting suggesting fatigue. In contrast, LeLamp introduces a more interactive and playful interpretation of similar expressive mechanics.

{{< img src="lamplet/lowlight.jpg" alt="Lowlight" size="400x" quality="q75" >}}

The design emphasizes curiosity and playfulness through interaction, combining human-like legged features with a system that actively responds to touch.

## Interaction & Touch System

This section defines how the lamp interprets touch and translates it to physical expression. The touch sensors are assumed to be at the head of the robot. The goal is not just to detect touch, but to translate it into responses that feel immediate, understandable, and expressive.

### Why Touch

Touch is intuitive enough to where a user can immediately understand how to interact with the system. It is independent of environment.

Compared to other input methods:
- Vision systems depend on lighting and positioning
- Voice input is ambiguous and also depends on noise of environment
- Touch provides a clear, localized signal

Since the lamp sits within arm's reach, touch naturally fits the use case. It reinforces the idea of the lamp as a physical companion rather than a passive object.

### Sensing Method

A capacitive touch sensor (TTP223) is placed beneath a ~2 mm plastic layer in the lamp head.

This approach allows for:
- Sensor to be hidden
- Detection through the enclosure
- Light mostly coming out of the face of the lamp

{{< img src="lamplet/touch-sensor.png" alt="Touch Sensor" size="400x" quality="q75" >}}

### Differentiating Touch from Normal Operation

The system separates real touch from noise or motion. Only the head contains the sensor, so body movement cannot trigger input. Calibration can be set in place to tune thresholds for what counts as a "pet" or a successful touch. Based on duration, or multiple sensors at the top to have multiple areas to validate a successful touch. This avoids false positives and creates a more controlled interaction loop.

### Mapping Touch to Response

Touch drives three separate channels: motion, light, and haptics.

<br>
{{< img src="lamplet/touch-response.png" alt="Touch Response" size="800x" quality="q75" >}}

### Head Motion

The head reorients using pitch and yaw toward the interaction point. This creates an immediate attention response and visually confirms input.

### Haptic Feedback

A small vibration is introduced during sustained contact. This confirms interaction without relying on sound and works even when the lamp is not directly in view.

### Light Response (Color & Intensity)

Brightness and color scale with touch duration. Longer contact increases brightness and warms the hue. This provides continuous feedback rather than a binary response.

### Feet Kicking

The legs swing slightly in response to touch. This acts as an additional expressive layer, similar to fidgeting behavior. The motion can be driven by a camshaft system using a single DC motor, allowing both legs to move with minimal added complexity.

## Mechanical System Design

### Customer Profile & User Context

The lamp is designed for desk use and primarily faces the user. Full 360° rotation is unnecessary, so motion is constrained to a more natural range.

### System Architecture (DOF + Layout)

The system uses a 4 DOF structure:

{{< img src="lamplet/DOF.png" alt="Touch Response" size="800x" quality="q75" >}}

This configuration mimics the movement of a seated person rather than maximizing range.

### Structural Design

The base acts as both structure and enclosure. It houses electronics and the leg mechanism.

Legs are split into upper and lower segments connected by a pin joint. The upper segment uses a compliant snap feature for assembly.

Body linkages use lofted geometry to allow smooth motion and consistent mounting for servo integration.

### Lamp Head

The lamp head uses a squircle profile instead of a circular cross-section. This makes roll motion visually readable and provides flat regions for mounting internal components.

The diffuser is positioned at the outer edge of the lampshade. This increases light spread compared to a focused spotlight design, while still preserving a clear directional component. The result is a balance between ambient illumination and a readable "gaze" direction.

<br>
{{< img src="lamplet/lamp-head.png" alt="Lamp Head Types" size="800x" quality="q75" >}}

As mentioned earlier, the capacitive touch sensor is placed behind a thin plastic layer, with approximately 2 mm of separation from the electronics. This prevents direct exposure while still allowing reliable capacitive sensing.

<br>
{{< img src="lamplet/head-cross-section.png" alt="Lamp Head Types" size="800x" quality="q75" >}}

### Base

The base is designed as a seated platform for the robot, with a rounded bottom profile to improve stability and reduce tipping risk during motion.

<br>
{{< img src="lamplet/base1.png" alt="Base Design" size="800x" quality="q75" >}}

It is split into two main bodies that friction-fit together. Manufacturing tolerances are used intentionally to create an interference fit, with chamfered edges to assist alignment during assembly.

<br>
{{< img src="lamplet/base2.png" alt="Base Design" size="800x" quality="q75" >}}

Internal mounting points use M2 screws to secure the Raspberry Pi and servo driver board. The enclosure also leaves space for future expansion, including additional mechanisms for leg motion.

<br>
{{< img src="lamplet/base3.png" alt="Heat Set Inserts in Base" size="800x" quality="q75" >}}

Cable routing is integrated into the base through dedicated slots and heat-set inserts, allowing power and signal wires to enter and exit cleanly without interfering with moving parts.

Large cutouts are placed behind the leg region. These are intended as potential entry points for a future cam or reciprocating mechanism to drive leg motion. This feature is not implemented in the current version due to time constraints but is preserved in the mechanical layout for future iteration.

<br>
{{< img src="lamplet/base4.png" alt="Base Design with Legs" size="800x" quality="q75" >}}

### Body Linkages

Consistent design features are used across all body linkages to maintain mechanical coherence.

Lofted geometry is used throughout to ensure smooth motion between joints. This helps maintain a usable range of motion while avoiding sharp transitions that could introduce stress concentrations or mechanical binding.

Servo mounting points are integrated directly into these linkages, allowing M3 fasteners to interface cleanly with rotating servo shafts.

## Electrical System Design

### Component Selection

#### Actuation

The system uses STS3215 serial bus servos rated for 7.4 V. These were selected due to their high torque (16.5 kg·cm stall) and compact form factor, which allows multiple DOF to be placed close together in the head and upper body.

<br>
{{< img src="lamplet/servos.png" alt="Servo Selection" size="400x" quality="q75" >}}

Although rated for 7.4 V, the servos are operated at 5 V. This reduces peak torque and speed, but results in smoother motion and safer interaction in a desk environment. The reduced stiffness also allows partial backdrivability (according to LeRobot's leader model), which is desirable when colliding with objects.

Servos are controlled using a Waveshare serial bus servo driver board. This simplifies wiring by allowing multiple servos to share a communication line while being individually addressed.

<br>
{{< img src="lamplet/driver-board.jpg" alt="Servo Driver Board" size="400x" quality="q75" >}}

#### Compute

A Raspberry Pi 3B+ is used as the main controller. It handles:
- Touch input processing
- LED control
- High-level motion commands

<br>
{{< img src="lamplet/raspi.jpg" alt="Raspberry Pi" size="400x" quality="q75" >}}

A headless setup is used to reduce overhead and allow remote access via SSH.

#### Sensors and Transducers

**Capacitive Touch (TTP223):**
The TTP223 provides a digital HIGH/LOW output based on capacitive proximity. It is placed beneath the lamp head enclosure, allowing touch detection through a thin plastic layer.

**LED System (WS2812B):**
WS2812B addressable LEDs are used for lighting. A small matrix is formed by segmenting and reconnecting LED strips.

Each WS2812B LED can draw up to ~60 mA at full white. For a 3×3 configuration (9 LEDs), maximum current draw is approximately:
- 9 × 60 mA ≈ 0.54 A maximum
- The Raspberry Pi 3B+ can support up to 1.2 A

<br>
{{< img src="lamplet/LED-matrix.png" alt="LED Matrix" size="400x" quality="q75" >}}

This is within safe limits for a dedicated 5 V rail. LED strips were chosen over ring modules for flexibility in layout and cost. While it adds time to the assembly process, as a personal project, there is much more value in purchasing LED strips rather than an LED matrix as there is more to work with. The strips also can be changed in positioning unlike the matrix. The LED strips are still addressable when wired in series.

Lighting is controlled using the FastLED library, which allows per-pixel RGB control and global brightness scaling. FastLED's global brightness control is used to scale LED output without modifying individual pixel values, enabling consistent color output while adjusting perceived intensity based on interaction state.

#### Power and Wiring

The system uses two separate 5 V power supplies:

**Motor supply**
- Powers all servos through the driver board
- Isolates high-current motor noise

**Raspberry Pi supply**
- Powers Raspberry Pi, LEDs, and touch sensor

The separation is important as servo motors introduce large voltage drops which can interfere with the Pi.

A shared ground is maintained between both supplies to ensure consistent signal reference.



### Electrical Architecture

<br>
{{< img src="lamplet/electrical-architecture1.jpg" alt="Electrical Architecture" size="800x" quality="q100" >}}

## Firmware & Software Architecture

### Runtime Setup

The Raspberry Pi 3B+ is meant to run a headless setup using Raspberry Pi OS Lite and is accessed via SSH.

## Cost Breakdown

The total system cost is approximately USD $335, which is comparable to existing LeLamp configurations using similar actuation and compute hardware.

Cost efficiency is primarily achieved through the use of commodity components such as WS2812B LED strips, TTP223 capacitive sensing, and a shared serial bus servo ecosystem, reducing both part cost and integration complexity.

## Assembly

### Assembly Order

The lamp head is assembled first. The LED strip is cut and wired into the desired matrix configuration, then connected to power and data lines. The capacitive touch sensor is mounted behind the head enclosure, with wiring routed internally. The diffuser is then attached to complete the head module.

From the head, the system is built downward by sequentially attaching servo motors and linkages. Each joint is fastened before moving to the next to ensure proper alignment and range of motion. The final servo in the chain is mounted directly to the base.

<br>
{{< img src="lamplet/top-assembly.png" alt="Top Assembly" size="800x" quality="q75" >}}

The base is assembled last. Heat-set inserts are installed into the enclosure to allow secure mounting of the Raspberry Pi and the servo driver board. All electrical connections are completed at this stage before closing the enclosure.

### Wiring Strategy

Wiring is routed externally along the back of the structure rather than through internal linkages. This avoids tangling and interference, especially if joints approach larger ranges of motion. 22 AWG wire is used for power distribution.

All wires from the head are bundled together and guided along the rear of the arm into the base enclosure. Zip ties or cable sleeves can be used for organization.

Standard jumper wires are used for connections:
- Female-to-female wires for the touch sensor
- Male-to-female wires for LED connections

This keeps the system modular and easy to debug or modify.

### Fasteners

The system primarily uses M2 and M3 screws with matching nuts and heat-set inserts.

Countersunk fasteners are used where possible to keep surfaces flush and avoid interference with motion. This also improves the overall appearance and reduces snag points during interaction.

## Testing, Risks, and Improvements

### Factors to Test

A major focus during validation is system behavior under real interaction, especially where physical motion and user perception overlap.

#### Audible Noise

Mechanical noise is a critical factor in perceived quality of interaction. In particular, the leg mechanism introduces the highest risk of audible disturbance during motion.

Noise affects the system in two ways:
- It can break immersion by making motion feel "mechanical" rather than expressive
- It can become distracting during normal desk use

For this reason, noise is treated as a design constraint rather than an afterthought. Audio feedback was intentionally avoided to preserve a quiet interaction model. Mechanical motion already introduces some noise.

#### Center of Gravity and Stability

Stability is influenced heavily by link length and mass distribution. Shorter linkages are used to reduce torque at the base and minimize tipping risk during fast motion.

This is especially important when:
- The head is extended forward
- Multiple joints are moving simultaneously
- The leg mechanism is active

### Failure Modes

#### Leg Mechanism

The legs are the most likely failure point due to the compliant geometry used in the upper joint. This design was intentionally chosen for prototyping expressivity, but it introduces stress concentration and potential snapping under repeated load.

<br>
{{< img src="lamplet/leg-failure.png" alt="Leg Failure" size="800x" quality="q75" >}}

#### Base Structure

The base and first linkage of the robot carry the highest structural load, especially when the lamp is extended. While designed with mounting points and internal support, it remains the primary load-bearing component and must resist both static and dynamic forces from motion.

### Improvements

Improvements for future iterations:

#### Expressive Add-ons

- Magnetic mounting on the head to allow physical accessories
- Optional vibration module in the head for richer haptic feedback
- Potential audio output system

<br>
{{< img src="lamplet/accessorize.png" alt="Accessorize" size="800x" quality="q75" >}}

#### Mechanical Optimizations

- Improve base aesthetics and manufacturability
- Redesign linkages for easier assembly access, especially near the first joint
- Optimize linkage geometry using FEA to reduce unnecessary mass and improve stiffness-to-weight ratio

#### Manufacturing Improvements

- Split base structure into multiple printable parts for better structural integrity and easier printing
- Align print orientation with expected load paths to take advantage of anisotropic strength
  - If using 3D printed parts
  - Especially in high-stress regions around the base ("butt") of the robot

## Version 2

Based on the feedback from the first iteration, the mechanical design was updated to address assembly, structural integrity, and actuation details. The focus was on making the system more buildable while preserving the original interaction and form.

### Mechanical Design

#### Friction Fits and Assembly

Several friction-based connections were replaced with more robust fastening methods.

The base is now secured using four M3 screws with heat-set inserts, creating a more rigid and reliable enclosure. This change improves overall structural stability and makes the assembly more suitable for repeated use.

<br>
{{< img src="lamplet/base5.png" alt="Base Assembly" size="800x" quality="q75" >}}

The lamp diffuser, which was previously friction fit, is now mounted using embedded magnets. This allows the diffuser to be easily removed for maintenance while keeping the exterior clean and uninterrupted. The magnets can be press-fit depending on print tolerances or secured with adhesive.

{{< slideshow >}}
  {{< slide src="lamplet/diffuser1.png" caption="Diffuser (cover)" >}}
  {{< slide src="lamplet/diffuser2.png" caption="Lamp Head" >}}
{{< /slideshow >}}

The leg joints were updated to use flanged ball bearings between the upper and lower segments. This constrains motion to a single axis and reduces unwanted play compared to plastic-on-plastic contact. With mass concentrated toward the feet, the legs naturally settle downward under gravity, improving consistency in motion.

<br>
{{< img src="lamplet/upper-legs.png" alt="Upper Legs" size="800x" quality="q75" >}}

#### Scotch Yoke System

The original cam-based concept was replaced with a scotch yoke mechanism to better fit within the constraints of the base and reduce part complexity.

This mechanism converts rotational motion into linear motion using a crank and sliding interface. Compared to a cam or slider-crank system, it requires fewer parts and is easier to replicate.

{{< my_video_embed src="https://www.youtube.com/embed/N3JcIAdKeUc" title="YouTube video player" >}}

The geometry of the lower legs was adjusted to accommodate the yoke interface, providing a surface for the mechanism to drive while keeping the system enclosed within the base. The base itself was modified from simple slots to carved internal volumes to house the mechanism.

<br>
{{< img src="lamplet/scotch-yoke.png" alt="Scotch Yoke" size="800x" quality="q75" >}}

Both legs are driven by a single DC motor. By offsetting the crank phases, alternating motion is achieved with a simple on/off control.

<br>
{{< img src="lamplet/motor.jpg" alt="Motor" size="800x" quality="q75" >}}

#### Failure Modes

The base linkage remains a critical load-bearing component. Its performance depends heavily on material choice, print orientation, and infill, which are difficult to fully evaluate without physical testing.

The scotch yoke introduces sliding contact between components, which may lead to wear over time. This could be mitigated by using smoother materials, adding lubrication, or replacing contact surfaces with metal components.

<br>
{{< img src="lamplet/scotch-yoke-zoom.png" alt="Scotch Yoke" size="800x" quality="q75" >}}

#### Improvements

Further improvements would focus on assembly and robustness.

The base could be split into multiple parts to improve accessibility during assembly, avoiding difficult tool access and reducing the need for awkward hand positioning. Removable faces would simplify installation of internal components.

Joint assembly could also be refined. While the current bearing-based approach constrains motion effectively, the method of installing these components can be improved. Alternatives include multiple parts that allow bearings or pins to be inserted before closing the joint, or the use of a separate shaft that passes through both segments.

These decisions would benefit from physical prototyping, where tolerances, fit, and ease of assembly can be evaluated more accurately.

### Electrical Design

A 6V DC hobby motor is used to drive the leg mechanism. This type of motor is widely available, compact, and fits within the base constraints of the design.

The motor is controlled using a single-channel 5V relay module. While the motor operates at 6V, the relay is only used as a switch, allowing the Raspberry Pi to safely control a higher-current load without directly driving the motor.

The relay module is powered from the 5V rail and triggered using a GPIO pin from the Raspberry Pi. This allows simple ON/OFF control of the motor, which is sufficient for driving the reciprocating motion of the scotch yoke mechanism.

#### Improvements

For future iterations, alternative switching methods could be considered.

Relay modules are widely available from sources such as Amazon, Digi-Key, and SparkFun, with variations in form factor and interface. For systems with multiple actuators or sensors, an I2C-based relay or driver could simplify wiring and improve scalability.

For this iteration, a standard GPIO-controlled relay module was selected to prioritize simplicity and rapid integration. The exact component is not tightly constrained and is not reflected in the mechanical design.
