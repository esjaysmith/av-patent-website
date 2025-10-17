# SEO Technical Specifications - Phase 3 Landing Pages

## Document Information
- **Created**: October 16, 2025
- **Purpose**: Technical SEO requirements for all 5 Phase 3 landing pages
- **Status**: Complete - Ready for Implementation
- **Related Task**: `.agent/Tasks/seo_landing_pages_phase3.md`
- **Applies To**: All Phase 3 landing pages + future content

---

## Executive Summary

This document defines the technical SEO specifications that MUST be implemented for all 5 Phase 3 landing pages (and future content). These specifications ensure consistent on-page SEO, technical SEO, and structured data implementation across the site.

**Key Requirements:**
- Title tags: 55-60 characters with primary keyword + benefit + brand
- Meta descriptions: 155-160 characters with primary keyword + CTA
- H1/H2/H3 hierarchy with strategic keyword placement
- Schema.org structured data (Article, FAQPage, HowTo)
- Internal linking strategy (5+ internal links per page)
- External linking to authoritative sources (3-5 per page)
- Mobile-responsive design (Bootstrap 5)
- Page load time <3 seconds

---

## Table of Contents

1. [Title Tag Formulas](#title-tag-formulas)
2. [Meta Description Templates](#meta-description-templates)
3. [Heading Structure & Keywords](#heading-structure--keywords)
4. [Image Alt Text Guidelines](#image-alt-text-guidelines)
5. [Internal Link Anchor Text Strategy](#internal-link-anchor-text-strategy)
6. [External Linking Best Practices](#external-linking-best-practices)
7. [Schema.org Structured Data](#schemaorg-structured-data)
8. [URL Structure & Canonical URLs](#url-structure--canonical-urls)
9. [Open Graph & Twitter Card Tags](#open-graph--twitter-card-tags)
10. [Mobile Optimization](#mobile-optimization)
11. [Page Speed Requirements](#page-speed-requirements)
12. [YAML Frontmatter Standards](#yaml-frontmatter-standards)

---

## 1. Title Tag Formulas

### Primary Formula (Recommended)
```
[Primary Keyword] | [Benefit] | [Brand/Patent Number]
```

**Example:**
```
Autonomous Trucking Patent Defense Strategy | US 12,001,207
```

### Length Requirements
- **Minimum**: 50 characters
- **Maximum**: 60 characters
- **Optimal**: 55-58 characters (to avoid truncation in search results)

### Character Counting Tool
- Google displays first ~60 characters on desktop, ~50-55 on mobile
- Use pixel-based measuring (not just character count) for accuracy
- Tool: SERP Snippet Preview Tool or Moz Title Tag Preview

### Keyword Placement
- **Primary keyword** must appear in first 60 characters
- **Brand or patent number** at end (after pipe "|")
- **Benefit or modifier** in middle

### Formula Variations for Different Pages

**Variation 1: Funding Stage Focus**
```
[Funding Stage] [Industry] Patent Strategy | [Brand]
```
Example: "Series A AV Patent Portfolio Strategy | US 12,001,207"

**Variation 2: Competitor Focus**
```
[Competitor] Alternative Patent Protection | [Brand]
```
Example: "Tesla FSD Competitor Camera Patent Licensing | AV IP"

**Variation 3: Application Focus**
```
[Application] Patent Portfolio for [Milestone] | [Brand]
```
Example: "Drone Delivery Patent Portfolio Pre-IPO | US 12,001,207"

**Variation 4: Audience Focus**
```
[Audience] [Topic] Due Diligence Guide | [Brand]
```
Example: "VC AV Patent Portfolio Due Diligence | IP Guide"

### Title Tag Best Practices

**DO:**
- Include primary keyword exactly as researched
- Front-load most important keywords
- Use natural, readable phrasing
- Include brand or patent number for credibility
- Make it compelling (entice clicks)
- Test with SERP preview tools

**DON'T:**
- Keyword stuff (looks spammy: "Patent Patents Patenting Patent License")
- Use ALL CAPS (except acronyms like "AV", "IP", "VC")
- Duplicate title tags across pages
- Exceed 60 characters (risks truncation)
- Use special characters excessively (!, ?, etc.)
- Separate with multiple pipes (use one "|" maximum)

### Title Tag Testing Checklist

For each landing page:
- [ ] Primary keyword present in first 60 characters
- [ ] Character count: 55-60 characters
- [ ] Unique across all site pages (no duplicates)
- [ ] Benefit or value prop included
- [ ] Brand or patent number at end
- [ ] Tested in SERP preview tool
- [ ] Compelling enough to earn clicks

---

## 2. Meta Description Templates

### Primary Template (Recommended)
```
[Primary benefit/solution]. [Secondary benefit]. [Specific technology or patent]. [Clear call-to-action].
```

**Example:**
```
Strengthen your autonomous trucking patent portfolio with camera-based navigation IP. Licensed patents = faster, cheaper than in-house development. Schedule consultation.
```

### Length Requirements
- **Minimum**: 120 characters (too short looks incomplete)
- **Maximum**: 160 characters (hard Google cutoff)
- **Optimal**: 155-160 characters (use full space)

### Character Counting
- Google displays ~155-160 characters on desktop
- ~120 characters on mobile (be mindful of key info placement)
- Every character counts—no wasted words

### Content Structure

**Element 1: Primary Benefit (30-50 characters)**
- What problem does this solve?
- Example: "Strengthen your autonomous trucking patent portfolio"

**Element 2: Specific Solution (30-50 characters)**
- What do we offer?
- Example: "with camera-based navigation IP from US Patent 12,001,207"

**Element 3: Value Proposition (20-40 characters)**
- Why choose this solution?
- Example: "Faster and cheaper than in-house development"

**Element 4: Call-to-Action (10-20 characters)**
- What should they do?
- Example: "Schedule consultation" or "Download guide" or "Learn more"

### Template Variations for Different Pages

**Variation 1: Problem-Solution-CTA**
```
[Problem]? [Solution with patent/technology]. [Benefit comparison]. [CTA].
```
Example: "Need defensive IP for AV? License US Patent 12,001,207 for camera-based safety. Faster than in-house development. Get started."

**Variation 2: Audience-Specific**
```
[Audience]: [Specific benefit]. [Patent/solution]. [Timing benefit]. [CTA].
```
Example: "Series A AV startups: Strengthen patent portfolios with licensed camera-based navigation IP. Deploy in 4-9 months. Schedule consultation."

**Variation 3: Statistic-Driven**
```
[Compelling statistic]. [Solution]. [Patent reference]. [CTA].
```
Example: "376 AV companies at Series A+ in 2024. Strengthen your IP with licensed camera patents (US 12,001,207). Contact us."

**Variation 4: Question-Answer**
```
[Question]? [Answer with solution]. [Patent reference]. [Benefit]. [CTA].
```
Example: "Preparing for IPO? Strengthen drone patent portfolio with visual navigation IP (US 12,001,207). Lower cost, faster deployment. Learn more."

### Meta Description Best Practices

**DO:**
- Include primary keyword naturally (not forced)
- Write compelling, action-oriented copy
- Include specific patent number or technology (credibility)
- End with clear call-to-action
- Match user search intent
- Use active voice ("Strengthen your portfolio" not "Your portfolio can be strengthened")
- Make it unique for each page

**DON'T:**
- Keyword stuff (Google may ignore and generate its own)
- Duplicate across pages
- Use quotation marks (they get truncated in SERPs)
- Make false promises or use clickbait
- Exceed 160 characters
- Use generic descriptions ("Learn more about our services...")
- Forget the call-to-action

### Meta Description Testing Checklist

For each landing page:
- [ ] Character count: 155-160 characters (optimal)
- [ ] Primary keyword included naturally
- [ ] Clear benefit or value proposition
- [ ] Specific patent number or technology mentioned
- [ ] Call-to-action present
- [ ] Unique across all site pages
- [ ] Tested in SERP preview tool
- [ ] Compelling enough to earn clicks (>2% CTR target)

---

## 3. Heading Structure & Keywords

### H1 Tag Requirements

**Count:** Exactly ONE H1 per page (never zero, never multiple)

**Content:**
- Must include primary keyword (exact match or close variation)
- Should be compelling and clear about page content
- Different from page title (avoid exact duplication)
- 50-70 characters optimal (readable, not truncated)

**Examples:**

| Page | H1 Tag |
|------|--------|
| Series A AV | Build Your Patent Portfolio Before Series B Funding: Strategic Licensing for AV Startups |
| Tesla FSD | How Tesla FSD Competitors Can License Camera-Based Safety Patents |
| Drone IPO | Strengthen Your Drone Patent Portfolio for IPO Success |
| VC Due Diligence | The Complete Guide to AV Patent Portfolio Due Diligence for Venture Capital |
| Trucking | Defensive Patent Strategy for Autonomous Trucking: Camera-Based Navigation IP |

**H1 Best Practices:**
- Front-load primary keyword (appears in first 3-5 words)
- Make it benefit-driven (what will reader learn/gain?)
- Use action words (Build, Strengthen, Discover, Learn)
- Avoid keyword stuffing
- Ensure it's unique on the page (not repeated as H2)

### H2 Tag Strategy

**Count:** 6-8 H2 sections per landing page (1,800-2,200 words)

**Keyword Distribution:**
- 2-3 H2 headings should include secondary keywords
- 2-3 H2 headings should be long-tail question keywords
- 1-2 H2 headings can be generic (but still descriptive)

**Examples:**

**H2 with Secondary Keywords:**
- "The Autonomous Trucking Patent Landscape: Why IP Protection is Non-Negotiable"
- "Strategic Patent Licensing for Trucking Companies"
- "Camera-Based Navigation Patents for Commercial Trucks"

**H2 with Long-Tail Questions:**
- "Why Do Autonomous Trucking Startups Need Defensive Patent Strategy?"
- "How Can Camera-Based Patents Apply to Class 8 Trucks?"
- "What Are the Licensing Options for Commercial Vehicle Patents?"

**H2 Generic but Descriptive:**
- "Case Studies: Trucking Companies Using Patent Strategy"
- "Next Steps for Strengthening Your Patent Portfolio"
- "Regulatory Requirements and Patent Compliance"

**H2 Best Practices:**
- Start with natural language (not keyword-stuffed)
- Use parallel structure across sections (consistency)
- Keep under 70 characters
- Make scannable (readers should understand content from headings alone)
- Order logically (problem → solution → action)

### H3 Tag Strategy

**Count:** 15-20 H3 subsections per landing page

**Keyword Distribution:**
- 5-7 H3 headings with long-tail keyword variations
- 3-5 H3 headings with LSI keywords (related terms)
- 5-8 H3 headings generic but descriptive

**Examples:**

**H3 with Long-Tail Keywords:**
- "Patent Licensing for Autonomous Trucking Startups"
- "Cost-Benefit Analysis: Licensing vs. In-House Development"
- "Waabi's $200M Series B: How Patent Strategy Influenced Funding"

**H3 with LSI Keywords:**
- "Class 8 Truck Patent Applications"
- "Fleet Deployment Economics for Camera-Based Systems"
- "NHTSA Safety Standards for Commercial AVs"

**H3 Generic but Descriptive:**
- "Key Patent Categories for Trucking"
- "Types of Patent Licenses Available"
- "When to License Camera-Based Navigation Patents"

**H3 Best Practices:**
- More specific than H2 (drill down into subtopics)
- Answer specific questions readers might have
- Use numbers when applicable ("3 Types of Patent Licenses")
- Include company/brand names when relevant (Waabi, Aurora, Tesla)

### Heading Hierarchy Rules

**Correct Hierarchy:**
```
H1: Main Page Topic
  H2: Major Section 1
    H3: Subsection 1.1
    H3: Subsection 1.2
  H2: Major Section 2
    H3: Subsection 2.1
    H3: Subsection 2.2
    H3: Subsection 2.3
```

**Incorrect Hierarchy (NEVER DO THIS):**
```
H1: Main Topic
H3: Subsection (skipped H2 - BAD)
  H2: Section (out of order - BAD)
H1: Another Main Topic (multiple H1s - BAD)
```

### Keyword Density in Headings

**Primary Keyword:**
- H1: 1 time (required)
- H2: 1-2 times across all H2s (not every H2)
- H3: 1-3 times across all H3s (naturally distributed)

**Secondary Keywords:**
- H2: 2-3 different secondary keywords across H2s
- H3: 5-7 different secondary/long-tail keywords across H3s

**LSI Keywords:**
- H2: 1-2 related terms
- H3: 3-5 related terms

### Heading Structure Checklist

For each landing page:
- [ ] Exactly 1 H1 tag (includes primary keyword)
- [ ] 6-8 H2 tags (section headings)
- [ ] 15-20 H3 tags (subsection headings)
- [ ] No skipped heading levels (H1 → H2 → H3, never H1 → H3)
- [ ] Primary keyword in H1 (required)
- [ ] Secondary keywords in 2-3 H2 headings
- [ ] Long-tail keywords in 5-7 H3 headings
- [ ] Headings scannable (readers understand structure from headings alone)
- [ ] Parallel structure (consistency across similar sections)

---

## 4. Image Alt Text Guidelines

### Purpose of Alt Text

**Primary Purpose:** Accessibility (screen readers for visually impaired)
**Secondary Purpose:** SEO (Google Image Search, contextual relevance)

### Alt Text Formula

```
[What is in the image] + [Relevant keyword if natural] + [Context]
```

**Example:**
```
Alt text: "Autonomous semi-truck with camera-based navigation system on highway"
```

### Length Requirements
- **Minimum**: 5 words (too short is not descriptive)
- **Maximum**: 125 characters (~15-20 words)
- **Optimal**: 80-100 characters (specific but concise)

### Alt Text Best Practices

**DO:**
- Describe what's actually in the image
- Include relevant keywords naturally (don't force)
- Be specific ("Class 8 autonomous truck" not "truck")
- Mention context if relevant ("...during highway testing")
- Use proper punctuation (helps screen readers)

**DON'T:**
- Start with "Image of..." or "Picture of..." (redundant)
- Keyword stuff ("patent patent licensing AV AV autonomous vehicle")
- Use generic descriptions ("diagram" or "chart")
- Leave alt text empty (bad for accessibility and SEO)
- Use exact same alt text for multiple images
- Include image file names ("IMG_1234.jpg")

### Alt Text Examples by Image Type

**Diagrams/Technical Illustrations:**
```
Alt text: "Dual-module safety system architecture showing camera input, safety-determining module, and control module for autonomous vehicles"
```

**Charts/Graphs:**
```
Alt text: "Bar chart comparing patent development costs versus licensing costs for autonomous vehicle startups over 3-year period"
```

**Company Logos:**
```
Alt text: "Waabi autonomous trucking company logo"
```

**Screenshots:**
```
Alt text: "USPTO patent search results showing US Patent 12,001,207 B2 grant date and classification"
```

**Infographics:**
```
Alt text: "Infographic illustrating Series A AV startup patent portfolio strategy with 5-step licensing process"
```

**Product Photos (if any):**
```
Alt text: "Camera array mounted on autonomous truck cab for visual navigation and object detection"
```

### Keyword Integration in Alt Text

**Primary Keyword:**
- Use in 1-2 images maximum (most relevant images only)
- Must be natural fit (don't force)

**Example:**
```
Alt text: "Autonomous trucking patent defense strategy flowchart showing licensing timeline versus in-house development"
```

**Secondary Keywords:**
- Use different secondary keywords in different images
- Distribute naturally across all images

**Example:**
```
Image 1 Alt: "Class 8 truck autonomous navigation patent system diagram"
Image 2 Alt: "Commercial vehicle AV patent licensing cost comparison table"
Image 3 Alt: "Long-haul autonomous vehicle camera-based safety system"
```

### Special Cases

**Decorative Images (no informational value):**
- Leave alt text EMPTY (alt="") so screen readers skip
- Examples: Background textures, divider lines, purely decorative icons

**Linked Images (image is a link):**
- Alt text should describe link destination, not image
- Example: Alt="Read full patent details for US 12,001,207 B2"

**Complex Images (detailed charts):**
- Use alt text for brief description
- Include longer description in surrounding text or figure caption
- Example: Alt="Patent portfolio growth timeline 2019-2024" + Caption with full data

### Image Alt Text Checklist

For each image:
- [ ] Alt text 80-100 characters (optimal length)
- [ ] Describes what's actually in the image
- [ ] Includes relevant keyword naturally (if appropriate)
- [ ] Unique alt text (not duplicated across images)
- [ ] No "Image of..." or "Picture of..." prefix
- [ ] Proper punctuation for screen readers
- [ ] Decorative images have empty alt (alt="")
- [ ] Linked images describe destination, not image

---

## 5. Internal Link Anchor Text Strategy

### Purpose of Internal Linking

**SEO Benefits:**
- Distributes page authority (link juice) across site
- Helps Google understand site structure and page relationships
- Improves crawlability (helps bots discover all pages)
- Establishes topical authority (related content clusters)

**User Benefits:**
- Helps visitors discover related content
- Improves navigation and UX
- Keeps visitors on site longer (reduces bounce rate)
- Guides visitors through conversion funnel

### Anchor Text Types

**1. Exact Match Anchor Text (Use Sparingly)**
- Exact keyword match
- Example: "camera-based navigation patent"
- **Risk**: Over-optimization penalty if used too much
- **Recommended**: 10-20% of internal links

**2. Partial Match Anchor Text (Most Common)**
- Includes keyword plus additional words
- Example: "Learn more about camera-based navigation technology"
- **Risk**: Low
- **Recommended**: 40-50% of internal links

**3. Branded Anchor Text**
- Brand name or patent number
- Example: "US Patent 12,001,207" or "AV Navigation IP Protection"
- **Risk**: None
- **Recommended**: 20-30% of internal links

**4. Generic Anchor Text**
- Non-descriptive phrases
- Example: "click here", "learn more", "read more"
- **Risk**: Low SEO value (but okay for UX)
- **Recommended**: 10-20% of internal links

**5. Naked URL**
- Actual URL as anchor text
- Example: "https://example.com/patent-details.html"
- **Risk**: None (but looks unprofessional)
- **Recommended**: 0-5% of internal links (rare use)

**6. Image Links**
- Image with alt text acts as anchor text
- Example: Image with alt="Patent technical diagram" linking to patent-details.html
- **Risk**: None
- **Recommended**: 5-10% of internal links

### Anchor Text Distribution Formula

For each landing page (5+ internal links):

| Anchor Type | Percentage | Number of Links (out of 5-8) |
|-------------|------------|-------------------------------|
| Exact Match | 10-20% | 1 link maximum |
| Partial Match | 40-50% | 2-3 links |
| Branded | 20-30% | 1-2 links |
| Generic | 10-20% | 1 link |
| Total | 100% | 5-7 links |

### Internal Linking Strategy by Page

**FROM Landing Pages TO Core Pages:**

Each landing page should link to:
1. **patent-details.md** (2-3 times)
   - Anchor text options:
     - "US Patent 12,001,207 B2 technical specifications"
     - "Learn more about camera-based navigation technology"
     - "View full patent details"
     - "Read patent claims and descriptions"

2. **licensing.md** (2-3 times)
   - Anchor text options:
     - "Explore licensing options"
     - "Exclusive and non-exclusive licensing available"
     - "Contact us about patent licensing"
     - "Learn about licensing terms and pricing"

3. **industry-insights.md** (1-2 times)
   - Anchor text options:
     - "Read about autonomous vehicle industry trends"
     - "Tesla FSD market analysis"
     - "Drone delivery industry insights"
     - "AV patent landscape overview"

4. **contact.md** (3-4 times via CTAs)
   - Anchor text options:
     - "Schedule a consultation"
     - "Contact us to discuss your patent portfolio"
     - "Request a licensing proposal"
     - "Get in touch with our team"

**FROM Core Pages TO Landing Pages:**

1. **homepage** (1 link to each landing page)
   - Add "Solutions" or "Resources" section
   - Anchor text: Descriptive, benefit-driven

2. **industry-insights.md** (1-2 links per landing page)
   - Contextual links in relevant sections
   - Anchor text: Topic-specific

3. **licensing.md** (1 link to each landing page)
   - "Industry Applications" section
   - Anchor text: Industry or audience-specific

**BETWEEN Landing Pages:**

- Limited cross-linking (only when highly relevant)
- Example: Tesla FSD page could link to Trucking page (Tesla Semi connection)
- Anchor text: Contextual, descriptive

### Contextual Link Placement

**Best Placement Locations:**
1. **Within body paragraphs** (most natural, highest SEO value)
2. **At section conclusions** (transitional, "Learn more about...")
3. **In callout boxes or sidebar** (supplementary content)
4. **In bullet point lists** (scannable, easy to notice)

**Avoid:**
- Link-heavy footer dumps ("Resources: link1, link2, link3...")
- Excessive linking in first paragraph (looks spammy)
- Linking every instance of a keyword (over-optimization)

### Internal Link Best Practices

**DO:**
- Link early in content (first 500 words should have 1-2 internal links)
- Use natural, descriptive anchor text
- Link to relevant, related content only
- Open internal links in same tab (external in new tab)
- Vary anchor text across pages (no exact duplicates)
- Use contextual links within paragraphs
- Deep link to specific sections (e.g., patent-details.html#safety-system)

**DON'T:**
- Link to same page (self-referential links)
- Use exact same anchor text repeatedly across site
- Link to irrelevant pages (hurts UX and SEO)
- Use too many links in a single paragraph (1-2 max)
- Link every instance of a keyword (once per page is enough)
- Use "click here" exclusively (mix with descriptive text)
- Create orphan pages (pages with no internal links to them)

### Internal Link Audit Checklist

For each landing page:
- [ ] 5-8 internal links total
- [ ] 2-3 links to patent-details.md
- [ ] 2-3 links to licensing.md
- [ ] 1-2 links to industry-insights.md
- [ ] 3-4 CTA links to contact.md
- [ ] Anchor text varied (no exact duplicates)
- [ ] 40-50% partial match anchor text
- [ ] 10-20% exact match anchor text (max 1 link)
- [ ] Links contextual (within paragraphs, not isolated)
- [ ] All links working (no 404 errors)

---

## 6. External Linking Best Practices

### Purpose of External Linking

**SEO Benefits:**
- Signals to Google that content is well-researched
- Associates your page with authoritative sources (trust signals)
- Improves E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
- Reduces risk of being seen as "thin content"

**User Benefits:**
- Provides citations and proof for claims
- Allows users to verify information
- Adds credibility and transparency

### Number of External Links

**Per Landing Page:**
- **Minimum**: 3 external links (to authoritative sources)
- **Optimal**: 5-7 external links (well-distributed)
- **Maximum**: 10 external links (avoid over-linking)

### Source Quality Requirements

**Use Source Verification Hierarchy (from content_quality_assurance.md):**

**Tier 1 Sources (Most Authoritative):**
- Official government websites (.gov): USPTO, NHTSA, FMCSA
- Official company press releases: Waabi.ai, Aurora.tech, Tesla.com
- SEC filings: 10-K, 10-Q, 8-K reports
- Academic journals: IEEE, ACM, peer-reviewed papers

**Tier 2 Sources (Reputable):**
- Major tech news: TechCrunch, The Verge, Reuters Technology
- Industry publications: FreightWaves, SAE International, Automotive News
- Analyst reports: McKinsey, Gartner, CB Insights
- Verified databases: Crunchbase, PitchBook

**Tier 3 Sources (Use with caution, verify with second source):**
- General news: CNN, Bloomberg, Wall Street Journal
- Expert blogs: Named industry experts with credentials
- Professional forums: Reddit (r/SelfDrivingCars), Hacker News

**NEVER Link To:**
- Wikipedia (use Wikipedia's sources instead)
- Content farms or low-quality sites
- Unverified social media posts
- Competitors offering similar services
- Questionable or biased sources

### When to Link Externally

**Always link when citing:**
1. **Specific statistics or data**
   - Example: "AV market projected to reach $X billion (McKinsey Report 2024)"
   - Link to: Original McKinsey report PDF or webpage

2. **Company announcements or funding news**
   - Example: "Waabi raised $200M Series B in June 2024"
   - Link to: Official Waabi press release or Crunchbase

3. **Regulatory information**
   - Example: "NHTSA requires safety self-assessment reports for Level 4 AVs"
   - Link to: NHTSA.gov official guidance document

4. **Patents (other than your own)**
   - Example: "Aurora's patent portfolio includes 500+ grants"
   - Link to: USPTO search results or Google Patents

5. **Research papers or technical studies**
   - Example: "Camera-based systems achieve 95% accuracy (MIT study 2024)"
   - Link to: MIT research paper or IEEE publication

6. **Industry standards**
   - Example: "SAE Level 4 autonomous vehicles require no human intervention"
   - Link to: SAE International standards page

### Anchor Text for External Links

**Preferred Approach:** Natural, descriptive anchor text

**Examples:**

**Good:**
- "According to [Waabi's official press release], the company raised..."
- "The [NHTSA safety guidance document] requires AV companies to..."
- "[McKinsey's 2024 AV market report] projects that..."

**Bad:**
- "According to [this source], the company raised..."
- "The [regulations] require AV companies to..."
- "[Click here] to read the report"

**Best Practice:**
- Anchor text describes the destination (source type or organization)
- Link opens in new tab (target="_blank" rel="noopener")
- Link is part of natural sentence flow

### External Link Placement

**Best Locations:**
1. **In-text citations** (immediately after claim or data point)
   - Example: "Waabi raised $200M in June 2024 (source)."

2. **Parenthetical references**
   - Example: "The AV market is projected to reach $500B by 2030 (McKinsey, 2024)."

3. **Inline source mentions**
   - Example: "According to NHTSA guidance, Level 4 AVs must submit safety reports."

**Avoid:**
- Footnote-style references at page bottom (less UX-friendly)
- Link-only sentences without context
- Linking from unrelated keywords

### Link Attributes

**Required Attributes:**

```html
<a href="https://example.com" target="_blank" rel="noopener">Link Text</a>
```

- `target="_blank"`: Opens in new tab (keeps visitors on your site)
- `rel="noopener"`: Security measure (prevents new page from accessing window.opener)

**Optional Attributes (Special Cases):**

```html
<a href="https://example.com" target="_blank" rel="noopener nofollow">Link Text</a>
```

- `rel="nofollow"`: Use for untrusted sources or paid links (not Tier 1/2 sources)

**When to use nofollow:**
- User-generated content (if applicable)
- Paid links or sponsorships
- Tier 3 sources with uncertain quality
- Login pages or registration forms

**When NOT to use nofollow:**
- Tier 1 authoritative sources (USPTO, NHTSA, official companies)
- Tier 2 reputable sources (TechCrunch, Reuters, McKinsey)
- Academic citations (IEEE, arXiv)

### External Linking Best Practices

**DO:**
- Link to original sources (not secondary coverage)
- Verify links work before publishing (no 404s)
- Use HTTPS links when available (security)
- Open external links in new tab
- Include rel="noopener" for security
- Cite publication date in text if relevant
- Update broken links quarterly

**DON'T:**
- Link to competitors offering similar services
- Use nofollow on all external links (hurts SEO)
- Link to low-quality or questionable sources
- Cite Wikipedia directly (use their sources)
- Link excessively (5-7 per page is enough)
- Link to outdated information (check dates)
- Use shortened URLs (bit.ly, etc.) - looks unprofessional

### External Link Audit Checklist

For each landing page:
- [ ] 5-7 external links to authoritative sources
- [ ] All links to Tier 1 or Tier 2 sources (per content_quality_assurance.md)
- [ ] All links verified working (no 404 errors)
- [ ] All links use HTTPS (when available)
- [ ] All links open in new tab (target="_blank")
- [ ] All links include rel="noopener"
- [ ] Nofollow only used on Tier 3 or untrusted sources
- [ ] Anchor text descriptive (not "click here")
- [ ] Links cited in context (after specific claims)
- [ ] No links to competitors or low-quality sites

---

## 7. Schema.org Structured Data

### Purpose of Structured Data

**Benefits:**
- Helps Google understand page content and context
- Enables rich snippets in search results (star ratings, FAQs, etc.)
- Improves click-through rate (CTR) from search results
- Enhances visibility in Knowledge Graph and featured snippets
- Required for some Google search features (HowTo, FAQ, etc.)

### Schema Types for Landing Pages

**Primary Schema: Article**
- Use for: All 5 landing pages (they are informational articles)
- Format: JSON-LD (recommended by Google)
- Placement: In `<head>` section of HTML

**Secondary Schema: FAQPage** (if page includes FAQ section)
- Use for: Pages with Q&A sections
- Required: Minimum 2 questions with answers

**Tertiary Schema: HowTo** (if page includes step-by-step guide)
- Use for: Pages with procedural content ("How to strengthen your patent portfolio")
- Required: Minimum 2 steps

**Sitewide Schema: Organization**
- Use for: All pages (describes the organization/website)
- Placement: In `<head>` section of HTML

**Navigation Schema: BreadcrumbList**
- Use for: All pages with breadcrumb navigation
- Placement: In `<head>` section of HTML

---

### Article Schema Template

**Required for:** All 5 landing pages

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[H1 Heading - Max 110 characters]",
  "description": "[Meta description or first paragraph excerpt]",
  "image": "[URL to featured image if any]",
  "author": {
    "@type": "Organization",
    "name": "AV Navigation IP Protection"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AV Navigation IP Protection",
    "logo": {
      "@type": "ImageObject",
      "url": "[URL to logo]"
    }
  },
  "datePublished": "2025-10-16T10:00:00+00:00",
  "dateModified": "2025-10-16T10:00:00+00:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[Full URL to this page]"
  },
  "articleSection": "Autonomous Vehicle Patent Licensing",
  "keywords": "[Primary keyword, secondary keyword 1, secondary keyword 2]"
}
</script>
```

**Example (Autonomous Trucking Page):**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Defensive Patent Strategy for Autonomous Trucking: Camera-Based Navigation IP",
  "description": "Strengthen your autonomous trucking patent portfolio with camera-based navigation IP. Licensed patents are faster and cheaper than in-house development.",
  "image": "https://example.com/assets/images/trucking-patent-feature.jpg",
  "author": {
    "@type": "Organization",
    "name": "AV Navigation IP Protection"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AV Navigation IP Protection",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/assets/images/logo.png"
    }
  },
  "datePublished": "2025-10-16T10:00:00+00:00",
  "dateModified": "2025-10-16T10:00:00+00:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/autonomous-trucking-patent-defense-strategy.html"
  },
  "articleSection": "Autonomous Trucking Patent Strategy",
  "keywords": "autonomous trucking patent defense strategy, commercial vehicle AV patent licensing, trucking autonomous navigation patents"
}
</script>
```

---

### FAQPage Schema Template

**Use when:** Page includes FAQ section with 2+ questions

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text exactly as appears on page]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text exactly as appears on page - HTML allowed]"
      }
    },
    {
      "@type": "Question",
      "name": "[Question 2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer 2]"
      }
    }
  ]
}
</script>
```

**Example (FAQ Section):**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does patent licensing take compared to in-house development?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patent licensing typically takes 4-9 months from initial due diligence to integration, compared to 30-66 months for in-house patent development. This includes due diligence (1-2 months), negotiation (1-3 months), and integration (2-4 months)."
      }
    },
    {
      "@type": "Question",
      "name": "What types of patent licenses are available for autonomous trucking applications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three main types of patent licenses are available: 1) Non-exclusive licenses for defensive IP positioning, 2) Exclusive licenses (field-of-use: commercial trucking) for competitive advantage, and 3) Cross-licensing agreements for companies with existing patent portfolios."
      }
    }
  ]
}
</script>
```

---

### HowTo Schema Template

**Use when:** Page includes step-by-step procedural content

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[Name of the how-to process]",
  "description": "[Brief description of what this teaches]",
  "step": [
    {
      "@type": "HowToStep",
      "name": "[Step 1 name]",
      "text": "[Detailed step 1 instructions]",
      "position": 1
    },
    {
      "@type": "HowToStep",
      "name": "[Step 2 name]",
      "text": "[Detailed step 2 instructions]",
      "position": 2
    }
  ]
}
</script>
```

**Example (Next Steps Section):**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Strengthen Your Autonomous Trucking Patent Portfolio",
  "description": "Step-by-step guide for autonomous trucking startups to conduct patent gap analysis and license camera-based navigation patents.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Conduct Patent Portfolio Gap Analysis",
      "text": "Audit existing patents and applications. Identify gaps in camera-based navigation, safety systems, and fleet management. Compare your portfolio to competitors like Aurora, Waabi, and Waymo Via.",
      "position": 1
    },
    {
      "@type": "HowToStep",
      "name": "Evaluate Licensing Opportunities",
      "text": "Review US Patent 12,001,207 B2 applicability to your trucking systems. Request technical specifications and claim charts. Assess integration effort and timeline.",
      "position": 2
    },
    {
      "@type": "HowToStep",
      "name": "Prepare for Investor Due Diligence",
      "text": "Document all patents and pending applications. Create IP strategy presentation for investors. Quantify patent portfolio impact on company valuation.",
      "position": 3
    }
  ]
}
</script>
```

---

### Organization Schema Template

**Use:** Sitewide (include on all pages)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AV Navigation IP Protection",
  "url": "https://[domain]",
  "logo": "https://[domain]/assets/images/logo.png",
  "description": "Patent licensing for autonomous vehicle camera-based navigation and safety systems. US Patent 12,001,207 B2 available for exclusive and non-exclusive licensing.",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Sales",
    "email": "[contact email]",
    "availableLanguage": ["English"]
  },
  "sameAs": [
    "[LinkedIn URL if applicable]",
    "[Twitter URL if applicable]"
  ]
}
</script>
```

---

### BreadcrumbList Schema Template

**Use:** All pages with breadcrumb navigation

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://[domain]/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Page Category or Section]",
      "item": "https://[domain]/[category].html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Current Page Name]",
      "item": "https://[domain]/[current-page].html"
    }
  ]
}
</script>
```

**Example (Trucking Page):**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Patent Licensing Solutions",
      "item": "https://example.com/licensing.html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Autonomous Trucking Patent Defense Strategy",
      "item": "https://example.com/autonomous-trucking-patent-defense-strategy.html"
    }
  ]
}
</script>
```

---

### Structured Data Best Practices

**DO:**
- Use JSON-LD format (easiest to implement, Google-recommended)
- Place schemas in `<head>` section of HTML
- Include all required properties for each schema type
- Validate with Google Rich Results Test before publishing
- Use accurate, factual information (no exaggerations)
- Match schema content to visible page content (Google requirement)
- Use multiple schema types when appropriate (Article + FAQPage)

**DON'T:**
- Hide content in schema that's not visible on page (Google penalty)
- Use schema for manipulative purposes (fake reviews, etc.)
- Include outdated information (update dateModified when editing)
- Use deprecated schema types (check schema.org for current specs)
- Forget to validate (broken schema = no rich snippets)
- Over-markup (not every sentence needs schema)

### Structured Data Testing & Validation

**Tools:**
1. **Google Rich Results Test**: https://search.google.com/test/rich-results
   - Use this to validate all schemas before publishing
   - Shows preview of how rich snippet will appear

2. **Schema Markup Validator**: https://validator.schema.org/
   - Validates JSON-LD syntax and structure
   - Checks for required properties

3. **Google Search Console**:
   - After publishing, monitor "Enhancements" report
   - Shows errors, warnings, and valid items
   - Alerts to schema issues

### Structured Data Checklist

For each landing page:
- [ ] Article schema implemented (required)
- [ ] FAQPage schema implemented (if FAQ section present)
- [ ] HowTo schema implemented (if step-by-step guide present)
- [ ] Organization schema implemented (sitewide)
- [ ] BreadcrumbList schema implemented (if breadcrumbs present)
- [ ] All schemas validated with Google Rich Results Test
- [ ] All required properties included
- [ ] Schema content matches visible page content
- [ ] DatePublished and dateModified accurate
- [ ] Image URLs valid (if images included)

---

## 8. URL Structure & Canonical URLs

### URL Structure Requirements

**Format:**
```
https://[domain]/[page-name].html
```

**Examples:**
- https://example.com/autonomous-trucking-patent-defense-strategy.html
- https://example.com/series-a-av-patent-portfolio-strategy.html
- https://example.com/tesla-fsd-competitor-camera-patent-licensing.html

### URL Best Practices

**DO:**
- Use lowercase letters only (never "MyPage.html")
- Separate words with hyphens (not underscores or spaces)
- Keep URLs under 100 characters
- Include primary keyword in URL
- Use descriptive, readable URLs
- Use .html extension (consistent with existing site)
- Match file name to URL slug

**DON'T:**
- Use query parameters for content pages (?page=trucking)
- Include session IDs or tracking codes in URL
- Use dates in URLs (/2025/10/trucking-patent.html) - makes content seem dated
- Use numbers (/page-123.html) - not descriptive
- Use special characters (#, %, &, etc.) except hyphens
- Create excessively long URLs (>100 characters)
- Change URLs after publishing (creates 301 redirect needs)

### URL Length Optimization

**Character Count Guidelines:**
- **Optimal**: 50-70 characters (readable, SEO-friendly)
- **Maximum**: 100 characters (Google may truncate in SERPs)
- **Minimum**: 30 characters (too short looks suspicious)

**Example Analysis:**

| URL | Length | Assessment |
|-----|--------|------------|
| /trucking-patent.html | 21 chars | Too short (not descriptive) |
| /autonomous-trucking-patent-defense-strategy.html | 53 chars | Optimal (descriptive, includes keyword) |
| /autonomous-trucking-patent-defense-strategy-for-startups-and-established-companies.html | 95 chars | Too long (truncated in SERPs) |

### Canonical URL Implementation

**Purpose:**
- Tells search engines which version of a page is "canonical" (primary)
- Prevents duplicate content issues
- Consolidates ranking signals to one URL

**Required for:** All pages

**Implementation:**
```html
<link rel="canonical" href="https://[domain]/[page-name].html" />
```

**Placement:** In `<head>` section of HTML

**Example:**
```html
<link rel="canonical" href="https://example.com/autonomous-trucking-patent-defense-strategy.html" />
```

### Self-Referencing Canonical

**Standard Practice:** Every page should have a self-referencing canonical URL

**Why:**
- Prevents duplicate content issues if page accessed via different parameters
- Consolidates ranking signals even if URL has tracking parameters
- Best practice even for pages with no duplicates

**Example Scenarios:**

**Scenario 1: UTM Parameters**
- User visits: `/trucking-patent.html?utm_source=linkedin&utm_campaign=october`
- Canonical URL: `/trucking-patent.html` (without parameters)
- Result: Google indexes only canonical version

**Scenario 2: HTTPS vs HTTP**
- Page accessible at both `http://` and `https://`
- Canonical URL: `https://example.com/trucking-patent.html` (HTTPS version)
- Result: Google indexes only HTTPS version

**Scenario 3: www vs non-www**
- Page accessible at both `www.example.com` and `example.com`
- Canonical URL: Choose one version consistently (e.g., non-www)
- Result: All ranking signals consolidated to chosen version

### Canonical URL Best Practices

**DO:**
- Use absolute URLs (full URL with domain, not relative paths)
- Use HTTPS (not HTTP)
- Match exact URL structure (including .html extension)
- Use self-referencing canonical on every page
- Be consistent across all pages (same domain format: www or non-www)

**DON'T:**
- Use relative paths (/trucking-patent.html) - use full URL
- Canonical to different content (must be same or very similar content)
- Change canonical URL after publishing (breaks SEO signals)
- Forget canonical on new pages

### URL Structure Checklist

For each landing page:
- [ ] URL format: /[page-name].html
- [ ] URL length: 50-70 characters (optimal)
- [ ] Primary keyword in URL
- [ ] Lowercase letters only
- [ ] Hyphens separating words (not underscores)
- [ ] No special characters (except hyphens)
- [ ] Canonical URL implemented (self-referencing)
- [ ] Canonical URL uses HTTPS
- [ ] Canonical URL absolute (full domain)
- [ ] Canonical URL matches exact page URL

---

## 9. Open Graph & Twitter Card Tags

### Purpose of Social Meta Tags

**Benefits:**
- Control how content appears when shared on social media
- Increase click-through rate from social platforms
- Improve brand presentation and professionalism
- Enable rich previews (images, descriptions, titles)

### Open Graph Tags (Facebook, LinkedIn, WhatsApp, etc.)

**Required for:** All pages

**Implementation:**
```html
<meta property="og:title" content="[Page title optimized for social sharing]" />
<meta property="og:description" content="[Compelling description for social preview]" />
<meta property="og:type" content="article" />
<meta property="og:url" content="[Full canonical URL]" />
<meta property="og:image" content="[Full URL to featured image]" />
<meta property="og:site_name" content="AV Navigation IP Protection" />
<meta property="og:locale" content="en_US" />
```

**Image Requirements:**
- **Minimum size**: 1200 x 630 pixels (Facebook recommended)
- **Aspect ratio**: 1.91:1 (landscape)
- **File format**: JPG or PNG
- **File size**: <8 MB
- **Content**: Relevant to page topic, includes text overlay if possible

**Example (Autonomous Trucking Page):**

```html
<meta property="og:title" content="Autonomous Trucking Patent Defense Strategy | Camera-Based Navigation IP" />
<meta property="og:description" content="Strengthen your trucking patent portfolio with licensed camera-based navigation patents. Faster and cheaper than in-house development (4-9 months vs 30-66 months)." />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://example.com/autonomous-trucking-patent-defense-strategy.html" />
<meta property="og:image" content="https://example.com/assets/images/trucking-patent-og-image.jpg" />
<meta property="og:site_name" content="AV Navigation IP Protection" />
<meta property="og:locale" content="en_US" />
```

### Twitter Card Tags

**Required for:** All pages

**Implementation (Summary Large Image card):**
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="[Page title optimized for Twitter]" />
<meta name="twitter:description" content="[Compelling description for Twitter preview]" />
<meta name="twitter:image" content="[Full URL to featured image]" />
<meta name="twitter:site" content="[@TwitterHandle if applicable]" />
<meta name="twitter:creator" content="[@AuthorTwitterHandle if applicable]" />
```

**Card Types:**
- **summary_large_image**: Large image display (recommended for landing pages)
- **summary**: Smaller image display
- **app**: Mobile app promotion
- **player**: Video/audio content

**Image Requirements:**
- **Minimum size**: 1200 x 628 pixels (summary_large_image)
- **Aspect ratio**: 2:1 (landscape)
- **File format**: JPG, PNG, WEBP, GIF
- **File size**: <5 MB
- **Content**: Same as Open Graph image (can reuse)

**Example (Autonomous Trucking Page):**

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Autonomous Trucking Patent Defense Strategy" />
<meta name="twitter:description" content="Licensed camera-based navigation patents for Class 8 trucks. Strengthen your patent portfolio in 4-9 months vs. 30-66 months for in-house development." />
<meta name="twitter:image" content="https://example.com/assets/images/trucking-patent-twitter-card.jpg" />
```

### Title & Description Optimization for Social

**Differences from SEO Title/Description:**

| Element | SEO Version | Social Version |
|---------|-------------|----------------|
| **Title Length** | 55-60 characters | 60-70 characters (more space) |
| **Description Length** | 155-160 characters | 200-300 characters (Facebook), 200 characters (Twitter) |
| **Tone** | Keyword-focused, informative | Engaging, benefit-driven, conversational |
| **Keywords** | Primary keyword required | Keywords helpful but not required |
| **Call-to-Action** | Subtle | Can be more direct |

**Example Comparison (Trucking Page):**

**SEO Title (60 chars):**
```
Autonomous Trucking Patent Defense Strategy | US 12,001,207
```

**Social Title (67 chars):**
```
How to Build a Defensive Patent Strategy for Autonomous Trucking
```

**SEO Description (159 chars):**
```
Strengthen your autonomous trucking patent portfolio with camera-based navigation IP. Licensed patents = faster, cheaper than in-house development. Schedule consultation.
```

**Social Description (248 chars):**
```
Autonomous trucking startups: Strengthen your patent portfolio with licensed camera-based navigation IP from US Patent 12,001,207. Get defensive IP protection in 4-9 months (vs. 30-66 months for in-house development). Learn how →
```

### Social Meta Tags Best Practices

**DO:**
- Include both Open Graph and Twitter Card tags (cover all platforms)
- Use compelling, benefit-driven titles for social (not just keywords)
- Create custom images for social sharing (1200 x 630 px minimum)
- Include specific data or stats in descriptions ("4-9 months")
- Use consistent branding across all social images
- Test with Facebook Debugger and Twitter Card Validator

**DON'T:**
- Reuse exact SEO title/description (optimize for each context)
- Use generic stock images (custom branded images perform better)
- Forget image alt text (Open Graph doesn't need it, but Twitter does)
- Use low-resolution images (<1200px width)
- Include UTM parameters in og:url (use clean canonical URL)

### Testing Tools

**Facebook/LinkedIn:**
1. **Facebook Sharing Debugger**: https://developers.facebook.com/tools/debug/
   - Paste URL to see preview
   - Shows all Open Graph tags detected
   - Click "Scrape Again" to refresh cache after changes

**Twitter:**
1. **Twitter Card Validator**: https://cards-dev.twitter.com/validator
   - Paste URL to see preview
   - Shows all Twitter Card tags detected
   - Preview how card will appear in timeline

**LinkedIn:**
1. **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/
   - Paste URL to see preview
   - Shows how content will appear when shared on LinkedIn
   - Clear cache if changes not appearing

### Social Meta Tags Checklist

For each landing page:
- [ ] Open Graph title implemented (og:title)
- [ ] Open Graph description implemented (og:description)
- [ ] Open Graph type implemented (og:type = "article")
- [ ] Open Graph URL implemented (og:url - canonical URL)
- [ ] Open Graph image implemented (og:image - 1200 x 630 px minimum)
- [ ] Open Graph site name implemented (og:site_name)
- [ ] Twitter Card type implemented (twitter:card = "summary_large_image")
- [ ] Twitter title implemented (twitter:title)
- [ ] Twitter description implemented (twitter:description)
- [ ] Twitter image implemented (twitter:image - same as OG image)
- [ ] Social title different from SEO title (optimized for engagement)
- [ ] Social description different from meta description (more detail, benefit-driven)
- [ ] Custom branded image created (not generic stock photo)
- [ ] Tested with Facebook Debugger (renders correctly)
- [ ] Tested with Twitter Card Validator (renders correctly)
- [ ] Tested with LinkedIn Post Inspector (renders correctly)

---

## 10. Mobile Optimization

### Responsive Design Requirements

**Framework:** Bootstrap 5 (already implemented sitewide)

**Viewport Meta Tag (Required):**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Purpose:**
- Ensures page scales correctly on mobile devices
- Prevents horizontal scrolling
- Makes text readable without zooming

### Mobile-Friendly Design Principles

**1. Responsive Grid System**
- Use Bootstrap's 12-column grid
- Stack columns on mobile (<768px breakpoint)
- Use responsive utilities (col-md-6, col-sm-12)

**Example:**
```html
<div class="row">
  <div class="col-md-6 col-sm-12">
    <!-- Content: 2 columns on desktop, 1 column on mobile -->
  </div>
  <div class="col-md-6 col-sm-12">
    <!-- Content: 2 columns on desktop, 1 column on mobile -->
  </div>
</div>
```

**2. Readable Font Sizes**
- **Body text**: 16px minimum (18px optimal for readability)
- **Headings**: Scale proportionally (H1: 28-32px, H2: 24-28px, H3: 20-24px on mobile)
- **Line height**: 1.5-1.7 (improves readability)
- **Paragraph width**: <75 characters per line on mobile

**3. Touch-Friendly Elements**
- **Buttons**: Minimum 44 x 44 pixels (Apple guideline) or 48 x 48 pixels (Google guideline)
- **Links**: Adequate spacing between links (minimum 8px padding)
- **Forms**: Large input fields (minimum 44px height)

**Bootstrap Button Classes (already touch-friendly):**
```html
<a href="/contact.html" class="btn btn-primary btn-lg">Schedule Consultation</a>
```

**4. Avoid Horizontal Scrolling**
- All content fits within viewport width
- Tables use responsive wrappers
- Images scale proportionally

**Responsive Table Example:**
```html
<div class="table-responsive">
  <table class="table">
    <!-- Table content -->
  </table>
</div>
```

**5. Fast-Loading Images**
- Use responsive images (multiple sizes)
- Lazy loading for images below fold
- Optimize file sizes (use WebP format when possible)

**Example:**
```html
<img src="image-800w.jpg"
     srcset="image-400w.jpg 400w, image-800w.jpg 800w, image-1200w.jpg 1200w"
     sizes="(max-width: 768px) 100vw, 50vw"
     alt="Descriptive alt text"
     loading="lazy">
```

### Mobile UX Considerations

**Navigation:**
- Hamburger menu on mobile (<768px)
- Easy-to-tap menu items
- Fixed or sticky header (optional, test for usability)

**CTAs:**
- Primary CTA visible above fold on mobile
- Sticky CTA at bottom on mobile (optional)
- Large, obvious buttons (use Bootstrap .btn-lg)

**Content:**
- Short paragraphs (2-4 sentences maximum)
- Bullet points for scannability
- Collapsible sections for long content (Bootstrap accordion)

**Forms:**
- One column layout on mobile
- Large input fields (44px minimum height)
- Clear labels above inputs (not placeholder-only)
- Submit button full-width on mobile

### Mobile Testing Requirements

**Devices to Test:**
1. **iPhone (iOS)**: Latest iOS version, Safari browser
2. **Android (Samsung/Pixel)**: Latest Android version, Chrome browser
3. **Tablet (iPad or Android tablet)**: Landscape and portrait

**Testing Tools:**

**1. Google Mobile-Friendly Test**
- URL: https://search.google.com/test/mobile-friendly
- Checks if page is mobile-friendly
- Shows preview of how Googlebot sees mobile page
- Identifies issues (text too small, links too close, etc.)

**2. Chrome DevTools Device Mode**
- Open Chrome DevTools (F12)
- Click "Toggle device toolbar" (Ctrl+Shift+M)
- Test multiple device sizes:
  - iPhone SE (375 x 667)
  - iPhone 12 Pro (390 x 844)
  - Samsung Galaxy S20 (360 x 800)
  - iPad (768 x 1024)

**3. BrowserStack or Similar**
- Test on real devices (not just emulators)
- Check iOS and Android differences
- Verify touch interactions work correctly

### Mobile Performance Requirements

**Page Speed Targets:**
- **Largest Contentful Paint (LCP)**: <2.5 seconds
- **First Input Delay (FID)**: <100 milliseconds
- **Cumulative Layout Shift (CLS)**: <0.1

**Core Web Vitals are now ranking factors - prioritize mobile speed!**

**Optimization Techniques:**
1. Minimize CSS/JS (Bootstrap minified version)
2. Lazy load images below fold
3. Use CDN for Bootstrap and static assets
4. Enable GZIP compression
5. Minimize HTTP requests
6. Use browser caching

### Mobile Optimization Checklist

For each landing page:
- [ ] Viewport meta tag implemented
- [ ] Responsive design (Bootstrap grid system)
- [ ] Font sizes readable (16px minimum body text)
- [ ] Touch-friendly buttons (44 x 44 px minimum)
- [ ] No horizontal scrolling on any device size
- [ ] Tables use responsive wrappers (.table-responsive)
- [ ] Images responsive (scale to fit viewport)
- [ ] CTAs visible and prominent on mobile
- [ ] Navigation works on mobile (hamburger menu)
- [ ] Forms one-column layout on mobile
- [ ] Tested on iPhone (Safari) and Android (Chrome)
- [ ] Passed Google Mobile-Friendly Test
- [ ] Core Web Vitals pass (LCP <2.5s, FID <100ms, CLS <0.1)
- [ ] Page loads <3 seconds on mobile (4G connection)

---

## 11. Page Speed Requirements

### Performance Targets

**Google PageSpeed Insights Scores:**
- **Mobile**: >85/100 (target: 90+)
- **Desktop**: >90/100 (target: 95+)

**Core Web Vitals (Required for Ranking):**

| Metric | Description | Target |
|--------|-------------|--------|
| **Largest Contentful Paint (LCP)** | Time for largest element to load | <2.5 seconds |
| **First Input Delay (FID)** | Time for page to respond to first interaction | <100 milliseconds |
| **Cumulative Layout Shift (CLS)** | Visual stability (elements don't jump around) | <0.1 |

**Additional Metrics:**

| Metric | Description | Target |
|--------|-------------|--------|
| **First Contentful Paint (FCP)** | Time for first text/image to appear | <1.8 seconds |
| **Time to Interactive (TTI)** | Time until page is fully interactive | <3.8 seconds |
| **Total Blocking Time (TBT)** | Time page is blocked from user input | <200 milliseconds |
| **Speed Index** | How quickly content is visually displayed | <3.4 seconds |

### Optimization Strategies

**1. Minimize HTTP Requests**
- Combine CSS files (Bootstrap + custom styles)
- Combine JavaScript files
- Use CSS sprites for multiple small images
- Remove unused CSS/JS

**Current Setup:**
- Bootstrap 5 (minified CDN version)
- Minimal custom CSS
- No heavy JavaScript frameworks

**2. Enable Compression**
- GZIP or Brotli compression for text assets
- Reduces file size by 60-80%

**Server Configuration (Apache .htaccess):**
```apache
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json
</IfModule>
```

**3. Optimize Images**
- Use modern formats: WebP (70-80% smaller than JPEG)
- Compress images: TinyPNG, ImageOptim, or similar
- Lazy load images below fold
- Use responsive images (srcset)

**Target Image Sizes:**
- Hero images: <200 KB
- In-content images: <100 KB
- Icons/logos: <50 KB

**4. Leverage Browser Caching**
- Set long cache times for static assets
- Use versioning for cache busting (e.g., style.css?v=1.2)

**Server Configuration (Apache .htaccess):**
```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
</IfModule>
```

**5. Minimize CSS and JavaScript**
- Use minified versions of Bootstrap (already implemented)
- Minify custom CSS/JS
- Remove unused CSS with PurgeCSS (advanced)

**6. Use CDN for Static Assets**
- Bootstrap from CDN (faster, often cached)
- Font Awesome from CDN (if using icons)

**Current Implementation:**
```html
<!-- Bootstrap 5 CSS from CDN -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap 5 JS from CDN -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

**7. Reduce Server Response Time**
- Optimize database queries (not applicable for static site)
- Use fast hosting (SSD, adequate resources)
- Enable caching at server level

**Target:** <200ms server response time (Time to First Byte)

**8. Avoid Render-Blocking Resources**
- Load CSS in `<head>` (required for rendering)
- Load JavaScript at end of `<body>` or use `async`/`defer`

**Example:**
```html
<!-- Non-blocking JavaScript -->
<script src="script.js" defer></script>
```

**9. Optimize Critical Rendering Path**
- Inline critical CSS (above-the-fold styles)
- Defer non-critical CSS
- Preload key resources

**Example:**
```html
<!-- Preload critical font -->
<link rel="preload" href="/fonts/main-font.woff2" as="font" type="font/woff2" crossorigin>
```

**10. Eliminate Layout Shifts**
- Set width and height attributes on images
- Reserve space for ads or dynamic content
- Use CSS aspect-ratio for responsive images

**Example:**
```html
<img src="image.jpg" alt="Description" width="800" height="600" loading="lazy">
```

### Performance Testing Tools

**1. Google PageSpeed Insights**
- URL: https://pagespeed.web.dev/
- Tests both mobile and desktop
- Shows Core Web Vitals
- Provides specific optimization recommendations

**2. Google Search Console (Core Web Vitals Report)**
- Shows real user data (field data)
- Identifies pages failing Core Web Vitals
- Tracks improvements over time

**3. WebPageTest**
- URL: https://www.webpagetest.org/
- Advanced performance testing
- Shows waterfall chart (resource loading)
- Tests from multiple locations

**4. Chrome DevTools Lighthouse**
- Built into Chrome (F12 → Lighthouse tab)
- Local testing (fast, convenient)
- Comprehensive performance, accessibility, SEO audits

**5. GTmetrix**
- URL: https://gtmetrix.com/
- Combines PageSpeed Insights and YSlow scores
- Provides detailed recommendations
- Monitors performance over time

### Performance Monitoring

**Monthly Performance Audit:**
- Run PageSpeed Insights on all 5 landing pages
- Check Core Web Vitals in Google Search Console
- Identify and fix pages below targets
- Monitor performance trends (improving or degrading?)

**Performance Degradation Causes:**
- New images added without optimization
- New JavaScript plugins added
- Server performance issues
- Increased traffic (server overload)
- External resource slowdowns (CDN issues)

### Page Speed Checklist

For each landing page:
- [ ] Google PageSpeed Insights score >85 (mobile), >90 (desktop)
- [ ] Core Web Vitals pass (LCP <2.5s, FID <100ms, CLS <0.1)
- [ ] Images optimized (<200 KB for hero, <100 KB for in-content)
- [ ] Images use lazy loading (below fold)
- [ ] Images have width/height attributes (prevent CLS)
- [ ] CSS minified (Bootstrap uses minified version)
- [ ] JavaScript deferred or async (non-critical scripts)
- [ ] GZIP compression enabled (server-side)
- [ ] Browser caching enabled (server-side)
- [ ] CDN used for Bootstrap and static assets
- [ ] No render-blocking resources in critical path
- [ ] Server response time <200ms (TTFB)
- [ ] Total page size <3 MB (including all assets)
- [ ] Page loads <3 seconds on 4G mobile connection

---

## 12. YAML Frontmatter Standards

### Purpose of YAML Frontmatter

**Function:**
- Defines metadata for static site generator
- Controls page rendering and templates
- Specifies SEO tags and social meta tags
- Configures page-specific features (CTAs, sidebars, etc.)

**Location:** Top of every Markdown (.md) file, between triple dashes (---)

### Required Fields

```yaml
---
title: "[SEO title - 55-60 characters]"
page_title: "[Display title - can be different/longer than SEO title]"
description: "[Meta description - 155-160 characters]"
keywords:
  - [primary keyword]
  - [secondary keyword 1]
  - [secondary keyword 2]
  - [additional keywords...]
show_cta: [true/false]
cta_text: "[CTA button text]"
cta_link: "[CTA destination URL]"
layout: [page/home/contact]
---
```

### Optional Fields (Recommended for Landing Pages)

```yaml
---
# Required fields (see above)
title: "..."
description: "..."
keywords: [...]
show_cta: true
cta_text: "..."
cta_link: "..."
layout: page

# Optional fields (SEO & Social)
author: "[Author name or organization]"
date: "[YYYY-MM-DD]"
modified: "[YYYY-MM-DD]"
canonical: "[Full canonical URL]"
og_type: "[article/website]"
og_image: "[Full URL to Open Graph image]"
twitter_card: "[summary_large_image/summary]"
schema_type: "[Article/FAQPage/HowTo]"
---
```

### Field Descriptions

**title** (Required)
- SEO title tag (appears in search results)
- Length: 55-60 characters
- Includes primary keyword
- Example: `"Autonomous Trucking Patent Defense Strategy | US 12,001,207"`

**page_title** (Required)
- Display title on page (H1 equivalent or page hero)
- Can be longer/different from SEO title
- More descriptive, benefit-driven
- Example: `"Build Your Defensive Patent Strategy for Autonomous Trucking"`

**description** (Required)
- Meta description (appears in search results)
- Length: 155-160 characters
- Includes primary keyword and CTA
- Example: `"Strengthen your autonomous trucking patent portfolio with camera-based navigation IP. Licensed patents = faster, cheaper than in-house development. Schedule consultation."`

**keywords** (Required)
- List of target keywords for page
- Include primary + 5-10 secondary keywords
- Used for internal tracking (not directly used by Google)
- Example:
  ```yaml
  keywords:
    - autonomous trucking patent defense strategy
    - commercial vehicle AV patent licensing
    - trucking autonomous navigation patents
    - Class 8 truck autonomous patents
  ```

**show_cta** (Required)
- Boolean: true or false
- Controls whether CTA section appears
- Set to `true` for all landing pages

**cta_text** (Required if show_cta: true)
- Text for primary CTA button
- Action-oriented, specific
- Example: `"Schedule Patent Portfolio Consultation"`

**cta_link** (Required if show_cta: true)
- Destination URL for CTA button
- Include UTM parameters for tracking
- Example: `"/contact.html?utm_source=landing&utm_medium=page&utm_campaign=trucking-patent"`

**layout** (Required)
- Specifies which template to use
- Options: `page` (default), `home`, `contact`
- Use `page` for all landing pages

**author** (Optional)
- Author name or organization name
- Used in Article schema
- Example: `"AV Navigation IP Protection"`

**date** (Optional)
- Publication date in YYYY-MM-DD format
- Used in Article schema, visible on page
- Example: `"2025-10-16"`

**modified** (Optional)
- Last modified date in YYYY-MM-DD format
- Updates Article schema dateModified
- Update whenever content is significantly changed
- Example: `"2025-10-16"`

**canonical** (Optional but Recommended)
- Full canonical URL (including https://)
- Prevents duplicate content issues
- Self-referencing for most pages
- Example: `"https://example.com/autonomous-trucking-patent-defense-strategy.html"`

**og_type** (Optional but Recommended)
- Open Graph content type
- Use `"article"` for landing pages
- Use `"website"` for homepage

**og_image** (Optional but Recommended)
- Full URL to Open Graph image (1200 x 630 px)
- Used when page is shared on Facebook, LinkedIn, etc.
- Example: `"https://example.com/assets/images/trucking-patent-og-image.jpg"`

**twitter_card** (Optional but Recommended)
- Twitter Card type
- Use `"summary_large_image"` for landing pages (large image preview)
- Use `"summary"` for pages without featured image

**schema_type** (Optional but Recommended)
- Primary schema type for structured data
- Options: `"Article"`, `"FAQPage"`, `"HowTo"`
- Use `"Article"` for landing pages (default)
- Add `"FAQPage"` if page has FAQ section

---

### Complete YAML Frontmatter Examples

**Example 1: Autonomous Trucking Landing Page**

```yaml
---
title: "Autonomous Trucking Patent Defense Strategy | US 12,001,207"
page_title: "Strengthen Your Autonomous Trucking Patent Portfolio with Camera-Based Navigation Patents"
description: "Licensed camera-based navigation patents for autonomous trucking companies. US Patent 12,001,207 B2 provides defensive IP for Class 8 trucks and commercial fleets. Faster and cheaper than in-house development."
keywords:
  - autonomous trucking patent defense strategy
  - commercial vehicle AV patent licensing
  - trucking autonomous navigation patents
  - freight AV IP protection
  - Class 8 truck autonomous patents
  - camera-based navigation patents for trucks
  - long-haul autonomous vehicle patents
  - logistics AV safety patents
show_cta: true
cta_text: "Schedule Patent Portfolio Consultation"
cta_link: "/contact.html?utm_source=landing&utm_medium=page&utm_campaign=trucking-patent"
layout: page
author: "AV Navigation IP Protection"
date: "2025-10-16"
modified: "2025-10-16"
canonical: "https://example.com/autonomous-trucking-patent-defense-strategy.html"
og_type: "article"
og_image: "https://example.com/assets/images/trucking-patent-og-image.jpg"
twitter_card: "summary_large_image"
schema_type: "Article"
---
```

**Example 2: Series A AV Landing Page**

```yaml
---
title: "Series A AV Patent Portfolio Strategy | US 12,001,207"
page_title: "Build Your Patent Portfolio Before Series B Funding: Strategic Licensing for AV Startups"
description: "Patent portfolio strategy for Series A autonomous vehicle startups. Strengthen IP with licensed camera-based navigation patents before Series B fundraising. 4-9 months vs. 30-66 months in-house development."
keywords:
  - patent portfolio strategy for series A autonomous vehicle startups
  - AV startup IP protection
  - series A patent licensing
  - autonomous vehicle patent portfolio funding
  - defensive patent strategy startups
show_cta: true
cta_text: "Schedule Patent Portfolio Assessment"
cta_link: "/contact.html?utm_source=landing&utm_medium=page&utm_campaign=series-a-av"
layout: page
author: "AV Navigation IP Protection"
date: "2025-10-16"
modified: "2025-10-16"
canonical: "https://example.com/series-a-av-patent-portfolio-strategy.html"
og_type: "article"
og_image: "https://example.com/assets/images/series-a-av-og-image.jpg"
twitter_card: "summary_large_image"
schema_type: "Article"
---
```

**Example 3: VC Due Diligence Landing Page (with FAQ schema)**

```yaml
---
title: "VC AV Patent Portfolio Due Diligence Guide | IP Assessment"
page_title: "The Complete Guide to AV Patent Portfolio Due Diligence for Venture Capital"
description: "Comprehensive guide for VCs evaluating autonomous vehicle patent portfolios. Learn how to assess patent quality, identify IP gaps, and evaluate camera-first technology patents during due diligence."
keywords:
  - AV patent portfolio due diligence for venture capital
  - autonomous vehicle IP due diligence checklist
  - patent portfolio valuation AV startups
  - VC investment IP assessment
show_cta: true
cta_text: "Request Patent Portfolio Analysis Template"
cta_link: "/contact.html?utm_source=landing&utm_medium=page&utm_campaign=vc-dd-guide"
layout: page
author: "AV Navigation IP Protection"
date: "2025-10-16"
modified: "2025-10-16"
canonical: "https://example.com/venture-capital-av-patent-portfolio-due-diligence.html"
og_type: "article"
og_image: "https://example.com/assets/images/vc-dd-guide-og-image.jpg"
twitter_card: "summary_large_image"
schema_type: "Article,FAQPage"
---
```

---

### YAML Best Practices

**DO:**
- Include all required fields (title, description, keywords, show_cta, layout)
- Use double quotes for strings with special characters
- Use proper YAML syntax (key: value format)
- Keep keywords list focused (5-10 keywords maximum)
- Update `modified` date when content changes
- Test frontmatter parsing after changes

**DON'T:**
- Use tabs (use spaces for indentation)
- Forget closing triple dashes (---) after frontmatter
- Include content before frontmatter (frontmatter must be first)
- Use single quotes inconsistently (use double quotes for all strings)
- Include HTML in frontmatter strings (plain text only)
- Forget to escape special characters (colons, quotes)

### YAML Validation

**Common Errors:**

**Error 1: Missing Closing Dashes**
```yaml
---
title: "My Page Title"
description: "My description"
# Missing closing --- below
```

**Fix:** Add closing `---` after all fields

**Error 2: Improper Quoting**
```yaml
title: My Page Title: A Comprehensive Guide
# Colon in value breaks parsing
```

**Fix:** Use quotes for strings with special characters:
```yaml
title: "My Page Title: A Comprehensive Guide"
```

**Error 3: Incorrect List Syntax**
```yaml
keywords:
keyword 1
keyword 2
# Missing hyphens for list items
```

**Fix:**
```yaml
keywords:
  - keyword 1
  - keyword 2
```

---

### YAML Frontmatter Checklist

For each landing page:
- [ ] Frontmatter starts on line 1 (no content before opening ---)
- [ ] Opening triple dashes (---) present
- [ ] Closing triple dashes (---) present
- [ ] All required fields present (title, description, keywords, show_cta, cta_text, cta_link, layout)
- [ ] Title 55-60 characters
- [ ] Description 155-160 characters
- [ ] Keywords list includes 5-10 keywords
- [ ] show_cta set to `true`
- [ ] cta_link includes UTM parameters for tracking
- [ ] layout set to `page`
- [ ] Optional fields included (author, date, canonical, og_image, twitter_card)
- [ ] Proper YAML syntax (key: value, lists with hyphens)
- [ ] Strings with special characters quoted
- [ ] No tabs (spaces only for indentation)
- [ ] Frontmatter validates (no parsing errors)

---

## Implementation Workflow

### Phase 1: Setup (Before Content Creation)

1. **Review this document** - All content creators read full SEO technical specs
2. **Create templates** - Set up YAML frontmatter templates for each landing page
3. **Prepare image assets** - Design Open Graph images (1200 x 630 px) for social sharing
4. **Set up testing tools** - Bookmark Google PageSpeed Insights, Mobile-Friendly Test, Rich Results Test

### Phase 2: Content Creation (During Drafting)

1. **Start with YAML frontmatter** - Fill in all required fields before writing content
2. **Follow heading structure** - 1 H1, 6-8 H2, 15-20 H3 with keywords
3. **Add internal links** - 5-8 internal links with varied anchor text
4. **Add external links** - 3-5 external links to Tier 1/2 sources
5. **Write alt text** - Descriptive alt text (80-100 chars) for all images
6. **Include CTAs** - Primary, secondary, tertiary CTAs with UTM parameters

### Phase 3: Technical SEO Implementation (After Drafting, Before Publishing)

1. **Validate YAML frontmatter** - Check for syntax errors
2. **Implement structured data** - Add Article schema (+ FAQPage/HowTo if applicable)
3. **Add canonical URL** - Self-referencing canonical tag
4. **Add Open Graph tags** - Optimize for social sharing (Facebook, LinkedIn)
5. **Add Twitter Card tags** - Optimize for Twitter sharing
6. **Optimize images** - Compress, convert to WebP, add lazy loading
7. **Test mobile responsiveness** - Chrome DevTools device mode

### Phase 4: Testing & Validation (Before Publishing)

1. **Google Mobile-Friendly Test** - Must pass
2. **Google Rich Results Test** - Validate all structured data
3. **Facebook Sharing Debugger** - Check Open Graph preview
4. **Twitter Card Validator** - Check Twitter Card preview
5. **PageSpeed Insights** - Score >85 mobile, >90 desktop
6. **HTML validator** - No critical errors
7. **Internal link checker** - All internal links work
8. **External link checker** - All external links work

### Phase 5: Post-Publishing (After Go-Live)

1. **Submit to Google Search Console** - Request indexing
2. **Monitor Core Web Vitals** - Check Search Console "Core Web Vitals" report
3. **Track keyword rankings** - Monitor primary/secondary keyword positions
4. **Analyze user behavior** - Google Analytics (bounce rate, time on page, conversions)
5. **Update content quarterly** - Refresh data, re-verify facts, update dateModified

---

## Quick Reference Checklist

### Per-Page Technical SEO Checklist

Print this checklist and use for each landing page:

**Meta Tags:**
- [ ] Title tag (55-60 chars, includes primary keyword)
- [ ] Meta description (155-160 chars, includes CTA)
- [ ] Viewport meta tag (mobile responsiveness)
- [ ] Canonical URL (self-referencing, HTTPS)

**Heading Structure:**
- [ ] Exactly 1 H1 (includes primary keyword)
- [ ] 6-8 H2 sections
- [ ] 15-20 H3 subsections
- [ ] Proper hierarchy (no skipped levels)

**Content Optimization:**
- [ ] 1,800-2,200 words (target range)
- [ ] Primary keyword density 1-2%
- [ ] Secondary keywords distributed naturally
- [ ] LSI keywords included

**Internal Linking:**
- [ ] 5-8 internal links total
- [ ] 2-3 links to patent-details.md
- [ ] 2-3 links to licensing.md
- [ ] 1-2 links to industry-insights.md
- [ ] 3-4 CTA links to contact.md
- [ ] Varied anchor text (no duplicates)

**External Linking:**
- [ ] 3-5 external links to authoritative sources
- [ ] All links Tier 1 or Tier 2 quality
- [ ] All links verified working (no 404s)
- [ ] All links open in new tab (target="_blank")
- [ ] All links include rel="noopener"

**Images:**
- [ ] All images optimized (<200 KB hero, <100 KB in-content)
- [ ] All images have alt text (80-100 chars)
- [ ] All images have width/height attributes
- [ ] Lazy loading enabled (below fold images)

**Structured Data:**
- [ ] Article schema implemented
- [ ] FAQPage schema (if FAQ section present)
- [ ] HowTo schema (if step-by-step guide present)
- [ ] Organization schema (sitewide)
- [ ] Validated with Google Rich Results Test

**Social Meta Tags:**
- [ ] Open Graph title, description, image, type, URL
- [ ] Twitter Card title, description, image, card type
- [ ] Custom branded image (1200 x 630 px minimum)
- [ ] Tested with Facebook Debugger
- [ ] Tested with Twitter Card Validator

**Mobile Optimization:**
- [ ] Viewport meta tag present
- [ ] Responsive design (Bootstrap grid)
- [ ] Touch-friendly buttons (44 x 44 px minimum)
- [ ] No horizontal scrolling
- [ ] Font sizes readable (16px minimum)
- [ ] Passed Google Mobile-Friendly Test

**Page Speed:**
- [ ] PageSpeed Insights score >85 mobile, >90 desktop
- [ ] Core Web Vitals pass (LCP <2.5s, FID <100ms, CLS <0.1)
- [ ] Images compressed and lazy loaded
- [ ] GZIP compression enabled
- [ ] Browser caching enabled
- [ ] Page loads <3 seconds (mobile)

**YAML Frontmatter:**
- [ ] All required fields present
- [ ] Title 55-60 characters
- [ ] Description 155-160 characters
- [ ] Keywords list (5-10 keywords)
- [ ] show_cta set to true
- [ ] cta_link includes UTM parameters
- [ ] Optional fields included (canonical, og_image, etc.)
- [ ] Proper YAML syntax (validates)

---

## Document Maintenance

### Update Schedule

**Monthly:**
- Review new Google algorithm updates (affects ranking factors)
- Check if any technical SEO best practices changed
- Update page speed targets if Google changes Core Web Vitals

**Quarterly:**
- Audit all 5 landing pages against this checklist
- Update examples if new landing pages created
- Add new schema types if Google releases new ones

**Annually:**
- Full document review (comprehensive update)
- Archive outdated sections
- Update benchmarks and targets based on industry standards

### Version History

**Version 1.0** - October 16, 2025
- Initial creation
- Comprehensive technical SEO specifications for Phase 3 landing pages
- Covers all aspects: meta tags, headings, links, schema, mobile, speed, YAML

**Next Review:** January 16, 2026 (Quarterly)

---

## Related Documentation

- **Keyword Research**: `/docs/landing-pages-keyword-research.md`
- **Content Briefs**: `/docs/content-briefs/[page-name]-brief.md`
- **Content Quality Assurance**: `/.agent/SOP/content_quality_assurance.md`
- **Content Management**: `/.agent/SOP/content_management.md`
- **Site Generation & Deployment**: `/.agent/SOP/site_generation_deployment.md`
- **Phase 3 Task Document**: `/.agent/Tasks/seo_landing_pages_phase3.md`

---

**Document Status:** Complete - Ready for Implementation
**Created:** October 16, 2025
**Last Updated:** October 16, 2025
**Next Review:** January 16, 2026

---

## End of SEO Technical Specifications Document
