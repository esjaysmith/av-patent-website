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
│   └── images/
│       └── backgrounds/    # Background images for OG image generation
│           ├── startup-innovation.jpg
│           ├── investment-finance.jpg
│           ├── technical-legal.jpg
│           └── general-info.jpg
├── build/                  # Generated static site (output)
├── .env.example            # Environment configuration template
├── .env                    # Local environment config (gitignored)
├── generate_site.py        # Static site generator script
├── generate_og_images.py   # Open Graph image generator
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

### 2. Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your environment-specific settings
# (domain, analytics ID, contact email, etc.)
```

### 3. Generate Social Images
```bash
# Generate Open Graph images for social sharing
python generate_og_images.py

# Or generate a single category
python generate_og_images.py --category general-info

# Preview without saving
python generate_og_images.py --preview
```

### 4. Generate Site
```bash
python generate_site.py
```

### 5. Preview Locally
```bash
# Open in browser
open build/index.html

# Or serve with Python
cd build && python -m http.server 8000
# Visit: http://localhost:8000
```

## Development Workflow

### Environment Configuration

The site uses environment-specific configuration via `.env` file:

```bash
# Environment
ENVIRONMENT=development

# Domain Configuration
SITE_DOMAIN=localhost
SITE_URL=http://localhost:8000

# Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
GOOGLE_ANALYTICS_ENABLED=false

# Contact
CONTACT_EMAIL=contact@example.com

# SEO
ROBOTS_INDEX=false
```

**Setup**:
1. Copy `.env.example` to `.env`
2. Update values for your environment (dev/staging/production)
3. `.env` is gitignored; `.env.example` provides template

### Adding New Content
1. Create new `.md` file in `content/` directory
2. Add YAML frontmatter with metadata
3. Write content in Markdown
4. Regenerate Open Graph images if needed: `python generate_og_images.py`
5. Run `python generate_site.py`
6. Preview in `build/` directory

### Content Frontmatter Format
```yaml
---
title: "Page Title"
description: "SEO meta description"
keywords: "SEO keywords, comma separated"
page_title: "Display title (optional)"
show_cta: true/false
is_homepage: true/false (homepage only)
og_category: "startup-innovation|investment-finance|technical-legal|general-info"
---
```

### Modifying Design
1. Edit templates in `templates/` directory
2. Add CSS to `templates/base.html` or `assets/` directory
3. Regenerate site with `python generate_site.py`

### Updating Social Sharing Images

**To regenerate all Open Graph images**:
```bash
python generate_og_images.py
```

**To update a single category**:
```bash
python generate_og_images.py --category general-info
```

**To replace a background image**:
1. Download new image (1200x630px minimum, CC0/Free license)
2. Save as `assets/images/backgrounds/[category].jpg`
3. Regenerate: `python generate_og_images.py --category [category]`
4. Commit background image to git

**Image Requirements**:
- Dimensions: 1200x630px minimum
- Format: JPG preferred
- License: CC0 or Free for commercial use
- Style: Clear space in bottom 40% for text overlay
- Sources: Unsplash, Pexels, Pixabay

## Deployment

### Local Testing
```bash
# Configure environment
cp .env.example .env
# Edit .env for local settings

# Generate Open Graph images
python generate_og_images.py

# Generate site
python generate_site.py

# Test locally
cd build && python -m http.server 8000
```

### Live Deployment

**Pre-deployment Checklist**:
1. Create production `.env` file with:
   - Production domain and URL
   - Google Analytics ID and enable tracking
   - Production contact email
   - Enable robots indexing (`ROBOTS_INDEX=true`)
2. Generate Open Graph images: `python generate_og_images.py`
3. Generate site: `python generate_site.py`
4. Test locally before deploying

**Deploy to Production**:
```bash
git add .
git commit -m "Update website content"
git push
```

**Environment-Specific Configuration**:
- `.env` is gitignored (create per environment)
- Background images ARE committed to git (for reproducibility)
- Generated OG images are gitignored (regenerate per deployment)
- Hosting service automatically builds and deploys on git push

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
- **Open Graph Images**: Category-based social sharing images (1200x630px)
- **Twitter Cards**: Optimized for social media sharing
- **Sitemap**: XML sitemap for search engines
- **Robots.txt**: Search crawler instructions
- **Semantic HTML**: Proper heading hierarchy
- **Internal Linking**: Cross-page navigation
- **Mobile Responsive**: Mobile-first design

### Social Sharing Images

The site uses a category-based system for Open Graph images:

**Categories**:
- **startup-innovation**: For AV startup and innovation pages
- **investment-finance**: For VC and investment-related pages
- **technical-legal**: For patent details and licensing pages
- **general-info**: Default for homepage, contact, and informational pages

**Image Generation Workflow**:
1. Background images are manually selected from CC0/free sources (Unsplash, Pexels)
2. Background images are committed to git for reproducibility
3. Python script generates Open Graph images with branded text overlay
4. Generated OG images are gitignored (derivatives that can be regenerated)

**Benefits**:
- High-quality, relevant imagery (manual selection)
- Clear licensing (CC0/Free sources)
- Consistent branding (automated text overlay)
- Easy maintenance (regenerate all images in seconds)
- No external dependencies (no AI services required)

## Technical Stack

- **Python 3.x**: Site generation
- **Markdown**: Content authoring
- **Jinja2**: HTML templating
- **Bootstrap 5**: CSS framework
- **PyYAML**: Frontmatter parsing
- **python-dotenv**: Environment configuration
- **Pillow**: Image processing for Open Graph images

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
1. Sign up for form service account (Formspree, Web3Forms, etc.)
2. Update form endpoint in `content/contact.md`
3. Configure email notifications
4. Test form submission

## Hosting Recommendations

### Option 1: Netlify (Recommended)
- **Cost**: Free tier available
- **Features**: Git-based deployment, auto-SSL, automatic builds
- **Deployment**: Git push (automatic)
- **Build Command**: `cd website && python generate_site.py`
- **Publish Directory**: `website/build`

### Option 2: Vercel
- **Cost**: Free tier available
- **Features**: Git-based deployment, edge network, automatic SSL
- **Deployment**: Git push (automatic)

### Option 3: AWS Amplify
- **Cost**: Pay-as-you-go (~$1-5/month)
- **Features**: Git-based deployment, global CDN, auto-SSL
- **Deployment**: Git push (automatic)

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