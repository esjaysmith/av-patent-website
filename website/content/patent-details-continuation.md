---
title: "US Patent 12,530,030: Continuation Patent Technical Details"
description: "Technical overview of US Patent 12,530,030, a continuation patent covering camera-based navigation safety with clear-passage-determining module for autonomous vehicles and drones."
keywords: "US patent 12530030, continuation patent, clear-passage-determining module, autonomous vehicle patent, camera-based navigation, patent portfolio"
page_title: "US Patent 12,530,030: Continuation Patent"
show_cta: true
og_title: "US Patent 12,530,030: Continuation Patent Technical Details"
og_description: "Technical overview of US Patent 12,530,030 covering camera-based navigation safety with clear-passage-determining module for autonomous vehicles and drones."
og_type: "article"
og_image: "/assets/images/og-technical-legal.jpg"
twitter_card: "summary_large_image"
twitter_title: "US Patent 12,530,030: Continuation Patent Technical Details"
twitter_description: "Technical overview of US Patent 12,530,030 covering camera-based navigation safety with clear-passage-determining module for autonomous vehicles and drones."
twitter_image: "/assets/images/og-technical-legal.jpg"
date_published: "2026-03-05"
date_modified: "2026-03-05"
---

# US Patent 12,530,030: Camera-based navigation safety with clear-passage determination

- **Patent Number:** US 12,530,030 B2 — **[View Full Patent on Google Patents →](https://patents.google.com/patent/US12530030B2)**
- **Issue Date:** January 20, 2026
- **Filing Date:** February 5, 2024
- **Expiration:** March 5, 2041 (terminal disclaimer)
- **Application No.:** 18/432,397
- **Relationship:** Continuation of US 12,001,207 (application 16/987,612, filed August 7, 2020)
- **Technology:** Dual-module camera-based navigation safety system with clear-passage determination
- **Assignee:** Individual (self-owned)
- **Inventors:** Stephan Johannes Smit, Johannes Wilhelmus Maria Van Bentum
- **Technology Classification:** G05D1/0088 (Autonomous decision-making), B60W60/001 (Autonomous road vehicle planning), G01C21/34 (Route guidance)

## Patent abstract

System for controlling an autonomous vehicle on the basis of control values and acceleration values, having a safety-determining module configured to receive live images from a camera, to receive recorded stored images preprocessed for image recognition from an internal safety-determining module data storage, to receive navigation instruction(s) from a navigation module; to compare the live images with the stored images to determine a degree of correspondence; and to determine a safety value which indicates the extent to which the determined degree of correspondence suffices to execute the navigation instruction(s); wherein a control module is configured to receive the navigation instruction(s); to receive the live images; to receive the safety value; to compare the safety value to a predetermined value; and if the safety value is greater than the predetermined value, to convert the navigation instruction(s) and the camera images into control values and acceleration values for the autonomous vehicle.

*For complete legal text and detailed claims, refer to official USPTO records.*

## Relationship to the original patent

US 12,530,030 is a continuation of US 12,001,207. Both patents share the same specification and describe the same underlying technology. The continuation was filed to obtain additional claims that cover the invention from different angles.

A terminal disclaimer ties the two patents together. Both expire on March 5, 2041 regardless of their individual filing dates, and they must share the same ownership throughout their lifetimes.

The original patent was granted on June 4, 2024 with 13 system-type claims. This continuation was granted on January 20, 2026 with 20 claims spanning method, software, and system claim types.

## The clear-passage-determining module

This is the main new element in the continuation claims. The module was described in the shared specification all along, but the original patent did not claim it directly. Claims 7 through 11 of US 12,530,030 now do.

Here is what the module does:

It receives live camera images from the vehicle's camera and navigation instructions from the navigation module (for example, "turn left at the next junction"). It maintains an internal store of recorded camera images, each annotated with navigation instructions and clear-passage values, preprocessed for image recognition. When a navigation instruction comes in, the module compares the current live images against those stored annotated images to decide whether traffic conditions actually allow the instruction to be carried out.

The specification gives a concrete example. Say the instruction is "turn left at the next junction," but there is oncoming traffic with right of way. During training, the system watched an operator wait in this situation rather than turn. It learned to associate that visual pattern (oncoming vehicles at a left turn) with "do not proceed." In autonomous operation, the module holds the turn instruction until new live images show the way is clear.

If the module decides the instruction cannot be executed yet, the system grabs fresh live images and checks again. This loop repeats until conditions allow the vehicle to proceed.

## Claims overview

US 12,530,030 has 20 claims in three groups.

### Method claims (1-15)

Claim 1 is the broadest independent method claim. It covers the full computer-implemented control loop: obtaining camera images, computing a safety value by comparing live images to stored reference images, checking that value against a threshold, either executing the navigation instruction autonomously or requesting human-provided control values, updating stored images with new data, and confirming execution by visually recognizing that the vehicle reached its target navigation point.

The dependent method claims add specifics:

- Claim 2: Image annotation with navigation point positions
- Claims 3-4: Route generation from current location to destination; destinations selected from a finite list
- Claim 5: Stopping or parking the vehicle when the safety value falls below threshold
- Claim 6: Recognition point comparison (matching extracted features rather than full images)
- Claims 7-11: Clear-passage annotation and determination, including annotating stored images with clear-passage values, checking whether a navigation instruction can be executed before proceeding, comparing live images against annotated stored images, re-checking with new images when execution is blocked, and computing a clear-passage-safety value
- Claim 12: Control frequency requirements (at least 2 Hz for control values, at least 10 Hz for acceleration values)
- Claim 13: Deep learning via network topology for converting navigation instructions into directional and acceleration values
- Claim 14: Vehicle types (land-based vehicles and aircraft)
- Claim 15: Continuous image capture from the camera

### Computer program product claims (16-18)

Claim 16 covers the same method as Claim 1, but as software stored on non-transitory computer readable storage media. This protects the technology when it is delivered as software, independent of any particular hardware.

- Claim 17: Adds image annotation (parallels Claim 2)
- Claim 18: Adds route generation (parallels Claims 3-4)

### System claims (19-20)

Claim 19 is a physical system: navigation module, control module, camera, recognition module, safety-determining module, communication module, memory, and processors, all configured to perform the method of Claim 1.

- Claim 20: Adds route generation (parallels Claims 3-4)

## What changed from the original patent

The original patent (US 12,001,207) has 13 claims, all system-type. This continuation has 20 claims across three types: method, computer program product, and system.

The clear-passage-determining module is now explicitly claimed (Claims 7-11) rather than just described in the specification.

The practical effect is broader protection. The original patent covered the system as built. The continuation also covers the method of using it and the software that runs it. That makes it harder to design around any single claim type.

## Further information

For the original patent and full portfolio details, see the [patent portfolio overview](/patent-details.html).

For licensing inquiries, visit our [licensing page](/licensing.html) or [contact us](/contact.html) directly.

---
