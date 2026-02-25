# SOP: Content Management

**Last Updated:** February 25, 2026

## Critical Rule

**Edit Markdown source files** in `/website/content/*.md`.
**Never edit HTML** in `/website/build/` — those are auto-generated and will be overwritten.

## Workflow

1. Edit or create `.md` file in `/website/content/`
2. Run `cd website && python generate_site.py`
3. Refresh browser at http://localhost:8000 (server usually already running)
4. Commit and push to deploy

## File Format

```markdown
---
title: "SEO Page Title (50-60 chars)"
description: "Meta description (127-157 chars)"
keywords: "keyword1, keyword2, keyword3"
page_title: "Display Title (optional)"
show_cta: true
is_homepage: false
---

# Page Heading

Content in Markdown...
```

### Required Frontmatter
- `title` — Browser tab / search results title (50-60 chars)
- `description` — Search result snippet (127-157 chars)
- `keywords` — Comma-separated, 4-6 terms

### Optional Frontmatter
- `page_title` — Display title if different from SEO title
- `show_cta` — Show call-to-action section (boolean)
- `is_homepage` — Enables hero section (only for index.md)
- `hero_title`, `hero_subtitle` — Hero text (homepage only)

## File Naming

- Lowercase with hyphens: `page-name.md`
- Homepage must be `index.md`
- No spaces, underscores, or special characters

## Content Guidelines

| Page Type | Word Count |
|-----------|-----------|
| Homepage | 800-1,000 |
| Core Pages | 1,000-1,500 |
| Landing Pages | 1,000-1,800 |
| Contact/Thank You | 600-800 |

**Style:** Professional, active voice, second person ("you/your"), short paragraphs, bullet points.

## SEO Checklist

- [ ] Primary keyword in first 100 words
- [ ] One H1, logical H2/H3 hierarchy
- [ ] 3-5 internal links per page
- [ ] Descriptive anchor text (no "Learn More" or "Click Here")
- [ ] Meta description includes primary keyword

## Fact-Checking (Required for All Content)

All factual claims must be verified before publishing. This is non-negotiable for legal and credibility reasons.

### Process

1. **Draft:** Mark unverified facts with `[VERIFY: claim]` tags
2. **Verify:** Launch a comprehensive fact-checking agent using the Task tool:
   - Agent must read `docs/System/patent_reference.md` first
   - Agent verifies patent facts, industry claims, dates, quotes
   - Each claim gets: verified/unverified/incorrect + source
3. **Correct:** Fix all flagged issues, remove unverifiable claims
4. **Document:** Keep a fact-check log if the page has significant factual content

### Source Hierarchy

| Priority | Source Type |
|----------|-----------|
| First | Local docs: `docs/System/patent_reference.md`, `docs/US12001207B2.html` |
| Tier 1 | USPTO, official company press releases, government sites, peer-reviewed papers |
| Tier 2 | Major tech news (TechCrunch, Reuters Tech), industry publications, analyst reports |
| Tier 3 | General news, expert social posts (verify with multiple sources) |
| Never | Anonymous sources, unverified social media, Wikipedia (use its sources instead) |

### High-Risk Content (Extra Scrutiny)

- Patent claims and dates — must match USPTO exactly
- Company/product names — use official sources
- Market statistics — cite original research
- Quotes — verify exact text and attribution
- Regulatory claims — official government sources only

## Troubleshooting

**Page not generating:** Check YAML frontmatter syntax, verify `.md` extension, ensure file is in `/website/content/`.

**Content not displaying:** Check Markdown syntax, ensure content is after `---` delimiter, verify spacing.

**SEO elements missing:** Verify frontmatter has title/description/keywords, regenerate site.
