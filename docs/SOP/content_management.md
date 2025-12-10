# Standard Operating Procedure: Content Management

## Overview

This SOP defines best practices for creating, editing, and managing content for the AV Navigation IP Protection website. The website uses a Markdown-based content system with YAML frontmatter for metadata.

## ⚠️ CRITICAL: Understanding the Static Site Generation Workflow

**This is a GENERATED static website. Understanding the workflow is essential:**

### Source vs. Generated Files

**✅ ALWAYS EDIT: Markdown Source Files**
- **Location:** `/website/content/*.md`
- **Format:** Markdown with YAML frontmatter
- **Examples:** `index.md`, `patent-details.md`, `licensing.md`
- **Purpose:** These are the SOURCE files you edit

**❌ NEVER EDIT: Generated HTML Files**
- **Location:** `/website/build/*.html`
- **Format:** Auto-generated HTML
- **Examples:** `index.html`, `patent-details.html`, `licensing.html`
- **Purpose:** These are OUTPUT files created by `generate_site.py`
- **⚠️ WARNING:** Any edits to HTML files will be OVERWRITTEN on next generation

### The Generation Process

```
┌─────────────────────────────────────┐
│  1. Edit Markdown Source Files      │
│     /website/content/*.md            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  2. Run Site Generator               │
│     python generate_site.py          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  3. HTML Files Generated/Updated     │
│     /website/build/*.html            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  4. View Changes in Browser          │
│     http://localhost:8000            │
└─────────────────────────────────────┘
```

### Typical Development Setup

**User usually runs:**
```bash
cd website/build
python -m http.server 8000
```

**This means:**
- Local web server is running on port 8000
- Access site at http://localhost:8000
- Server keeps running during development
- **After editing content, just regenerate (no need to restart server)**

### Quick Workflow for Content Changes

**1. Edit Content**
```bash
# Edit the Markdown source file
vim website/content/index.md
```

**2. Regenerate Site**
```bash
cd website
python generate_site.py
```

**3. View Changes**
- Refresh browser at http://localhost:8000
- Server usually already running (no restart needed)

**Common Mistake:**
❌ Editing HTML files in `/website/build/` (changes will be lost)
✅ Always edit Markdown files in `/website/content/`

## Content File Structure

### Location
All content **source** files are located in: `/website/content/`
Generated HTML files are created in: `/website/build/`

### File Naming Convention
- Use lowercase with hyphens: `page-name.md`
- Homepage must be: `index.md`
- No spaces or special characters
- Keep names SEO-friendly

### Standard Content File Format

```markdown
---
title: "SEO-Optimized Page Title"
description: "Meta description for search engines (127-157 characters)"
keywords: "keyword1, keyword2, keyword3, keyword4, keyword5"
page_title: "Display Title on Page (optional)"
show_cta: true
is_homepage: false
---

# Main Heading (H1)

Content begins here in Markdown format...

## Subheading (H2)

More content...

### Sub-subheading (H3)

Additional content...
```

## Frontmatter Metadata Guide

### Required Fields

#### `title`
- **Purpose**: SEO title tag, appears in browser tab and search results
- **Format**: String
- **Length**: 50-60 characters (optimal for search engines)
- **Example**: `"Protect Your AV Innovations with US Patent 12,001,207 Licensing"`

#### `description`
- **Purpose**: SEO meta description for search results
- **Format**: String
- **Length**: 127-157 characters (optimal for Google)
- **Example**: `"License US Patent 12,001,207 for camera-based navigation safety in autonomous vehicles and drones. Strengthen your IP portfolio."`

#### `keywords`
- **Purpose**: SEO keywords for page optimization
- **Format**: Comma-separated string
- **Count**: 4-6 keywords/phrases
- **Example**: `"autonomous vehicle patent licensing, US patent 12001207, camera-based navigation safety"`

### Optional Fields

#### `page_title`
- **Purpose**: Display title on the page (different from SEO title if needed)
- **Format**: String
- **Default**: Uses `title` field if not provided
- **Example**: `"Patent Details"`

#### `show_cta`
- **Purpose**: Show call-to-action button/section on page
- **Format**: Boolean (`true` or `false`)
- **Default**: `false`
- **Example**: `true`

#### `is_homepage`
- **Purpose**: Identifies homepage for special hero section rendering
- **Format**: Boolean (`true` or `false`)
- **Default**: `false`
- **Usage**: Only set to `true` for `index.md`

#### `hero_title`
- **Purpose**: Hero section main title (homepage only)
- **Format**: String
- **Example**: `"Protect Your AV Innovations with US Patent 12,001,207"`

#### `hero_subtitle`
- **Purpose**: Hero section subtitle (homepage only)
- **Format**: String
- **Example**: `"License cutting-edge camera-based navigation safety technology"`

## ⚠️ CRITICAL: Fact-Checking and Content Quality Assurance

### The Quantity vs. Quality Challenge

As this project scales to **tens of landing pages** (Phase 3+), maintaining factual accuracy is **NON-NEGOTIABLE**. Each landing page must:
- Focus on different aspects of the patent (US 12,001,207)
- Connect to current events, trends, and industry insights
- Include relevant quotes and expert perspectives
- **REMAIN 100% FACTUALLY CORRECT**

### Mandatory Comprehensive Fact-Checking Protocol

**⚠️ CRITICAL REQUIREMENT:** For ALL content creation or editing (homepage, landing pages, core pages, ANY page):

#### Before Publishing ANY Content:

**1. Launch Comprehensive Fact-Checking Agent**

Use the Task tool to spin up a comprehensive fact-checking agent that covers all verification areas:

```
Comprehensive Fact-Checking Agent:
SECTION 1: Patent Facts Verification
- Verify patent number, issue date, claims
- Validate technical specifications
- Check USPTO records (after reading local docs documentation)
- Verify continuation application status

SECTION 2: Industry Claims Verification
- Verify market statistics and trends
- Validate company references (Tesla, etc.)
- Check technology claims (FSD, E2E neural networks)
- Verify regulatory information

SECTION 3: Current Events & Quotes Verification
- Verify all dates and timelines
- Validate quotes and attributions
- Check news sources and links
- Verify industry reports cited
```

**2. Cross-Reference Verification Requirements**

Every factual claim must have:
- **Primary Source**: USPTO records, official company announcements, peer-reviewed research
- **Secondary Source**: Industry news, reputable tech publications
- **Date Verification**: Ensure all dates and timelines are accurate
- **Context Check**: Verify claims are not taken out of context

**3. High-Risk Content Categories Requiring Extra Scrutiny**

Pay special attention to:
- ✅ Patent claims and technical details
- ✅ Patent dates (issue, filing, continuation status)
- ✅ Company names and product names (Tesla FSD, etc.)
- ✅ Market statistics and financial data
- ✅ Regulatory requirements and legal claims
- ✅ Technology capabilities and limitations
- ✅ Industry trends and predictions
- ✅ Quotes from individuals or publications
- ✅ Dates of events or announcements

### Landing Page Content Strategy (Quantity + Quality)

#### Content Differentiation Approaches

To create tens of unique landing pages while maintaining accuracy:

**1. Patent Aspect Focus**
- Safety mechanisms (verified claims from patent)
- Camera-based navigation (specific technical details)
- Fail-safe systems (documented in USPTO filing)
- AI integration points (cited in patent claims)
- Sensor fusion approaches (patent specifications)

**2. Industry Application Focus**
- Autonomous vehicles (verify market data)
- Commercial drones (validate use cases)
- Delivery robots (check deployment examples)
- Agricultural automation (confirm applications)
- Marine navigation (verify relevance)

**3. Current Event Tie-Ins** (REQUIRES INTENSIVE FACT-CHECKING)
- Tesla FSD rollout timeline (verify dates and milestones)
- Regulatory changes (check official sources)
- Competitor announcements (validate via press releases)
- Funding rounds (verify via Crunchbase, official announcements)
- Technology breakthroughs (peer-reviewed sources)

**4. Company/Persona Target Focus**
- Startups building AV technology (factual use cases)
- Established manufacturers (verify company info)
- Research institutions (confirm affiliations)
- Drone manufacturers (validate market position)

### Fact-Checking Workflow (MANDATORY FOR ALL CONTENT)

#### Stage 1: Content Draft
1. Write content with placeholders for unverified facts: `[VERIFY: claim]`
2. Mark all statistics, dates, quotes: `[CHECK: statistic]`
3. Flag bold claims for scrutiny: `[BOLD CLAIM: needs verification]`

#### Stage 2: Self-Verification Pass
1. Check USPTO database for patent facts
2. Verify dates against official sources
3. Validate company information via official websites
4. Cross-reference statistics with original sources

#### Stage 3: Comprehensive Agent Verification (CRITICAL)
```bash
# Launch comprehensive fact-checking agent
Comprehensive Agent: Verify all claims (patent, industry, and events)
```

**Agent Instructions Template:**
```
You are a comprehensive fact-checking agent. Review the following content and verify EVERY factual claim across all categories:

Content: [paste content]

Check:
1. Patent numbers, dates, claims
2. Company names, product names, capabilities
3. Statistics, market data, financial figures
4. Dates of events, announcements, milestones
5. Quotes and attributions
6. Technology specifications and capabilities

For EACH claim, provide:
- Claim: [exact text from content]
- Verification: [verified/unverified/incorrect]
- Source: [primary source URL or reference]
- Correction: [if incorrect, provide correct information]
- Confidence: [high/medium/low]

Flag ANY claim you cannot verify with a primary source.
```

#### Stage 4: Correction and Re-verification
1. Correct all flagged issues
2. Remove unverifiable claims
3. Add source citations where appropriate
4. Re-run agent verification on corrected sections

#### Stage 5: Final Editorial Pass
1. Ensure all corrections integrated
2. Verify flow and readability maintained
3. Check that accuracy doesn't compromise SEO
4. Confirm all factual claims have been verified

### Sources Hierarchy (Trustworthiness)

**TIER 1 (Always Trust):**
- USPTO patent database
- Official company press releases
- Government regulatory documents
- Peer-reviewed academic papers
- Official financial filings (SEC, etc.)

**TIER 2 (Verify with Second Source):**
- Major tech news outlets (TechCrunch, The Verge, etc.)
- Industry trade publications
- Company blog posts
- Expert interviews
- Conference presentations

**TIER 3 (Verify with Multiple Sources):**
- General news outlets
- Industry analyst reports
- Social media posts (even verified accounts)
- Forums and community discussions
- Blog posts

**NEVER USE:**
- Unverified social media claims
- Anonymous sources
- Speculation presented as fact
- Outdated information (check publication dates)

### Content Accuracy Red Flags

❌ **STOP and fact-check if you see:**
- Specific numbers without source
- "Studies show..." without citation
- Quotes without attribution
- Bold predictions about future
- Comparisons to competitors without data
- Technical specifications not in patent
- Market size claims without source
- Timeline claims without verification

### Documentation Requirements

For each landing page, maintain a **fact-check log**:

```markdown
# Fact-Check Log: [Page Name]

## Patent Claims Verified
- Claim: "US Patent 12,001,207 issued June 4, 2024"
- Source: docs/System/patent_reference.md + USPTO database (direct link)
- Verified by: Comprehensive Fact-Checking Agent
- Date: [date]
- Status: ✅ VERIFIED

## Industry Statistics Verified
- Claim: "Tesla deployed FSD v12 in March 2024"
- Source: Tesla official announcement + TechCrunch article
- Verified by: Comprehensive Fact-Checking Agent
- Date: [date]
- Status: ✅ VERIFIED

## Current Events Verified
[...]

## Quotes Verified
[...]

## Claims Removed (Unverifiable)
- Original claim: [...]
- Reason: No primary source found
- Date removed: [date]
```

### Quality Metrics for Scaled Content

Track these metrics across all landing pages:

- **Fact-Check Pass Rate**: 100% required before publish
- **Source Quality Score**: % of Tier 1 sources used
- **Claims Verified**: Total factual claims / Total verified
- **Corrections Made**: Track pre-publish corrections
- **Agent Flags Resolved**: Must be 100% before publish

## Content Creation Workflow

### Step 1: Plan Content
1. Identify target keywords for the page
2. Research competitor content
3. Outline structure (H1, H2, H3 hierarchy)
4. Define word count target (800-1,800 words)
5. **Identify all factual claims that will need verification**
6. **Pre-check availability of primary sources**

### Step 2: Create Markdown File
1. Navigate to `/website/content/`
2. Create new file: `page-name.md`
3. Add YAML frontmatter with all required fields
4. Write content in Markdown
5. **Mark all claims requiring verification with [VERIFY] tags**

### Step 3: Write Content
1. Start with compelling H1 heading
2. Use H2 for main sections
3. Use H3 for subsections
4. Include bullet points and lists
5. Add emphasis with **bold** and *italic*
6. Include relevant links (internal and external)
7. **Flag all factual claims for verification**

### Step 4: Comprehensive Fact-Checking (MANDATORY)
**⚠️ CRITICAL: Launch comprehensive fact-checking agent before proceeding**
1. Launch comprehensive fact-checking agent (covers patent facts, industry claims, and current events)
2. Agent MUST read docs/System/patent_reference.md FIRST for patent verification
3. Review all agent findings across all categories
4. Correct ALL flagged issues
5. Re-verify corrected content
6. Document verification in fact-check log

### Step 5: Optimize for SEO
1. Include primary keyword in first paragraph
2. Use keywords naturally throughout content
3. Optimize heading structure (H1 → H2 → H3)
4. Add internal links to other pages
5. Ensure meta description is compelling
6. **Verify SEO optimization didn't compromise factual accuracy**

### Step 6: Generate and Preview
```bash
# Generate site from Markdown source files
cd /website
python generate_site.py

# If local server not running, start it:
cd build
python -m http.server 8000

# Visit: http://localhost:8000
# (Usually server is already running, just refresh browser)
```

**Note:** The server typically stays running during development. After regenerating the site, simply refresh your browser to see changes.

### Step 7: Review and Test
1. Check page loads correctly
2. Verify navigation links work
3. Test responsive design (mobile, tablet, desktop)
4. Validate SEO elements (title, description)
5. Proofread content for typos/errors
6. **Final fact-check pass: Re-read all claims one more time**

### Step 8: Deploy
**⚠️ ONLY deploy after fact-checking complete and documented**
```bash
# Commit and push to deploy
git add .
git commit -m "Add new page: [page name]"
git push
```

## Editing Existing Content

### Step 1: Locate Source File
Find the **Markdown source file** in `/website/content/`:
- Homepage: `index.md`
- Patent Details: `patent-details.md`
- Licensing: `licensing.md`
- Industry Insights: `industry-insights.md`
- Contact: `contact.md`
- Thank You: `thank-you.md`

**⚠️ IMPORTANT:** Edit the `.md` file, NOT the `.html` file in `/website/build/`

### Step 2: Edit Content
1. Open **source file** in text editor (`.md` file in `/website/content/`)
2. Modify frontmatter if metadata changes
3. Edit Markdown content
4. Save file

### Step 3: Regenerate Site
```bash
cd website
python generate_site.py
```

**What happens:** Generator reads your edited `.md` file and creates/updates the corresponding `.html` file in `/website/build/`

### Step 4: Test Changes
1. Refresh browser at http://localhost:8000 (server usually already running)
2. Verify changes appear correctly
3. Test affected links and navigation

**If server not running:**
```bash
cd website/build
python -m http.server 8000
```

### Step 5: Deploy Updates
```bash
git add .
git commit -m "Update [page name]"
git push
```

## Content Guidelines

### Word Count Targets
- **Homepage**: 800-1,000 words
- **Core Pages**: 1,000-1,500 words
- **Landing Pages**: 1,000-1,800 words
- **Contact/Thank You**: 600-800 words

### Writing Style
- **Tone**: Professional, authoritative, helpful
- **Voice**: Active voice preferred
- **Perspective**: Second person ("your", "you") for engagement
- **Formatting**: Short paragraphs (2-4 sentences), bullet points, subheadings

### SEO Best Practices
1. **Keyword Density**: 1-2% (natural usage)
2. **Heading Structure**: One H1, multiple H2s, H3s as needed
3. **Internal Links**: 3-5 per page to related pages
4. **Meta Description**: Include primary keyword, compelling CTA
5. **Content Length**: Minimum 800 words for SEO value

### Content Structure Template
```markdown
# Main Heading (H1) - Include Primary Keyword

Introduction paragraph with primary keyword in first 100 words.

## Key Benefit or Topic 1 (H2)

Content explaining this benefit...

### Sub-topic 1.1 (H3)

Details...

### Sub-topic 1.2 (H3)

More details...

## Key Benefit or Topic 2 (H2)

Content...

## Call to Action (H2)

Compelling CTA paragraph with link to [Contact](/contact.html) page.
```

## Common Markdown Syntax

### Headings
```markdown
# H1 Heading
## H2 Heading
### H3 Heading
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
```

### Lists
```markdown
- Bullet point 1
- Bullet point 2
  - Nested bullet
- Bullet point 3

1. Numbered item 1
2. Numbered item 2
3. Numbered item 3
```

### Links
```markdown
[Link text](/page-name.html)
[External link](https://example.com)
```

### Blockquotes
```markdown
> This is a quoted text block
```

### Code
```markdown
Inline `code` within text.

```
Code block
```
```

## Troubleshooting

### Issue: Page Not Generating
**Symptoms**: HTML file not appearing in `/build/`
**Solutions**:
1. Check for YAML frontmatter syntax errors
2. Verify file has `.md` extension
3. Ensure file is in `/website/content/`
4. Run generator with verbose output

### Issue: Broken Frontmatter
**Symptoms**: Page generates with missing metadata
**Solutions**:
1. Verify YAML syntax (proper indentation, quotes)
2. Check for missing closing quotes
3. Ensure `---` delimiters are present
4. Test frontmatter with YAML validator

### Issue: Content Not Displaying
**Symptoms**: Page loads but content is missing
**Solutions**:
1. Check Markdown syntax
2. Verify content is after frontmatter
3. Ensure proper spacing after `---`
4. Review generated HTML in `/build/`

### Issue: SEO Elements Missing
**Symptoms**: Meta tags not appearing in HTML
**Solutions**:
1. Verify frontmatter includes `title`, `description`, `keywords`
2. Check template file (`base.html`) has meta tag placeholders
3. Regenerate site
4. Clear browser cache and reload

## Quality Checklist

Before publishing new or updated content, verify:

### Content Quality
- [ ] Frontmatter includes all required fields
- [ ] Title is 50-60 characters
- [ ] Description is 127-157 characters
- [ ] Keywords are relevant and targeted (4-6 keywords)
- [ ] Content is 800+ words (appropriate for page type)
- [ ] No spelling or grammar errors
- [ ] CTA is clear and compelling

### ⚠️ FACT-CHECKING (MANDATORY)
- [ ] **ALL factual claims marked with [VERIFY] during drafting**
- [ ] **Comprehensive fact-checking agent launched and completed**
- [ ] **Agent verified all patent facts (100% complete) - MUST read docs/System/patent_reference.md FIRST**
- [ ] **Agent verified all industry/market claims (100% complete)**
- [ ] **Agent verified all quotes/dates/current events (100% complete)**
- [ ] **All agent findings reviewed and corrections made**
- [ ] **Fact-check log created and documented**
- [ ] **Zero unverified claims remain in content**
- [ ] **All sources are Tier 1 or Tier 2 (with secondary verification)**
- [ ] **No red flag content remains (see red flags list)**

### SEO & Technical
- [ ] Primary keyword appears in first 100 words
- [ ] Heading hierarchy is logical (H1 → H2 → H3)
- [ ] Internal links included (3-5 per page)
- [ ] Page generates without errors
- [ ] Preview looks correct in browser
- [ ] Responsive design works (mobile, tablet)
- [ ] Navigation links functional
- [ ] SEO meta tags present in HTML source
- [ ] **SEO optimization didn't compromise factual accuracy**

## Related Documentation

- **Project Architecture**: `/docs/System/project_architecture.md`
- **Site Generation SOP**: `/docs/SOP/site_generation.md`
- **Website README**: `/website/README.md`
- **Original PRD**: `/docs/website_prd_001.md`
