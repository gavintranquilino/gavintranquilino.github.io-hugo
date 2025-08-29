---
title: "This is <strong>bAIRiatric Supports</strong>"
date: "2025-02-10"
imageUrl: "bAIRiatric-Supports/team-photo.jpg"
thumbnailUrl: "bAIRiatric-Supports/deflated-inflated.jpg"
subtitle: "Inflatable positioning aids for patients"
---

## Current Prototype

The following videos show the current prototype of the bAIRiatric Supports. It is a set of inflatable positioning aids designed to help patients with fragile skin in a hospital setting.

### Full Investor Pitch

Re-iteration of the investor pitch to Velocity, a University of Waterloo incubator program. This pitch was presented in February 2025 in front of .
{{< my_video_embed src="https://www.youtube.com/embed/0gSxQEFNIAI" title="YouTube video player" >}}

### Late Night Prototype Demonstration

{{< my_video_embed src="https://www.youtube.com/embed/VJ1yfOQpn9E" title="YouTube video player" >}}

## Understanding the Problem

The following sections provide an overview of the problem that bAIRiatric Supports aims to solve, including the types of skin injuries, common mechanisms of skin injury, and current problems that staff at the Grand River Hospital (GRH)/Waterloo Regional Health Network (WRHN) face when dealing with patients with fragile skin.

![WRHN Logo](https://www.grhosp.on.ca/assets/images/interface/logo-wrhn.svg)

*All information in this section is based on a presentation using retrieved information from the Skin and Wound Team, Grand River Hospital, February 2025.*

#### ⚠️ QUICK NOTE:

> Jump to [Building the Prototype](#building-the-prototype) to see the technical details for how the prototype was built and **skip** the background information.

### Moisture Associated Skin Damage (MASD)
- Moisture from urine, stool, sweat or wound exudate causes irritation and damage, worsened by rubbing and shearing.

![image.jpg](https://www.3m.com.au/wps/wcm/connect/579302e3-aa7b-4761-a29a-12dbef76eb35/moisture+graphic.jpg?MOD=AJPERES&CACHEID=ROOTWORKSPACE-579302e3-aa7b-4761-a29a-12dbef76eb35-ofHDGsQ)

- Overhydration of the stratum corneum increases skin pH, making it more alkaline, inflamed, and susceptible to friction damage.
    - Retrieved from [3M](https://www.3m.com.au/3M/en_AU/cavilon-au/conditions/)

### Types of Skin Injury & Bariatric Context

- **Pressure Injury:** External pressure compresses tissue, reducing blood flow and causing skin death.

- **Friction Injury:** Surface rubbing creates heat, wearing away the epidermis and exposing deeper layers.

- **Shear:** Tissue and bone move in opposite directions, causing tearing and deep damage with potential tunneling.

#### What does "Bariatric" mean?
- **"Bariatric"** refers to medical care for patients with obesity (BMI > 30). Over 30% of Canadian adults have obesity according to [Statistics Canada 2022](https://www.statcan.gc.ca/o1/en/plus/7877-examining-health-consequences-obesity-over-time0).

![Wii Fit BMI](https://i.ytimg.com/vi/RrG4nopGsOo/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCSvJcXRFyU_oZAHMybbVuhz3dWqA)

<br>

### Pressure Injury Timeline & Risk Factors

- **Development:** Starts as discoloration over bony prominences, progresses to blisters, open sores, and potentially deep infections reaching muscle or bone.

#### How long does it take for a pressure injury to develop?
> # 2 HOURS

- *Retrieved from Skin and Wound Team, Grand River Hospital, February 2025.*

**High-Risk Patients:** Elderly, immobile, post-operative (especially with epidurals), stroke patients, those with neurological disorders causing spasticity, medical device users, and anyone with a [Braden Scale](https://www.in.gov/health/files/Braden_Scale.pdf) score ≤ 16.

![Elderly Patients](https://www.grhosp.on.ca/assets/images/general/_contentLarge/QualityImprovementInterview_9041.jpg)

> Materials positioned **against** patient skin can also cause pressure injuries.

### Current Hospital Challenges

Staff at Grand River Hospital face multiple challenges with bariatric and fragile-skin patients:

**Patient Factors:** Cognitive limitations, physical weakness, coordination issues, and mental health concerns (depression, anxiety, feeling burdensome).

**Environmental Barriers:** Narrow doorways, weight-limited equipment, tight maneuvering spaces, storage limitations, and inadequate pressure-relieving surfaces.

**Equipment Needs:** Specialized wheelchairs with proper weight capacity, pressure-relieving cushions, bariatric walkers, beds with appropriate mattresses, wide commodes, and lifting devices (passive/active lifts). However, lift slings can increase pressure and shearing, and improperly sized equipment causes injury from lack of weight-shifting ability.

![Hoyer Lifts](https://qbank.arjo.com/productpageimages/Arjo.Tenor%20transfer%20to%20Carmina_Product_Page_Main_Image.jpg)

<br>

## Speaking with the Experts (Dr. Arash Arami)
- [Dr. Arash Arami](https://uwaterloo.ca/mechanical-mechatronics-engineering/profile/aarami), Professor in Mechanical & Mechatronics Engineering at University of Waterloo
- Specializes in biomedical device design, rehabilitation robotics, and wearable health technologies

![Dr. Arash Arami Profile](https://ofis.uwaterloo.ca/profile/aarami.png)

**🔑 Key Insights:**
- Emphasized the importance of **🧩 modular, scalable designs** for hospital environments
- Avoid reinventing complex specialized equipment (lifts, beds) that already exists
- Focus on **💡 simple, cost-effective solutions** that set us apart from existing designs
- Traditional equipment requires intrusive installation and takes up significant space
- **🔗 Integration is key:** Solutions must easily fit into existing hospital workflows without disruption

## 🧑‍⚕️ Speaking with the Nurses
**Interview Focus:** Understanding challenges and needs when caring for patients with fragile skin at Grand River Hospital

**🔍 Key Challenges Identified:**
- **💪 Physical demands:** Moving patients is extremely taxing with limited resources
- **📍 Patient tracking:** Difficult to locate patients who move frequently around the hospital
- **💬 Communication gaps:** Staff must constantly brief each other on patient status and care plans
- **🔒 Privacy concerns:** Storing patient information poses additional privacy risks

**⚠️ Important Constraints:**
- **📜 Regulatory compliance:** Must maintain existing patient movement protocols and rolling techniques
- **👁️ Human oversight required:** Cannot fully automate patient care due to liability issues
- **🩺 Nurse involvement essential:** Solutions must support, not replace, nursing staff

**💻 Technology Opportunities:**
- Current hospital software is outdated and inefficient
- Staff typically carry tablets or smartphones daily
- Potential for mobile apps to help manage patients on the same floor

## Building the Prototype

The following sections provide an overview of the process of building the bAIRiatric Supports prototype, including the initial design, final design, materials used, and the development of both physical and digital prototypes.

### What is the hospital looking for?
The Grand River Hospital is looking for innovative solutions to improve mobility aids for bariatric patients and those 
with or at risk for skin injury.

They seek solutions that:
- **🛡️ Protect Delicate Skin**: Reduce friction, minimize shear forces, and offer advanced cushioning.
- **💪 Support Bariatric Patients**: Provide higher weight capacity and ergonomic, stable designs.
- **👩‍⚕️ Enhance Caregiver Safety**: Reduce strain with powered mechanisms or adjustable supports.
- **♻️ Ensure Durability and Sustainability**: Use materials that are long-lasting, easy to clean, and eco-friendly.
- **📋 Standardize Care Products**: Align with evidence-based guidelines for consistent care quality.
- **💰 Improve Cost-Effectiveness**: Deliver scalable, affordable solutions that lower long-term costs.

#### Guidelines for Solutions
- Propose innovative mobility aids, care products, or workflows that prioritize safety, comfort, and usability.
- Solutions should balance sustainability, efficiency, and adaptability across care settings.
- Creative approaches leveraging technology or advanced materials are highly encouraged.

### Physical Inflatable Prototype

The physical prototype of the bAIRiatric Supports is designed to mimic the inflatable positioning aid that can be used to help patients with fragile skin.

The prototype is a 3D-printed simplified model of the final design, allowing for demonstration of the product's functionality and user experience.
- The inflatable components are represented with microservo motors that raise the left and right sections of the bed.
- The **3D-printed** bed was created in **SolidWorks**, and printed on my Kingroon KP3S 3D printer.

{{< slideshow >}}
  {{< slide src="/img/bAIRiatric-Supports/physical-prototype1.jpg" caption="Front View" >}}
  {{< slide src="/img/bAIRiatric-Supports/physical-prototype2.jpg" caption="Side View" >}}
{{< /slideshow >}}

The microservo motors are controlled by an **Arduino IoT 33 microcontroller**, which is connected wirelessly through WiFi to the host system that manages the web app that the nurses and caregivers handle.

### Digital Web App + Mobile Prototype

The digital prototype consists of a web application that allows nurses and caregivers to control the inflatable positioning aids from their devices. The idea is that nurses or caregivers manage a room full of patients using a centralized interface.

<!-- Slideshow of the app interface -->
{{< slideshow >}}
  {{< slide src="/img/bAIRiatric-Supports/mobile-interface.jpg" caption="Mobile Interface" >}}
  {{< slide src="/img/bAIRiatric-Supports/mobile-interface2.jpg" caption="Login Page" >}}
{{< /slideshow >}}

The tech stack for the digital prototype includes:
- **Frontend**: <i class="devicon-bootstrap-plain colored tech-stack-icon"></i> <u>Bootstrap</u> for building a cohesive and responsive UI.
- **Backend**: <i class="devicon-flask-original colored tech-stack-icon"></i> <u>Flask</u> for handling HTTP requests and managing the communication between the web app and the microcontroller.
- **Database**: <i class="devicon-sqlite-plain colored tech-stack-icon"></i> <u>SQLite</u> for lightweight and local data storage. No need for centralized database management.

## First Pitch
- Of the ~50 other groups participating in the innovation challenge, our team received positive feedback and moved on within the top 8 finalists.

![finalist email](/img/bAIRiatric-Supports/finalists.jpg)

## Final Pitch

> Scroll back to the top of this page to watch the final pitch presentation! 

We had so much fun presenting our project, staying up at E7 until 3 AM, and even going to Walmart and the Dollar Store to try to find materials foor our project. Overall such a fun experience.

<!-- Slideshow of final pitch pics -->
{{< slideshow >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch1.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch2.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch3.jpg" >}} 
  {{< slide src="/img/bAIRiatric-Supports/final-pitch4.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch5.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch6.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch7.jpg" >}}
  {{< slide src="/img/bAIRiatric-Supports/final-pitch8.jpg" content="Judging Panel">}}
{{< /slideshow >}}

Could not have done it without this team:

![team photo](/img/bAIRiatric-Supports/team.jpg)

- [Sima Alekberova](https://www.linkedin.com/in/sima-alekberova-823109302/), Biochemistry
- [Astrid Stinson](https://www.linkedin.com/in/astrid-stinson/), Nanotechnology Engineering
- [Michael Chan](https://www.linkedin.com/in/michaelchanwh8/), Biomedical Engineering
- [Sukie Liu](https://www.linkedin.com/in/sukie-liu-9a05b81b0/), Kinesiology



