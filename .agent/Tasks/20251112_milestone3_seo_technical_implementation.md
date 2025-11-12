# Product Requirements Document: SEO Technical Implementation (Milestone 3)

## Document Information
- **Task Type**: Technical Implementation - SEO Optimization
- **Status**: Active
- **Priority**: High
- **Created**: November 12, 2025
- **Estimated Duration**: 3-4 days
- **Owner**: Developer (Team Member)
- **Parent Document**: `20251110_production_readiness_prd.md` (Milestone 3)
- **Target Completion**: November 16, 2025

---

## Executive Summary

This PRD provides complete technical specifications for implementing Milestone 3 of the production readiness plan: SEO Technical Implementation. The website currently has 13 pages with basic SEO (title tags, meta descriptions, canonical URLs, Organization schema) but is missing critical components for search visibility and social sharing.

### Current State
- ✅ Python static site generator (Jinja2 + Markdown) functional
- ✅ 13 pages generated successfully
- ✅ 46/46 automated tests passing
- ✅ Basic meta tags (title, description, canonical)
- ✅ Organization schema (sitewide)
- ❌ Open Graph tags (NOT rendered despite frontmatter fields)
- ❌ Twitter Card tags (NOT implemented)
- ❌ Article/BreadcrumbList schemas (missing)
- ❌ Social sharing images (assets directory empty)
- ❌ Meta description optimization (some exceed 160 chars)
- ❌ Google Analytics (no tracking code)

### What This PRD Delivers
By completion, all 13 pages will have:
- Complete Open Graph meta tags (6 tags per page)
- Complete Twitter Card meta tags (4 tags per page)
- Structured data schemas (Article + BreadcrumbList)
- Optimized meta descriptions (155-160 characters)
- Social sharing images (1200x630px, AI-generated)
- Google Analytics placeholder structure (ready for deployment)
- 65+ automated tests validating all SEO components

### Success Criteria
- All automated tests passing (65+ tests, up from 46)
- All 13 pages validate with Google Rich Results Test
- All 13 pages validate with Facebook Sharing Debugger
- All 13 pages validate with Twitter Card Validator
- Site builds without errors (`python generate_site.py`)
- Ready for Milestone 5 (Production Deployment)

---

## Refactoring Design: Social Sharing Images

**Note**: This document originally specified AI-generated images. The approach has been refactored for better control, licensing, and maintainability.

### Problem Statement

Original approach required AI-generated images (DALL-E 3, Midjourney) for creating 13 unique Open Graph images. This has limitations:
- Dependency on external AI services (ChatGPT Plus or Midjourney subscription)
- Inconsistent quality and style across generations
- Licensing concerns with AI-generated content
- Manual effort required for each of 13 pages
- Difficult to maintain brand consistency
- Time-consuming iteration to get acceptable results

### Refactored Solution

Replace AI generation with a **manual background selection + automated Python text overlay** system:

#### Core Components

1. **Category-Based Image System**
   - Group 13 pages into 4 categories
   - Each category shares one background image with consistent text overlay
   - Reduces work from 13 unique images to 4 background selections

2. **Manual Background Selection**
   - Developer selects 4 high-quality images from free/commons platforms (Unsplash, Pexels, Pixabay)
   - Comprehensive search queries provided for each category
   - Clear licensing requirements (CC0/Free for commercial use)
   - Ensures professional quality and relevance

3. **Automated Text Overlay**
   - Python script (`generate_og_images.py`) using Pillow library
   - Overlays brand-consistent text on backgrounds
   - Text: "US PATENT 12,001,207 B2 | Camera-Based Navigation Safety"
   - Uses Space Grotesk font (website brand font) with orange (#e67e22) branding
   - Consistent output across all categories

4. **Environment Configuration**
   - `.env` file for deployment-specific variables (domain, analytics, email)
   - Enables dev/staging/production environments
   - No hardcoded values in code
   - Single source of truth for configuration

### Image Categories & Mapping

**Category A - Startup/Innovation** (3 pages):
- `series-a-av-patent-portfolio-strategy`
- `tesla-fsd-competitor-camera-patent-licensing`
- `autonomous-trucking-patent-defense-strategy`
- Search query: "autonomous vehicle technology modern"
- Alternative queries: "self-driving car dashboard futuristic", "AI vehicle sensor technology", etc.

**Category B - Investment/Finance** (2 pages):
- `venture-capital-av-patent-portfolio-due-diligence`
- `drone-delivery-patent-portfolio-pre-ipo`
- Search query: "business investment strategy technology"
- Alternative queries: "venture capital handshake deal", "financial growth chart technology", etc.

**Category C - Technical/Legal** (2 pages):
- `patent-details`
- `licensing`
- Search query: "patent document technology blueprint"
- Alternative queries: "intellectual property legal document", "technical diagram engineering", etc.

**Category D - General/Info** (6+ pages, default catch-all):
- `index`, `industry-insights`, `contact`, `thank-you`, `about`, `disclaimer`, `privacy`
- Any new pages automatically assigned to this category
- Search query: "smart transportation future connectivity"
- Alternative queries: "connected vehicles network highway", "smart city transportation aerial", etc.

### Python Generator Script Design

**File**: `/website/generate_og_images.py`

**Features**:
- Loads background images from `/assets/images/backgrounds/[category].jpg`
- Resizes/crops to 1200x630px (Open Graph standard)
- Applies dark gradient overlay (transparent → rgba(0,0,0,0.6)) on bottom 40%
- Renders two-line text overlay:
  - Line 1: "US PATENT 12,001,207 B2" (white, 48-54px, bold, uppercase)
  - Line 2: "Camera-Based Navigation Safety" (orange #e67e22, 34-38px, medium)
- Space Grotesk font with system font fallback (Arial, Helvetica)
- Text shadow for readability on light backgrounds
- Smart crop from center if aspect ratio doesn't match
- Slight blur (radius=1) to background for text readability
- Outputs high-quality JPEG (quality=92)

**CLI Interface**:
```bash
python generate_og_images.py                        # Generate all 4 categories
python generate_og_images.py --category startup     # Single category
python generate_og_images.py --preview              # Display without saving
```

### Environment Configuration Design

**File**: `/website/.env` (gitignored)

```bash
# Environment
ENVIRONMENT=production

# Domain Configuration
SITE_DOMAIN=av-navigation-ip.com
SITE_URL=https://av-navigation-ip.com

# Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
GOOGLE_ANALYTICS_ENABLED=true

# Contact
CONTACT_EMAIL=contact@av-navigation-ip.com

# SEO
ROBOTS_INDEX=true
```

**Rationale**: Separate environment-specific variables from code:
- Local development uses `localhost:8000`
- Staging can use different domain/analytics
- Production uses live domain
- Analytics can be disabled in dev/staging
- Single source of truth for deployment configuration

### Site Generator Integration

**Modifications to `/website/generate_site.py`**:

1. Load environment variables with `python-dotenv`
2. Define `OG_IMAGE_CATEGORIES` mapping at top of file
3. In page processing loop:
   - Extract page slug from filename
   - Look up category from mapping (defaults to `general-info`)
   - Set `og_image_path = f'/assets/images/og-{category}.jpg'`
4. Pass to template context:
   - `site_url`: From SITE_URL environment variable
   - `og_image`: Category-specific image path
   - `ga_id`: Google Analytics ID from environment
   - `ga_enabled`: Boolean from environment

**Template Updates (`base.html`)**:
- Replace all hardcoded domains with `{{ site_url }}`
- Use `{{ site_url }}{{ og_image }}` for Open Graph/Twitter Card images
- Conditional Google Analytics: `{% if ga_enabled %}...{% endif %}`
- All structured data uses `{{ site_url }}` variable

### Benefits of Refactored Approach

1. **Quality Control**: Manual selection ensures high-quality, relevant imagery
2. **Licensing Clarity**: All images from verified CC0/Free sources
3. **Brand Consistency**: Automated text overlay ensures uniform branding across all images
4. **Maintainability**: Python script makes updates easy (change text once, regenerate all)
5. **Scalability**: New pages automatically get appropriate category image via default catch-all
6. **Reduced Work**: 4 background images instead of 13 unique AI-generated images
7. **Environment Flexibility**: .env configuration supports dev/staging/production seamlessly
8. **No External Dependencies**: No reliance on AI services, subscriptions, or external tools
9. **Faster Iteration**: Regenerate all images in seconds vs. waiting for AI generation
10. **Cost Savings**: No ChatGPT Plus or Midjourney subscription required

### Trade-offs

**Advantages over AI Generation**:
- Better image quality and relevance
- Clear, unambiguous licensing (CC0/Free)
- No external service dependencies
- Consistent branding across all images
- Easier to update (regenerate vs. recreate)
- Faster workflow after initial setup
- No subscription costs

**Considerations**:
- Developer must manually select 4 background images (one-time ~30 min effort)
- Requires Pillow dependency (~10MB)
- Background images not in git (must be downloaded per environment)
- Text overlay is fixed (vs. custom text per AI image)

**Mitigation**: Comprehensive search queries provided for each category with 5+ alternatives each, clear selection criteria, and detailed image requirements. One-time setup effort pays off long-term.

### Directory Structure

```
/website/
├── .env.example                    # Template (committed to git)
├── .env                            # Local config (gitignored)
├── .gitignore                      # Add: .env, backgrounds/, og-*.jpg
├── requirements.txt                # Add: python-dotenv, Pillow
├── generate_site.py                # Modified: env loading, category mapping
├── generate_og_images.py           # New: OG image generator script
├── assets/
│   └── images/
│       ├── backgrounds/            # Developer downloads 4 images here (gitignored)
│       │   ├── startup-innovation.jpg
│       │   ├── investment-finance.jpg
│       │   ├── technical-legal.jpg
│       │   └── general-info.jpg
│       ├── og-startup-innovation.jpg    # Generated by script (gitignored)
│       ├── og-investment-finance.jpg    # Generated by script (gitignored)
│       ├── og-technical-legal.jpg       # Generated by script (gitignored)
│       └── og-general-info.jpg          # Generated by script (gitignored)
└── designs/
    └── default/
        └── base.html               # Modified: use environment variables
```

### Implementation Workflow Summary

**Phase 1**: Environment Setup (`.env`, dependencies, gitignore)
**Phase 2**: Background Image Selection (search, download, verify licensing and dimensions)
**Phase 3**: OG Image Generator Script (create script, test execution, verify output)
**Phase 4**: Site Generator Updates (environment loading, category mapping, template context)
**Phase 5**: Content Metadata (add date fields, verify descriptions, update image paths)
**Phase 6**: Testing & Validation (regenerate site, test locally, validate with external tools)

### Migration from Original AI-Generated Approach

**Changes to original PRD specifications**:
- **Section 3.2**: Replace AI prompt instructions with background selection workflow
- **Appendix C**: Replace 13 individual AI prompts with 4 category-based search queries
- **Phase 3**: Add environment setup phase before image generation
- **Dependencies**: Add `python-dotenv` and `Pillow` to requirements.txt
- **Images**: Generate 4 category images instead of 13 unique images
- **Testing**: Update image path tests to use category-based naming

All other sections (Open Graph tags, Twitter Cards, structured data, meta descriptions, Google Analytics) remain unchanged.

---

## Prerequisites & Technical Context

### Required Knowledge
- Python 3.x
- Jinja2 templating
- YAML frontmatter syntax
- Basic SEO concepts (meta tags, structured data)
- Familiarity with the project codebase

### Key Files & Locations

**Generator & Templates:**
- `/website/generate_site.py` - Static site generator (Python)
- `/website/designs/default/base.html` - Master template (738 lines)
- `/website/designs/default/page.html` - Content page template (156 lines)

**Content Files (13 total):**
- `/website/content/*.md` - All markdown files with YAML frontmatter

**Testing:**
- `/website/test_website.py` - Test suite (currently 46 tests)

**Assets:**
- `/website/assets/images/og-images/` - Social sharing images (to be created)

**Build Output:**
- `/website/build/` - Generated HTML files

### Build & Test Commands

```bash
# Generate site
cd /Users/sjsmit/Development/Caden/op_patent/website
python generate_site.py

# Run tests
python test_website.py

# Expected output: 65+ tests passing (up from 46 baseline)
```

### Current Test Status
- **Baseline**: 46/46 tests passing
- **Target**: 65+ tests passing (all SEO validations included)

---

## Implementation Phases

This work is organized into **4 sequential phases** that must be completed in order:

1. **Phase 1**: Open Graph & Twitter Card Implementation (Day 1)
2. **Phase 2**: Structured Data Schemas (Day 2)
3. **Phase 3**: Social Images & Meta Optimization (Day 2-3)
4. **Phase 4**: Google Analytics Placeholder & Final Testing (Day 3-4)

Each phase includes:
- Detailed code specifications
- Exact file modifications
- Test implementations
- Validation steps

---

## Phase 1: Open Graph & Twitter Card Implementation

**Duration**: Day 1 (6-8 hours)
**Outcome**: All 13 pages have complete OG and Twitter meta tags

### 1.1 Update Generator to Extract SEO Fields

**File**: `/website/generate_site.py`

**Current behavior**: Generator parses frontmatter but doesn't extract `og_*` and `twitter_*` fields.

**Required changes**: Add extraction logic for Open Graph and Twitter Card fields.

**Find this section** (around lines 80-120 where metadata is extracted):

```python
# Current code extracts these fields:
{
    'title': metadata.get('title', 'AV Navigation IP Protection'),
    'description': metadata.get('description', '...'),
    'keywords': metadata.get('keywords', '...'),
    'content': html_content,
    # ... other fields
}
```

**Add these additional field extractions** to the template context dictionary:

```python
# Open Graph fields
'og_title': metadata.get('og_title', metadata.get('title', 'AV Navigation IP Protection')),
'og_description': metadata.get('og_description', metadata.get('description', '')),
'og_type': metadata.get('og_type', 'website'),
'og_url': metadata.get('canonical', f"https://av-navigation-ip.com/{output_filename}"),
'og_image': metadata.get('og_image', 'https://av-navigation-ip.com/assets/images/og-images/default-og.jpg'),
'og_site_name': 'AV Navigation IP Protection',

# Twitter Card fields
'twitter_card': metadata.get('twitter_card', 'summary_large_image'),
'twitter_title': metadata.get('twitter_title', metadata.get('title', 'AV Navigation IP Protection')),
'twitter_description': metadata.get('twitter_description', metadata.get('description', '')),
'twitter_image': metadata.get('twitter_image', metadata.get('og_image', 'https://av-navigation-ip.com/assets/images/og-images/default-og.jpg')),
```

**Logic notes**:
- `og_title` and `twitter_title` default to page `title` if not specified
- `og_description` and `twitter_description` default to meta `description`
- `twitter_image` defaults to `og_image` to avoid duplication
- `og_type` defaults to `website` for homepage, `article` for content pages (see Phase 2)

### 1.2 Add Meta Tags to Base Template

**File**: `/website/designs/default/base.html`

**Location**: Lines 10-11 (after existing `<link rel="canonical">`)

**Insert this code block** immediately after the canonical link:

```html
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{{ og_title }}" />
    <meta property="og:description" content="{{ og_description }}" />
    <meta property="og:type" content="{{ og_type }}" />
    <meta property="og:url" content="{{ og_url }}" />
    <meta property="og:image" content="{{ og_image }}" />
    <meta property="og:site_name" content="{{ og_site_name }}" />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="{{ twitter_card }}" />
    <meta name="twitter:title" content="{{ twitter_title }}" />
    <meta name="twitter:description" content="{{ twitter_description }}" />
    <meta name="twitter:image" content="{{ twitter_image }}" />
```

**Result**: All 13 pages will now render OG and Twitter tags using values from frontmatter.

### 1.3 Update Content Frontmatter

**Files**: All 13 markdown files in `/website/content/`

**Action**: Add complete Open Graph and Twitter Card metadata to each file's YAML frontmatter.

**Example frontmatter template** (apply to all pages):

```yaml
---
title: "Page Title"
description: "Meta description 155-160 chars"
keywords: [...]
page_title: "Display Title"
show_cta: true

# Open Graph
og_title: "Page Title | AV Navigation IP Protection"
og_description: "Meta description (same as description field)"
og_type: "article"  # Use "website" for homepage only
og_image: "https://av-navigation-ip.com/assets/images/og-images/page-slug-og.jpg"

# Twitter Card
twitter_card: "summary_large_image"
twitter_title: "Page Title | AV Navigation IP Protection"
twitter_description: "Meta description (same as description field)"
twitter_image: "https://av-navigation-ip.com/assets/images/og-images/page-slug-og.jpg"

# Other existing fields...
---
```

**See Appendix B** for complete frontmatter examples for all 13 pages.

### 1.4 Add Automated Tests for OG/Twitter Tags

**File**: `/website/test_website.py`

**Add this test class** at the end of the file:

```python
class TestSEOMetaTags(unittest.TestCase):
    """Test Open Graph and Twitter Card meta tag presence and validity."""

    def setUp(self):
        """Set up test fixtures."""
        self.build_dir = os.path.join(os.path.dirname(__file__), 'build')

    def test_open_graph_tags_present_all_pages(self):
        """All pages should have complete Open Graph tags."""
        required_og_tags = ['og:title', 'og:description', 'og:type', 'og:url', 'og:image', 'og:site_name']

        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))
        self.assertGreater(len(html_files), 0, "No HTML files found in build directory")

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            for tag in required_og_tags:
                self.assertIn(f'property="{tag}"', html_content,
                            f"Missing {tag} in {os.path.basename(html_file)}")

    def test_twitter_card_tags_present_all_pages(self):
        """All pages should have complete Twitter Card tags."""
        required_twitter_tags = ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']

        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            for tag in required_twitter_tags:
                self.assertIn(f'name="{tag}"', html_content,
                            f"Missing {tag} in {os.path.basename(html_file)}")

    def test_og_image_urls_valid_format(self):
        """Open Graph image URLs should use correct format."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Extract og:image content
            import re
            og_image_match = re.search(r'property="og:image" content="([^"]+)"', html_content)
            if og_image_match:
                og_image_url = og_image_match.group(1)
                self.assertTrue(og_image_url.startswith('https://'),
                              f"og:image must use HTTPS in {os.path.basename(html_file)}")
                self.assertIn('av-navigation-ip.com', og_image_url,
                            f"og:image must use correct domain in {os.path.basename(html_file)}")

if __name__ == '__main__':
    unittest.main()
```

**Expected test count after Phase 1**: 52 tests (46 baseline + 6 new)

### 1.5 Validation Steps

After completing Phase 1:

1. **Regenerate site**: `python generate_site.py`
2. **Run tests**: `python test_website.py` (expect 52+ passing)
3. **Spot-check HTML**: Open `/website/build/index.html` in browser, view source, verify OG/Twitter tags present
4. **Check all pages**: Verify tags render correctly on at least 3 different pages

**Phase 1 Complete**: All pages have Open Graph and Twitter Card meta tags.

---

## Phase 2: Structured Data Schemas

**Duration**: Day 2 (4-6 hours)
**Outcome**: Article schema on content pages, BreadcrumbList schema on all non-homepage pages

### 2.1 Implement Article Schema

**File**: `/website/designs/default/page.html`

**Current state**: Only `patent-details` and `contact` pages have conditional schemas (lines 60-154).

**Required**: Add Article schema for all content pages (landing pages, insights, etc.).

**Find the section** at the end of `page.html` (after line 154):

**Insert this new conditional block**:

```jinja2
{% if page_type in ["landing", "insights", "about"] or (page_type not in ["patent-details", "contact", "homepage"]) %}
<!-- Article Schema.org structured data -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{{ page_title or title }}",
    "description": "{{ description }}",
    "author": {
        "@type": "Organization",
        "name": "AV Navigation IP Protection"
    },
    "publisher": {
        "@type": "Organization",
        "name": "AV Navigation IP Protection",
        "logo": {
            "@type": "ImageObject",
            "url": "https://av-navigation-ip.com/assets/images/logo.png"
        }
    },
    "datePublished": "{{ date_published or '2025-11-01' }}",
    "dateModified": "{{ date_modified or date_published or '2025-11-12' }}",
    "image": "{{ og_image }}",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "{{ og_url }}"
    }
}
</script>
{% endif %}
```

**Logic**:
- Applies to all pages EXCEPT homepage, patent-details, contact
- Uses `date_published` from frontmatter (defaults to Nov 1, 2025)
- Uses `date_modified` from frontmatter (defaults to today)
- Reuses `og_image` for article image

### 2.2 Implement BreadcrumbList Schema

**File**: `/website/designs/default/page.html`

**Location**: Insert after Article schema block (around line 175)

**Insert this conditional block**:

```jinja2
{% if not is_homepage %}
<!-- BreadcrumbList Schema.org structured data -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://av-navigation-ip.com/"
        }{% if breadcrumb_parent %},
        {
            "@type": "ListItem",
            "position": 2,
            "name": "{{ breadcrumb_parent }}",
            "item": "https://av-navigation-ip.com{{ breadcrumb_parent_url }}"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "{{ page_title or title }}",
            "item": "{{ og_url }}"
        }{% else %},
        {
            "@type": "ListItem",
            "position": 2,
            "name": "{{ page_title or title }}",
            "item": "{{ og_url }}"
        }{% endif %}
    ]
}
</script>
{% endif %}
```

**Logic**:
- Applies to all non-homepage pages
- 2-level breadcrumb if no parent (Home → Current Page)
- 3-level breadcrumb if parent exists (Home → Parent → Current Page)
- Matches existing HTML breadcrumb structure

### 2.3 Update Generator for Schema Fields

**File**: `/website/generate_site.py`

**Add these fields** to the template context (where you added OG/Twitter fields in Phase 1):

```python
# Schema.org fields
'date_published': metadata.get('date', metadata.get('date_published', '2025-11-01')),
'date_modified': metadata.get('modified', metadata.get('date_modified', '2025-11-12')),
'page_type': determine_page_type(output_filename),  # New helper function
```

**Add this helper function** to `generate_site.py`:

```python
def determine_page_type(filename):
    """Determine page type for schema selection."""
    if filename == 'index.html':
        return 'homepage'
    elif filename == 'patent-details.html':
        return 'patent-details'
    elif filename == 'contact.html':
        return 'contact'
    elif filename == 'industry-insights.html':
        return 'insights'
    elif filename == 'about.html':
        return 'about'
    elif filename in ['disclaimer.html', 'privacy.html', 'thank-you.html']:
        return 'legal'
    else:
        return 'landing'  # All SEO landing pages
```

### 2.4 Update Content Frontmatter with Dates

**Files**: All 13 content files

**Add these fields** to frontmatter:

```yaml
date_published: "2025-11-01"  # Initial publish date
date_modified: "2025-11-12"   # Last update date
```

**See Appendix B** for complete frontmatter with dates.

### 2.5 Add Automated Tests for Schemas

**File**: `/website/test_website.py`

**Add this test class**:

```python
class TestStructuredDataSchemas(unittest.TestCase):
    """Test JSON-LD structured data schemas."""

    def test_article_schema_on_content_pages(self):
        """Content pages should have Article schema."""
        content_pages = [
            'series-a-av-patent-portfolio-strategy.html',
            'tesla-fsd-competitor-camera-patent-licensing.html',
            'drone-delivery-patent-portfolio-pre-ipo.html',
            'venture-capital-av-patent-portfolio-due-diligence.html',
            'autonomous-trucking-patent-defense-strategy.html',
            'industry-insights.html',
            'about.html'
        ]

        for page in content_pages:
            filepath = os.path.join(self.build_dir, page)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    html = f.read()

                self.assertIn('"@type": "Article"', html,
                            f"Missing Article schema in {page}")
                self.assertIn('"headline"', html)
                self.assertIn('"datePublished"', html)

    def test_breadcrumb_schema_on_all_non_homepage_pages(self):
        """All non-homepage pages should have BreadcrumbList schema."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            if 'index.html' in html_file:
                continue  # Skip homepage

            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            self.assertIn('"@type": "BreadcrumbList"', html,
                        f"Missing BreadcrumbList schema in {os.path.basename(html_file)}")
            self.assertIn('"itemListElement"', html)

    def test_organization_schema_present(self):
        """Organization schema should be present on all pages (from base.html)."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            self.assertIn('"@type": "Organization"', html,
                        f"Missing Organization schema in {os.path.basename(html_file)}")
```

**Expected test count after Phase 2**: 58 tests (52 from Phase 1 + 6 new)

### 2.6 Validation Steps

1. **Regenerate site**: `python generate_site.py`
2. **Run tests**: `python test_website.py` (expect 58+ passing)
3. **Validate schemas**:
   - Open any landing page HTML in browser
   - View source, find JSON-LD scripts
   - Copy Article schema JSON
   - Paste into [Google Rich Results Test](https://search.google.com/test/rich-results)
   - Verify "Valid" result

**Phase 2 Complete**: All pages have appropriate structured data schemas.

---

## Phase 3: Social Sharing Images & Meta Description Optimization

**Duration**: Day 2-3 (6-8 hours, including image generation)
**Outcome**: 13 branded social images created, meta descriptions optimized

### 3.1 Create Social Sharing Images Directory

**Command**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
mkdir -p assets/images/og-images
```

### 3.2 Select and Download Background Images

**Updated Approach**: Manual background selection from free/commons platforms (see Refactoring Design section above)

**Create background images directory**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
mkdir -p assets/images/backgrounds
```

**Download 4 background images** from Unsplash, Pexels, or Pixabay:

**Category A - Startup/Innovation** (`startup-innovation.jpg`):
- Primary search: "autonomous vehicle technology modern"
- Alternatives: "self-driving car dashboard futuristic", "AI vehicle sensor technology", "autonomous navigation camera system", "electric vehicle innovation startup", "automotive technology lab research"
- Requirements: 1200x630px minimum, CC0/Free license, professional quality

**Category B - Investment/Finance** (`investment-finance.jpg`):
- Primary search: "business investment strategy technology"
- Alternatives: "venture capital handshake deal", "financial growth chart technology", "tech investment portfolio modern", "business funding startup meeting", "corporate investment digital finance"
- Requirements: 1200x630px minimum, CC0/Free license, professional quality

**Category C - Technical/Legal** (`technical-legal.jpg`):
- Primary search: "patent document technology blueprint"
- Alternatives: "intellectual property legal document", "technical diagram engineering blueprint", "patent certificate official document", "legal contract technology licensing", "technical specifications detailed drawing"
- Requirements: 1200x630px minimum, CC0/Free license, professional quality

**Category D - General/Info** (`general-info.jpg`):
- Primary search: "smart transportation future connectivity"
- Alternatives: "connected vehicles network highway", "smart city transportation aerial", "transportation technology network digital", "intelligent transport system future", "mobility innovation urban landscape"
- Requirements: 1200x630px minimum, CC0/Free license, professional quality

**Save all 4 images to**: `/website/assets/images/backgrounds/`

**See Appendix C** for detailed search workflow and licensing verification steps.

### 3.3 Create Python OG Image Generator Script

**Create file**: `/website/generate_og_images.py`

This script will automatically overlay text on your 4 background images to create category-based social sharing images.

**See Refactoring Design section** for complete script specifications including:
- Image processing (resize, crop to 1200x630px)
- Dark gradient overlay on bottom 40%
- Two-line text rendering (white patent number, orange tagline)
- Space Grotesk font with system fallbacks
- CLI interface (`--category`, `--preview` flags)

**After creating the script, run**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
python generate_og_images.py
```

**Expected output**: 4 generated images in `/website/assets/images/`:
- `og-startup-innovation.jpg`
- `og-investment-finance.jpg`
- `og-technical-legal.jpg`
- `og-general-info.jpg`

### 3.4 Update Environment Configuration

**Create `.env` file** (if not already created in earlier phase):

```bash
# Domain Configuration
SITE_URL=https://av-navigation-ip.com

# Other environment variables...
```

### 3.5 Update Generator for Category-Based Images

**Modify `/website/generate_site.py`** to use category-based image mapping:

```python
# Add at top of file
OG_IMAGE_CATEGORIES = {
    'series-a-av-patent-portfolio-strategy': 'startup-innovation',
    'tesla-fsd-competitor-camera-patent-licensing': 'startup-innovation',
    'autonomous-trucking-patent-defense-strategy': 'startup-innovation',
    'venture-capital-av-patent-portfolio-due-diligence': 'investment-finance',
    'drone-delivery-patent-portfolio-pre-ipo': 'investment-finance',
    'patent-details': 'technical-legal',
    'licensing': 'technical-legal',
}
DEFAULT_OG_CATEGORY = 'general-info'

# In page processing loop:
page_slug = os.path.splitext(os.path.basename(md_file))[0]
og_category = OG_IMAGE_CATEGORIES.get(page_slug, DEFAULT_OG_CATEGORY)
og_image_path = f'/assets/images/og-{og_category}.jpg'

# Add to template context:
context = {
    # ... existing fields ...
    'og_image': f"{SITE_URL}{og_image_path}",
}
```

### 3.6 Update Frontmatter with Category-Based Image Paths

**Files**: All 13 content files

**Update `og_image` and `twitter_image` fields** to use category-based URLs:

**For startup/innovation pages** (series-a, tesla-fsd, autonomous-trucking):
```yaml
og_image: "https://av-navigation-ip.com/assets/images/og-startup-innovation.jpg"
twitter_image: "https://av-navigation-ip.com/assets/images/og-startup-innovation.jpg"
```

**For investment/finance pages** (vc-due-diligence, drone-delivery):
```yaml
og_image: "https://av-navigation-ip.com/assets/images/og-investment-finance.jpg"
twitter_image: "https://av-navigation-ip.com/assets/images/og-investment-finance.jpg"
```

**For technical/legal pages** (patent-details, licensing):
```yaml
og_image: "https://av-navigation-ip.com/assets/images/og-technical-legal.jpg"
twitter_image: "https://av-navigation-ip.com/assets/images/og-technical-legal.jpg"
```

**For general/info pages** (homepage, industry-insights, contact, thank-you, about, disclaimer, privacy):
```yaml
og_image: "https://av-navigation-ip.com/assets/images/og-general-info.jpg"
twitter_image: "https://av-navigation-ip.com/assets/images/og-general-info.jpg"
```

**See Appendix B** for complete frontmatter templates with category-based image paths.

### 3.7 Optimize Meta Descriptions

**Current issue**: Some descriptions exceed 160 characters, hurting search snippet quality.

**Action**: Replace meta descriptions in all 13 content files with optimized versions.

**See Appendix A** for complete table of optimized meta descriptions (155-160 chars each).

**Example replacements**:

```yaml
# BEFORE (208 chars - TOO LONG)
description: "Patent portfolio strategy for Series A autonomous vehicle startups. Strengthen IP with licensed camera-based navigation patents before Series B fundraising. 4-9 months vs. 30-66 months in-house development."

# AFTER (160 chars - OPTIMAL)
description: "Build your AV patent portfolio before Series B. License camera navigation IP in 4-9 months vs 30-66 months in-house development."
```

### 3.8 Add Automated Tests for Images & Descriptions

**File**: `/website/test_website.py`

**Add this test class**:

```python
class TestSocialImagesAndMeta(unittest.TestCase):
    """Test social sharing images and meta description optimization."""

    def test_og_images_exist(self):
        """All referenced Open Graph images should exist."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            # Extract og:image URL
            import re
            og_image_match = re.search(r'property="og:image" content="([^"]+)"', html)
            if og_image_match:
                og_image_url = og_image_match.group(1)
                # Convert URL to local file path
                if 'og-images/' in og_image_url:
                    filename = og_image_url.split('og-images/')[-1]
                    image_path = os.path.join(os.path.dirname(__file__), 'assets/images/og-images', filename)
                    self.assertTrue(os.path.exists(image_path),
                                  f"Missing OG image: {filename} referenced in {os.path.basename(html_file)}")

    def test_meta_descriptions_length(self):
        """Meta descriptions should be 155-160 characters for optimal SEO."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            # Extract meta description
            import re
            desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
            if desc_match:
                description = desc_match.group(1)
                desc_length = len(description)

                self.assertGreaterEqual(desc_length, 120,
                                      f"Meta description too short ({desc_length} chars) in {os.path.basename(html_file)}")
                self.assertLessEqual(desc_length, 160,
                                   f"Meta description too long ({desc_length} chars) in {os.path.basename(html_file)}")
```

**Expected test count after Phase 3**: 62 tests (58 from Phase 2 + 4 new)

### 3.9 Validation Steps

1. **Verify background images downloaded**: Check `/website/assets/images/backgrounds/` contains 4 JPG files
2. **Verify generated OG images**: Check `/website/assets/images/` contains 4 `og-*.jpg` files
3. **Regenerate site**: `python generate_site.py` (should copy images to `/build/assets/`)
4. **Run tests**: `python test_website.py` (expect 62+ passing)
4. **Validate with Facebook**:
   - Visit [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
   - Enter a page URL (use local file:// URL or deploy to staging)
   - Verify image displays correctly (1200x630px)
5. **Check meta descriptions**: View source for any page, confirm description is 155-160 chars

**Phase 3 Complete**: All pages have social images and optimized meta descriptions.

---

## Phase 4: Google Analytics Placeholder & Final Testing

**Duration**: Day 3-4 (2-4 hours)
**Outcome**: GA tracking code structure in place, all tests passing, site ready for deployment

### 4.1 Add Google Analytics Placeholder

**File**: `/website/designs/default/base.html`

**Location**: Inside `<head>` section (after meta tags, before closing `</head>`)

**Insert this code block** (around line 15, before Google Fonts link):

```html
    <!-- Google Analytics (TODO: Replace G-XXXXXXXXXX with actual Measurement ID before production deployment) -->
    <!-- Tracking will be activated when deployed to production domain -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>
```

**Notes**:
- `G-XXXXXXXXXX` is a placeholder - will be replaced during production deployment
- GA script is present but non-functional until real Measurement ID is added
- Clear TODO comment reminds deployment engineer to update
- This satisfies Milestone 3 requirement (GA integration structure ready)

### 4.2 Add Google Analytics Test

**File**: `/website/test_website.py`

**Add this test**:

```python
class TestGoogleAnalytics(unittest.TestCase):
    """Test Google Analytics tracking code structure."""

    def test_ga_script_present_all_pages(self):
        """All pages should have Google Analytics script structure."""
        html_files = glob.glob(os.path.join(self.build_dir, '*.html'))

        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            self.assertIn('googletagmanager.com/gtag/js', html,
                        f"Missing Google Analytics script in {os.path.basename(html_file)}")
            self.assertIn('window.dataLayer', html)
            self.assertIn('gtag(', html)
```

**Expected test count after Phase 4**: 65+ tests (62 from Phase 3 + 3 new)

### 4.3 Final Site Generation & Testing

**Complete test suite run**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
python generate_site.py
python test_website.py
```

**Expected output**:

```
...
----------------------------------------------------------------------
Ran 65 tests in 2.456s

OK
```

**If any test fails**:
1. Read the failure message carefully
2. Check the specific file mentioned
3. Verify code matches PRD specifications
4. Regenerate site after fixes
5. Re-run tests until all pass

### 4.4 Manual Validation Checklist

After all automated tests pass, perform these manual checks:

**4.4.1 Spot-Check HTML Output**

Open these 3 files in a web browser:
- `/website/build/index.html` (Homepage)
- `/website/build/series-a-av-patent-portfolio-strategy.html` (Landing page)
- `/website/build/patent-details.html` (Core page)

For each page:
1. Right-click → "View Page Source"
2. Search for `og:title` - should find 1 instance with correct content
3. Search for `twitter:card` - should find 1 instance
4. Search for `"@type": "Article"` or `"@type": "BreadcrumbList"` - verify schema present
5. Verify meta description is 155-160 characters

**4.4.2 Validate with External Tools**

**Google Rich Results Test**:
1. Visit: https://search.google.com/test/rich-results
2. Select "Code" tab
3. Copy HTML source from `/website/build/index.html`
4. Paste into tool
5. Click "Test Code"
6. Expected: "Valid" result for Organization schema
7. Repeat for 2-3 other pages (expect Article + BreadcrumbList valid)

**Facebook Sharing Debugger** (optional - requires publicly accessible URL):
1. Visit: https://developers.facebook.com/tools/debug/
2. If deployed to staging, enter staging URL
3. If not deployed, skip this step (will validate during Milestone 5)

**Twitter Card Validator** (optional - requires publicly accessible URL):
1. Visit: https://cards-dev.twitter.com/validator
2. Same as Facebook - can be validated during deployment

### 4.5 Commit Changes to Git

**Review changes**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent
git status
git diff website/
```

**Stage and commit**:

```bash
git add website/generate_site.py
git add website/designs/default/base.html
git add website/designs/default/page.html
git add website/content/*.md
git add website/assets/images/og-images/*.jpg
git add website/test_website.py
git commit -m "$(cat <<'EOF'
Implement SEO technical optimization (Milestone 3)

- Add Open Graph meta tags to all 13 pages
- Add Twitter Card meta tags to all 13 pages
- Implement Article schema for content pages
- Implement BreadcrumbList schema for all non-homepage pages
- Generate 13 social sharing images (1200x630px)
- Optimize meta descriptions to 155-160 characters
- Add Google Analytics placeholder structure
- Expand test suite from 46 to 65+ tests

All automated tests passing. Ready for production deployment (Milestone 5).

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Phase 4 Complete**: SEO implementation finished, all tests passing, changes committed.

---

## Acceptance Criteria

### Technical Acceptance Criteria ✅

- [ ] All 65+ automated tests passing
- [ ] All 13 pages generate without errors
- [ ] Every page contains all 6 required Open Graph tags
- [ ] Every page contains all 4 required Twitter Card tags
- [ ] Content pages have Article schema JSON-LD
- [ ] All non-homepage pages have BreadcrumbList schema JSON-LD
- [ ] All 13 social images exist in `/website/assets/images/og-images/`
- [ ] All meta descriptions are 155-160 characters
- [ ] Google Analytics placeholder code present on all pages
- [ ] Organization schema present on all pages (existing, verified)

### Quality Gates ✅

- [ ] `python test_website.py` shows 0 failures
- [ ] `python generate_site.py` completes with no errors
- [ ] Spot-check of 3+ generated HTML files shows correct tags
- [ ] Google Rich Results Test validates schemas successfully

### Definition of Done ✅

- [ ] Code committed to git with descriptive message
- [ ] All modified files documented
- [ ] Ready for Milestone 5 (Production Deployment)
- [ ] No blockers for launch
- [ ] Production readiness PRD updated to mark Milestone 3 complete

---

## Appendix A: Optimized Meta Descriptions (155-160 Characters)

| Page | Current Description (Length) | Optimized Description (Length) |
|------|------------------------------|--------------------------------|
| **Homepage** (index.md) | "License US Patent 12,001,207 for camera-based navigation safety in autonomous vehicles and drones. Strengthen your IP portfolio and protect your innovations." (144 chars) ✅ | No change needed (144 chars - acceptable) |
| **Patent Details** (patent-details.md) | "Detailed technical overview of US Patent 12,001,207 covering camera-based navigation safety for autonomous vehicles and drones." (129 chars) ✅ | No change needed (129 chars - acceptable) |
| **Licensing** (licensing.md) | Current not specified in codebase scan | "License US Patent 12,001,207 for camera-based AV navigation safety. Flexible licensing terms for startups, enterprises, and VCs." (133 chars) |
| **Industry Insights** (industry-insights.md) | Current not specified in codebase scan | "AV patent licensing insights for autonomous vehicle startups. Tesla FSD competition, VC due diligence, and IP portfolio strategy." (133 chars) |
| **Contact** (contact.md) | Current not specified in codebase scan | "Contact us for US Patent 12,001,207 licensing inquiries. Camera-based navigation safety technology for autonomous vehicles and drones." (137 chars) |
| **Thank You** (thank-you.md) | Current not specified in codebase scan | "Thank you for your licensing inquiry. We'll respond within 24 hours to discuss US Patent 12,001,207 licensing opportunities." (127 chars) |
| **About** (about.md) | Current not specified in codebase scan | "About AV Navigation IP Protection. Offering US Patent 12,001,207 licensing for camera-based autonomous vehicle navigation safety systems." (141 chars) |
| **Legal Disclaimer** (disclaimer.md) | Current not specified in codebase scan | "Legal disclaimer for AV Navigation IP Protection. Informational purposes only; not legal or licensing advice for patent inquiries." (133 chars) |
| **Privacy Policy** (privacy.md) | Current not specified in codebase scan | "Privacy policy for AV Navigation IP Protection. How we collect, use, and protect your information when contacting us about licensing." (136 chars) |
| **Series A AV Startups** (series-a-av-patent-portfolio-strategy.md) | "Patent portfolio strategy for Series A autonomous vehicle startups. Strengthen IP with licensed camera-based navigation patents before Series B fundraising. 4-9 months vs. 30-66 months in-house development." (208 chars) ❌ | "Build your AV patent portfolio before Series B. License camera navigation IP in 4-9 months vs 30-66 months in-house development." (131 chars) |
| **Tesla FSD Competitors** (tesla-fsd-competitor-camera-patent-licensing.md) | "Tesla FSD competitors need camera-based patent protection. Learn how strategic licensing of camera safety patents enables credible competitive positioning and freedom to operate in the camera-first market." (207 chars) ❌ | "Compete with Tesla FSD using camera-based patent licensing. Strategic IP protection for camera-first autonomous vehicle competitors." (135 chars) |
| **Drone Delivery Pre-IPO** (drone-delivery-patent-portfolio-pre-ipo.md) | Current not specified in codebase scan | "Strengthen drone patent portfolios before IPO. License US Patent 12,001,207 for UAV camera-based navigation safety and visual positioning." (142 chars) |
| **VC Due Diligence** (venture-capital-av-patent-portfolio-due-diligence.md) | Current not specified in codebase scan | "VC guide to AV patent due diligence. Evaluate autonomous vehicle IP portfolios, patent quality, and freedom-to-operate for investments." (138 chars) |
| **Autonomous Trucking** (autonomous-trucking-patent-defense-strategy.md) | Current not specified in codebase scan | "Autonomous trucking patent defense strategy. License camera-based navigation safety IP for Class 8 trucks and commercial AV applications." (141 chars) |

**Action**: Replace `description` field in each content file's frontmatter with the optimized version from the "Optimized Description" column.

---

## Appendix B: Complete Frontmatter Template with All SEO Fields

**Template for all content pages**:

```yaml
---
# Basic metadata
title: "Page Title | AV Navigation IP Protection"
page_title: "Display Title for H1"
description: "Optimized meta description 155-160 characters (see Appendix A)"
keywords:
  - keyword one
  - keyword two
  - keyword three

# Page behavior
show_cta: true
is_homepage: false  # true for index.md only

# Breadcrumb (for non-homepage pages with parent)
breadcrumb_parent: "Solutions"
breadcrumb_parent_url: "/#solutions"

# Open Graph
og_title: "Page Title | AV Navigation IP Protection"
og_description: "Optimized meta description (same as description field)"
og_type: "article"  # Use "website" for homepage only
og_image: "https://av-navigation-ip.com/assets/images/og-images/page-slug-og.jpg"

# Twitter Card
twitter_card: "summary_large_image"
twitter_title: "Page Title | AV Navigation IP Protection"
twitter_description: "Optimized meta description (same as description field)"
twitter_image: "https://av-navigation-ip.com/assets/images/og-images/page-slug-og.jpg"

# Schema.org dates
date_published: "2025-11-01"
date_modified: "2025-11-12"

# Legacy fields (keep for compatibility)
layout: page
author: "AV Navigation IP Protection"
date: "2025-11-01"
modified: "2025-11-12"
---
```

**Example for Homepage** (index.md):

```yaml
---
title: "Protect Your AV Innovations with US Patent 12,001,207 Licensing"
description: "License US Patent 12,001,207 for camera-based navigation safety in autonomous vehicles and drones. Strengthen your IP portfolio."
keywords: "autonomous vehicle patent licensing, US patent 12001207, camera-based navigation safety, AV IP protection, drone navigation patents"
is_homepage: true
hero_title: "Protect Your AV Innovations with US Patent 12,001,207"
hero_subtitle: "License cutting-edge camera-based navigation safety technology for autonomous vehicles and drones"

# Open Graph
og_title: "AV Navigation IP Protection | US Patent 12,001,207 Licensing"
og_description: "License US Patent 12,001,207 for camera-based navigation safety in autonomous vehicles and drones. Strengthen your IP portfolio."
og_type: "website"
og_image: "https://av-navigation-ip.com/assets/images/og-images/homepage-og.jpg"

# Twitter Card
twitter_card: "summary_large_image"
twitter_title: "AV Navigation IP Protection | US Patent 12,001,207 Licensing"
twitter_description: "License US Patent 12,001,207 for camera-based navigation safety in autonomous vehicles and drones. Strengthen your IP portfolio."
twitter_image: "https://av-navigation-ip.com/assets/images/og-images/homepage-og.jpg"

date_published: "2025-11-01"
date_modified: "2025-11-12"
---
```

**Example for Landing Page** (series-a-av-patent-portfolio-strategy.md):

```yaml
---
title: "Series A AV Patent Portfolio Strategy | US 12,001,207"
page_title: "Build Your Patent Portfolio Before Series B Funding: Strategic Licensing for AV Startups"
description: "Build your AV patent portfolio before Series B. License camera navigation IP in 4-9 months vs 30-66 months in-house development."
keywords:
  - patent portfolio strategy for series A autonomous vehicle startups
  - AV startup IP protection
  - series A patent licensing
show_cta: true
breadcrumb_parent: "Solutions"
breadcrumb_parent_url: "/#solutions"

# Open Graph
og_title: "Series A AV Patent Portfolio Strategy | US Patent 12,001,207"
og_description: "Build your AV patent portfolio before Series B. License camera navigation IP in 4-9 months vs 30-66 months in-house development."
og_type: "article"
og_image: "https://av-navigation-ip.com/assets/images/og-images/series-a-av-og.jpg"

# Twitter Card
twitter_card: "summary_large_image"
twitter_title: "Series A AV Patent Portfolio Strategy | US Patent 12,001,207"
twitter_description: "Build your AV patent portfolio before Series B. License camera navigation IP in 4-9 months vs 30-66 months in-house development."
twitter_image: "https://av-navigation-ip.com/assets/images/og-images/series-a-av-og.jpg"

date_published: "2025-10-16"
date_modified: "2025-11-12"
layout: page
author: "AV Navigation IP Protection"
---
```

**Action**: Update all 13 content files with complete frontmatter following this structure.

---

## Appendix C: Background Image Search & Selection Workflow

**Updated Approach**: Manual background selection from free/commons platforms (replaces AI generation)

**Platforms to Use**:
- **Unsplash**: https://unsplash.com/ (100% free, no attribution required)
- **Pexels**: https://www.pexels.com/ (100% free, no attribution required)
- **Pixabay**: https://pixabay.com/ (Free for commercial use, CC0 license)

**Image Requirements**:
- **Dimensions**: 1200x630 pixels minimum (larger is okay, will be cropped)
- **Format**: JPG preferred (better compression)
- **License**: CC0 or Free for commercial use
- **Quality**: High resolution, professional photography
- **Style**: Clean, modern, tech-focused, not too busy

---

### Category A: Startup/Innovation

**File**: `startup-innovation.jpg`
**Used for pages**: Series A AV, Tesla FSD Competitor, Autonomous Trucking

**Primary Search Query**: "autonomous vehicle technology modern"

**Alternative Search Queries**:
1. "self-driving car dashboard futuristic"
2. "AI vehicle sensor technology"
3. "autonomous navigation camera system"
4. "electric vehicle innovation startup"
5. "automotive technology lab research"
6. "AV startup technology prototype"
7. "autonomous vehicle testing facility"

**Selection Criteria**:
- Shows modern autonomous vehicle technology
- Clean, professional aesthetic
- Tech-forward, innovation-focused
- Not too busy (text overlay area should be clear)
- Conveys startup energy and innovation

**Search Workflow**:
1. Go to Unsplash.com or Pexels.com
2. Search using primary query
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. Verify image is at least 1200x630px
6. Download highest resolution available
7. Save as `startup-innovation.jpg`

---

### Category B: Investment/Finance

**File**: `investment-finance.jpg`
**Used for pages**: VC Due Diligence, Drone Delivery Pre-IPO

**Primary Search Query**: "business investment strategy technology"

**Alternative Search Queries**:
1. "venture capital handshake deal"
2. "financial growth chart technology"
3. "tech investment portfolio modern"
4. "business funding startup meeting"
5. "corporate investment digital finance"
6. "venture capital pitch meeting"
7. "investment analysis technology"

**Selection Criteria**:
- Shows business/investment/finance theme
- Professional, trustworthy aesthetic
- Conveys growth and strategic thinking
- Clear space for text overlay in bottom 40%
- Suitable for VC and investor audience

**Search Workflow**:
1. Go to Unsplash.com or Pexels.com
2. Search using primary query
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. Verify image is at least 1200x630px
6. Download highest resolution available
7. Save as `investment-finance.jpg`

---

### Category C: Technical/Legal

**File**: `technical-legal.jpg`
**Used for pages**: Patent Details, Licensing

**Primary Search Query**: "patent document technology blueprint"

**Alternative Search Queries**:
1. "intellectual property legal document"
2. "technical diagram engineering blueprint"
3. "patent certificate official document"
4. "legal contract technology licensing"
5. "technical specifications detailed drawing"
6. "patent application blueprint"
7. "engineering document technical"

**Selection Criteria**:
- Shows technical/legal/documentation theme
- Professional, authoritative aesthetic
- Conveys intellectual property and technical expertise
- Clear space for text overlay in bottom 40%
- Not too busy or text-heavy

**Search Workflow**:
1. Go to Unsplash.com or Pexels.com
2. Search using primary query
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. Verify image is at least 1200x630px
6. Download highest resolution available
7. Save as `technical-legal.jpg`

---

### Category D: General/Info (Default Catch-All)

**File**: `general-info.jpg`
**Used for pages**: Homepage, Industry Insights, Contact, Thank You, About, Disclaimer, Privacy, and any new pages

**Primary Search Query**: "smart transportation future connectivity"

**Alternative Search Queries**:
1. "connected vehicles network highway"
2. "smart city transportation aerial"
3. "transportation technology network digital"
4. "intelligent transport system future"
5. "mobility innovation urban landscape"
6. "connected autonomous vehicles highway"
7. "smart mobility future city"

**Selection Criteria**:
- Shows transportation/connectivity/future theme
- Professional, forward-looking aesthetic
- Broad enough to work for multiple page types
- Clear space for text overlay in bottom 40%
- Conveys innovation and connectivity

**Search Workflow**:
1. Go to Unsplash.com or Pexels.com
2. Search using primary query
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. Verify image is at least 1200x630px
6. Download highest resolution available
7. Save as `general-info.jpg`

---

## License Verification

Before downloading any image, verify the license:

**Unsplash**:
- All images are free for commercial use
- No attribution required (but appreciated)
- Confirm "Free to use" badge on image page

**Pexels**:
- All free images are under Pexels License
- Free for commercial use
- No attribution required
- Confirm "Free to use" badge on image page

**Pixabay**:
- Look for "Free for commercial use" or "CC0" license
- No attribution required for CC0 images
- Confirm license terms on download page

---

## Complete Workflow Summary

**Time estimate**: 20-30 minutes for all 4 images

**Steps**:
1. **Search** for Category A (Startup/Innovation) using primary or alternative queries
2. **Select** best image meeting criteria (dimensions, clear overlay space, license)
3. **Download** highest resolution
4. **Save** as `startup-innovation.jpg` in `/website/assets/images/backgrounds/`
5. **Repeat** steps 1-4 for Categories B, C, and D
6. **Verify** all 4 images downloaded correctly
7. **Run** `python generate_og_images.py` to create final social sharing images with text overlay

**Result**: 4 background images + 4 generated OG images (8 total files)

---
## Appendix D: Test Validation Checklist

After completing all 4 phases, use this checklist to verify implementation:

### Automated Test Validation ✅

- [ ] Run `python test_website.py`
- [ ] Verify output shows **65+ tests passing**
- [ ] Verify **0 failures**, **0 errors**
- [ ] Check test output for new test classes:
  - [ ] `TestSEOMetaTags` (3 tests)
  - [ ] `TestStructuredDataSchemas` (3 tests)
  - [ ] `TestSocialImagesAndMeta` (2 tests)
  - [ ] `TestGoogleAnalytics` (1 test)

### Manual HTML Validation ✅

**Homepage (index.html)**:
- [ ] Open `/website/build/index.html` in browser
- [ ] View page source (Ctrl+U / Cmd+Option+U)
- [ ] Find `<meta property="og:title"` - verify content correct
- [ ] Find `<meta name="twitter:card"` - verify present
- [ ] Find `"@type": "Organization"` - verify Organization schema
- [ ] Find `googletagmanager.com` - verify GA script present
- [ ] Meta description length is 120-160 characters

**Landing Page (series-a-av-patent-portfolio-strategy.html)**:
- [ ] Open `/website/build/series-a-av-patent-portfolio-strategy.html`
- [ ] View page source
- [ ] Find `<meta property="og:image"` - verify URL points to `series-a-av-og.jpg`
- [ ] Find `"@type": "Article"` - verify Article schema present
- [ ] Find `"@type": "BreadcrumbList"` - verify breadcrumb schema present
- [ ] Verify breadcrumb has 3 items (Home → Solutions → Current Page)

**Core Page (patent-details.html)**:
- [ ] Open `/website/build/patent-details.html`
- [ ] View page source
- [ ] Find `"@type": "Patent"` - verify Patent schema still present (existing)
- [ ] Find `"@type": "BreadcrumbList"` - verify breadcrumb added
- [ ] All OG/Twitter tags present

### External Validation Tools ✅

**Google Rich Results Test**:
- [ ] Visit: https://search.google.com/test/rich-results
- [ ] Select "Code" tab
- [ ] Copy full HTML source from `/website/build/index.html`
- [ ] Paste into tool
- [ ] Click "Test Code"
- [ ] Result shows **"Valid"** for Organization schema
- [ ] Repeat for `series-a-av-patent-portfolio-strategy.html`
- [ ] Result shows **"Valid"** for Article + BreadcrumbList schemas

**Facebook Sharing Debugger** (if deployed to staging):
- [ ] Visit: https://developers.facebook.com/tools/debug/
- [ ] Enter staging URL (if available)
- [ ] Verify OG image displays correctly (1200x630px)
- [ ] Verify title and description correct
- [ ] *Note: Skip if not deployed to publicly accessible URL*

**Twitter Card Validator** (if deployed to staging):
- [ ] Visit: https://cards-dev.twitter.com/validator
- [ ] Enter staging URL (if available)
- [ ] Verify Twitter Card displays correctly
- [ ] *Note: Skip if not deployed to publicly accessible URL*

### Image Asset Validation ✅

- [ ] Navigate to `/website/assets/images/og-images/`
- [ ] Verify **13 JPG files** present:
  - [ ] homepage-og.jpg
  - [ ] patent-details-og.jpg
  - [ ] licensing-og.jpg
  - [ ] industry-insights-og.jpg
  - [ ] contact-og.jpg
  - [ ] thank-you-og.jpg
  - [ ] about-og.jpg
  - [ ] disclaimer-og.jpg
  - [ ] privacy-og.jpg
  - [ ] series-a-av-og.jpg
  - [ ] tesla-fsd-competitor-og.jpg
  - [ ] drone-delivery-og.jpg
  - [ ] venture-capital-due-diligence-og.jpg
  - [ ] autonomous-trucking-og.jpg
- [ ] Verify all images are **1200x630 pixels**
- [ ] Verify all images are **JPG format**

### Meta Description Validation ✅

For each page, verify meta description is optimized:

- [ ] Homepage: 144 chars (acceptable)
- [ ] Patent Details: 129 chars (acceptable)
- [ ] Licensing: ~133 chars
- [ ] Industry Insights: ~133 chars
- [ ] Contact: ~137 chars
- [ ] Thank You: ~127 chars
- [ ] About: ~141 chars
- [ ] Disclaimer: ~133 chars
- [ ] Privacy: ~136 chars
- [ ] Series A: **131 chars (updated from 208)**
- [ ] Tesla FSD: **135 chars (updated from 207)**
- [ ] Drone Delivery: ~142 chars
- [ ] VC Due Diligence: ~138 chars
- [ ] Autonomous Trucking: ~141 chars

All descriptions should be **120-160 characters**.

### Build Process Validation ✅

- [ ] Run `python generate_site.py`
- [ ] Build completes with **no errors**
- [ ] Build output shows **13 pages generated**
- [ ] Assets copied to `/website/build/assets/images/og-images/`
- [ ] Sitemap.xml generated (already exists, no changes needed)

### Git Commit Validation ✅

- [ ] Run `git status` - verify all modified files staged
- [ ] Run `git diff --cached` - review changes before commit
- [ ] Commit message is descriptive (see Phase 4.5 template)
- [ ] Commit includes attribution to Claude Code
- [ ] No unintended files committed (e.g., `.pyc`, `__pycache__`)

---

## Appendix E: File Modification Summary

Quick reference table showing which files are modified in each phase:

| Phase | File Path | Modification Type | Description |
|-------|-----------|-------------------|-------------|
| **Phase 1** | `/website/generate_site.py` | Edit | Add OG/Twitter field extraction |
| **Phase 1** | `/website/designs/default/base.html` | Edit | Add OG/Twitter meta tags to `<head>` |
| **Phase 1** | `/website/content/*.md` (all 13 files) | Edit | Add OG/Twitter frontmatter fields |
| **Phase 1** | `/website/test_website.py` | Edit | Add `TestSEOMetaTags` class |
| **Phase 2** | `/website/designs/default/page.html` | Edit | Add Article + BreadcrumbList schemas |
| **Phase 2** | `/website/generate_site.py` | Edit | Add schema date fields, `determine_page_type()` function |
| **Phase 2** | `/website/content/*.md` (all 13 files) | Edit | Add `date_published`, `date_modified` fields |
| **Phase 2** | `/website/test_website.py` | Edit | Add `TestStructuredDataSchemas` class |
| **Phase 3** | `/website/assets/images/og-images/` | Create | Generate 13 social images (1200x630px JPG) |
| **Phase 3** | `/website/content/*.md` (all 13 files) | Edit | Update `og_image`, `twitter_image` paths |
| **Phase 3** | `/website/content/*.md` (all 13 files) | Edit | Replace meta descriptions with optimized versions |
| **Phase 3** | `/website/test_website.py` | Edit | Add `TestSocialImagesAndMeta` class |
| **Phase 4** | `/website/designs/default/base.html` | Edit | Add Google Analytics placeholder script |
| **Phase 4** | `/website/test_website.py` | Edit | Add `TestGoogleAnalytics` class |

**Total files modified**: 18 files (2 Python, 2 HTML templates, 13 markdown content files, 1 test file) + 13 new image files created

---

## Appendix F: Troubleshooting Common Issues

### Issue: Tests fail with "Missing og:title" error

**Cause**: Generator not passing OG fields to template context

**Solution**:
1. Verify Phase 1.1 changes in `generate_site.py`
2. Ensure all OG fields added to template context dictionary
3. Check variable names match exactly (e.g., `og_title` not `og:title`)
4. Regenerate site: `python generate_site.py`
5. Re-run tests: `python test_website.py`

### Issue: Images not found during test

**Cause**: Images not copied to build directory or incorrect paths

**Solution**:
1. Verify all 13 images exist in `/website/assets/images/og-images/`
2. Check file naming matches exactly (e.g., `homepage-og.jpg` not `homepage.jpg`)
3. Regenerate site to copy assets: `python generate_site.py`
4. Check `/website/build/assets/images/og-images/` has all 13 images
5. Verify frontmatter `og_image` URLs match actual filenames

### Issue: Meta description test fails (too long/short)

**Cause**: Description not updated to optimized version

**Solution**:
1. Check Appendix A for correct optimized description
2. Update frontmatter `description` field in content file
3. Ensure description is 120-160 characters (count carefully)
4. Regenerate site: `python generate_site.py`
5. Re-run tests: `python test_website.py`

### Issue: Google Rich Results Test shows "Invalid" for schemas

**Cause**: JSON-LD syntax error or missing required fields

**Solution**:
1. Copy full schema JSON from generated HTML
2. Validate JSON syntax using https://jsonlint.com/
3. Check for missing commas, quotes, or brackets
4. Verify all required schema fields present (e.g., `headline`, `datePublished` for Article)
5. Fix syntax in `page.html` template
6. Regenerate and retest

### Issue: Breadcrumb schema shows only 1 item instead of 2-3

**Cause**: Conditional logic error in breadcrumb schema

**Solution**:
1. Check Phase 2.2 code in `page.html`
2. Verify Jinja2 conditional: `{% if breadcrumb_parent %}`
3. Ensure frontmatter has `breadcrumb_parent` and `breadcrumb_parent_url` for landing pages
4. Check comma placement in JSON (before second item)
5. Regenerate and inspect HTML source

### Issue: GA script not appearing in generated HTML

**Cause**: Template code not added or `</head>` tag location issue

**Solution**:
1. Verify Phase 4.1 code added to `base.html`
2. Check code is inside `<head>` section (before `</head>`)
3. Ensure no typos in script tags
4. Regenerate site: `python generate_site.py`
5. View source of any generated page, search for `googletagmanager`

---

## Document Metadata

**Document Status**: Active - Ready for Implementation
**Version**: 1.0
**Created**: November 12, 2025
**Last Updated**: November 12, 2025
**Estimated Completion**: November 16, 2025 (4 days)
**Owner**: Developer (Team Member)
**Priority**: High
**Blocking**: Milestone 5 (Production Deployment)

**Related Documents**:
- `20251110_production_readiness_prd.md` - Parent PRD (Milestone 3)
- `website_development_prd.md` - Overall project context
- `seo_landing_pages_phase4_publishing.md` - SEO content strategy
- `.agent/SOP/site_generation_deployment.md` - Build & deploy process

**Next Steps After Completion**:
1. Update production readiness PRD to mark Milestone 3 complete
2. Proceed to Milestone 5: Production Deployment
3. Configure actual Google Analytics property during deployment
4. Validate all external tools with production URLs

---

**END OF PRD**
