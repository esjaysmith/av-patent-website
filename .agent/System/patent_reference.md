# US Patent 12,001,207 B2 - Technical Reference

## Patent Overview

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

**Legal Status:** Active

**Patent Classification:**
- Prior art keywords: module, value, determining, navigational, vehicle

## Abstract

System for controlling an autonomous vehicle on the basis of control values and acceleration values, having a safety-determining module configured to receive live images from a camera, to receive recorded stored images preprocessed for image recognition from an internal safety-determining module data storage, to receive navigation instruction(s) from a navigation module; to compare the live images with the stored images to determine a degree of correspondence; and to determine a safety value which indicates the extent to which the determined degree of correspondence suffices to execute the navigation instruction(s); wherein a control module is configured to receive the navigation instruction(s); to receive the live images; to receive the safety value; to compare the safety value to a predetermined value; and if the safety value is greater than the predetermined value, to convert the navigation instruction(s) and the camera images into control values and acceleration values for the autonomous vehicle.

## Technical Innovation

### Core Technology

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

### Key Innovation: Navigation Point Recognition

The system uses **navigation points** that can be visually recognized from camera images, enabling:
- High-level navigation instructions (e.g., "turn left at the second turn-off")
- Route following based on visual recognition rather than precise GPS coordinates
- Autonomous navigation without requiring exact location data beforehand

### Training Method

The patent includes a training methodology:
1. **A.** Move the vehicle over an intended autonomous route with a human driver
2. **B.** Record camera images of the route while moving
3. **C.** Store navigation points in relation to the camera images
4. **D.** Annotate navigation points with coordinates for the navigation module

Alternative: Training can occur entirely in simulation using real-world images from other routes.

## Applications

### Primary Applications
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

### Industry Relevance

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

## Technical Architecture

### System Components

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

### Data Flows

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

## Competitive Landscape

### Related Patents & Prior Art

The patent references multiple prior art patents, including:
- US 9,151,626 - Related autonomous vehicle systems
- US 11,222,299 - Related navigation technology
- Various 2015-2022 patent applications in autonomous navigation

**European Patent Office Search Report:** Conducted April 23, 2020 for NL 2023628

### Differentiation

**Unique aspects of US12001207B2:**
1. **Dual-module safety architecture** separating safety determination from control
2. **Visual navigation point recognition** for high-level navigation instructions
3. **Safety value threshold system** for decision-making
4. **Preprocessed image storage** for efficient comparison
5. **Applicability to both ground and air vehicles**

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
- Patent granted June 2024 (recent)
- 17-year term until 2041
- AV industry scaling rapidly (2024-2030)
- Regulatory frameworks maturing globally

## Technical Claims Overview

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

## Related Documentation

### Internal References
- **Full Patent HTML:** `.agent/US12001207B2.html` (3,689 lines)
- **Patent PDF:** Available at Google Patents
- **USPTO Link:** https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=12001207.PN.

### Website Content References
- **Patent Details Page:** `/website/content/patent-details.md`
- **Licensing Page:** `/website/content/licensing.md`
- **Industry Insights:** `/website/content/industry-insights.md`

### External Links
- **Google Patents:** https://patents.google.com/patent/US12001207B2/en
- **USPTO PatentCenter:** https://patentcenter.uspto.gov/applications/16987612
- **Espacenet:** https://worldwide.espacenet.com/publicationDetails/biblio?CC=US&NR=12001207B2&KC=B2&FT=D

## Content Development Guidelines

### When Creating Content About This Patent

**MANDATORY Requirements (per content_quality_assurance.md):**

1. **Source Hierarchy:**
   - PRIMARY: Official patent document (US12001207B2.html)
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
1. Patent legal status (active, maintenance fees)
2. Related patent applications or continuations
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

**Document Version:** 1.0
**Created:** October 14, 2025
**Last Updated:** October 14, 2025
**Source:** US Patent 12,001,207 B2 (Full HTML document in `.agent/US12001207B2.html`)
**Next Review:** January 14, 2026
