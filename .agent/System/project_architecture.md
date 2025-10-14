# Project Architecture

## Project Overview

**Project Name:** AV Navigation IP Protection Website
**Purpose:** Static website for monetizing US Patent 12,001,207 B2 through licensing opportunities
**Target Audience:** Companies in autonomous vehicles, drones, and AI navigation; inventors building IP portfolios
**Goal:** Generate licensing leads via organic SEO traffic and educate visitors on patent's role in IP portfolio expansion

**Core Patent:** US Patent 12,001,207 B2
- **Technology:** Dual-module safety system for autonomous vehicles and aircraft using visual navigation point recognition
- **Status:** Active (granted June 4, 2024, expires March 5, 2041)
- **Full Technical Reference:** See [`patent_reference.md`](./patent_reference.md) for complete details

## Project Structure

```
op_patent/
├── .agent/                    # Documentation folder
│   ├── Tasks/                # PRD and implementation plans
│   ├── System/               # Architecture and system state docs
│   │   ├── project_architecture.md   # This file
│   │   └── patent_reference.md       # US Patent 12,001,207 B2 reference
│   ├── SOP/                  # Standard operating procedures
│   ├── US12001207B2.html     # Full patent document (official source)
│   └── README.md             # Documentation index
├── .claude/                   # Claude Code configuration
│   └── settings.local.json   # Local settings
├── docs/                      # Analysis and PRD documents
│   ├── site_analysis_001.md  # Website testing and analysis
│   └── website_prd_001.md    # Product Requirements Document
├── website/                   # Main website application
│   ├── content/              # Markdown content files
│   │   ├── index.md         # Homepage
│   │   ├── patent-details.md
│   │   ├── licensing.md
│   │   ├── industry-insights.md
│   │   ├── contact.md
│   │   └── thank-you.md
│   ├── designs/              # Design templates
│   │   └── default/         # Default design theme
│   │       ├── base.html    # Base template with nav/footer
│   │       └── page.html    # Content page template
│   ├── assets/               # Static assets (CSS, images, JS)
│   ├── build/                # Generated static site (output)
│   ├── generate_site.py      # Static site generator script
│   ├── deploy.sh            # Deployment script
│   ├── test_website.py      # Comprehensive test suite
│   ├── requirements.txt     # Python dependencies
│   └── README.md            # Website documentation
├── .gitignore                # Git ignore rules
├── .mcp.json                 # MCP server configuration
├── opencode.json             # OpenCode configuration
└── CLAUDE.md                 # Project instructions for Claude
```

## Technology Stack

### Core Technologies
- **Python 3.x**: Static site generation and scripting
- **Markdown**: Content authoring format
- **Jinja2 3.1.2**: HTML templating engine
- **YAML**: Frontmatter metadata parsing
- **Bootstrap 5**: CSS framework for responsive design

### Development Dependencies
```
markdown==3.5.1       # Markdown to HTML conversion
jinja2==3.1.2         # Template rendering
beautifulsoup4==4.12.2  # HTML parsing (for testing)
```

### Frontend Stack
- **HTML5**: Semantic markup
- **CSS3**: Styling via Bootstrap 5 CDN
- **JavaScript**: Bootstrap components (minimal JS)
- **Bootstrap 5**: Responsive framework (via CDN)

### Development Tools
- **Git**: Version control
- **Python HTTP Server**: Local development preview
- **rsync**: Deployment to hosting

## Architecture Design

### Static Site Generation Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Content Creation                          │
│  (Markdown files with YAML frontmatter in /content/)        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────────┐
│              Static Site Generator                           │
│              (generate_site.py)                             │
│                                                              │
│  1. Parse frontmatter (YAML) from markdown                  │
│  2. Convert markdown to HTML                                │
│  3. Load Jinja2 templates from /designs/{theme}/            │
│  4. Render HTML with template + content                     │
│  5. Generate sitemap.xml and robots.txt                     │
│  6. Copy assets to build directory                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────────┐
│                  Build Output                                │
│           (Static HTML files in /build/)                     │
│                                                              │
│  - index.html, patent-details.html, etc.                    │
│  - sitemap.xml, robots.txt                                  │
│  - assets/ (copied from source)                             │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────────┐
│               Deployment (rsync)                             │
│        (Upload to hosting provider)                          │
└─────────────────────────────────────────────────────────────┘
```

### Design System Architecture

The project uses a **design theme system** allowing multiple visual designs:

```
designs/
└── default/
    ├── base.html      # Base template (header, nav, footer)
    └── page.html      # Page template (extends base)
```

**Template Inheritance:**
- `base.html`: Defines overall page structure, navigation, footer
- `page.html`: Extends base, fills in page-specific content blocks
- Templates use Jinja2 template variables for dynamic content

### Content Architecture

**Frontmatter Structure** (YAML):
```yaml
---
title: "SEO-optimized page title"
description: "Meta description for search engines"
keywords: "keyword1, keyword2, keyword3"
page_title: "Display title on page"
show_cta: true/false
is_homepage: true/false
hero_title: "Hero section title (homepage)"
hero_subtitle: "Hero section subtitle (homepage)"
---
```

**Content Flow:**
1. Author content in Markdown with frontmatter
2. Generator parses frontmatter for metadata
3. Converts Markdown body to HTML
4. Injects content + metadata into templates
5. Outputs complete HTML pages

## Core Components

### 1. Static Site Generator (`generate_site.py`)

**Class:** `StaticSiteGenerator`

**Key Methods:**
- `__init__(design="default")`: Initialize with design theme
- `clean_build_dir()`: Remove/recreate build directory
- `copy_assets()`: Copy assets to build
- `parse_frontmatter(content)`: Extract YAML frontmatter
- `process_markdown_file(md_file_path)`: Convert MD to HTML
- `generate_page(md_file_path)`: Generate single HTML page
- `generate_sitemap(pages)`: Create sitemap.xml
- `generate_robots_txt()`: Create robots.txt
- `build_site()`: Main build orchestration

**Configuration:**
- Supports multiple design themes via `--design` flag
- Configurable paths for content, templates, build output
- Extensible for future features (subdirectories, image optimization)

### 2. Content Management

**Content Files** (`/content/*.md`):
- **index.md**: Homepage with hero section
- **patent-details.md**: Technical patent overview
- **licensing.md**: Licensing opportunities and process
- **industry-insights.md**: Market trends and timing
- **contact.md**: Contact form with Formspree integration
- **thank-you.md**: Form submission confirmation

**Content Guidelines:**
- 800-1,800 words per page
- SEO-optimized with target keywords
- YAML frontmatter for all metadata
- Markdown formatting for structure

### 3. Template System

**Base Template** (`base.html`):
- Responsive Bootstrap 5 layout
- Navigation menu with all core pages
- Professional footer with disclaimer
- Meta tags for SEO
- Mobile-first design

**Page Template** (`page.html`):
- Extends base template
- Conditional hero section (homepage)
- Content area with proper hierarchy
- Call-to-action sections
- Page-specific styling

### 4. Testing Framework (`test_website.py`)

**Test Coverage:**
- File existence validation
- Page loading and title verification
- Navigation link functionality
- SEO element validation (meta tags)
- Responsive design checks
- Contact form structure
- Accessibility basics
- Performance metrics

**Results:** 46/46 tests passing (100% success rate)

## Integration Points

### External Services

1. **Formspree** (Contact Form)
   - Service: Form submission handling
   - Integration: HTML form action URL
   - Configuration: Requires Formspree account setup
   - Status: Placeholder in code, requires configuration

2. **Bootstrap CDN**
   - Service: CSS/JS framework delivery
   - Integration: CDN links in base.html
   - Version: Bootstrap 5
   - Status: Production-ready

3. **Hosting Provider** (Future)
   - Recommended: SiteGround or Netlify
   - Deployment: rsync or Git-based
   - SSL: HTTPS required
   - Status: Not yet configured

4. **Google Analytics** (Future)
   - Purpose: Traffic tracking
   - Integration: Tracking code in base.html
   - Status: Not yet implemented

5. **Google Search Console** (Future)
   - Purpose: SEO monitoring
   - Integration: Sitemap submission
   - Status: Ready (sitemap.xml generated)

## Deployment Architecture

### Build Process
```bash
# 1. Generate static site
python generate_site.py [--design theme_name]

# 2. Preview locally
cd build && python -m http.server 8000

# 3. Deploy to hosting
./deploy.sh production  # (requires configuration)
# OR
rsync -avz build/ user@host:/path/to/site
```

### Deployment Requirements
- Python 3.x environment
- Write access to hosting server
- Domain configuration (DNS)
- SSL certificate setup
- Formspree account for contact form

## Performance Characteristics

### Load Time Targets
- Static HTML: <100ms server response
- Bootstrap CDN: <200ms (cached)
- Total load time: <500ms (PRD requirement: <2s)

### Optimization Features
- Static HTML (no server processing)
- CDN-hosted CSS/JS frameworks
- Minimal JavaScript
- Clean, semantic HTML
- Mobile-responsive design

## Security Considerations

### Current Security Measures
- Static site (no dynamic vulnerabilities)
- No user data storage
- External form service (Formspree)
- HTTPS-ready structure

### Security Requirements
- HTTPS enabled on hosting
- Secure form submission endpoint
- Privacy policy for contact form
- GDPR compliance ready

## Scalability and Extensibility

### Current Limitations
- Single directory for content (no subdirectories)
- No image optimization
- Manual build process
- Single design theme in use

### Future Expansion Capabilities
- Phase 3: Additional landing pages (trend-based)
- Multi-theme support (already architected)
- Subdirectory content organization
- Image processing pipeline
- Automated build/deploy
- Analytics integration

## Development Workflow

### Adding New Content
1. Create `.md` file in `/content/`
2. Add YAML frontmatter with metadata
3. Write content in Markdown
4. Run `python generate_site.py`
5. Preview in `/build/` directory
6. Deploy with rsync or deploy script

### Modifying Design
1. Edit templates in `/designs/default/`
2. Update base.html or page.html
3. Regenerate site
4. Test across devices
5. Deploy changes

### Testing Changes
1. Run test suite: `python test_website.py`
2. Manual browser testing
3. Mobile responsiveness check
4. SEO validation
5. Link verification

## Related Documentation

### Core Documentation
- **Patent Reference**: [`patent_reference.md`](./patent_reference.md) - Complete US Patent 12,001,207 B2 technical reference
- **Patent Document**: `.agent/US12001207B2.html` - Official patent HTML (3,689 lines)
- **PRD**: `/docs/website_prd_001.md` - Complete product requirements
- **Site Analysis**: `/docs/site_analysis_001.md` - Testing and SEO analysis

### Additional Resources
- **Website README**: `/website/README.md` - Detailed usage guide
- **Project Instructions**: `/CLAUDE.md` - Claude Code instructions
- **Documentation Index**: `.agent/README.md` - Complete documentation map
