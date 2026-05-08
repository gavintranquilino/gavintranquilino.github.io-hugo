---
title: "Acceleration Consortium"
date: "2026-04-22"
imageUrl: "acceleration-consortium/ot-flex-render.png"
thumbnailUrl: "acceleration-consortium/ot-flex-render.png"
subtitle: "Self-Driving Lab"
bulletPoints:
  - "Integrated a self-driving lab automating a 2D gantry and <strong>6DoF robot arm</strong> for autonomous material discovery experiments"
  - "Architected <strong>MQTT</strong>-based control infrastructure orchestrating 8 connected <strong>IoT devices</strong> over ethernet and wireless links"
  - "Developed <strong>inverse kinematics</strong> in <strong>Python</strong> and designed custom <strong>Fusion360</strong> tooling for autonomous material handling"
---

# OTFlex

{{< my_video_embed src="https://www.youtube.com/embed/BVLOpPXhVL8" title="YouTube video player" >}}


> BELOW IS WORK IN PROGRESS FOR ASSETS
## Overview
OTFlex is the main self-driving lab workflow and the system I owned most directly from the start. It combines robot-arm motion, automated reactor handling, furnace transfer, MQTT-controlled hardware, electrochemistry, liquid handling, and camera monitoring.

The final workflow is notebook-driven. Each notebook cell maps to a single function or step, which keeps the control flow readable without collapsing everything into one large script. The codebase is organized as a monorepo, with each device isolated in its own folder and documented with a local README.

OTFlex is now in use by a postdoc for experiments. The setup includes the reactor hardware, the syringe pump workflow, the robot arm, the furnace, and the monitoring and control infrastructure needed to run the lab as a connected system.

## Networking Architecture
The lab network is built around a NETGEAR GS308EP switch. All MQTT devices and the control computers connect through the switch. The OTFlex MQTT stack uses 192.168.0.100, and OT2 uses the same address within its own separate workflow. When the two systems need to communicate, OT2 uses 192.168.0.102 to avoid ambiguity.

Most lab devices are controlled over Ethernet. The network was set up with static IPv4 addresses, SSH access, and Windows firewall configuration so the MQTT broker, IoT devices, and control computers could be reached without depending on external network services.

## MQTT IoT Device Tower
The MQTT tower coordinates the connected hardware through ESP32-based devices and relay boards. The tower was wired into the switch and iterated alongside the rest of the lab network.

Key work included:
- Wiring the ESP tower and the network switch into the OTFlex control path
- Debugging thermistor behavior on the newer tower hardware
- Replacing a failed relay when one channel stopped clicking
- Cleaning up cable routing and labeling across the tower and surrounding devices
- Using heartbeat and status topics so the devices could report connectivity and state

## Autoreactor
The reactor hardware went through several redesigns before settling on a usable geometry. The final well design uses a 60 degree funnel that stops tapering at a fixed diameter. That version gave the best cleaning behavior, the cleanest reaction geometry, and the most useful imaging results.

The reactor substrate uses 15.8 mm cut zinc circles sandwiched between two 3D printed plates. That assembly can be transferred by the robot arm between the reactor and the furnace. The plates are preassembled and stored in a dedicated tower so they can be swapped into the workflow as a unit.

Earlier work on the reactor focused on o-ring fit, leak testing, screw length, substrate plate tolerances, and separating the o-ring retention geometry from the well geometry so each parameter could be changed independently.

## Robot Arm
The robot arm is used to move plates through the OTFlex workflow, including transfers between the reactor and furnace. The arm layout was recalibrated as the lab arrangement changed, and the movement steps were rewritten to match the final physical setup.

The arm work also included safe handling around the furnace door and repeated manual testing of reach, pickup location, and repeatability. One furnace door was damaged during early testing, which made slow motion and e-stop access part of the standard operating procedure.

## Ultrasonic Bath
The ultrasonic bath is part of the cleaning and sample-prep workflow. I set up the bath hardware, mounted the ultrasonic transducer in a food-container style bath, and worked through the container geometry needed to hold the beakers.

The bath was used for electrode cleaning and solvent handling. The hardware was documented with annotated images so the physical assembly and wiring could be reproduced later.

## Documentation
Documentation moved from scattered daily notes into a monorepo structure with local README files, device-specific folders, and annotated diagrams. Drawio was used for wiring and system diagrams, and the repository was cleaned up so each module has a clear role.

The notebook workflow for OTFlex also became part of the documentation style. Each step is kept in a separate cell, which makes the sequence readable while still leaving the code editable and close to the hardware behavior it controls.

## Potentiostat
I first tried a 4-potentiostat parallel setup. That path did not work because the wells and substrate were electrically shorted once the hardware was connected through the USB hub, so all channels ended up measuring the same thing.

The final electrochemistry setup uses a Biologic VSP-3e connected to another PC. The OTFlex computer reaches that machine over SSH and runs the Biologic API from there, which keeps the serial connection local to the Biologic host while still allowing the workflow to be driven from the OTFlex side.

The earlier wiring work, plot validation, and channel debugging were still useful for identifying where the electrical isolation problems came from before the system was simplified.

## Setting Up New Computer
OTFlex and the related lab machines were brought up with the same basic control stack: Windows 11, Mosquitto, Python, Git, VS Code, Wireshark, SSH, static IPs, and firewall configuration.

Two Raspberry Pi camera setups were used:
- A top-down SSH-only Pi mounted above OTFlex for labware capture and later computer vision work on labware configuration
- A Tailscale Pi that auto-connects over eduroam and streams to a private YouTube channel for remote monitoring of the self-driving lab

This setup made it possible to keep a top-down view for offline analysis while also maintaining a remote live feed without depending on local WiFi access.

## 3D Models
Most of the mechanical work was done in Fusion 360. That included the reactor wells, substrate plates, o-ring fit experiments, substrate cutter concepts, the syringe pump housing, bottle trays, PSU mounts, and other support parts around the workflow.

The 3D models were used for both functional fit checks and manufacturing handoff. Some parts were exported as 2D drawings for machining, while others were printed for direct use in the lab.

# OT2
## Reactor Design and Manufacture
OT2 was kept as a separate, simpler workflow. It shared some of the same lab ideas as OTFlex, but the automation stack was less integrated and did not include the same robot arm and furnace-driven transfer path.

The reactor work focused on well geometry, o-ring fit, substrate plate tolerances, and manufacturability. Early iterations used DTU-inspired geometry, including a 24.8 degree internal funnel angle and a 25 mm reactor height reference. Other work covered 2D drawings for machining alumina, where complex features such as fillets and lofted details were removed to make the parts easier to machine.

## Troubleshooting
The main OT2 troubleshooting work centered on reactor leakage, hardware fit, and workstation stability.

Key issues and fixes included:
- Leak testing reactor wells and tracing leaks to overhang gaps and support material in printed parts
- Adjusting screw lengths and substrate plate tolerances to improve sealing and fit
- Investigating memory creep on the Windows 11 lab desktop and reducing it by disabling Fast Startup and using RAMMap to clear standby lists and working sets
- Debugging IP addressing and device reachability on the lab network when devices could not find the host computer
- Reworking relay and pump addressing issues when hardware channels failed to respond as expected

# 12 Channel Syringe Pump Reactor
## 3D Modelling
The 12 channel syringe pump reactor was built as a separate hardware project for liquid handling. The mechanical design includes a central pump holder, PSU mounting, communication board space, and modular storage for bottles and solution containers.

The tray and support pieces were modeled in Fusion 360 and printed as modular parts so the pump system could be assembled, serviced, and reconfigured without rebuilding the whole frame.

## RS485 and Pump Control
I tested CAN and serial communication paths before settling on RS485 and the pump vendor workflow. The final control path uses the library and tooling that matched the pumps best, including medusa-sdl and the Matter Labs pump tooling.

Work on the control path included:
- Testing USB to CAN and serial adapters
- Trying official vendor software and Linux command-line tools
- Using Python notebooks for direct control once the communication path was understood
- Building a CSV-driven recipe interface so pump steps could be described as input data rather than hardcoded control logic

## Bottle Tray
The bottle tray was designed as a modular storage and support system for the syringe pump workflow. It holds bottles and vials in a repeatable layout and can be rearranged as needed for different solution sets.

The tray design was built to fit into the broader lab workflow, including the pump module, the solution storage layout, and the surrounding hardware footprint.

## Workflow
The final pump workflow is notebook-based. A CSV file can define the recipe, a Python object maps the ingredients and volumes, and the notebook executes the pumping sequence step by step.

That setup was used for the new syringe pump reactor and the related liquid handling work in Ethan’s reactor workflow. The final workflow is easy to inspect in the notebook while still being direct enough to run against the hardware.