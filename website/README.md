# AV Navigation IP Protection Website

A static website for licensing US Patent 12,001,207 covering camera-based navigation safety technology for autonomous vehicles and drones.

## Project Structure

```
website/
├── content/                 # Markdown source files
│   ├── index.md            # Homepage
│   ├── patent-details.md   # Technical patent overview
│   ├── licensing.md        # Licensing opportunities
│   ├── industry-insights.md # Market trends & strategy
│   ├── contact.md          # Contact form
│   └── thank-you.md        # Form confirmation page
├── templates/              # Jinja2 HTML templates
│   ├── base.html          # Base template with navigation
│   └── page.html          # Content page template
├── assets/                 # Static assets (CSS, images, JS)
├── build/                  # Generated static site (output)
├── generate_site.py        # Static site generator script
├── deploy.sh              # Deployment script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Features

- **Static Site Generation**: Python-based generator using Markdown + Jinja2
- **SEO Optimized**: Meta tags, sitemap.xml, robots.txt
- **Mobile Responsive**: Bootstrap 5 framework
- **Professional Design**: Clean, business-focused layout
- **Contact Form**: Integrated with external form service
- **Phase 1 Complete**: Homepage + Patent Details (MVP)
- **Phase 2 Complete**: Full site with all core pages

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Site
```bash
python generate_site.py
```

### 3. Preview Locally
```bash
# Open in browser
open build/index.html

# Or serve with Python
cd build && python -m http.server 8000
# Visit: http://localhost:8000
```

## Development Workflow

### Adding New Content
1. Create new `.md` file in `content/` directory
2. Add YAML frontmatter with metadata
3. Write content in Markdown
4. Run `python generate_site.py`
5. Preview in `build/` directory

### Content Frontmatter Format
```yaml
---
title: "Page Title"
description: "SEO meta description"
keywords: "SEO keywords, comma separated"
page_title: "Display title (optional)"
show_cta: true/false
is_homepage: true/false (homepage only)
---
```

### Modifying Design
1. Edit templates in `templates/` directory
2. Add CSS to `templates/base.html` or `assets/` directory
3. Regenerate site with `python generate_site.py`

## Deployment

### Local Testing
```bash
# Generate site
python generate_site.py

# Test deployment script (dry run)
./deploy.sh staging
```

### Live Deployment
1. Configure hosting credentials in `deploy.sh`
2. Set up domain and hosting (SiteGround, Netlify, etc.)
3. Run deployment:
```bash
./deploy.sh production
```

## Site Pages

| Page | Purpose | SEO Keywords |
|------|---------|-------------|
| **Homepage** | Hero section, patent overview, CTA | autonomous vehicle patent licensing, US patent 12001207 |
| **Patent Details** | Technical specifications, claims | US patent 12001207 technical details, camera-based navigation |
| **Licensing** | Licensing options, process | patent licensing opportunities, exclusive licensing |
| **Industry Insights** | Market trends, timing | Tesla FSD patent protection, camera-first AV technology |
| **Contact** | Inquiry form, contact info | patent licensing contact, licensing consultation |
| **Thank You** | Form confirmation | licensing inquiry received |

## SEO Features

- **Meta Tags**: Title, description, keywords for each page
- **Sitemap**: XML sitemap for search engines
- **Robots.txt**: Search crawler instructions
- **Semantic HTML**: Proper heading hierarchy
- **Internal Linking**: Cross-page navigation
- **Mobile Responsive**: Mobile-first design

## Technical Stack

- **Python 3.x**: Site generation
- **Markdown**: Content authoring
- **Jinja2**: HTML templating
- **Bootstrap 5**: CSS framework
- **PyYAML**: Frontmatter parsing

## Content Strategy

### Target Keywords
- Primary: "autonomous vehicle patent licensing", "US patent 12001207"
- Secondary: "camera-based navigation safety", "AV IP protection"
- Long-tail: "Tesla FSD patent protection", "drone navigation patents"

### Content Themes
1. **IP Protection**: Defensive strategies, portfolio building
2. **Market Timing**: Tesla FSD impact, industry trends
3. **Technology Value**: Camera-first architectures, safety applications
4. **Business Benefits**: Valuation, funding, competitive advantage

## Form Integration

### Current Setup
- Form service: Formspree (placeholder)
- Action URL: `https://formspree.io/f/YOUR_FORM_ID`
- Thank you page: `/thank-you.html`

### Configuration Steps
1. Sign up for Formspree account
2. Replace `YOUR_FORM_ID` in `contact.md`
3. Configure email notifications
4. Test form submission

## Hosting Recommendations

### Option 1: SiteGround (PRD Recommendation)
- **Cost**: ~$10/month
- **Features**: SSL, fast loading, WordPress compatible
- **Deployment**: rsync or FTP

### Option 2: Netlify (Alternative)
- **Cost**: Free tier available
- **Features**: Git-based deployment, auto-SSL
- **Deployment**: Git push or drag-and-drop

### Option 3: AWS S3 + CloudFront
- **Cost**: ~$5/month
- **Features**: High performance, global CDN
- **Deployment**: AWS CLI or sync

## Performance Targets

- **Page Load Time**: <2 seconds (PRD requirement)
- **Mobile Performance**: Lighthouse score >90
- **SEO Score**: Lighthouse score >90
- **Accessibility**: WCAG 2.1 compliance

## Maintenance

### Regular Tasks
- **Content Updates**: Add industry trend pages monthly
- **SEO Monitoring**: Track keyword rankings, traffic
- **Technical Updates**: Security patches, dependency updates
- **Performance Monitoring**: Page speed, uptime checks

### Monitoring Setup
- Google Analytics: Traffic tracking
- Google Search Console: SEO monitoring
- Uptime monitoring: Status checks

## Future Enhancements (Phase 3+)

### Content Expansion
- Industry-specific landing pages
- Tesla FSD trend analysis
- Case studies and success stories
- Blog section for SEO content

### Technical Improvements
- Image optimization and lazy loading
- Advanced SEO schema markup
- A/B testing for conversion optimization
- Integration with CRM for lead tracking

## Legal Compliance

- **Disclaimer**: Present on all pages
- **Privacy Policy**: Contact form data handling
- **Terms**: Licensing inquiry terms
- **GDPR**: European visitor compliance (if applicable)

## Support

For technical issues or enhancement requests:
1. Check existing documentation
2. Review generated HTML for debugging
3. Test changes in local environment first
4. Create backups before major updates

---

**Status**: Phase 1 & 2 Complete - Ready for deployment and SEO analysis