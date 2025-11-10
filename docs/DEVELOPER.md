# Developer README

## Project Overview

This is a Python-based static website for licensing **US Patent 12,001,207 B2**, which covers camera-based navigation safety technology for autonomous vehicles and drones. The website is built using a custom static site generator that converts Markdown content to HTML using Jinja2 templates.

**Key Point**: This is a **pure Python project** - no Node.js, npm, webpack, or JavaScript build tools required.

## Quick Start

```bash
# 1. Install dependencies
cd website
pip install -r requirements.txt

# 2. Generate the website
python generate_site.py

# 3. Run development server
cd build
python -m http.server 8000

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
├── .agent/                    # ⭐ COMPLETE PROJECT DOCUMENTATION (START HERE!)
│   ├── README.md              # Documentation index - read this first
│   ├── Tasks/                 # Product requirements and implementation plans
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
│   ├── deploy.sh            # 🚀 Deployment script
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
   - See `.agent/SOP/content_quality_assurance.md`
   - All patent claims must be verified against the source document
   - Technical specifications must be accurate

5. **Generate the site**:
   ```bash
   cd website
   python generate_site.py
   ```

6. **Test locally** (see "Running the Development Server" below)

7. **Update documentation** in `.agent/` folder if you added new features

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

## Build Process

### Generate the Website

The `generate_site.py` script converts Markdown files to HTML:

```bash
cd website
python generate_site.py
```

**What happens during generation:**
1. Reads all `.md` files from `content/` directory
2. Parses YAML frontmatter for metadata
3. Converts Markdown to HTML using Python's markdown library
4. Renders content through Jinja2 templates in `designs/default/`
5. Generates static HTML files in `build/` directory
6. Creates `sitemap.xml` and `robots.txt`
7. Copies assets to `build/assets/`

### Use Alternative Design Theme

If you have multiple design themes:

```bash
python generate_site.py --design theme-name
```

Current theme: `default`

## Running the Development Server

### Method 1: Python Built-in HTTP Server (Recommended)

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

### Using the Deployment Script

```bash
cd website

# Deploy to staging
./deploy.sh staging

# Deploy to production
./deploy.sh production
```

**What the script does:**
1. Regenerates the site with `python generate_site.py`
2. Runs the test suite to ensure quality
3. Uses `rsync` to upload files to the hosting server
4. Prompts for confirmation before deploying to production

### Manual Deployment

If you prefer to deploy manually:

1. **Generate the site**:
   ```bash
   python generate_site.py
   ```

2. **Upload the `build/` directory** to your web host using:
   - FTP/SFTP client
   - rsync
   - Git-based deployment (Netlify, Vercel, etc.)
   - AWS S3 + CloudFront

The entire website is in the `build/` directory - just upload its contents to your web server's root.

## Important Documentation

### Must-Read Documentation in `.agent/` Folder

**⭐ Start here**: `.agent/README.md` - Complete documentation index

**System Documentation:**
- `.agent/System/project_architecture.md` - Full technical architecture
- `.agent/System/patent_reference.md` - US Patent 12,001,207 B2 details
- `.agent/System/technology_stack.md` - Detailed tech stack information

**Standard Operating Procedures (SOPs):**
- `.agent/SOP/content_management.md` - How to create and edit content
- `.agent/SOP/site_generation_deployment.md` - Build and deploy procedures
- `.agent/SOP/content_quality_assurance.md` - **MANDATORY fact-checking protocol**
- `.agent/SOP/template_editing.md` - How to modify Jinja2 templates

**Task Documentation:**
- `.agent/Tasks/` - Product requirements and implementation plans for features

### Why `.agent/` Documentation Matters

Per `CLAUDE.md` project instructions:
> We maintain all essential documents in the `.agent` folder, ensuring they are regularly updated... Before planning any implementation, always review the `.agent/README.md` first to gain proper context.

The `.agent/` documentation ensures:
- ✅ Consistent development practices
- ✅ Accurate patent information
- ✅ Quality content standards
- ✅ Proper architecture understanding

## Content Guidelines

### ⚠️ CRITICAL: Fact-Checking Protocol

**ALL content must follow the comprehensive fact-checking protocol** documented in:
`.agent/SOP/content_quality_assurance.md`

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
5. **Check documentation first** - `.agent/README.md` has answers

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

1. **Read `.agent/README.md`** - Get complete context
2. **Review existing content** - Look at `website/content/*.md` files
3. **Run the test suite** - Ensure everything works
4. **Make a small change** - Practice the workflow
5. **Review SOPs** - Understand the quality standards

## Getting Help

- **Documentation**: Start with `.agent/README.md`
- **Code Examples**: Review existing files in `website/content/`
- **Architecture**: See `.agent/System/project_architecture.md`
- **Procedures**: Check `.agent/SOP/` for specific task guidance

## Contributing

When adding new features or content:

1. ✅ Follow the development workflow above
2. ✅ Adhere to the fact-checking protocol
3. ✅ Run all tests before committing
4. ✅ Update `.agent/` documentation to reflect changes
5. ✅ Test in the development environment first
6. ✅ Deploy to staging before production

---

**Remember**: This is a static site generator. Every change requires regenerating the site with `python generate_site.py`. When in doubt, check `.agent/README.md` for comprehensive guidance.
