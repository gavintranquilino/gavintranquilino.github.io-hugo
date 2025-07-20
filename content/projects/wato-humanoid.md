---
title: "Dexterous Robotic<strong>Humanoid Arms</strong>"
date: "2025-05-05"
thumbnailUrl: "/img/wato-humanoid/thumbs-up.jpg"
imageUrl: "/img/wato-humanoid/thumbs-up.gif"
subtitle: "WATonomous x UW Reality Labs"
---

## Currently in Development
I am currently working on a humanoid robot arm project with the University of Waterloo's design teams, <em>WATonomous</em> and <em>UW Reality Labs</em>. The goal is to create an <strong>anthropomorphic humanoid robot arm</strong> that can perform a variety of tasks with dexterity and precision.

The <em>CURRENT</em> focus is on creating a V1 prototype with full hardware. This includes the mechanical design, power electronics, embedded software, and control algorithms. The V1 prototype will be capable of teleoperated control via Quest 3 Headsets' hand tracking through a custom Unity application built by the UW Reality Labs team.

The <em>ULTIMATE</em> goal is to train the humanoid arm to perform tasks automatically using reinforcement learning. This will involve developing a robust simulation environment using NVIDIA's Isaac Sim. The main objective is to get the humanoid arms to learn to <strong>autonomously type on a keyboard</strong>, which requires precise finger movements and coordination. <em>(It would also look really cool since now LLMs can interact with my physical keyboard and edit code directly!)</em>

<br>

## My Role
I am a Co-op student for the WATonomous team during the Winter 2025 term, and I am responsible for several key aspects of the humanoid arm project:

### Mounting a CANbus Transceiver in Docker

I am responsible for the interfacing between the hardware and software components of the humanoid arm. This includes developing the CAN bus communication protocols, integrating the sensors and actuators, and ensuring smooth data flow between the different systems. An interfacing ROS2 (Robot Operating System 2) C++ node is being developed to mount a USB2CAN transceiver to send and receive messages using a CANable 2.0 device.

{{< my_video_embed src="https://www.youtube.com/embed/qJ9y6icVFc8" title="YouTube video player" >}}

I am mounting the CANable 2.0 device in a Docker container to allow communication through ROS2 topics and services over a CAN bus. This setup requires configuration of the Docker container to recognize the CANable device, which is done by adding the device with a Linux symlink to the /dev/canable interface. The Dockerfile includes the necessary dependencies and configurations to ensure that the ROS2 node can communicate with the CAN bus effectively. Check it out 

### URDF Simulation in NVIDIA Isaac Sim
I am also working on the simulation URDF (Unified Robot Description Format) for the humanoid arm in NVIDIA's Isaac Sim. This will allow us to test and refine the control algorithms in a virtual environment before deploying them on the physical robot. Within the URDF, I am also implementing the hardware IDs of all the motors and sensors, which is crucial for the CAN bus communication.

I first created a URDF file for the humanoid arm, which includes the kinematic and dynamic properties of the robot by using an open source Fusion360 script to export the model called fusion2urdf. This script generates a URDF file from the Fusion360 model, which can then be imported into Isaac Sim for simulation.

Here is my motion study of the humanoid arm to visualize the dynamics of the arm to gesture a thumbs up:

{{< my_video_embed src="https://www.youtube.com/embed/csXZSvSeIx4" title="YouTube video player" >}}


