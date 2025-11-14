# Standard Operating Procedure: Site Generation and Deployment

## Overview

This SOP covers the complete process of generating the static website, testing it locally, and deploying it to production hosting. The AV Navigation IP Protection website uses a Python-based static site generator.

## Prerequisites

### Required Software
- Python 3.x (3.7 or higher)
- pip (Python package manager)
- Git (for version control)
- SSH access (for rsync deployment)

### Required Python Packages
```bash
pip install -r website/requirements.txt
```

Installs:
- markdown==3.5.1
- jinja2==3.1.2
- beautifulsoup4==4.12.2

### Directory Structure
Ensure you're in the project root: `/Users/sjsmit/Development/Caden/op_patent/`

## Site Generation Process

### Basic Generation

#### Step 1: Navigate to Website Directory
```bash
cd website
```

#### Step 2: Run Site Generator
```bash
python generate_site.py
```

**Expected Output:**
```
🚀 Starting static site generation using 'default' design...
✓ Cleaned build directory: /path/to/website/build
✓ Copied assets to: /path/to/website/build/assets
✓ Generated: index.html from index.md
✓ Generated: patent-details.html from patent-details.md
✓ Generated: licensing.html from licensing.md
✓ Generated: industry-insights.html from industry-insights.md
✓ Generated: contact.html from contact.md
✓ Generated: thank-you.html from thank-you.md
✓ Generated sitemap: /path/to/website/build/sitemap.xml
✓ Generated robots.txt: /path/to/website/build/robots.txt

✅ Site generation complete!
📁 Output directory: /path/to/website/build
📄 Generated 6 pages
🌐 Open /path/to/website/build/index.html in your browser to preview
```

#### Step 3: Verify Build Output
```bash
ls -la build/
```

**Expected Files:**
- `index.html`
- `patent-details.html`
- `licensing.html`
- `industry-insights.html`
- `contact.html`
- `thank-you.html`
- `sitemap.xml`
- `robots.txt`
- `assets/` (directory)

### Advanced Generation Options

#### Use Alternative Design Theme
```bash
python generate_site.py --design theme-name
```

**Available Themes:**
- `default` (current production theme)

**Example:**
```bash
python generate_site.py --design minimal-tech
```

#### Email Obfuscation Utility
Generate base64-encoded email for anti-spam:
```bash
python generate_site.py --obfuscate-email your@email.com
```

## Local Testing

### Method 1: Simple Browser Preview
```bash
# macOS
open build/index.html

# Linux
xdg-open build/index.html

# Windows
start build/index.html
```

### Method 2: Local Development Server (Recommended)
```bash
cd build
python -m http.server 8000
```

**Access in Browser:**
- Homepage: http://localhost:8000
- Patent Details: http://localhost:8000/patent-details.html
- Licensing: http://localhost:8000/licensing.html
- etc.

**Benefits:**
- Tests relative links correctly
- Simulates production environment
- Allows mobile device testing (via local network IP)

### Method 3: Run Test Suite
```bash
cd website
python test_website.py
```

**Test Coverage:**
- File existence (8 tests)
- Page loading (6 tests)
- Navigation links (5 tests)
- SEO elements (6 tests)
- Responsive design (3 tests)
- Contact form (5 tests)
- Accessibility (3 tests)
- Performance basics (3 tests)

**Expected Output:**
```
Testing AV Navigation IP Protection Website
Total Tests: 46
Passed: 46
Failed: 0
Success Rate: 100%
```

## Pre-Deployment Checklist

Before deploying to production, verify:

### Content Verification
- [ ] All content pages exist and load
- [ ] No Lorem Ipsum placeholder text
- [ ] All links functional (internal and external)
- [ ] Contact form endpoint configured (Formspree)
- [ ] Legal disclaimer present on all pages

### SEO Verification
- [ ] Meta titles present (50-60 characters)
- [ ] Meta descriptions present (127-157 characters)
- [ ] Keywords defined for each page
- [ ] Sitemap.xml generated
- [ ] Robots.txt generated
- [ ] Canonical URLs configured (if implemented)

### Technical Verification
- [ ] All assets copied to build directory
- [ ] No broken images or CSS
- [ ] JavaScript functional (if any)
- [ ] Mobile responsive design working
- [ ] Browser compatibility tested (Chrome, Firefox, Safari)

### Testing Verification
- [ ] Test suite passes 100%
- [ ] Manual browser testing complete
- [ ] Mobile device testing complete
- [ ] Form submission tested (if Formspree configured)

## Deployment Process

### Initial Setup (One-Time)

#### Option 1: rsync Deployment (SiteGround, VPS)

**1. Configure SSH Access**
```bash
# Test SSH connection
ssh username@your-server.com

# Set up SSH key (recommended)
ssh-copy-id username@your-server.com
```

**2. Update deploy.sh Script**
Edit `/website/deploy.sh`:
```bash
# Production configuration
REMOTE_USER="your-username"
REMOTE_HOST="your-server.com"
REMOTE_PATH="/path/to/public_html"
```

**3. Make Script Executable**
```bash
chmod +x deploy.sh
```

#### Option 2: Netlify Deployment (Git-Based)

**1. Install Netlify CLI**
```bash
npm install -g netlify-cli
```

**2. Login to Netlify**
```bash
netlify login
```

**3. Initialize Site**
```bash
netlify init
```

**4. Configure Build Settings**
- Build command: `python generate_site.py`
- Publish directory: `website/build`

### Deployment Execution

#### Option 1: rsync Deployment

**Production Deployment:**
```bash
cd website
./deploy.sh production
```

**Staging Deployment (if configured):**
```bash
./deploy.sh staging
```

**Manual rsync:**
```bash
rsync -avz --delete build/ username@server.com:/path/to/public_html/
```

**Flags Explained:**
- `-a`: Archive mode (preserves permissions, timestamps)
- `-v`: Verbose output
- `-z`: Compress during transfer
- `--delete`: Remove files on server not in source

#### Option 2: Netlify Deployment

**Deploy to Production:**
```bash
netlify deploy --prod
```

**Deploy to Draft (preview):**
```bash
netlify deploy
```

**Git-Based Deployment:**
```bash
git add .
git commit -m "Update website content"
git push origin main
# Netlify auto-deploys on push
```

### Post-Deployment Verification

#### Step 1: Check Live Site
Visit your production URL: `https://av-navigation-ip.com`

**Verify:**
- [ ] Homepage loads correctly
- [ ] All pages accessible via navigation
- [ ] SSL/HTTPS active (secure connection)
- [ ] No 404 errors on any page
- [ ] Contact form submits correctly

#### Step 2: Test Cross-Browser
Test on:
- [ ] Chrome (desktop)
- [ ] Firefox (desktop)
- [ ] Safari (desktop)
- [ ] Mobile Safari (iOS)
- [ ] Mobile Chrome (Android)

#### Step 3: Test Responsive Design
Test at breakpoints:
- [ ] Mobile: 375px width
- [ ] Tablet: 768px width
- [ ] Desktop: 1920px width

#### Step 4: SEO Verification
**View Page Source (Right-click → View Page Source):**
- [ ] `<title>` tag present and correct
- [ ] `<meta name="description">` present
- [ ] `<meta name="keywords">` present
- [ ] Canonical URL present (if implemented)
- [ ] Open Graph tags present (if implemented)

**Check Search Console:**
- [ ] Submit sitemap: `https://av-navigation-ip.com/sitemap.xml`
- [ ] Verify sitemap indexed
- [ ] Request indexing for key pages

## Continuous Deployment Workflow

### Making Content Updates

**1. Edit Content**
```bash
cd website/content
# Edit file (e.g., vim index.md)
```

**2. Regenerate Site**
```bash
cd website
python generate_site.py
```

**3. Test Locally**
```bash
cd build
python -m http.server 8000
# Verify changes at http://localhost:8000
```

**4. Run Tests**
```bash
cd website
python test_website.py
```

**5. Commit Changes**
```bash
git add website/content/
git commit -m "Update homepage content"
git push
```

**6. Deploy**
```bash
cd website
./deploy.sh production
```

### Adding New Pages

**1. Create Content File**
```bash
cd website/content
# Create new-page.md with frontmatter
```

**2. Generate Site**
```bash
cd website
python generate_site.py
```

**3. Update Navigation (if needed)**
Edit `/website/designs/default/base.html` to add nav link.

**4. Test**
```bash
python test_website.py
```

**5. Deploy**
```bash
./deploy.sh production
```

## Rollback Procedure

If deployment causes issues, rollback to previous version:

### Option 1: Git Rollback
```bash
# Find previous commit
git log --oneline

# Rollback to previous commit
git checkout <commit-hash>

# Regenerate site
cd website
python generate_site.py

# Redeploy
./deploy.sh production

# Return to latest
git checkout main
```

### Option 2: Keep Build Backups
```bash
# Before deployment, backup current build
cp -r build build_backup_$(date +%Y%m%d_%H%M%S)

# If rollback needed
rsync -avz --delete build_backup_YYYYMMDD_HHMMSS/ username@server.com:/path/
```

## Monitoring and Maintenance

### Weekly Checks
- [ ] Site uptime (all pages loading)
- [ ] SSL certificate valid
- [ ] Contact form functional
- [ ] No broken links

### Monthly Checks
- [ ] Google Analytics traffic review
- [ ] Search Console indexing status
- [ ] Keyword ranking monitoring
- [ ] Performance metrics (Lighthouse)

### Quarterly Updates
- [ ] Content refresh (update statistics, trends)
- [ ] Dependency updates (`pip install --upgrade`)
- [ ] Security patches
- [ ] SEO optimization based on data

## Troubleshooting

### Issue: Site Generation Fails
**Symptoms:** Error messages during `python generate_site.py`

**Solutions:**
1. Check Python version: `python --version` (needs 3.7+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Verify content files have valid frontmatter
4. Check for syntax errors in Markdown files

### Issue: Deployment Fails (rsync)
**Symptoms:** rsync command fails or times out

**Solutions:**
1. Test SSH connection: `ssh username@server.com`
2. Verify server path is correct
3. Check disk space on server: `df -h`
4. Ensure proper permissions on remote directory

### Issue: Pages Not Updating on Live Site
**Symptoms:** Changes deployed but not visible

**Solutions:**
1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Verify deployment completed successfully
3. Check file timestamps on server
4. Clear CDN cache (if using CDN)
5. Check browser is not using cached version

### Issue: Test Suite Fails
**Symptoms:** Some tests fail after changes

**Solutions:**
1. Review error messages carefully
2. Regenerate site: `python generate_site.py`
3. Verify content files have correct frontmatter
4. Check for broken links in content
5. Ensure assets directory exists and has files

## Emergency Procedures

### Site Down Emergency
1. Check hosting provider status
2. Verify DNS configuration
3. Test server connectivity: `ping your-domain.com`
4. Check SSL certificate expiration
5. Contact hosting support if needed

### Broken Deployment
1. Stop deployment immediately
2. Rollback to previous version (see Rollback Procedure)
3. Diagnose issue locally
4. Fix and test thoroughly
5. Redeploy cautiously

## Related Documentation

- **Content Management SOP**: `/docs/SOP/content_management.md`
- **Project Architecture**: `/docs/System/project_architecture.md`
- **Website README**: `/website/README.md`
- **PRD**: `/docs/plans/archived/website_development_prd.md`
