# AV Navigation IP Protection Website — Documentation

**Last Updated:** February 25, 2026

## Quick Start

This is a static site generated from Markdown. The golden rule:

- **Edit:** `/website/content/*.md` (Markdown source)
- **Never edit:** `/website/build/*.html` (auto-generated, will be overwritten)
- **After editing:** `cd website && python generate_site.py`
- **Preview:** http://localhost:8000

## Documentation Map

### System/
Current system state and reference material.

| File | Contents |
|------|----------|
| [project_architecture.md](./System/project_architecture.md) | Project structure, tech stack, site generation flow, SEO implementation, security headers, hosting, integrations |
| [patent_reference.md](./System/patent_reference.md) | US Patent 12,001,207 B2 — full technical reference, claims, applications, licensing targets |

### SOP/
Step-by-step procedures for common tasks.

| File | Contents |
|------|----------|
| [content_management.md](./SOP/content_management.md) | Creating/editing content, frontmatter format, SEO checklist, fact-checking protocol |
| [site_generation_deployment.md](./SOP/site_generation_deployment.md) | Generating the site, local testing, deployment, rollback |

### plans/
Active plans and strategy documents.

| File | Contents |
|------|----------|
| [20260126_zero_budget_traffic_plan.md](./plans/20260126_zero_budget_traffic_plan.md) | Traffic acquisition strategy — SEO fixes, LinkedIn, Quora, backlinks, direct outreach |

Completed plans are in `plans/archived/`.

### Other
| File | Contents |
|------|----------|
| [US12001207B2.html](./US12001207B2.html) | Official patent document (3,689 lines) |

## Project Quick Facts

- **URL:** https://av-navigation-ip.com
- **Hosting:** Netlify (auto-deploy on git push)
- **Patent:** US 12,001,207 B2 (granted June 4, 2024, expires March 5, 2041)
- **Pages:** 14 (9 core + 5 SEO landing pages)
- **Tech:** Python, Markdown, Jinja2, Bootstrap 5
- **Contact form:** Web3Forms
- **Domain registrar:** Namecheap (catch-all email configured)

## Common Tasks

**Edit content:** See [content_management.md](./SOP/content_management.md)

**Deploy:** `git add . && git commit -m "description" && git push`

**Generate site:** `cd website && python generate_site.py`

**Run tests:** `cd website && python test_website.py` (46 tests)

**Patent facts:** Start with [patent_reference.md](./System/patent_reference.md), then `US12001207B2.html` for details
