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

### 5. Social Sharing Images

Create default Open Graph image (1200x630px):
- File: `/website/assets/images/og-default.jpg`
- Content: Site branding + patent number
- Text overlay: "US Patent 12,001,207 B2 | Camera-Based Navigation Safety"
- Tool: Canva (free) or similar

### 6. Meta Description Optimization

Verify all pages have meta descriptions 155-160 characters:
- Review YAML frontmatter `description:` field
- Ensure includes primary keyword + CTA
- Update if too short (<150 chars) or too long (>160 chars)

### 7. Google Analytics Integration

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

### 8. Google Search Console Setup

**Setup Steps**:
1. Go to https://search.google.com/search-console
2. Add property (use domain or URL prefix)
3. Verify ownership (HTML file upload or DNS TXT record)
4. Submit sitemap: `https://[domain]/sitemap.xml`
5. Monitor "Pages" report for indexing status

## Implementation Approach

### Option 1: Template-Level Implementation (Recommended)

Modify `/website/designs/default/base.html` to dynamically generate meta tags from YAML frontmatter:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }}</title>
  <meta name="description" content="{{ description }}">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://[domain]/{{ filename }}" />

  <!-- Open Graph -->
  <meta property="og:title" content="{{ title }}" />
  <meta property="og:description" content="{{ description }}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://[domain]/{{ filename }}" />
  <meta property="og:image" content="https://[domain]/assets/images/og-default.jpg" />
  <meta property="og:site_name" content="AV Navigation IP Protection" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{{ title }}" />
  <meta name="twitter:description" content="{{ description }}" />
  <meta name="twitter:image" content="https://[domain]/assets/images/og-default.jpg" />

  <!-- Organization Schema (sitewide) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "AV Navigation IP Protection",
    "url": "https://[domain]"
  }
  </script>

  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
</head>
```

### Option 2: Generator Script Updates

Modify `/website/generate_site.py` to inject SEO tags during site generation:
- Parse YAML frontmatter
- Generate canonical URLs
- Insert structured data scripts
- Pass domain variable to templates

## Acceptance Criteria

### Validation
- [ ] All pages validate with Google Rich Results Test (structured data)
- [ ] All pages validate with Facebook Sharing Debugger (Open Graph)
- [ ] All pages validate with Twitter Card Validator
- [ ] No structured data errors or warnings

### Meta Tags
- [ ] All 12 pages have canonical URLs
- [ ] All 12 pages have Open Graph tags
- [ ] All 12 pages have Twitter Card tags
- [ ] Meta descriptions 155-160 characters (all pages)

### Structured Data
- [ ] Organization schema present on all pages
- [ ] Article schema present on all content pages
- [ ] BreadcrumbList schema present on pages with breadcrumbs

### Analytics
- [ ] Google Analytics tracking code on all pages
- [ ] Google Analytics tracking verified (GA Debugger extension)
- [ ] Test pageview event fires

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

1. **Create Open Graph image** (1200x630px) at `/website/assets/images/og-default.jpg`
2. **Update base.html template** with all meta tags (Option 1)
3. **Update generator script** if needed (Option 2)
4. **Set domain variable** (replace `[domain]` with actual domain)
5. **Set Google Analytics ID** (replace `G-XXXXXXXXXX`)
6. **Add date fields** to YAML frontmatter if missing:
   ```yaml
   date: "2025-10-16"
   modified: "2025-11-10"
   ```
7. **Regenerate site**: `python generate_site.py`
8. **Run validation tests** (Rich Results, Facebook, Twitter)
9. **Test Google Analytics** (GA Debugger)
10. **Set up Google Search Console**

## Files to Modify

- `/website/designs/default/base.html` - Add meta tags and schemas
- `/website/generate_site.py` - Update to pass domain and canonical URLs to templates (if needed)
- `/website/assets/images/og-default.jpg` - Create social sharing image
- All `.md` files - Add `date` and `modified` fields to frontmatter (if missing)

## Success Metrics

- 100% of pages pass Google Rich Results Test
- 100% of pages pass Facebook Sharing Debugger
- 100% of pages pass Twitter Card Validator
- Google Analytics tracking 100% of pageviews
- Google Search Console shows no critical errors

## Related Documentation

- `.agent/Tasks/seo_technical_specs.md` - Comprehensive SEO specifications
- `.agent/Tasks/seo_landing_pages_phase4_publishing.md` - Phase 4 SEO publishing task

---

**Status**: Not Started
**Created**: November 10, 2025
**Priority**: Critical
**Estimated Effort**: 3-4 days
