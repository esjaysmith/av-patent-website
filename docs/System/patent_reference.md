# Patent Portfolio Technical Reference

## Portfolio Overview

This document serves as the internal technical reference for the autonomous vehicle patent portfolio, comprising two granted US patents:

| Patent | Grant Date | Claims | Status |
|--------|-----------|--------|--------|
| US 12,001,207 B2 | June 4, 2024 | 13 | Active |
| US 12,530,030 B2 | January 20, 2026 | 20 | Active |

Both patents share the same title, inventors, and core technology. US 12,530,030 is a continuation of US 12,001,207 with expanded claims covering the clear-passage-determining module and three distinct claim types (method, computer program product, system).

---

## US Patent 12,001,207 B2

### Patent Overview

**Patent Number:** US12001207B2
**Title:** System for controlling an autonomous driving vehicle or air vessel, which can be controlled on the basis of steering and acceleration values, and an autonomous driving vehicle or air vessel provided with such a system

**Inventors:**
- Stephan Johannes Smit
- Johannes Wilhelmus Maria VAN BENTUM

**Current Assignee:** Individual

**Key Dates:**
- **Priority Date:** August 9, 2019
- **Filing Date:** August 7, 2020
- **Publication Date (Pre-grant):** February 11, 2021 (US20210041872A1)
- **Grant Date:** June 4, 2024
- **Expiration Date:** March 5, 2041

**Application No:** 16/987,612

**Legal Status:** Active

**Patent Classification:**
- Prior art keywords: module, value, determining, navigational, vehicle

### Abstract

System for controlling an autonomous vehicle on the basis of control values and acceleration values, having a safety-determining module configured to receive live images from a camera, to receive recorded stored images preprocessed for image recognition from an internal safety-determining module data storage, to receive navigation instruction(s) from a navigation module; to compare the live images with the stored images to determine a degree of correspondence; and to determine a safety value which indicates the extent to which the determined degree of correspondence suffices to execute the navigation instruction(s); wherein a control module is configured to receive the navigation instruction(s); to receive the live images; to receive the safety value; to compare the safety value to a predetermined value; and if the safety value is greater than the predetermined value, to convert the navigation instruction(s) and the camera images into control values and acceleration values for the autonomous vehicle.

### Technical Innovation

#### Core Technology

The patent describes a **dual-module safety system** for autonomous vehicles and aircraft that combines:

1. **Safety-Determining Module:**
   - Receives live camera images from the vehicle
   - Compares live images with preprocessed stored images from internal data storage
   - Receives navigation instructions from a navigation module
   - Determines a "degree of correspondence" between live and stored images
   - Calculates a safety value indicating whether navigation instructions can be safely executed

2. **Control Module:**
   - Receives navigation instructions
   - Receives live camera images
   - Receives the safety value from the safety-determining module
   - Compares safety value to a predetermined threshold
   - Only converts navigation instructions into control/acceleration values if safety value exceeds threshold

#### Key Innovation: Navigation Point Recognition

The system uses **navigation points** that can be visually recognized from camera images, enabling:
- High-level navigation instructions (e.g., "turn left at the second turn-off")
- Route following based on visual recognition rather than precise GPS coordinates
- Autonomous navigation without requiring exact location data beforehand

#### Training Method

The patent includes a training methodology:
1. **A.** Move the vehicle over an intended autonomous route with a human driver
2. **B.** Record camera images of the route while moving
3. **C.** Store navigation points in relation to the camera images
4. **D.** Annotate navigation points with coordinates for the navigation module

Alternative: Training can occur entirely in simulation using real-world images from other routes.

### Applications

#### Primary Applications
1. **Autonomous Vehicles:**
   - Self-driving cars
   - Autonomous delivery vehicles
   - Ground-based autonomous systems

2. **Aerial Vehicles (Air Vessels):**
   - Drones
   - Autonomous aircraft
   - UAVs (Unmanned Aerial Vehicles)

3. **Other Autonomous Systems:**
   - Maritime vessels (mentioned in specification)
   - Any controllable autonomously moving vehicle or craft

#### Industry Relevance

**Autonomous Vehicle Industry:**
- Tesla FSD (Full Self-Driving)
- Waymo
- Cruise
- Aurora
- Other AV manufacturers

**Drone/UAV Industry:**
- Delivery drones (Amazon, Wing)
- Agricultural drones
- Inspection drones
- Commercial UAV operators

**Navigation Technology:**
- Companies developing visual-based navigation
- AI navigation systems
- Computer vision for autonomous systems

### Technical Architecture

#### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Camera System                             │
│              (Live Image Capture)                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│              Safety-Determining Module                       │
│                                                              │
│  • Receives live images                                     │
│  • Accesses stored preprocessed images                      │
│  • Receives navigation instructions                         │
│  • Compares images (degree of correspondence)              │
│  • Calculates safety value                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │ safety value
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   Control Module                             │
│                                                              │
│  • Receives navigation instructions                         │
│  • Receives live images                                     │
│  • Receives safety value                                    │
│  • Compares to predetermined threshold                      │
│  • Converts to control/acceleration values (if safe)        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│              Vehicle/Craft Control System                    │
│         (Steering and Acceleration Implementation)           │
└─────────────────────────────────────────────────────────────┘
```

#### Data Flows

1. **Training Phase:**
   - Driver operates vehicle on intended route
   - Camera records images continuously
   - Navigation points are identified and stored
   - Images are preprocessed for image recognition
   - Coordinates are annotated

2. **Autonomous Operation:**
   - Camera captures live images
   - Navigation module provides high-level instructions
   - Safety module compares live vs. stored images
   - Safety value calculated based on correspondence
   - If safe, control module executes navigation instructions
   - Vehicle steering and acceleration adjusted accordingly

### Claims Overview

**Total Claims:** 13

The patent includes multiple independent and dependent claims covering:
- System architecture (safety module + control module)
- Safety value determination methods
- Image comparison techniques
- Navigation point recognition
- Training methods
- Vehicle and aircraft applications

**Key Claim Elements:**
1. Safety-determining module with specific capabilities
2. Control module with conditional execution logic
3. Degree of correspondence calculation
4. Safety value threshold comparison
5. Navigation instruction abstraction
6. Stored image preprocessing for recognition

---

## US Patent 12,530,030 B2

### Patent Overview

**Patent Number:** US 12,530,030 B2
**Title:** System for controlling an autonomous driving vehicle or air vessel, which can be controlled on the basis of steering and acceleration values, and an autonomous driving vehicle or air vessel provided with such a system

**Inventors:**
- Stephan Johannes Smit
- Johannes Wilhelmus Maria Van Bentum

**Current Assignee:** Individual

**Key Dates:**
- **Priority Date:** August 9, 2019
- **Filing Date:** February 5, 2024
- **Publication Date (Pre-grant):** May 30, 2024 (US 2024/0176345 A1)
- **Grant Date:** January 20, 2026
- **Expiration Date:** March 5, 2041
- **Application No:** 18/432,397

**Relationship to Parent:** Continuation of application No. 16/987,612 (now US 12,001,207 B2)
**Terminal Disclaimer:** Subject to terminal disclaimer

**Legal Status:** Active

### Abstract

System for controlling an autonomous vehicle on the basis of control values and acceleration values, having a safety-determining module configured to receive live images from a camera, to receive recorded stored images preprocessed for image recognition from an internal safety-determining module data storage, to receive navigation instruction(s) from a navigation module; to compare the live images with the stored images to determine a degree of correspondence; and to determine a safety value which indicates the extent to which the determined degree of correspondence suffices to execute the navigation instruction(s); wherein a control module is configured to receive the navigation instruction(s); to receive the live images; to receive the safety value; to compare the safety value to a predetermined value; and if the safety value is greater than the predetermined value, to convert the navigation instruction(s) and the camera images into control values and acceleration values for the autonomous vehicle.

### Technical Innovation — What's New vs. Original

The continuation patent expands claim coverage in several key areas beyond the original US 12,001,207:

1. **Clear-Passage-Determining Module (Claims 7-11):**
   - Receives live camera images from the camera
   - Receives navigation instructions from the navigation module
   - Compares live images against stored annotated images with clear-passage values
   - Determines whether a navigation instruction can be executed (e.g., yielding to traffic with right-of-way)
   - If instruction cannot be executed, obtains new live images and re-evaluates
   - Outputs a clear-passage-safety value indicating degree of certainty

2. **Three Distinct Claim Types:**
   - **Method claims (1-15):** Computer-implemented method for the full vehicle control loop
   - **Computer program product claims (16-18):** Software implementation on non-transitory storage media
   - **System claims (19-20):** Physical system with all hardware and software modules

3. **Expanded Claim Detail:**
   - Explicit update/feedback loop: stored images are updated with acceleration values after execution
   - Confirmation step: analyzing post-execution camera images to verify navigational point reached
   - Control frequency requirements (Claims 12): at least 2 Hz for control, at least 10 Hz for acceleration
   - Deep learning via network topology (Claim 13): accessing a network topology for converting navigational instructions into directional and acceleration values
   - Vehicle type coverage (Claim 14): explicitly covers land-based vehicles and aircraft

### Claims Overview

**Total Claims:** 20

#### Method Claims (1-15)

**Independent Claim 1** defines a computer-implemented method comprising the full autonomous vehicle control loop:
- Obtaining and storing camera images
- Obtaining control/acceleration values for navigational instructions via safety value assessment
- Safety value threshold comparison with two branches (autonomous conversion vs. requesting external input)
- Updating stored images with acceleration values (feedback loop)
- Controlling the vehicle based on obtained values
- Confirming execution by analyzing post-control camera images

**Key Dependent Claims:**
- **Claim 2:** Annotating stored images with navigation point positions
- **Claims 3-4:** Route generation from current location to destination (finite destination list)
- **Claim 5:** Stop/park behavior when safety value insufficient
- **Claim 6:** Recognition point-based image comparison
- **Claims 7-11:** Clear-passage annotation and determination chain:
  - Claim 7: Annotating images with clear-passage values
  - Claim 8: Pre-execution clear-passage check
  - Claim 9: Comparing live images against stored annotated images for clear-passage
  - Claim 10: Re-evaluation loop when instruction cannot be executed
  - Claim 11: Clear-passage-safety value quantification
- **Claim 12:** Control frequency (at least 2 Hz control, at least 10 Hz acceleration)
- **Claim 13:** Deep learning via network topology for directional/acceleration conversion
- **Claim 14:** Vehicle types (land-based vehicle and aircraft)
- **Claim 15:** Continuous image capture

#### Computer Program Product Claims (16-18)

**Independent Claim 16** mirrors Claim 1 as a computer program product on non-transitory computer readable storage media.

- **Claim 17:** Image annotation with navigation point positions (mirrors Claim 2)
- **Claim 18:** Route generation and conversion (mirrors Claims 3-4)

#### System Claims (19-20)

**Independent Claim 19** defines a physical system comprising: navigation module, control module, camera, recognition module, safety-determining module, communication module, memory, and processors. The method performed mirrors Claim 1.

- **Claim 20:** Route generation and conversion (mirrors Claims 3-4)

### Classifications

**International Classification:**
- B60W60/00, B60W30/06, G01C21/34, G01C21/36, G05D1/00, G05D1/243, G05D1/246, G05D1/249, G05D1/46, G05D1/81, G08G5/32, G08G5/50, G08G5/55

**U.S. Classification (CPC):**
- G05D1/0088, B60W30/06, B60W60/0015, G01C21/3407, G01C21/3602, G05D1/0246, G05D1/0251, G05D1/0274, G05D1/101, G05D1/2435, G05D1/246, G05D1/249, G05D1/46, G05D1/81, G08G5/32, G08G5/50, G08G5/55, B60W2420/403, B60W2520/00

---

## Competitive Landscape

### Related Patents & Prior Art

The patents reference multiple prior art patents, including:
- US 9,151,626 - Related autonomous vehicle systems
- US 11,222,299 - Related navigation technology
- Various 2015-2022 patent applications in autonomous navigation

**European Patent Office Search Report:** Conducted April 23, 2020 for NL 2023628

### Differentiation

**Unique aspects of the patent portfolio:**
1. **Dual-module safety architecture** separating safety determination from control
2. **Visual navigation point recognition** for high-level navigation instructions
3. **Safety value threshold system** for decision-making
4. **Preprocessed image storage** for efficient comparison
5. **Applicability to both ground and air vehicles**
6. **Clear-passage-determining module** for yielding to right-of-way traffic (continuation)
7. **Three claim types** (method, CPP, system) providing broad enforcement coverage (continuation)

## Licensing Opportunities

### Target Companies

**Tier 1: Major AV Players**
- Tesla, Waymo, Cruise, Aurora
- Traditional automakers with AV programs (GM, Ford, VW, etc.)

**Tier 2: Drone/UAV Manufacturers**
- DJI, Parrot, Skydio
- Amazon (Prime Air), Wing (Alphabet)
- Agricultural drone companies

**Tier 3: Navigation Technology Providers**
- Mobileye (Intel)
- NVIDIA (DRIVE platform)
- Qualcomm (Snapdragon Ride)

**Tier 4: Startups & Emerging Players**
- Autonomous delivery startups
- Agricultural robotics companies
- Industrial automation companies

### Value Proposition

**For Licensees:**
1. **Patent Protection:** Defensive IP position against litigation
2. **Technology Access:** Proven safety-determining architecture
3. **Market Differentiation:** Visual navigation point technology
4. **Reduced R&D Costs:** Leverage patented system design
5. **Regulatory Compliance:** Safety-focused architecture aids certification

**Market Timing:**
- Original patent granted June 2024, continuation granted January 2026
- 17-year term until 2041
- AV industry scaling rapidly (2024-2030)
- Regulatory frameworks maturing globally

## Related Documentation

### Internal References
- **Full Original Patent HTML:** `docs/US12001207B2.html` (3,689 lines)
- **Continuation Patent Markdown:** `docs/US_Patent_12530030.md`
- **Patent PDFs:** Available at Google Patents

### Website Content References
- **Original Patent Details Page:** `/website/content/patent-details.md`
- **Continuation Patent Details Page:** `/website/content/patent-details-continuation.md`
- **Licensing Page:** `/website/content/licensing.md`
- **Industry Insights:** `/website/content/industry-insights.md`

### External Links

**US 12,001,207 B2:**
- **Google Patents:** https://patents.google.com/patent/US12001207B2/en
- **USPTO PatentCenter:** https://patentcenter.uspto.gov/applications/16987612
- **Espacenet:** https://worldwide.espacenet.com/publicationDetails/biblio?CC=US&NR=12001207B2&KC=B2&FT=D

**US 12,530,030 B2:**
- **Google Patents:** https://patents.google.com/patent/US12530030B2
- **USPTO PatentCenter:** https://patentcenter.uspto.gov/applications/18432397

## Content Development Guidelines

### When Creating Content About These Patents

**MANDATORY Requirements (per content_quality_assurance.md):**

1. **Source Hierarchy:**
   - PRIMARY: Official patent documents (US12001207B2.html, US_Patent_12530030.md)
   - SECONDARY: USPTO records, EPO records
   - TERTIARY: Industry analysis from reputable sources

2. **Fact-Checking Protocol:**
   - All technical claims must reference patent document
   - All dates must be verified against USPTO records
   - All company names/applications must be current and accurate
   - Industry claims require multiple independent sources

3. **Verification Tags:**
   - Use `[VERIFY]` tags for all factual claims in draft content
   - Launch multi-agent fact-checking for any new content
   - Document verification in fact-check logs

4. **Prohibited:**
   - Do NOT exaggerate patent scope or applications
   - Do NOT make unsupported licensing value claims
   - Do NOT claim partnerships or implementations that don't exist
   - Do NOT misrepresent technical capabilities

### Recommended Content Topics

**Technical Deep-Dives:**
1. Visual navigation point recognition explained
2. Safety value calculation methodology
3. Comparison with GPS-based systems
4. Training methodology for autonomous systems
5. Clear-passage determination and right-of-way handling

**Industry Analysis:**
1. Patent relevance to Tesla FSD architecture
2. Drone delivery safety requirements
3. Regulatory landscape for autonomous vehicles
4. IP strategy for AV startups

**Business/Licensing:**
1. Patent portfolio expansion for inventors
2. Defensive vs. offensive patent strategies
3. Licensing models for autonomous technology
4. Patent valuation in AV industry

## Maintenance & Updates

### Regular Review Schedule
- **Quarterly:** Check USPTO records for any legal status changes
- **Semi-Annual:** Review industry developments and potential infringement
- **Annual:** Update competitive landscape and licensing opportunities

### Key Monitoring Points
1. Patent legal status (active, maintenance fees) for both patents
2. Related patent applications or continuations — US 12,530,030 B2 has been granted as of January 20, 2026
3. Industry developments in visual navigation
4. Potential infringement by major AV players
5. Licensing inquiries and negotiations

### Documentation Updates
When updating this document:
- Note the date of update
- Reference specific sources for new information
- Update related website content accordingly
- Follow content quality assurance protocols

---

**Document Version:** 2.0
**Created:** October 14, 2025
**Last Updated:** March 5, 2026
**Sources:**
- US Patent 12,001,207 B2 (Full HTML document in `docs/US12001207B2.html`)
- US Patent 12,530,030 B2 (Full text in `docs/US_Patent_12530030.md`)
**Next Review:** June 5, 2026
