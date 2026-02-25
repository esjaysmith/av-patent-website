# SOP: Site Generation & Deployment

**Last Updated:** February 25, 2026

## Quick Reference

```bash
# Generate site
cd website && python generate_site.py

# Preview locally
cd website/build && python -m http.server 8000
# → http://localhost:8000

# Run tests
cd website && python test_website.py

# Deploy
git add . && git commit -m "Update website" && git push
```

## How It Works

```
/website/content/*.md  →  generate_site.py  →  /website/build/*.html
```

- Generator reads Markdown + YAML frontmatter
- Applies Jinja2 templates from `/website/designs/default/`
- Outputs HTML pages, sitemap.xml, and robots.txt to `/website/build/`
- `git push` to master triggers Netlify auto-deploy

## Generation

```bash
cd website
python generate_site.py
```

Expected output: 14 pages generated + sitemap.xml + robots.txt.

### Prerequisites

```bash
pip install -r website/requirements.txt
# markdown==3.5.1, jinja2==3.1.2, beautifulsoup4==4.12.2
```

## Local Testing

**Start local server** (usually already running during development):
```bash
cd website/build
python -m http.server 8000
```

After editing content, just regenerate and refresh the browser — no need to restart the server.

**Run test suite:**
```bash
cd website
python test_website.py
# Expected: 46/46 tests passing
```

## Deployment

The site deploys automatically when you push to the master branch.

```bash
git add .
git commit -m "Update: brief description"
git push
```

Netlify detects the push, runs the build, and deploys `/website/build/` to production at https://av-navigation-ip.com.

### Pre-Deploy Checklist

- [ ] Site generates without errors
- [ ] Pages load correctly at localhost:8000
- [ ] Navigation links work
- [ ] Test suite passes
- [ ] Fact-checking complete (for content changes)

### Post-Deploy Verification

- [ ] Live site loads at https://av-navigation-ip.com
- [ ] Changed pages reflect updates
- [ ] Contact form submits correctly
- [ ] No console errors in browser DevTools

## Rollback

```bash
git log --oneline          # Find previous commit
git revert HEAD            # Create a revert commit
git push                   # Deploy the revert
```

## Troubleshooting

**Generation fails:** Check Python version (3.7+), reinstall requirements, check frontmatter syntax.

**Deploy doesn't update:** Clear browser cache (Cmd+Shift+R), check Netlify build logs, verify push succeeded.

**Tests fail:** Regenerate site first, check frontmatter, verify content files exist.
