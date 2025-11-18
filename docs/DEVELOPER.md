# Developer README

## Project Overview

This is a Python-based static website for licensing **US Patent 12,001,207 B2**, which covers camera-based navigation safety technology for autonomous vehicles and drones. The website is built using a custom static site generator that converts Markdown content to HTML using Jinja2 templates.

**Key Point**: This is a **pure Python project** - no Node.js, npm, webpack, or JavaScript build tools required.

## Quick Start

```bash
# 1. Install dependencies
cd website
pip install -r requirements.txt

# 2. Set up environment configuration
cp .env.example .env
# Edit .env if needed (defaults are fine for local development)

# 3. Build and serve the site (one-liner)
rm -rf build && python generate_site.py && python -m http.server -d build 8000

# 4. Open in browser
# Visit http://localhost:8000
```

## Technology Stack

- **Python 3.x** - Static site generation engine
- **Markdown 3.5.1** - Content authoring format
- **Jinja2 3.1.2** - HTML templating engine
- **Bootstrap 5** - CSS framework (via CDN)
- **YAML** - Frontmatter metadata parsing
- **BeautifulSoup4 4.12.2** - HTML parsing for testing

## Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)
- Basic knowledge of Markdown and YAML

## Installation

1. **Clone the repository** (if not already done)

2. **Navigate to the website directory**:
   ```bash
   cd website
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - markdown==3.5.1
   - Jinja2==3.1.2
   - PyYAML==6.0.1
   - beautifulsoup4==4.12.2
   - playwright==1.40.0

## Project Structure

```
op_patent/
├── docs/                    # ⭐ COMPLETE PROJECT DOCUMENTATION (START HERE!)
│   ├── README.md              # Documentation index - read this first
│   ├── plans/                 # Product requirements and implementation plans
│   ├── System/                # Architecture docs, patent reference
│   └── SOP/                   # Standard operating procedures
│
├── website/                   # Main application
│   ├── content/              # 📝 Markdown source files (.md)
│   ├── designs/default/      # 🎨 Jinja2 templates (base.html, page.html)
│   ├── assets/               # 🖼️ Static assets (CSS, images, JS)
│   ├── build/                # 🏗️ Generated static site (output directory)
│   ├── generate_site.py      # 🔧 Site generator (main script)
│   ├── test_website.py       # 🧪 Test suite
│   └── requirements.txt     # 📦 Python dependencies
│
├── docs/                     # Developer documentation
│   └── DEVELOPER.md         # This file
│
└── CLAUDE.md                # Agent instructions
```

## Development Workflow

### Adding New Content Pages

1. **Create a new Markdown file** in `/website/content/`:
   ```bash
   cd website/content
   touch my-new-page.md
   ```

2. **Add YAML frontmatter** at the top of the file:
   ```yaml
   ---
   title: "Page Title for SEO"
   description: "Meta description for search engines"
   keywords: "keyword1, keyword2, keyword3"
   page_title: "Display Title (optional, uses 'title' if omitted)"
   show_cta: true
   ---
   ```

3. **Write your content** in Markdown below the frontmatter:
   ```markdown
   ## Section Heading

   Your content here with **bold**, *italic*, and [links](https://example.com).

   - Bullet points
   - Work great too
   ```

4. **⚠️ MANDATORY: Follow the fact-checking protocol**
   - See `docs/SOP/content_quality_assurance.md`
   - All patent claims must be verified against the source document
   - Technical specifications must be accurate

5. **Generate the site**:
   ```bash
   cd website
   python generate_site.py
   ```

6. **Test locally** (see "Running the Development Server" below)

7. **Update documentation** in `docs/` folder if you added new features

### Editing Existing Content

1. **Locate the Markdown file** in `/website/content/`
2. **Edit the content** - modify frontmatter or Markdown as needed
3. **Regenerate the site**:
   ```bash
   cd website
   python generate_site.py
   ```
4. **Test your changes** locally before deploying

### Content Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | SEO title (appears in `<title>` tag) |
| `description` | Yes | Meta description for search engines |
| `keywords` | Yes | Comma-separated SEO keywords |
| `page_title` | No | H1 heading (defaults to `title` if omitted) |
| `show_cta` | No | Show call-to-action button (true/false) |
| `is_homepage` | No | Set to `true` for index.md only |

## Environment Configuration

The site generator uses environment variables from a `.env` file to configure URLs, indexing, and other settings.

### Setting Up Your `.env` File

1. **Copy the example file:**
   ```bash
   cd website
   cp .env.example .env
   ```

2. **Edit for your environment:**
   ```bash
   # Development (default)
   ENVIRONMENT=development
   SITE_URL=http://localhost:8000
   ROBOTS_INDEX=false  # Blocks search engines

   # Staging
   ENVIRONMENT=staging
   SITE_URL=https://staging.av-navigation-ip.com
   ROBOTS_INDEX=false  # Still blocks search engines

   # Production
   ENVIRONMENT=production
   SITE_URL=https://av-navigation-ip.com
   ROBOTS_INDEX=true   # Allows search engine indexing
   ```

### Environment Variables Explained

| Variable | Description | Example Values |
|----------|-------------|----------------|
| `ENVIRONMENT` | Current environment | `development`, `staging`, `production` |
| `SITE_URL` | Full base URL of your site | `http://localhost:8000`, `https://av-navigation-ip.com` |
| `ROBOTS_INDEX` | Allow search engine indexing | `false` (dev/staging), `true` (production) |
| `GOOGLE_ANALYTICS_ID` | GA4 Measurement ID (renders in all pages) | `G-XXXXXXXXXX` (placeholder), `G-ABC123DEF4` (real) |
| `CONTACT_EMAIL` | Contact email address | `licensing@av-navigation-ip.com` |

### How Environment Variables Affect Generation

The `.env` configuration impacts:

**Open Graph & Twitter Card URLs:**
- `og:url` - Uses `SITE_URL` as base
- `og:image` - Converts hardcoded URLs to use `SITE_URL`
- `twitter:image` - Converts hardcoded URLs to use `SITE_URL`

**Sitemap.xml:**
- All `<loc>` URLs use `SITE_URL` as base

**robots.txt:**
- `ROBOTS_INDEX=false` → `Disallow: /` (blocks search engines)
- `ROBOTS_INDEX=true` → `Allow: /` (allows indexing)
- Sitemap URL uses `SITE_URL`

**Google Analytics:**
- `GOOGLE_ANALYTICS_ID` - Renders in all pages' `<head>` section
- Uses placeholder `G-XXXXXXXXXX` by default (dev/staging)
- Set to your real GA4 Measurement ID for production tracking

**Example Output:**

Development (localhost:8000):
```html
<meta property="og:url" content="http://localhost:8000/" />
<meta property="og:image" content="http://localhost:8000/assets/images/og-general-info.jpg" />
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

Production (av-navigation-ip.com):
```html
<meta property="og:url" content="https://av-navigation-ip.com/" />
<meta property="og:image" content="https://av-navigation-ip.com/assets/images/og-general-info.jpg" />
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123DEF4"></script>
```

### Testing with Different Environments

```bash
# Test with development settings
python generate_site.py
# Output: Uses http://localhost:8000, blocks robots

# Test with production settings (temporarily)
# 1. Edit .env and change:
#    SITE_URL=https://av-navigation-ip.com
#    ROBOTS_INDEX=true
#    GOOGLE_ANALYTICS_ID=G-YOUR-REAL-ID
# 2. Regenerate:
python generate_site.py
# Output: Uses https://av-navigation-ip.com, allows robots, uses real GA ID

# 3. Don't forget to change .env back to development settings!
```

### Setting Up Google Analytics for Production

When deploying to production, you'll need to set up a real Google Analytics 4 (GA4) property:

1. **Create a GA4 Property:**
   - Visit [Google Analytics](https://analytics.google.com/)
   - Click "Admin" (gear icon in bottom left)
   - Create a new GA4 property for your website
   - Set up a "Web" data stream

2. **Get Your Measurement ID:**
   - In the data stream details, find your **Measurement ID**
   - Format: `G-XXXXXXXXXX` (e.g., `G-ABC123DEF4`)
   - Copy this ID

3. **Update Your `.env` File:**
   ```bash
   # Edit website/.env
   GOOGLE_ANALYTICS_ID=G-ABC123DEF4  # Replace with your actual ID
   ```

4. **Regenerate and Deploy:**
   ```bash
   cd website
   python generate_site.py
   # Deploy to production
   ```

5. **Verify Tracking:**
   - Visit your production site
   - Check Google Analytics "Realtime" view
   - You should see your visit appear within seconds

**Important Notes:**
- The placeholder `G-XXXXXXXXXX` will not track any data
- GA tracking only works on publicly accessible domains (not `localhost` or `file://`)
- Keep your development `.env` using the placeholder to avoid polluting production analytics

## Build Process

### Generate the Website

The `generate_site.py` script converts Markdown files to HTML:

```bash
cd website
python generate_site.py
```

**What happens during generation:**
1. Loads environment variables from `.env` file
2. Displays current environment configuration (URL, indexing policy)
3. Reads all `.md` files from `content/` directory
4. Parses YAML frontmatter for metadata
5. Converts Markdown to HTML using Python's markdown library
6. Renders content through Jinja2 templates in `designs/default/`
7. **Normalizes all URLs** to use `SITE_URL` from `.env`
8. Generates static HTML files in `build/` directory
9. Creates `sitemap.xml` (with environment-based URLs)
10. Creates `robots.txt` (with environment-based indexing policy)
11. Copies assets to `build/assets/`

### Use Alternative Design Theme

If you have multiple design themes:

```bash
python generate_site.py --design theme-name
```

Current theme: `default`

## Running the Development Server

### Quick One-Liner (Recommended)

Build and serve the site in one command:

```bash
cd website && rm -rf build && python generate_site.py && python -m http.server -d build 8000
```

Then visit: **http://localhost:8000**

**What this does:**
- Navigates to website directory
- Removes old build artifacts
- Generates fresh site from content
- Starts HTTP server serving the build directory

### Method 1: Python Built-in HTTP Server (Manual Steps)

```bash
cd website/build
python -m http.server 8000
```

Then visit: **http://localhost:8000**

**Why this method?**
- No additional dependencies
- Serves all static files correctly
- Mimics production environment
- Allows testing relative URLs

### Method 2: Direct File Access

```bash
# macOS
open website/build/index.html

# Linux
xdg-open website/build/index.html

# Windows
start website/build/index.html
```

**Limitation**: Some features (like relative links) may not work correctly with `file://` protocol.

## Testing

Run the comprehensive test suite:

```bash
cd website
python test_website.py
```

**The test suite validates:**
- ✅ All expected HTML files exist in `build/`
- ✅ HTML structure is valid
- ✅ SEO meta tags are present and correct
- ✅ Navigation links work properly
- ✅ Contact form elements exist
- ✅ `sitemap.xml` is generated
- ✅ `robots.txt` is configured correctly

**Expected output**: All tests should pass (46/46 tests passing as of last run)

## Deployment

### Git-Based Deployment

The site uses git push for deployment. Simply commit your changes and push to deploy:

1. **Generate the site**:
   ```bash
   python generate_site.py
   ```

2. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update website content"
   git push
   ```

The hosting service will automatically build and deploy the site from the repository.

## Important Documentation

### Must-Read Documentation in `docs/` Folder

**⭐ Start here**: `docs/README.md` - Complete documentation index

**System Documentation:**
- `docs/System/project_architecture.md` - Full technical architecture
- `docs/System/patent_reference.md` - US Patent 12,001,207 B2 details
- `docs/System/technology_stack.md` - Detailed tech stack information

**Standard Operating Procedures (SOPs):**
- `docs/SOP/content_management.md` - How to create and edit content
- `docs/SOP/site_generation_deployment.md` - Build and deploy procedures
- `docs/SOP/content_quality_assurance.md` - **MANDATORY fact-checking protocol**
- `docs/SOP/template_editing.md` - How to modify Jinja2 templates

**Task Documentation:**
- `docs/plans/` - Product requirements and implementation plans for features

### Why `docs/` Documentation Matters

Per `CLAUDE.md` project instructions:
> We maintain all essential documents in the `docs` folder, ensuring they are regularly updated... Before planning any implementation, always review the `docs/README.md` first to gain proper context.

The `docs/` documentation ensures:
- ✅ Consistent development practices
- ✅ Accurate patent information
- ✅ Quality content standards
- ✅ Proper architecture understanding

## Content Guidelines

### ⚠️ CRITICAL: Fact-Checking Protocol

**ALL content must follow the comprehensive fact-checking protocol** documented in:
`docs/SOP/content_quality_assurance.md`

Key requirements:
1. **Patent claims** must be verified against `/US12001207B2.html`
2. **Technical specifications** must be accurate
3. **Market data** must be cited and current
4. **Legal language** must be precise

### Content Best Practices

- ✅ Use clear, professional language
- ✅ Focus on the patent's unique value proposition
- ✅ Avoid marketing hyperbole
- ✅ Cite sources for statistics and claims
- ✅ Keep technical accuracy paramount
- ✅ Maintain consistent terminology

## Common Tasks

### Add a New Page to Navigation

1. Create the `.md` file in `website/content/`
2. Generate the site
3. Edit `website/designs/default/base.html` to add the nav link
4. Regenerate and test

### Modify Page Templates

1. Edit templates in `website/designs/default/`:
   - `base.html` - Site-wide layout, nav, footer
   - `page.html` - Individual page content wrapper
2. Regenerate the site
3. Test thoroughly

### Update Styling

1. Edit `website/assets/css/styles.css`
2. Regenerate the site (copies assets to `build/`)
3. Clear browser cache when testing

### Add Static Assets

1. Place files in `website/assets/` (images/, js/, css/)
2. Reference in templates or Markdown: `/assets/images/photo.jpg`
3. Regenerate the site (copies assets automatically)

### Maintain Background Images for Social Sharing

The website uses background images to generate Open Graph (OG) social sharing images that appear when pages are shared on social media platforms like LinkedIn, Twitter, and Facebook.

**Location**: `website/assets/images/backgrounds/`

**What are these images?**
- These are high-quality JPG images used as backgrounds for generating OG social sharing preview images
- They are NOT displayed on the website itself (the site uses CSS gradients for visual backgrounds)
- They are processed by `generate_og_images.py` to create composite images with text overlays

**Four categories of background images:**

1. **`startup-innovation.jpg`** - Used for Series A, Tesla FSD, and Autonomous Trucking pages
2. **`investment-finance.jpg`** - Used for VC Due Diligence and Drone Delivery pages
3. **`technical-legal.jpg`** - Used for Patent Details and Licensing pages
4. **`general-info.jpg`** - Default for Homepage, Industry Insights, Contact, About, and other pages

**How to replace or update background images:**

1. **Image Requirements:**
   - Dimensions: 1200x630 pixels minimum (larger is fine, will be center-cropped)
   - Format: JPG (better compression than PNG)
   - License: CC0 or free for commercial use
   - Quality: High resolution, professional photography
   - Style: Clean, modern, with clear space in bottom 40% for text overlay

2. **Finding new images:**
   ```bash
   # Use these free image sources:
   # - Unsplash: https://unsplash.com/
   # - Pexels: https://www.pexels.com/
   # - Pixabay: https://pixabay.com/

   # See website/assets/images/backgrounds/README.md for:
   # - Specific search queries for each category
   # - Selection criteria
   # - License verification steps
   ```

3. **Replace a background image:**
   ```bash
   # Download new image and save with exact filename
   # Example: Replace the startup/innovation background
   cd website/assets/images/backgrounds/
   # Save new image as startup-innovation.jpg (overwrites old one)
   ```

4. **Regenerate OG images:**
   ```bash
   cd website

   # Preview changes before saving (recommended)
   python generate_og_images.py --preview --category startup-innovation

   # Generate single category
   python generate_og_images.py --category startup-innovation

   # Or regenerate all 4 categories at once
   python generate_og_images.py
   ```

5. **Verify the output:**
   ```bash
   # Check that OG images were created in assets/images/
   ls -lh website/assets/images/og-*.jpg

   # Expected output:
   # - og-startup-innovation.jpg
   # - og-investment-finance.jpg
   # - og-technical-legal.jpg
   # - og-general-info.jpg
   ```

6. **Regenerate the site and test:**
   ```bash
   python generate_site.py

   # Test locally to verify OG meta tags reference the new images
   # View page source and check for: <meta property="og:image" content="...">
   ```

**Important notes:**
- Background source images (`backgrounds/*.jpg`) are committed to git for reproducibility
- Generated OG images (`og-*.jpg`) are also committed since they're used in production
- All images must be present before running the generator script
- See `website/assets/images/backgrounds/README.md` for detailed guidance on image selection

### Testing Social Sharing Images

After generating or updating OG images, you can test how they'll appear when shared on social media:

#### Method 1: Facebook Sharing Debugger (Recommended)

The easiest way to preview your social sharing images:

1. **Visit the Facebook Sharing Debugger:**
   ```
   https://developers.facebook.com/tools/debug/
   ```

2. **Test with local or production URLs:**
   ```bash
   # Option A: Test production URL (after deployment)
   https://av-navigation-ip.com/series-a-av-patent-portfolio-strategy.html

   # Option B: Test staging URL (if you have staging environment)
   https://staging.av-navigation-ip.com/series-a-av-patent-portfolio-strategy.html
   ```

3. **Enter the URL** in the debugger and click "Debug"

4. **Review the preview:**
   - Image displays correctly (1200x630px)
   - Title shows your page title
   - Description shows your meta description
   - Any warnings or errors are displayed

5. **Click "Scrape Again"** if you've updated the image and want to clear Facebook's cache

**Note:** Facebook Debugger works with LinkedIn previews too, as LinkedIn uses Open Graph tags.

#### Method 2: Twitter Card Validator

For Twitter-specific previews:

1. **Visit the Twitter Card Validator:**
   ```
   https://cards-dev.twitter.com/validator
   ```

2. **Enter your page URL** (production or staging)

3. **Review the card preview** - shows how your page will appear in tweets

#### Method 3: Local Testing with ngrok (For Development)

If you want to test before deploying to production:

1. **Install ngrok** (if not already installed):
   ```bash
   # macOS with Homebrew
   brew install ngrok

   # Or download from: https://ngrok.com/download
   ```

2. **Start your local server:**
   ```bash
   cd website/build
   python -m http.server 8000
   ```

3. **In a new terminal, create a public tunnel:**
   ```bash
   ngrok http 8000
   ```

4. **Copy the HTTPS URL** from ngrok output (e.g., `https://abc123.ngrok.io`)

5. **Use this URL in Facebook Debugger or Twitter Validator:**
   ```
   https://abc123.ngrok.io/series-a-av-patent-portfolio-strategy.html
   ```

6. **Review the social preview** with your local changes

**Important:** ngrok URLs are temporary and change each time you restart ngrok.

#### Method 4: Manual HTML Inspection (Quick Check)

For a quick verification without external tools:

1. **Open a generated HTML file:**
   ```bash
   open website/build/series-a-av-patent-portfolio-strategy.html
   # Or: open website/build/index.html
   ```

2. **View page source** (Right-click → "View Page Source" or Cmd+Option+U / Ctrl+U)

3. **Search for Open Graph tags:**
   ```html
   <!-- Look for these meta tags: -->
   <meta property="og:image" content="https://av-navigation-ip.com/assets/images/og-startup-innovation.jpg" />
   <meta property="og:title" content="..." />
   <meta property="og:description" content="..." />
   ```

4. **Verify the image URL is correct** and points to the right category image

5. **Test the image URL directly** by pasting it into your browser:
   ```
   https://av-navigation-ip.com/assets/images/og-startup-innovation.jpg
   ```
   (Use `http://localhost:8000/assets/images/og-startup-innovation.jpg` for local testing)

#### Method 5: Browser Extension (LinkedIn Post Inspector)

For quick LinkedIn previews:

1. **Install the "LinkedIn Post Inspector" Chrome extension**

2. **Navigate to your page** (local or deployed)

3. **Click the extension icon** to see how the page will appear when shared on LinkedIn

#### Validation Checklist

When testing, verify:

- ✅ Image displays correctly (not broken, proper dimensions)
- ✅ Image is relevant to the page content
- ✅ Title is compelling and accurate (50-60 characters ideal)
- ✅ Description is clear and enticing (120-160 characters)
- ✅ No errors or warnings in debugger tools
- ✅ Image loads quickly (file size under 300KB)

#### Common Issues and Solutions

**Issue: "Image could not be downloaded"**
- **Cause:** Image path is incorrect or server isn't serving the image
- **Solution:** Check that the image exists in `build/assets/images/` and the URL is correct

**Issue: "Image too small"**
- **Cause:** OG image is smaller than 1200x630px
- **Solution:** Regenerate images using `python generate_og_images.py`

**Issue: "Old image still showing"**
- **Cause:** Facebook/LinkedIn has cached the old image
- **Solution:** Use Facebook Debugger and click "Scrape Again" to clear cache

**Issue: "Image shows but with wrong content"**
- **Cause:** Wrong category image assigned to the page
- **Solution:** Check frontmatter `og_image` field points to correct category image

## Troubleshooting

### Site Not Generating

**Problem**: `python generate_site.py` fails

**Solutions**:
- Check that you're in the `website/` directory
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check for syntax errors in Markdown files (malformed YAML frontmatter)

### Changes Not Appearing

**Problem**: Edited content doesn't show up in browser

**Solutions**:
1. Regenerate the site: `python generate_site.py`
2. Hard refresh browser: Ctrl+F5 (Windows/Linux) or Cmd+Shift+R (macOS)
3. Restart the development server
4. Clear browser cache

### Test Failures

**Problem**: `python test_website.py` shows failures

**Solutions**:
- Ensure site was generated: `python generate_site.py`
- Check that all required `.md` files exist in `content/`
- Verify frontmatter fields are complete
- Review error messages for specific issues

### Development Server Not Accessible

**Problem**: Can't access http://localhost:8000

**Solutions**:
- Verify you're in the `build/` directory when running the server
- Check that port 8000 isn't already in use
- Try a different port: `python -m http.server 3000`
- Check firewall settings

### Broken Links

**Problem**: Navigation links return 404

**Solutions**:
- Ensure corresponding `.md` files exist in `content/`
- Regenerate the site
- Check that filenames match exactly (case-sensitive)
- Use relative URLs: `/page.html` not `https://domain.com/page.html`

## Development Tips

### Efficient Workflow

1. **Keep the development server running** - just regenerate when you make changes
2. **Use a second terminal** - one for the server, one for generating
3. **Test frequently** - run `python test_website.py` before committing
4. **Reference existing pages** - look at current `.md` files for examples
5. **Check documentation first** - `docs/README.md` has answers

### File Watching (Optional)

For automatic regeneration when files change, you can use tools like:

```bash
# Install watchdog
pip install watchdog

# Watch for changes (example using watchmedo)
watchmedo shell-command \
  --patterns="*.md;*.html;*.css" \
  --recursive \
  --command='python generate_site.py' \
  website/
```

### IDE Setup

Recommended for development:
- **VS Code** with extensions:
  - Markdown Preview Enhanced
  - Jinja (for template syntax highlighting)
  - Python
- **PyCharm** (has built-in support for Jinja2 and Markdown)

## Next Steps

1. **Read `docs/README.md`** - Get complete context
2. **Review existing content** - Look at `website/content/*.md` files
3. **Run the test suite** - Ensure everything works
4. **Make a small change** - Practice the workflow
5. **Review SOPs** - Understand the quality standards

## Getting Help

- **Documentation**: Start with `docs/README.md`
- **Code Examples**: Review existing files in `website/content/`
- **Architecture**: See `docs/System/project_architecture.md`
- **Procedures**: Check `docs/SOP/` for specific task guidance

## Contributing

When adding new features or content:

1. ✅ Follow the development workflow above
2. ✅ Adhere to the fact-checking protocol
3. ✅ Run all tests before committing
4. ✅ Update `docs/` documentation to reflect changes
5. ✅ Test in the development environment first
6. ✅ Deploy to staging before production

---

**Remember**: This is a static site generator. Every change requires regenerating the site with `python generate_site.py`. When in doubt, check `docs/README.md` for comprehensive guidance.
