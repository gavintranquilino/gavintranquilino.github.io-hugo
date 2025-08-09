---
title: "This is <strong>bAIRiatric Supports</strong>"
date: "2025-02-10"
imageUrl: "/img/bAIRiatric-Supports/thumbnail.jpg"
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

> This page is a WORK IN PROGRESS

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

**Key Insights:**
- Emphasized the importance of **modular, scalable designs** for hospital environments
- Avoid reinventing complex specialized equipment (lifts, beds) that already exists
- Focus on **simple, cost-effective solutions** that set us apart from existing designs
- Traditional equipment requires intrusive installation and takes up significant space
- **Integration is key:** Solutions must easily fit into existing hospital workflows without disruption

## Speaking with the Nurses
**Interview Focus:** Understanding challenges and needs when caring for patients with fragile skin at Grand River Hospital

**Key Challenges Identified:**
- **Physical demands:** Moving patients is extremely taxing with limited resources
- **Patient tracking:** Difficult to locate patients who move frequently around the hospital
- **Communication gaps:** Staff must constantly brief each other on patient status and care plans
- **Privacy concerns:** Storing patient information poses additional privacy risks

**Important Constraints:**
- **Regulatory compliance:** Must maintain existing patient movement protocols and rolling techniques
- **Human oversight required:** Cannot fully automate patient care due to liability issues
- **Nurse involvement essential:** Solutions must support, not replace, nursing staff

**Technology Opportunities:**
- Current hospital software is outdated and inefficient
- Staff typically carry tablets or smartphones daily
- Potential for mobile apps to help manage patients on the same floor

## Building the Prototype

The following sections provide an overview of the process of building the bAIRiatric Supports prototype, including the initial design, final design, materials used, and the development of both physical and digital prototypes.

### What is the hospital looking for?
The Grand River Hospital is looking for innovative solutions to improve mobility aids for bariatric patients and those 
with or at risk for skin injury.

They seek solutions that:
- **Protect Delicate Skin**: Reduce friction, minimize shear forces, and offer advanced cushioning.
- **Support Bariatric Patients**: Provide higher weight capacity and ergonomic, stable designs.
- **Enhance Caregiver Safety**: Reduce strain with powered mechanisms or adjustable supports.
- **Ensure Durability and Sustainability**: Use materials that are long-lasting, easy to clean, and eco-friendly.
- **Standardize Care Products**: Align with evidence-based guidelines for consistent care quality.
- **Improve Cost-Effectiveness**: Deliver scalable, affordable solutions that lower long-term costs.

#### Guidelines for Solutions
- Propose innovative mobility aids, care products, or workflows that prioritize safety, comfort, and usability.
- Solutions should balance sustainability, efficiency, and adaptability across care settings.
- Creative approaches leveraging technology or advanced materials are highly encouraged.

### Physical Inflatable Prototype

The physical prototype of the bAIRiatric Supports is designed to mimic the inflatable positioning aid that can be used to help patients with fragile skin. The prototype is made from a combination of materials that are both durable and comfortable for the patient.

### Digital Web-app + Mobile Prototype

### Failed Ideas

### Future Directions

## First Pitch

## Final Pitch

<!-- {{< slideshow >}}
  {{< slide src="/img/TFP3D/smol_tfp_side.png" caption="Front View" >}}
  {{< slide src="/img/TFP3D/TFPthicc.png" caption="Back View" >}}
{{< /slideshow >}} -->
