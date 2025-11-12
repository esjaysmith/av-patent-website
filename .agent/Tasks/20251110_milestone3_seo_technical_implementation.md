# Milestone 3: SEO Technical Implementation

## Task Information
- **Parent PRD**: `20251110_production_readiness_prd.md`
- **Milestone**: 3 of 6
- **Priority**: Critical (Launch Blocker)
- **Duration**: 3-4 days
- **Status**: Not Started
- **Dependencies**: Milestone 1 (breadcrumbs needed for BreadcrumbList schema)
- **Blocks**: Milestone 5 (SEO must be complete before production deployment)
- **Reference**: `.agent/Tasks/seo_technical_specs.md` (comprehensive specifications)

## Overview

Implement all missing SEO technical requirements per `seo_technical_specs.md`: Open Graph tags, Twitter Cards, canonical URLs, structured data (JSON-LD schemas), Google Analytics, and Google Search Console setup.

**Problem**: Site missing critical SEO tags that affect search visibility and social sharing.

**Solution**: Implement all technical SEO requirements per detailed specifications.

## Deliverables

### 1. Open Graph Meta Tags (All 12 Pages)

Add to `<head>` section of all pages:
```html
<meta property="og:title" content="[Page Title]" />
<meta property="og:description" content="[Meta Description]" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://[domain]/[page-slug].html" />
<meta property="og:image" content="https://[domain]/assets/images/og-default.jpg" />
<meta property="og:site_name" content="AV Navigation IP Protection" />
<meta property="og:locale" content="en_US" />
```

### 2. Twitter Card Meta Tags (All 12 Pages)

Add to `<head>` section of all pages:
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="[Page Title]" />
<meta name="twitter:description" content="[Meta Description]" />
<meta name="twitter:image" content="https://[domain]/assets/images/og-default.jpg" />
```

### 3. Canonical URLs (All 12 Pages)

Add to `<head>` section of all pages:
```html
<link rel="canonical" href="https://[domain]/[page-slug].html" />
```

### 4. Structured Data Schemas

#### Organization Schema (Sitewide - in base.html)
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AV Navigation IP Protection",
  "url": "https://[domain]",
  "logo": "https://[domain]/assets/images/logo.png",
  "description": "Patent licensing for autonomous vehicle camera-based navigation and safety systems. US Patent 12,001,207 B2.",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Sales",
    "email": "[contact-email]",
    "availableLanguage": ["English"]
  }
}
</script>
```

#### Article Schema (All Content Pages)
```json
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
      "url": "https://[domain]/assets/images/logo.png"
    }
  },
  "datePublished": "{{ date or '2025-10-16' }}",
  "dateModified": "{{ modified or date or '2025-10-16' }}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ canonical_url }}"
  }
}
</script>
```

#### BreadcrumbList Schema (All Pages with Breadcrumbs)
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
      "name": "{{ page_title or title }}",
      "item": "{{ canonical_url }}"
    }
  ]
}
</script>
```

### 5. Environment Configuration

**Create `.env` file for environment-specific variables:**

Required variables:
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

**Files:**
- `/website/.env.example` - Template (committed to git)
- `/website/.env` - Local configuration (gitignored)
- Update `/website/.gitignore` - Add `.env` entry

**Dependencies:**
Add to `requirements.txt`:
```
python-dotenv==1.0.0
Pillow==10.1.0
```

### 6. Social Sharing Images - Background Image Selection

**Developer must select 4 background images from free/commons platforms (Unsplash, Pexels, or Pixabay):**

#### Category A - Startup/Innovation
Pages: Series A AV, Tesla FSD Competitor, Autonomous Trucking

- **Primary search query**: "autonomous vehicle technology modern"
- **Alternative queries**:
  - "self-driving car dashboard futuristic"
  - "AI vehicle sensor technology"
  - "autonomous navigation camera system"
  - "electric vehicle innovation startup"
  - "automotive technology lab research"
- **Save as**: `/website/assets/images/backgrounds/startup-innovation.jpg`

#### Category B - Investment/Finance
Pages: VC Due Diligence, Drone Delivery Pre-IPO

- **Primary search query**: "business investment strategy technology"
- **Alternative queries**:
  - "venture capital handshake deal"
  - "financial growth chart technology"
  - "tech investment portfolio modern"
  - "business funding startup meeting"
  - "corporate investment digital finance"
- **Save as**: `/website/assets/images/backgrounds/investment-finance.jpg`

#### Category C - Technical/Legal
Pages: Patent Details, Licensing

- **Primary search query**: "patent document technology blueprint"
- **Alternative queries**:
  - "intellectual property legal document"
  - "technical diagram engineering blueprint"
  - "patent certificate official document"
  - "legal contract technology licensing"
  - "technical specifications detailed drawing"
- **Save as**: `/website/assets/images/backgrounds/technical-legal.jpg`

#### Category D - General/Info (Default Catch-All)
Pages: Homepage, Industry Insights, Contact, Thank You, About, and any new pages

- **Primary search query**: "smart transportation future connectivity"
- **Alternative queries**:
  - "connected vehicles network highway"
  - "smart city transportation aerial"
  - "transportation technology network digital"
  - "intelligent transport system future"
  - "mobility innovation urban landscape"
- **Save as**: `/website/assets/images/backgrounds/general-info.jpg`

#### Background Image Requirements
- **Minimum resolution**: 1200x630px (will be cropped/resized if larger)
- **License**: Free for commercial use (Unsplash, Pexels Free License, or CC0)
- **Style**: Professional, modern, relevant to category theme
- **Avoid**: Text overlays, watermarks, busy/cluttered compositions

### 7. Social Sharing Images - Python Generator Script

**Create `/website/generate_og_images.py`**

This script generates 1200x630px social sharing images with text overlay.

#### Script Features:
- Loads background images from `/website/assets/images/backgrounds/`
- Applies dark gradient overlay (transparent to rgba(0,0,0,0.6)) on bottom 40%
- Renders text in two lines:
  - Line 1: "US PATENT 12,001,207 B2" (white, 48-54px, bold, uppercase)
  - Line 2: "Camera-Based Navigation Safety" (orange #e67e22, 34-38px, medium)
- Uses Space Grotesk font (website brand font) with fallback to system fonts
- Adds text shadow for readability on light backgrounds
- Smart crop from center if aspect ratio doesn't match 1200:630
- Outputs high-quality JPEG (quality=92) to `/website/assets/images/og-[category].jpg`

#### CLI Usage:
```bash
# Generate all 4 category images
python generate_og_images.py

# Regenerate single category
python generate_og_images.py --category startup-innovation

# Preview without saving
python generate_og_images.py --preview
```

#### Page-to-Category Mapping:
```python
OG_IMAGE_CATEGORIES = {
    'series-a-av-patent-portfolio-strategy': 'startup-innovation',
    'tesla-fsd-competitor-camera-patent-licensing': 'startup-innovation',
    'autonomous-trucking-patent-defense-strategy': 'startup-innovation',
    'venture-capital-av-patent-portfolio-due-diligence': 'investment-finance',
    'drone-delivery-patent-portfolio-pre-ipo': 'investment-finance',
    'patent-details': 'technical-legal',
    'licensing': 'technical-legal',
}
DEFAULT_OG_CATEGORY = 'general-info'  # Catch-all for unlisted pages
```

#### Generated Output Files:
- `/website/assets/images/og-startup-innovation.jpg`
- `/website/assets/images/og-investment-finance.jpg`
- `/website/assets/images/og-technical-legal.jpg`
- `/website/assets/images/og-general-info.jpg`

### 8. Meta Description Optimization

Verify all pages have meta descriptions 155-160 characters:
- Review YAML frontmatter `description:` field
- Ensure includes primary keyword + CTA
- Update if too short (<150 chars) or too long (>160 chars)

### 9. Google Analytics Integration

Add to `base.html` template before `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Setup**:
1. Create Google Analytics 4 property
2. Get Measurement ID (G-XXXXXXXXXX)
3. Replace placeholder in code
4. Test with Google Analytics Debugger extension

### 10. Google Search Console Setup

**Setup Steps**:
1. Go to https://search.google.com/search-console
2. Add property (use domain or URL prefix)
3. Verify ownership (HTML file upload or DNS TXT record)
4. Submit sitemap: `https://[domain]/sitemap.xml`
5. Monitor "Pages" report for indexing status

## Implementation Approach

### Environment Configuration Integration

Modify `/website/generate_site.py` to read environment variables:

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SITE_URL = os.getenv('SITE_URL', 'http://localhost:8000')
SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'localhost:8000')
GA_ID = os.getenv('GOOGLE_ANALYTICS_ID', '')
GA_ENABLED = os.getenv('GOOGLE_ANALYTICS_ENABLED', 'false').lower() == 'true'
```

Pass these variables to templates for use in meta tags and analytics.

### Template-Level Implementation (Recommended)

Modify `/website/designs/default/base.html` to use environment variables and dynamically generate meta tags from YAML frontmatter:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }}</title>
  <meta name="description" content="{{ description }}">

  <!-- Canonical URL -->
  <link rel="canonical" href="{{ site_url }}/{{ filename }}" />

  <!-- Open Graph -->
  <meta property="og:title" content="{{ title }}" />
  <meta property="og:description" content="{{ description }}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{{ site_url }}/{{ filename }}" />
  <meta property="og:image" content="{{ site_url }}{{ og_image }}" />
  <meta property="og:site_name" content="AV Navigation IP Protection" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{{ title }}" />
  <meta name="twitter:description" content="{{ description }}" />
  <meta name="twitter:image" content="{{ site_url }}{{ og_image }}" />

  <!-- Organization Schema (sitewide) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "AV Navigation IP Protection",
    "url": "{{ site_url }}"
  }
  </script>

  <!-- Google Analytics -->
  {% if ga_enabled %}
  <script async src="https://www.googletagmanager.com/gtag/js?id={{ ga_id }}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '{{ ga_id }}');
  </script>
  {% endif %}
</head>
```

### Generator Script - OG Image Category Assignment

Add category mapping and lookup logic to `/website/generate_site.py`:

```python
# Page-to-category mapping for OG images
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
    # ... existing context ...
    'site_url': SITE_URL,
    'og_image': og_image_path,
    'ga_id': GA_ID,
    'ga_enabled': GA_ENABLED,
}
```

## Acceptance Criteria

### Environment Configuration
- [ ] `.env.example` template created and committed to git
- [ ] `.env` added to `.gitignore`
- [ ] `.env` file configured locally with all required variables
- [ ] `generate_site.py` reads environment variables correctly
- [ ] All absolute URLs (OG tags, canonical) use environment domain
- [ ] Local development works with localhost domain
- [ ] Dependencies added to `requirements.txt`: `python-dotenv`, `Pillow`

### Social Sharing Images
- [ ] 4 background images downloaded to `/website/assets/images/backgrounds/`
- [ ] All background images are 1200x630px minimum, properly licensed (CC0/Free)
- [ ] `generate_og_images.py` script created and functional
- [ ] Script successfully generates all 4 OG images with text overlay
- [ ] Generated images use Space Grotesk font with orange branding
- [ ] Text overlay: "US PATENT 12,001,207 B2 | Camera-Based Navigation Safety"
- [ ] All pages reference correct OG image based on category mapping
- [ ] Background images and generated OG images added to `.gitignore`

### Validation
- [ ] All pages validate with Google Rich Results Test (structured data)
- [ ] All pages validate with Facebook Sharing Debugger (Open Graph)
- [ ] All pages validate with Twitter Card Validator
- [ ] No structured data errors or warnings
- [ ] OG images display correctly in social media previews (1200x630px)

### Meta Tags
- [ ] All 12 pages have canonical URLs using environment domain
- [ ] All 12 pages have Open Graph tags
- [ ] All 12 pages have Twitter Card tags
- [ ] Meta descriptions 155-160 characters (all pages)

### Structured Data
- [ ] Organization schema present on all pages
- [ ] Article schema present on all content pages
- [ ] BreadcrumbList schema present on pages with breadcrumbs

### Analytics
- [ ] Google Analytics tracking code conditional on `ga_enabled` variable
- [ ] Google Analytics ID from environment variable
- [ ] Google Analytics tracking verified (GA Debugger extension)
- [ ] Test pageview event fires
- [ ] Analytics disabled in development environment

### Search Console
- [ ] Site verified in Google Search Console
- [ ] Sitemap submitted: `https://[domain]/sitemap.xml`
- [ ] No critical errors in "Pages" report

## Testing Checklist

### Google Rich Results Test
1. Go to https://search.google.com/test/rich-results
2. Test 3 sample pages (homepage, 1 landing page, patent-details)
3. Verify Organization, Article, BreadcrumbList schemas detected
4. Fix any errors or warnings

### Facebook Sharing Debugger
1. Go to https://developers.facebook.com/tools/debug/
2. Test 3 sample pages
3. Verify Open Graph tags detected correctly
4. Verify image displays (1200x630px minimum)

### Twitter Card Validator
1. Go to https://cards-dev.twitter.com/validator
2. Test 3 sample pages
3. Verify Twitter Card type: summary_large_image
4. Verify preview displays correctly

### Google Analytics
1. Install Google Analytics Debugger extension (Chrome)
2. Open site in browser
3. Open DevTools Console
4. Verify GA tracking events fire
5. Check Google Analytics real-time report

## Implementation Steps

### Phase 1: Environment Setup
1. **Create `.env.example`** template with all required variables
2. **Copy to `.env`** and configure for local development
3. **Update `.gitignore`** to exclude `.env`, background images, and generated OG images
4. **Update `requirements.txt`** with `python-dotenv==1.0.0` and `Pillow==10.1.0`
5. **Install dependencies**: `pip install -r requirements.txt`

### Phase 2: Background Image Selection
6. **Create directory**: `/website/assets/images/backgrounds/`
7. **Download 4 background images** from Unsplash/Pexels/Pixabay using search queries:
   - `startup-innovation.jpg` - "autonomous vehicle technology modern"
   - `investment-finance.jpg` - "business investment strategy technology"
   - `technical-legal.jpg` - "patent document technology blueprint"
   - `general-info.jpg` - "smart transportation future connectivity"
8. **Verify image requirements**: 1200x630px minimum, CC0/Free license

### Phase 3: OG Image Generator Script
9. **Create `/website/generate_og_images.py`** with:
   - Pillow image processing
   - Text overlay rendering (Space Grotesk font)
   - Category-based output
   - CLI interface (--category, --preview flags)
10. **Test script**: `python generate_og_images.py`
11. **Verify output**: 4 images in `/website/assets/images/og-*.jpg`

### Phase 4: Site Generator Updates
12. **Modify `generate_site.py`**:
   - Add dotenv import and environment variable loading
   - Add OG_IMAGE_CATEGORIES mapping
   - Add category lookup in page processing loop
   - Pass `site_url`, `og_image`, `ga_id`, `ga_enabled` to template context
13. **Update `base.html` template**:
   - Replace hardcoded domain with `{{ site_url }}`
   - Add `{{ og_image }}` for category-based images
   - Add conditional Google Analytics with `{% if ga_enabled %}`
   - Update all structured data to use environment variables

### Phase 5: Content Metadata
14. **Add date fields** to YAML frontmatter if missing:
   ```yaml
   date: "2025-10-16"
   modified: "2025-11-10"
   ```
15. **Verify meta descriptions** 155-160 characters (all pages)

### Phase 6: Testing & Validation
16. **Regenerate site**: `python generate_site.py`
17. **Test locally**: Verify OG images load correctly
18. **Run validation tests**:
   - Google Rich Results Test (3 sample pages)
   - Facebook Sharing Debugger (3 sample pages)
   - Twitter Card Validator (3 sample pages)
19. **Test Google Analytics** (GA Debugger extension)
20. **Set up Google Search Console** and submit sitemap

## Files to Modify

### New Files
- `/website/.env.example` - Environment variable template (commit to git)
- `/website/.env` - Local environment configuration (gitignored)
- `/website/generate_og_images.py` - OG image generator script
- `/website/assets/images/backgrounds/` - Directory for background images (4 files)
- `/website/assets/images/og-*.jpg` - Generated social sharing images (4 files, gitignored)

### Modified Files
- `/website/.gitignore` - Add `.env`, background images, generated OG images
- `/website/requirements.txt` - Add `python-dotenv==1.0.0`, `Pillow==10.1.0`
- `/website/designs/default/base.html` - Update meta tags, add environment variables
- `/website/generate_site.py` - Add environment loading, OG category mapping, template context
- All `/website/content/*.md` files - Add `date` and `modified` fields to frontmatter (if missing)

## Directory Structure

After implementation, the directory structure will be:

```
/website/
├── .env.example                    # Environment template (committed)
├── .env                            # Local config (gitignored)
├── .gitignore                      # Updated with new entries
├── requirements.txt                # Updated with new dependencies
├── generate_site.py                # Modified for environment variables
├── generate_og_images.py           # New OG image generator script
├── assets/
│   └── images/
│       ├── backgrounds/            # Background images (gitignored)
│       │   ├── startup-innovation.jpg
│       │   ├── investment-finance.jpg
│       │   ├── technical-legal.jpg
│       │   └── general-info.jpg
│       ├── og-startup-innovation.jpg    # Generated (gitignored)
│       ├── og-investment-finance.jpg    # Generated (gitignored)
│       ├── og-technical-legal.jpg       # Generated (gitignored)
│       └── og-general-info.jpg          # Generated (gitignored)
└── designs/
    └── default/
        └── base.html               # Modified for environment variables
```

## Success Metrics

- 100% of pages pass Google Rich Results Test
- 100% of pages pass Facebook Sharing Debugger with correct category images
- 100% of pages pass Twitter Card Validator with correct category images
- Google Analytics tracking 100% of pageviews (when enabled)
- Google Search Console shows no critical errors
- All 4 OG images render correctly with brand-consistent text overlay
- Environment configuration works correctly in dev/staging/production

## Related Documentation

- `.agent/Tasks/seo_technical_specs.md` - Comprehensive SEO specifications
- `.agent/Tasks/seo_landing_pages_phase4_publishing.md` - Phase 4 SEO publishing task

---

**Status**: Not Started
**Created**: November 10, 2025
**Last Updated**: November 12, 2025
**Priority**: Critical
**Estimated Effort**: 3-4 days

## Change Log

### November 12, 2025 - Social Sharing Images Refactored
- **Removed**: AI-generated image approach
- **Added**: Manual image selection from free/commons platforms (Unsplash, Pexels, Pixabay)
- **Added**: Python script (`generate_og_images.py`) to overlay text on background images
- **Added**: Category-based image system (4 categories for 12 pages)
- **Added**: Environment configuration (.env file) for deployment-specific variables
- **Added**: Comprehensive search queries for each image category
- **Updated**: Implementation steps to 6-phase workflow
- **Updated**: Acceptance criteria with environment and image generation requirements
