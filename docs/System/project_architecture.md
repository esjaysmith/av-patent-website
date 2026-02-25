# Project Architecture

**Last Updated:** February 25, 2026

## Overview

**Project:** AV Navigation IP Protection Website
**Purpose:** Static website for monetizing US Patent 12,001,207 B2 through licensing
**URL:** https://av-navigation-ip.com
**Hosting:** Netlify (git-based deployment)
**Status:** Live in production, SEO optimization ongoing

## Project Structure

```
op_patent/
├── docs/
│   ├── plans/                    # Active plans
│   │   ├── archived/             # Completed/superseded plans
│   │   └── 20260126_zero_budget_traffic_plan.md
│   ├── System/
│   │   ├── project_architecture.md   # This file
│   │   └── patent_reference.md       # US Patent 12,001,207 B2 reference
│   ├── SOP/
│   │   ├── content_management.md
│   │   └── site_generation_deployment.md
│   ├── US12001207B2.html         # Full patent document (official source)
│   └── README.md                 # Documentation index
├── website/
│   ├── content/                  # Markdown source files (EDIT THESE)
│   ├── designs/default/          # Jinja2 templates (base.html, page.html)
│   ├── assets/                   # Static assets (CSS, images, JS)
│   ├── build/                    # Generated output (DO NOT EDIT)
│   ├── generate_site.py          # Static site generator
│   ├── test_website.py           # Test suite
│   ├── deploy.sh                 # Deployment script
│   └── requirements.txt          # Python dependencies
├── kanban.md                     # Project kanban board
├── CLAUDE.md                     # Claude Code instructions
└── .gitignore
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Content | Markdown with YAML frontmatter |
| Generator | Python 3.x, markdown 3.5.1, Jinja2 3.1.2 |
| Frontend | HTML5, Bootstrap 5 (CDN), minimal JS |
| Testing | BeautifulSoup4 4.12.2, Python test suite (46 tests) |
| Hosting | Netlify (auto-deploy on git push) |
| Contact Form | Web3Forms |
| Domain | av-navigation-ip.com (Namecheap, catch-all email) |

## Site Generation Flow

```
/website/content/*.md  →  generate_site.py  →  /website/build/*.html
     (source)              (Jinja2 templates)        (output)
```

1. Edit Markdown in `/website/content/`
2. Run `cd website && python generate_site.py`
3. Output lands in `/website/build/` (14 pages + sitemap.xml + robots.txt)
4. `git push` triggers Netlify deploy

## Current Pages (14)

### Core Pages
- `index.md` — Homepage with hero section
- `patent-details.md` — Technical patent overview
- `about.md` — About the patent/inventors
- `licensing.md` — Licensing opportunities
- `industry-insights.md` — Market trends
- `contact.md` — Contact form (Web3Forms)
- `thank-you.md` — Form confirmation
- `privacy.md` — Privacy policy
- `disclaimer.md` — Legal disclaimer

### SEO Landing Pages
- `series-a-av-patent-portfolio-strategy.md`
- `tesla-fsd-competitor-camera-patent-licensing.md`
- `drone-delivery-patent-portfolio-pre-ipo.md`
- `venture-capital-av-patent-portfolio-due-diligence.md`
- `autonomous-trucking-patent-defense-strategy.md`

## Template System

```
designs/default/
├── base.html    # Header, nav, footer, meta tags, security headers
└── page.html    # Extends base, renders content blocks
```

**Frontmatter fields:**
- `title`, `description`, `keywords` (required — SEO)
- `page_title`, `show_cta`, `is_homepage`, `hero_title`, `hero_subtitle` (optional)

## SEO Implementation

**Implemented:**
- Meta tags (title, description, keywords) on all pages
- Open Graph and Twitter Card meta tags
- Self-referencing canonical URLs (homepage canonicalizes to `/`)
- Structured data (JSON-LD)
- sitemap.xml and robots.txt auto-generated
- Descriptive anchor text (no generic "Learn More" links)
- Hyphen-separated URLs throughout

**Canonical URL strategy:** All pages use self-referencing canonicals. Homepage `/index.html` canonicalizes to `/`. No tracking parameters in canonical URLs.

## Security Headers

All pages include via `<meta>` tags in `base.html`:
- **Content-Security-Policy** — Whitelists self, Google Analytics, Google Fonts; blocks frames
- **X-Frame-Options** — DENY (prevents clickjacking)
- **X-Content-Type-Options** — nosniff
- **Referrer-Policy** — strict-origin-when-cross-origin

Server-level headers should also be configured on Netlify for full protection (see archived `security-headers-implementation.md` if details needed).

## Domain & Hosting

- **Primary domain:** `av-navigation-ip.com` (non-www)
- **www redirect:** Netlify auto-redirects www to non-www (301)
- **SSL:** HTTPS via Netlify (auto-provisioned)
- **Deployment:** `git push` to master triggers auto-build and deploy

## External Integrations

| Service | Purpose | Status |
|---------|---------|--------|
| Web3Forms | Contact form submissions | Active |
| Google Search Console | SEO monitoring, indexing | Configured |
| Bing Webmaster Tools | Bing indexing | Configured |
| Google Analytics (GA4) | Traffic tracking | Pending activation |
| Bootstrap 5 CDN | CSS/JS framework | Active |
| Google Fonts | Typography | Active |

## Patent Reference

- **Patent:** US 12,001,207 B2
- **Technology:** Dual-module safety system for autonomous vehicles/aircraft using visual navigation point recognition
- **Granted:** June 4, 2024 | **Expires:** March 5, 2041
- **Inventors:** Stephan Johannes Smit, Johannes Wilhelmus Maria VAN BENTUM
- **Full reference:** `docs/System/patent_reference.md`
- **Official document:** `docs/US12001207B2.html`
