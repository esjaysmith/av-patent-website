# Standard Operating Procedure: Content Quality Assurance & Fact-Checking

## ⚠️ CRITICAL: This SOP is MANDATORY for ALL Content

This document defines the **non-negotiable** fact-checking and quality assurance process for the AV Navigation IP Protection Website. **Every piece of content**—homepage, landing pages, core pages, blog posts—must pass through this verification process before publication.

## The Scale Challenge: Quantity + Quality

### Project Scope
- **Current**: 6 core pages (Phase 1 & 2 complete)
- **Future**: **Tens of landing pages** (Phase 3+)
- **Challenge**: Maintain 100% factual accuracy while scaling content

### Why This Matters
- **Legal Risk**: Incorrect patent information could create liability
- **Credibility**: Factual errors damage trust with potential licensees
- **SEO Risk**: Search engines penalize misinformation
- **Professional Reputation**: Errors reflect poorly on patent holder

## Multi-Agent Fact-Checking Protocol

### Overview

**EVERY content piece** must be verified by **minimum 3 specialized AI agents** running in parallel:

1. **Patent Facts Verification Agent**
2. **Industry & Market Claims Agent**
3. **Current Events & Quotes Agent**

### Agent Launch Procedure

#### When to Launch Agents
- ✅ **BEFORE** publishing any new content
- ✅ **BEFORE** editing existing content (if factual claims change)
- ✅ **BEFORE** updating current event references
- ✅ **ANY TIME** factual accuracy is in question

#### How to Launch Agents

Use Claude Code's Task tool to spin up parallel fact-checking agents:

```
Task 1: Patent Facts Verification
Prompt: "You are a fact-checking agent specializing in patent information.
Review the following content and verify EVERY patent-related claim.

⚠️ CRITICAL FIRST STEP - READ PATENT DOCUMENTATION FROM DISK:
Before verifying any claims, you MUST read these files from the local .agent directory:
1. Read file: .agent/System/patent_reference.md (comprehensive patent technical reference)
2. Read file: .agent/US12001207B2.html (official patent document - use offset/limit for specific sections)

These files contain the authoritative source material for all patent claims. Your verification
MUST be based on the content of these local files as the primary source.

Content to Verify:
[PASTE CONTENT HERE]

Verify:
1. Patent number (US 12,001,207 B2)
2. Issue date (June 4, 2024)
3. Expiration date (March 5, 2041)
4. Continuation application status (18/432,397)
5. Patent claims and technical specifications
6. Inventors (Stephan Johannes Smit, Johannes Wilhelmus Maria VAN BENTUM)
7. Patent categories and classifications
8. Abstract and technical description accuracy

For EACH claim:
- Claim: [exact text]
- Verification: [verified/unverified/incorrect]
- Source: [.agent/System/patent_reference.md line X OR .agent/US12001207B2.html section Y]
- Correction: [if incorrect]
- Confidence: [high/medium/low]

PRIMARY SOURCE: .agent/System/patent_reference.md and .agent/US12001207B2.html (local disk)
SECONDARY SOURCE: USPTO database online (if local files insufficient)

Flag ANY claims that don't match the local patent documentation."

---

Task 2: Industry & Market Claims Verification
Prompt: "You are a fact-checking agent specializing in autonomous vehicle
industry claims. Review the following content and verify EVERY industry/market claim:

Content:
[PASTE CONTENT HERE]

Verify:
1. Company names, products (Tesla FSD, etc.)
2. Market statistics and financial figures
3. Technology capabilities (E2E neural networks, camera systems)
4. Regulatory information
5. Industry trends and predictions
6. Competitive landscape claims

For EACH claim:
- Claim: [exact text]
- Verification: [verified/unverified/incorrect]
- Source: [official source URL]
- Correction: [if incorrect]
- Confidence: [high/medium/low]

Use official company announcements, reputable tech news, industry reports.
Flag ANY unverifiable claims."

---

Task 3: Current Events & Quotes Verification
Prompt: "You are a fact-checking agent specializing in dates, timelines,
quotes, and current events. Review the following content and verify EVERY
temporal claim and quote:

Content:
[PASTE CONTENT HERE]

Verify:
1. All dates (announcements, releases, milestones)
2. Event timelines (Tesla FSD rollout, etc.)
3. Quotes and attributions
4. News references and links
5. Report publication dates
6. Technology deployment dates

For EACH claim:
- Claim: [exact text]
- Verification: [verified/unverified/incorrect]
- Source: [primary source URL]
- Correction: [if incorrect]
- Confidence: [high/medium/low]

Check official announcements, press releases, reputable news sources.
Flag ANY unverifiable claims or incorrect attributions."
```

### ⚠️ CRITICAL: Avoiding Agent Duplication

**Problem:** Multiple agents may navigate to the same URL (YouTube video, website, etc.), consuming excessive tokens and context.

**Solution: Clear Division of Responsibilities**

**Agent 1: Patent & Academic References**
- **MANDATORY FIRST STEP**: Read .agent/System/patent_reference.md and .agent/US12001207B2.html from disk
- **PRIMARY FOCUS**: Patent documentation (local files), USPTO database, academic papers (arXiv, IEEE)
- **DO NOT**: Navigate to YouTube, test external URLs, check news sites
- **DEFERS TO**: Agent 3 for any URLs/videos, Agent 2 for market data

**Agent 2: Industry & Market Data**
- **PRIMARY FOCUS**: Market reports, company websites, analyst research
- **DO NOT**: Navigate to YouTube, check patent database, verify academic citations
- **DEFERS TO**: Agent 1 for patents/papers, Agent 3 for URLs/dates

**Agent 3: URLs, Dates & Media**
- **PRIMARY FOCUS**: ALL URL testing (YouTube, external links), dates, timelines
- **EXCLUSIVE RESPONSIBILITY**: Navigate to videos, test links, verify media
- **DO NOT**: Check USPTO database, verify market statistics, read academic papers
- **DEFERS TO**: Agent 1 for technical details, Agent 2 for industry claims

**Example Coordination:**
```
Agent 1 encounters: "Video available at youtube.com/watch?v=ABC"
Agent 1 response: "YouTube video link found - deferring to Agent 3 for verification"

Agent 2 encounters: "According to research paper (arxiv.org/abs/123)"
Agent 2 response: "Academic reference found - deferring to Agent 1 for paper verification"

Agent 3 encounters: "Market projected to reach $500B"
Agent 3 response: "Market statistic found - deferring to Agent 2 for source verification"
```

**Template Updates to Prevent Duplication:**

Update Agent 1 prompt to include:
```
CRITICAL FIRST STEP: Before starting verification, read these files from disk:
1. Read file: .agent/System/patent_reference.md
2. Read file: .agent/US12001207B2.html (use offset/limit for large sections)

Use these local files as your PRIMARY source for all patent verification.

IMPORTANT: If you encounter URLs to videos, websites, or external media,
note them but DO NOT navigate to them. These will be verified by Agent 3.
Simply note: "URL found - deferring to Agent 3"
```

Update Agent 2 prompt to include:
```
IMPORTANT: If you encounter academic paper citations or patent references,
note them but DO NOT verify them. These will be verified by Agent 1.
Simply note: "Academic/patent reference found - deferring to Agent 1"
```

Update Agent 3 prompt to include:
```
IMPORTANT: You are the ONLY agent that should navigate to URLs, test video
links, or access external media. Do NOT verify patent details or market
statistics - defer those to Agents 1 and 2 respectively.
```

### Agent Results Review Process

#### Step 1: Collect All Agent Reports
Wait for all 3 agents to complete. Review each report thoroughly.

#### Step 2: Categorize Findings
Sort findings into:
- ✅ **VERIFIED**: Confirmed by primary source (no action needed)
- ⚠️ **UNVERIFIED**: No primary source found (must remove or find source)
- ❌ **INCORRECT**: Factually wrong (must correct immediately)
- 🔍 **LOW CONFIDENCE**: Needs manual verification

#### Step 3: Take Action on Each Finding

**For VERIFIED claims:**
- Document source in fact-check log
- No content changes needed

**For UNVERIFIED claims:**
- **Option A**: Find primary source and re-verify
- **Option B**: Remove claim from content
- **Option C**: Rephrase as opinion/speculation (if appropriate)

**For INCORRECT claims:**
- Correct immediately with accurate information
- Document correction in fact-check log
- Re-run agent on corrected section

**For LOW CONFIDENCE:**
- Manually verify with primary sources
- If can't verify, treat as UNVERIFIED
- Document manual verification process

## Fact-Checking Stages

### Stage 1: Content Drafting with Verification Tags

While writing content, mark **every factual claim** for verification:

```markdown
US Patent [VERIFY: patent number] was issued on [VERIFY: issue date]
and covers [VERIFY: patent scope].

The autonomous vehicle market is projected to reach [VERIFY: market size]
by [VERIFY: year], according to [VERIFY: source].

Tesla announced [VERIFY: what announcement] on [VERIFY: date], marking
a significant shift toward [VERIFY: technology trend].

"[VERIFY: quote text]" said [VERIFY: attribution] in [VERIFY: source/date].
```

**Tag Types:**
- `[VERIFY: claim]` - Needs fact-checking
- `[CHECK: statistic]` - Numbers, percentages, market data
- `[BOLD CLAIM: needs verification]` - Controversial or surprising claims
- `[CITE: source needed]` - Missing source citation

### Stage 2: Self-Verification Pass

Before launching agents, do a self-check:

**Patent Information:**
- **START HERE**: Read `.agent/System/patent_reference.md` for comprehensive patent details
- **THEN**: Check specific claims in `.agent/US12001207B2.html` if needed
- **ONLY IF NEEDED**: Visit USPTO database: https://patft.uspto.gov/
- Verify issue date, claims, classifications
- Check continuation application status (18/432,397)
- **PRIMARY SOURCE**: Local .agent documentation (always accurate)

**Company Information:**
- Visit official company websites
- Check official press release pages
- Verify product names, capabilities
- Confirm dates of announcements

**Market Statistics:**
- Find original research source
- Verify numbers match source exactly
- Check publication date (not outdated)
- Verify context (not taken out of context)

### Stage 3: Multi-Agent Verification (CRITICAL)

**Launch all 3 agents in parallel** (see Agent Launch Procedure above).

**Minimum Requirements:**
- All 3 agents must complete verification
- All findings must be reviewed and addressed
- 100% of flagged issues must be resolved
- No unverified claims can remain

### Stage 4: Correction and Re-Verification

**For each correction:**
1. Update content with accurate information
2. Document correction in fact-check log
3. Re-run relevant agent on corrected section
4. Verify correction is accurate
5. Update verification tags (remove [VERIFY] markers)

**Example Correction Log:**
```markdown
## Correction Log

**Correction 1:**
- Original: "Tesla FSD was released in January 2024"
- Issue: Incorrect date (Agent 3 flagged)
- Correction: "Tesla FSD v12 was released in March 2024"
- Source: Tesla official announcement (link)
- Verified by: Agent 3 (re-run)
- Date: [date]
```

### Stage 5: Final Editorial Pass

**Before declaring content "ready for publish":**

1. **Re-read entire content** looking for any remaining [VERIFY] tags
2. **Verify all corrections** are integrated properly
3. **Check flow and readability** weren't damaged by corrections
4. **Ensure SEO keywords** still present (accuracy > SEO, but both important)
5. **Confirm fact-check log** is complete and documented
6. **Run final agent spot-check** on high-risk sections

## Source Verification Hierarchy

### Tier 0: Local Patent Documentation (ALWAYS START HERE)

**⚠️ MANDATORY FIRST SOURCE for All Patent Claims:**

Before consulting any external sources, fact-checking agents MUST read the local patent documentation:

**Primary Local Sources:**
1. **`.agent/System/patent_reference.md`** - Comprehensive patent technical reference
   - Patent overview, abstract, claims summary
   - Technical architecture and applications
   - Licensing opportunities and target companies
   - Content development guidelines
   - Use this for: Quick reference, technical summaries, verified facts

2. **`.agent/US12001207B2.html`** - Official complete patent document (3,689 lines)
   - Full legal patent text from Google Patents
   - Complete claims, descriptions, drawings
   - All metadata and legal information
   - Use this for: Detailed verification, exact claim text, technical specifications
   - NOTE: Large file - use Read tool with offset/limit for specific sections

**Why Local First:**
- ✅ Guaranteed accurate (official document)
- ✅ Always available (no network issues)
- ✅ No token waste on web fetches
- ✅ Faster verification
- ✅ Complete context in one place

**Agent Workflow:**
```
Step 1: Read .agent/System/patent_reference.md (comprehensive reference)
Step 2: If more detail needed, read specific sections of .agent/US12001207B2.html
Step 3: Only if local files insufficient, consult external USPTO database
```

### Tier 1: Primary Sources (External - Use After Local Files)

**Patent Information:**
- USPTO Patent Database (patft.uspto.gov) - Use only if local files insufficient
- Google Patents (patents.google.com) - Use only for updates/changes
- Official patent PDF from USPTO - Use only if HTML unclear

**Company Information:**
- Official company press releases
- SEC filings (10-K, 10-Q, 8-K)
- Official company blogs
- Verified company social media (CEO announcements)

**Government/Regulatory:**
- NHTSA announcements
- Federal Register
- Official government websites (.gov)

**Academic:**
- Peer-reviewed journal articles
- University research publications
- Conference proceedings (IEEE, ACM)

### Tier 2: Verify with Second Source

**Tech News:**
- TechCrunch, The Verge, Ars Technica
- Reuters Technology, Bloomberg Technology
- Wall Street Journal Tech, Financial Times

**Industry Publications:**
- IEEE Spectrum
- SAE International
- Autonomous Vehicle Technology Journal

**Analyst Reports:**
- Gartner, Forrester, IDC
- McKinsey, BCG reports
- CB Insights research

**Expert Commentary:**
- Named industry experts (verifiable credentials)
- Conference presentations by experts
- Expert interviews in reputable publications

### Tier 3: Verify with Multiple Sources

**General News:**
- CNN, NBC, ABC, CBS
- Major newspapers (not op-eds)
- International news agencies

**Industry Analyst Opinions:**
- Analyst blog posts
- Twitter/X threads from experts
- LinkedIn posts by industry professionals

**Forums and Communities:**
- Reddit discussions (with verification)
- Hacker News (with verification)
- Professional forums (with verification)

### Never Use (Unverifiable)

❌ Anonymous sources
❌ Unverified social media claims
❌ Blog posts from unknown authors
❌ Wikipedia (use Wikipedia's sources instead)
❌ Content farms or low-quality sites
❌ Outdated information (>2 years old for tech claims)
❌ Speculation presented as fact
❌ "Industry sources say..." without attribution

## High-Risk Content Categories

### CRITICAL: Extra Scrutiny Required

#### Patent Claims
**Risk Level:** 🔴 CRITICAL

**Why:** Legal liability if incorrect

**Verification:**
- Patent number: Exact match to USPTO
- Issue date: Exact match to USPTO
- Claims: Direct quotes from patent text
- Technical specs: From patent diagrams/text
- Continuation status: Current USPTO PAIR data

**Sources Required:** Tier 1 only (USPTO)

#### Dates and Timelines
**Risk Level:** 🔴 CRITICAL

**Why:** Easy to verify, damages credibility if wrong

**Verification:**
- Product releases: Official company announcements
- Company milestones: Press releases, SEC filings
- Regulatory dates: Official government sources
- Event dates: Multiple news sources

**Sources Required:** Tier 1 or Tier 2 (with 2+ sources)

#### Company and Product Names
**Risk Level:** 🟠 HIGH

**Why:** Legal issues with trademark misuse

**Verification:**
- Company names: Official websites
- Product names: Official product pages
- Capabilities: Official specs/documentation
- Partnerships: Official announcements

**Sources Required:** Tier 1 (official company sources)

#### Market Statistics
**Risk Level:** 🟠 HIGH

**Why:** Easily challenged, affects credibility

**Verification:**
- Market size: Original research report
- Growth rates: Primary analyst source
- Projections: Reputable analyst firm
- Financial data: SEC filings, official reports

**Sources Required:** Tier 1 or Tier 2 (original research)

#### Quotes and Attributions
**Risk Level:** 🟠 HIGH

**Why:** Misquotes damage reputation and legal risk

**Verification:**
- Exact quote text: Original source
- Attribution: Verify person/title
- Context: Full context reviewed
- Date/publication: Verified

**Sources Required:** Tier 1 or Tier 2 (original publication)

#### Technology Capabilities
**Risk Level:** 🟡 MEDIUM

**Why:** Technical accuracy important for credibility

**Verification:**
- Technology specs: Technical documentation
- Capabilities: Official product specs
- Limitations: Engineering documentation
- Comparisons: Multiple sources

**Sources Required:** Tier 1 or Tier 2

#### Industry Trends
**Risk Level:** 🟡 MEDIUM

**Why:** Subjective but should be supported

**Verification:**
- Trends: Multiple analyst reports
- Predictions: Reputable analysts
- Shifts: Industry publications
- Adoption rates: Research data

**Sources Required:** Tier 2 (multiple sources)

#### Regulatory Claims
**Risk Level:** 🔴 CRITICAL

**Why:** Legal implications if incorrect

**Verification:**
- Regulations: Official government sources
- Requirements: Agency websites
- Compliance: Official documentation
- Deadlines: Government announcements

**Sources Required:** Tier 1 only (official government)

## Content Accuracy Red Flags

### 🚨 STOP and Fact-Check Immediately

If you see any of these in content, **STOP and verify before proceeding**:

1. **Specific numbers without source**
   - ❌ "The AV market will reach $500B"
   - ✅ "The AV market will reach $500B by 2030 (McKinsey Report, 2023)"

2. **"Studies show..." without citation**
   - ❌ "Studies show camera-based systems are more reliable"
   - ✅ "An MIT study (2023) found camera-based systems..."

3. **Quotes without attribution**
   - ❌ "The technology is revolutionary"
   - ✅ "The technology is revolutionary, according to Tesla CEO Elon Musk (March 2024 keynote)"

4. **Bold predictions about future**
   - ❌ "AVs will dominate by 2025"
   - ✅ "Industry analysts project AVs may reach X% market share by 2025 (source)"

5. **Comparisons without data**
   - ❌ "Better than competitors"
   - ✅ "Achieves 95% accuracy vs industry average of 87% (IEEE study, 2024)"

6. **Technical specs not in patent**
   - ❌ "Uses advanced neural networks" (if not in patent)
   - ✅ "Employs camera-based safety mechanisms (US Patent 12,001,207, Claim 3)"

7. **Market size claims without source**
   - ❌ "The drone market is growing rapidly"
   - ✅ "The commercial drone market grew 15% in 2023 (Gartner report)"

8. **Timeline claims without verification**
   - ❌ "Tesla launched FSD last year"
   - ✅ "Tesla launched FSD v12 in March 2024 (Tesla press release)"

9. **Superlatives without proof**
   - ❌ "The most advanced patent"
   - ✅ "A comprehensive patent covering [specific aspects]"

10. **Competitor claims without verification**
    - ❌ "Competitors lack this technology"
    - ✅ "Few patents address [specific aspect] (USPTO search, Oct 2024)"

## Fact-Check Log Requirements

### Log Template

For **every page**, create and maintain this log:

```markdown
# Fact-Check Log: [Page Name]

**Page:** [page-name.md]
**Created:** [date]
**Last Verified:** [date]
**Verified By:** [agent names + human reviewer]
**Status:** [Draft/In Review/Verified/Published]

---

## Patent Claims Verified

### Claim 1
- **Claim:** "US Patent 12,001,207 issued June 4, 2024"
- **Verification:** Verified
- **Source:** .agent/System/patent_reference.md (line 21) + .agent/US12001207B2.html
- **Verified By:** Agent 1 (Patent Facts)
- **Date:** [date]
- **Confidence:** High
- **Status:** ✅ VERIFIED

### Claim 2
- **Claim:** "Patent covers dual-module safety system for autonomous vehicles using visual navigation"
- **Verification:** Verified
- **Source:** .agent/System/patent_reference.md (Abstract section) + .agent/US12001207B2.html (lines 1737-1739)
- **Verified By:** Agent 1 (Patent Facts)
- **Date:** [date]
- **Confidence:** High
- **Status:** ✅ VERIFIED

[Continue for all patent claims...]

---

## Industry/Market Claims Verified

### Claim 1
- **Claim:** "Tesla deployed FSD v12 in March 2024"
- **Verification:** Verified
- **Source:** Tesla press release (link) + TechCrunch article (link)
- **Verified By:** Agent 2 (Industry Claims)
- **Date:** [date]
- **Confidence:** High
- **Status:** ✅ VERIFIED

### Claim 2
- **Claim:** "AV market projected to reach $X billion by 2030"
- **Verification:** Verified
- **Source:** McKinsey & Company Report 2023 (link)
- **Verified By:** Agent 2 (Industry Claims)
- **Date:** [date]
- **Confidence:** Medium (projection)
- **Status:** ✅ VERIFIED WITH CAVEAT (noted as projection)

[Continue for all industry claims...]

---

## Current Events/Quotes Verified

### Claim 1
- **Claim:** "Event X occurred on October 12, 2024"
- **Verification:** Verified
- **Source:** Official announcement (link) + Reuters (link)
- **Verified By:** Agent 3 (Current Events)
- **Date:** [date]
- **Confidence:** High
- **Status:** ✅ VERIFIED

[Continue for all dates/quotes...]

---

## Claims Corrected

### Correction 1
- **Original Claim:** "Tesla released FSD in January 2024"
- **Issue:** Incorrect date
- **Flagged By:** Agent 3
- **Correction:** "Tesla released FSD v12 in March 2024"
- **New Source:** Tesla official announcement
- **Re-Verified By:** Agent 3 (re-run)
- **Date Corrected:** [date]
- **Status:** ✅ CORRECTED AND VERIFIED

[Continue for all corrections...]

---

## Claims Removed (Unverifiable)

### Removed 1
- **Original Claim:** "Industry experts believe..."
- **Issue:** No verifiable source, vague attribution
- **Flagged By:** Agent 3
- **Reason:** Cannot verify "industry experts" without specific attribution
- **Date Removed:** [date]
- **Replacement:** Removed sentence, flow maintained

[Continue for all removals...]

---

## Verification Summary

**Total Claims:** [number]
**Verified:** [number] ([percentage]%)
**Corrected:** [number]
**Removed:** [number]
**Source Quality:**
- Tier 1 Sources: [number] ([percentage]%)
- Tier 2 Sources: [number] ([percentage]%)
- Tier 3 Sources: [number] ([percentage]%)

**Agent Performance:**
- Agent 1 (Patent Facts): [X claims verified, Y flagged]
- Agent 2 (Industry Claims): [X claims verified, Y flagged]
- Agent 3 (Current Events): [X claims verified, Y flagged]

**Final Status:** ✅ READY FOR PUBLICATION
**Sign-off:** [Human reviewer name/date]

---

## Re-Verification Schedule

This content should be re-verified if:
- [ ] Current events referenced are >3 months old
- [ ] Patent continuation status changes
- [ ] Company/product information changes
- [ ] Market statistics become outdated (>1 year)
- [ ] Any factual claim is questioned

**Next Scheduled Re-Verification:** [date - typically 6 months]
```

### Log Storage

Store fact-check logs in:
```
/website/content/fact-check-logs/
├── homepage-fact-check.md
├── patent-details-fact-check.md
├── licensing-fact-check.md
├── tesla-fsd-landing-fact-check.md
└── [page-name]-fact-check.md
```

## Quality Metrics and Tracking

### Per-Page Metrics

Track for each page:

1. **Fact-Check Pass Rate:**
   - Formula: (Verified Claims / Total Claims) × 100
   - Target: 100% before publish

2. **Source Quality Score:**
   - Formula: (Tier 1 Sources × 3 + Tier 2 × 2 + Tier 3 × 1) / Total Sources
   - Target: >2.5 (mostly Tier 1 & 2)

3. **Claims Density:**
   - Formula: Total Factual Claims / Total Word Count
   - Target: 3-5% (30-50 claims per 1000 words)

4. **Correction Rate:**
   - Formula: (Corrected Claims / Total Claims) × 100
   - Target: <10% (catch errors in draft stage)

5. **Agent Flag Rate:**
   - Formula: (Flagged Claims / Total Claims) × 100
   - Target: <15% (indicates quality draft)

### Site-Wide Metrics

Track across all pages:

1. **Overall Verification Rate:** >99%
2. **Average Source Quality Score:** >2.5
3. **Tier 1 Source Usage:** >60%
4. **Pages Requiring Re-Verification:** Track monthly
5. **Time Since Last Verification:** Track per page

### Quality Dashboard (Recommended)

Create a tracking spreadsheet:

| Page | Total Claims | Verified | Corrections | Source Score | Last Verified | Next Review | Status |
|------|-------------|----------|-------------|--------------|---------------|-------------|--------|
| Homepage | 25 | 25 (100%) | 2 (8%) | 2.8 | 2024-10-12 | 2025-04-12 | ✅ |
| Patent Details | 42 | 42 (100%) | 5 (12%) | 2.9 | 2024-10-12 | 2025-04-12 | ✅ |
| Tesla FSD Landing | 38 | 38 (100%) | 3 (8%) | 2.6 | 2024-11-15 | 2025-02-15 | ✅ |

## Content Scaling Strategy

### Phase 3: Creating Tens of Landing Pages

#### Content Differentiation Approaches

To create many unique landing pages while maintaining accuracy:

**1. Patent Aspect Focus** (10-15 pages possible)
- Safety mechanisms (Claim 1 focus)
- Camera-based navigation (Claim 2 focus)
- Fail-safe systems (Claim 3 focus)
- AI integration points (Technical specs)
- Sensor fusion approaches (Patent diagrams)
- Image processing techniques
- Object detection methods
- Path planning algorithms
- Emergency response systems
- Redundancy mechanisms

**2. Industry Application Focus** (15-20 pages possible)
- Autonomous passenger vehicles
- Commercial delivery vehicles
- Long-haul trucking
- Last-mile delivery robots
- Commercial drones (inspection)
- Commercial drones (delivery)
- Agricultural automation
- Mining equipment automation
- Marine navigation
- Airport ground vehicles
- Warehouse automation
- Construction equipment
- Public transportation
- Ride-sharing fleets
- Emergency vehicles

**3. Current Event Tie-Ins** (Ongoing - new pages quarterly)
- Tesla FSD rollout updates
- Regulatory changes (NHTSA, etc.)
- Competitor announcements
- Technology breakthroughs
- Funding rounds in AV space
- Major partnerships
- Pilot programs
- Market milestones
- Conference announcements
- Research publications

**4. Company/Persona Focus** (10-15 pages possible)
- Early-stage AV startups
- Series A-C funded companies
- Public AV companies
- Traditional automakers (transition to AV)
- Tech companies (Apple, etc.)
- Research institutions
- Defense contractors
- Agriculture companies
- Logistics companies
- Drone manufacturers

### Fact-Checking at Scale

**Challenges:**
- More content = more factual claims
- More claims = higher error risk
- Time pressure vs quality

**Solutions:**

**1. Content Templates with Pre-Verified Sections**
Create reusable blocks of verified content:
- Patent description (verified once, reuse everywhere)
- Company background (verify quarterly, reuse)
- Industry overview (verify semi-annually)

**2. Batch Fact-Checking**
For similar pages (e.g., 5 drone application pages):
- Draft all 5 pages
- Run agents once across all 5
- Consolidate verification findings

**3. Verification Prioritization**
- **High Priority:** Current events, quotes, new statistics
- **Medium Priority:** Company information updates
- **Low Priority:** Evergreen patent information (verify once)

**4. Rolling Re-Verification Schedule**
- Current event pages: Re-verify every 3 months
- Industry trend pages: Re-verify every 6 months
- Patent core pages: Re-verify annually
- Evergreen content: Re-verify when challenged

**5. Automated Red Flag Detection**
Create a script to scan content for red flags:
- Numbers without parenthetical source
- "Studies show" without citation
- Superlatives (most, best, first) without proof
- Dates in specific formats without source

## Emergency Fact-Check Procedures

### When Content is Challenged

If factual accuracy is questioned (by user, competitor, etc.):

**1. Immediate Response (Within 1 Hour)**
- Take page offline or add disclaimer
- Document the challenge
- Identify specific claims in question

**2. Emergency Verification (Within 24 Hours)**
- Launch all 3 agents on questioned claims
- Manual verification of flagged sections
- Consult primary sources directly
- Document findings

**3. Correction or Reinstatement (Within 48 Hours)**
- If incorrect: Correct immediately, document
- If correct: Reinstate with added citation
- If unclear: Add disclaimer or remove claim
- Update fact-check log

**4. Process Review (Within 1 Week)**
- Review how error occurred
- Update SOP to prevent recurrence
- Re-train on fact-checking procedures

## Quick Reference: Patent Documentation Locations

**For All Fact-Checking Agents:**

1. **Comprehensive Reference** (Start Here):
   - File: `.agent/System/patent_reference.md`
   - Contents: Full patent overview, technical details, licensing info, content guidelines
   - When to use: First stop for any patent verification

2. **Official Patent Document** (Detailed Verification):
   - File: `.agent/US12001207B2.html` (3,689 lines)
   - Contents: Complete official patent from Google Patents
   - When to use: Detailed claim text, technical specifications, exact legal language
   - How to read: Use Read tool with offset/limit for specific sections

3. **External Sources** (Only if Local Insufficient):
   - USPTO Database: https://patft.uspto.gov/
   - Google Patents: https://patents.google.com/patent/US12001207B2/en
   - When to use: Only for updates, changes, or if local files don't have needed info

**Agent Reminder Checklist:**
- [ ] Read .agent/System/patent_reference.md FIRST
- [ ] Read specific sections of .agent/US12001207B2.html if needed
- [ ] Document local file sources in verification report
- [ ] Only consult external sources if local files insufficient

## Related Documentation

- **Patent Reference**: `/.agent/System/patent_reference.md` - **PRIMARY SOURCE** for all patent information
- **Patent HTML**: `/.agent/US12001207B2.html` - Complete official patent document
- **Content Management SOP**: `/.agent/SOP/content_management.md` - General content procedures
- **Site Generation & Deployment**: `/.agent/SOP/site_generation_deployment.md` - Deployment process
- **Project Architecture**: `/.agent/System/project_architecture.md` - System overview
- **PRD**: `/.agent/Tasks/website_development_prd.md` - Product requirements
- **Documentation Index**: `/.agent/README.md` - Complete documentation map

---

**Version:** 1.1
**Last Updated:** October 14, 2025 (Added local patent documentation requirements)
**Previous Update:** October 12, 2025 (Initial version)
**Next Review:** January 14, 2026 (Quarterly)
**Status:** ACTIVE - MANDATORY FOR ALL CONTENT

**Version 1.1 Changes:**
- ✅ Added mandatory local patent documentation reading for fact-checking agents
- ✅ Created Tier 0 source hierarchy (local .agent files as PRIMARY source)
- ✅ Updated Agent 1 prompts to require reading .agent/System/patent_reference.md
- ✅ Added .agent/US12001207B2.html as official patent source
- ✅ Updated fact-check log examples to reference local file sources
- ✅ Added Quick Reference section for patent documentation locations
- ✅ Emphasized local-first verification workflow to reduce token usage and ensure accuracy
