# Milestone 5: Production Deployment

## Task Information
- **Parent PRD**: `20251110_production_readiness_prd.md`
- **Milestone**: 5 of 6
- **Priority**: Critical (Launch)
- **Duration**: 1-2 days
- **Status**: Not Started
- **Dependencies**: Milestones 1-4 must be complete
- **Blocks**: Milestone 6 (Post-Launch Optimization)

## Overview

Deploy the website to production hosting with HTTPS/SSL, configure domain, test all functionality on production, and set up monitoring.

**Problem**: Site is only accessible locally at localhost:8000.

**Solution**: Deploy to production hosting (Netlify, SiteGround, or AWS S3), configure domain, enable HTTPS.

## Deliverables

### 1. Production Hosting Setup
- Choose hosting provider (Netlify, SiteGround, or AWS S3+CloudFront)
- Create account and configure hosting
- Set up deployment method

### 2. Domain Configuration
- Point domain (av-navigation-ip.com) to hosting
- Configure DNS records
- Set up www → non-www redirect (or vice versa)

### 3. HTTPS/SSL Certificate
- Install Let's Encrypt SSL certificate (free)
- Configure HTTPS redirect (HTTP → HTTPS)
- Verify certificate validity

### 4. Deploy Website
- Generate site with production domain
- Deploy to hosting
- Test deployment

### 5. Production Testing
- Test all pages load
- Test all links work
- Test contact form submits
- Test mobile responsiveness
- Test performance

### 6. Monitoring Setup
- Configure uptime monitoring
- Set up error tracking (optional)
- Document deployment process

## Hosting Options

### Option 1: Netlify (Recommended for Static Sites)

**Pros**:
- Free tier (100GB bandwidth/month)
- Git-based deployment (auto-deploy on push)
- Automatic SSL (Let's Encrypt)
- Form handling built-in
- CDN included
- Easy rollbacks

**Setup Steps**:
1. Go to https://netlify.com/
2. Sign up with GitHub account
3. Connect repository: `/Users/sjsmit/Development/Caden/op_patent`
4. Configure build settings:
   - Build command: `cd website && python generate_site.py`
   - Publish directory: `website/build`
5. Deploy site (first deploy)
6. Configure custom domain: av-navigation-ip.com
7. Enable HTTPS (automatic)
8. Configure forms (if using Netlify Forms):
   - Add `netlify` attribute to form tag
   - Netlify auto-detects forms

**Cost**: Free (50k requests/month, 100GB bandwidth)

### Option 2: SiteGround (Traditional Hosting)

**Pros**:
- Excellent support
- Fast servers (SSD)
- One-click SSL
- cPanel access
- Email hosting included

**Setup Steps**:
1. Go to https://www.siteground.com/
2. Choose StartUp plan (~$3-15/month)
3. Purchase hosting + domain (or point existing domain)
4. Access cPanel
5. Upload site via FTP/SFTP or File Manager
6. Install SSL certificate (one-click via cPanel)
7. Configure HTTPS redirect (.htaccess)

**Cost**: ~$10-15/month (after introductory pricing)

### Option 3: AWS S3 + CloudFront (Advanced)

**Pros**:
- Highly scalable
- Pay-per-use (very cheap for low traffic)
- Global CDN
- Integrates with other AWS services

**Setup Steps**:
1. Create S3 bucket: `av-navigation-ip.com`
2. Enable static website hosting
3. Upload files to S3: `aws s3 sync website/build/ s3://bucket-name/`
4. Create CloudFront distribution
5. Configure SSL certificate (AWS Certificate Manager)
6. Point domain to CloudFront distribution

**Cost**: ~$1-5/month (low traffic)

## Domain Configuration

### DNS Records

**If using Netlify**:
- A record: `@` → `75.2.60.5` (Netlify load balancer)
- CNAME record: `www` → `[your-site].netlify.app`

**If using SiteGround**:
- A record: `@` → `[SiteGround IP address]`
- CNAME record: `www` → `av-navigation-ip.com`

**If using AWS CloudFront**:
- A record (Alias): `@` → `[CloudFront distribution domain]`
- CNAME record: `www` → `[CloudFront distribution domain]`

### www Redirect

**Recommended**: Redirect www to non-www (or vice versa)

**Netlify**: Configure in `netlify.toml`:
```toml
[[redirects]]
  from = "https://www.av-navigation-ip.com/*"
  to = "https://av-navigation-ip.com/:splat"
  status = 301
  force = true
```

**SiteGround**: Add to `.htaccess`:
```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.av-navigation-ip\.com [NC]
RewriteRule ^(.*)$ https://av-navigation-ip.com/$1 [L,R=301]
```

## Deployment Workflow

### Pre-Deployment Checklist
- [ ] All Milestones 1-4 complete
- [ ] All 46+ tests passing
- [ ] Legal pages published
- [ ] Contact form tested
- [ ] SEO tags implemented
- [ ] Site generated with production domain in canonical URLs

### Generate Site with Production Domain

Update `generate_site.py` to accept domain parameter:
```bash
python generate_site.py --domain av-navigation-ip.com
```

Or manually replace `[domain]` placeholders in templates with `av-navigation-ip.com`.

### Deploy to Netlify

**Method 1: Git-Based (Recommended)**:
1. Commit all changes: `git add . && git commit -m "Production ready"`
2. Push to GitHub: `git push origin main`
3. Netlify auto-deploys from GitHub

**Method 2: Manual Upload**:
1. Drag and drop `website/build/` folder to Netlify dashboard
2. Configure custom domain
3. Enable HTTPS

### Deploy to SiteGround

**Method 1: FTP/SFTP**:
1. Connect via FileZilla or similar
2. Upload `website/build/*` contents to `/public_html/`
3. Verify files uploaded correctly

**Method 2: rsync** (from `docs/SOP/site_generation_deployment.md`):
```bash
rsync -avz --delete website/build/ user@siteground-server:/home/user/public_html/
```

### Deploy to AWS S3

```bash
aws s3 sync website/build/ s3://av-navigation-ip.com/ --delete
aws cloudfront create-invalidation --distribution-id XXXXXX --paths "/*"
```

## Production Testing

### Functionality Tests
- [ ] All 12 pages load without errors
- [ ] All internal links work
- [ ] All external links work (open in new tab)
- [ ] Navigation dropdown works
- [ ] Contact form submits successfully
- [ ] Thank-you page displays after form submission
- [ ] Footer links work (sitemap, disclaimer, privacy)
- [ ] Breadcrumbs display correctly

### HTTPS/SSL Tests
- [ ] Site loads via HTTPS: `https://av-navigation-ip.com`
- [ ] HTTP redirects to HTTPS: `http://av-navigation-ip.com` → `https://av-navigation-ip.com`
- [ ] No browser security warnings
- [ ] SSL certificate valid (green padlock icon)
- [ ] www redirects to non-www (or vice versa)

### Performance Tests
- [ ] PageSpeed Insights score >85 mobile, >90 desktop
- [ ] Google Mobile-Friendly Test passes
- [ ] Core Web Vitals pass (LCP <2.5s, FID <100ms, CLS <0.1)
- [ ] All images load correctly
- [ ] No 404 errors in browser console

### Analytics Tests
- [ ] Google Analytics tracking fires
- [ ] Google Analytics real-time report shows pageviews
- [ ] Contact form submissions tracked (if configured)

## Monitoring Setup

### Uptime Monitoring

**UptimeRobot (Free)**:
1. Go to https://uptimerobot.com/
2. Create free account
3. Add monitor: `https://av-navigation-ip.com`
4. Set check interval: 5 minutes
5. Configure email alerts

**Pingdom (Paid)**:
- More advanced monitoring
- Performance tracking
- Transaction monitoring

### Error Tracking (Optional)

**Sentry**:
- JavaScript error tracking
- Real-time error alerts
- Free tier available

## Acceptance Criteria

### Deployment
- [ ] Site accessible via production domain with HTTPS
- [ ] All pages load correctly on production
- [ ] Contact form submits successfully on production
- [ ] All internal links work
- [ ] All external links work
- [ ] SSL certificate valid (no warnings)
- [ ] 301 redirects configured (www/non-www)

### Performance
- [ ] PageSpeed score >85 mobile, >90 desktop
- [ ] Mobile-Friendly Test passes
- [ ] No 404 errors or broken links

### Monitoring
- [ ] Uptime monitoring configured
- [ ] Email alerts set up for downtime
- [ ] Deployment process documented

## Files to Update

### Before Deployment
- `/website/generate_site.py` - Add `--domain` parameter (optional)
- Templates - Replace `[domain]` with `av-navigation-ip.com`
- `/website/content/*.md` - Verify all pages have correct frontmatter

### Deployment Configuration
- `.gitignore` - Exclude `build/` from git (already done)
- `netlify.toml` - Netlify configuration (if using Netlify)
- `.htaccess` - Apache configuration (if using SiteGround)

### Documentation
- `docs/SOP/site_generation_deployment.md` - Update with production deployment steps

## Success Metrics

- Site live and accessible via HTTPS
- Zero downtime during deployment
- All functionality working on production
- Uptime monitoring configured and sending alerts
- Deployment process documented for future updates

## Backup & Rollback

### Backup Before Deployment
- [ ] Backup current production site (if updating existing site)
- [ ] Export current DNS settings
- [ ] Save current hosting configuration

### Rollback Plan
- **Netlify**: Rollback to previous deploy via dashboard (1-click)
- **SiteGround**: Restore from backup via cPanel
- **AWS**: Revert S3 files, create new CloudFront invalidation

## Notes

- DNS propagation can take 24-48 hours (plan accordingly)
- Test on staging domain first if available (e.g., `staging.av-navigation-ip.com`)
- Keep local copy of site as backup
- Document any custom server configurations

---

**Status**: Not Started
**Created**: November 10, 2025
**Priority**: Critical
**Estimated Effort**: 1-2 days
