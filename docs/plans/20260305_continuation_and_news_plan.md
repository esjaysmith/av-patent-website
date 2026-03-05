# Plan: Add Continuation Patent + Industry News to Website ✅ COMPLETE (Mar 5, 2026)

## Context

Two developments need to be reflected on the site:
1. **US Patent 12,530,030** (continuation) was granted Jan 20, 2026 — 20 claims, adds clear-passage-determining module and method/system/CPP claim types. The site currently only references the original patent (US 12,001,207).
2. **Industry developments** (Alpamayo/Nvidia, Wayve Series D, etc.) provide timely hooks connecting the patent portfolio to current events.

This plan covers Option C: update existing pages + add a news page.

## Steps

### 1. Update patent pages and reference docs

#### 1a. Reframe `patent-details.md` as portfolio page
- Update page title/meta from "US Patent 12,001,207" to "Patent Portfolio: Technical Overview"
- Update OG/Twitter meta tags to match portfolio framing
- Add a short "Continuation Patent: What's New" section after the original patent content:
  - US 12,530,030 granted Jan 20, 2026
  - 20 claims (vs 13 in original) — adds method claims (1–15), CPP claims (16–18), system claims (19–20)
  - Key addition: clear-passage-determining module (determines whether navigation instructions can be executed based on traffic/right-of-way)
  - Link to standalone continuation page for full details
- Update FAQ: rewrite existing answers to reference portfolio where relevant, add 2–3 new Q&As:
  - "What does the continuation patent add?" (clear-passage module, broader claim types)
  - "What is a terminal disclaimer?" (both patents expire March 5, 2041)
  - "How many claims does the portfolio cover?" (33 total: 13 + 20)
- Update Licensing section at bottom to reference portfolio
- Update `date_modified`
- **File:** `website/content/patent-details.md`

#### 1b. Create standalone continuation patent page
- New page `patent-details-continuation.md` with full deep-dive on US 12,530,030
- Content: patent metadata, abstract, detailed claims breakdown (method/CPP/system), clear-passage-determining module explanation, relationship to original patent
- Own SEO meta/OG tags targeting "US Patent 12530030" keywords
- Cross-link to main portfolio page and licensing page
- Add to site navigation alongside existing patent details link
- **File:** `website/content/patent-details-continuation.md` (new), possibly nav template

#### 1c. Update `patent_reference.md` system doc
- Add full US 12,530,030 section: dates, claim count, claim types, clear-passage module, terminal disclaimer
- Update overview to reflect 2-patent portfolio
- Add internal reference links (continuation page, Google Patents link)
- **File:** `docs/System/patent_reference.md`

### 2. Update `index.md` homepage
- Change "Patent details" stats to reflect portfolio (2 granted US patents + EP patent)
- Update hero text and "What this patent covers" to reference both patents
- **File:** `website/content/index.md`

### 3. Update `licensing.md`
- Reference portfolio (2 US patents) instead of single patent
- Update geographic coverage if continuation changes anything
- **File:** `website/content/licensing.md`

### 4. Update `industry-insights.md` with current developments
- Add sections for Alpamayo/Nvidia, Wayve Series D, and other recent developments
- Connect each development back to the patent portfolio's relevance
- Update date_modified
- **File:** `website/content/industry-insights.md`

### 5. Create `news.md` page
- New content page with dated announcement entries
- First entries: continuation patent granted (Jan 2026), industry developments
- Add to site navigation (will need to check how nav is configured in the template)
- **File:** `website/content/news.md` (new), possibly `website/designs/default/base.html` for nav

### 6. Update all 5 SEO landing pages
- Change references from "US Patent 12,001,207" (single) to "patent portfolio" (2 granted US patents) where appropriate
- Add mention of the continuation's clear-passage claims where relevant (especially trucking and drone pages)
- **Files:** `website/content/series-a-av-patent-portfolio-strategy.md`, `tesla-fsd-competitor-camera-patent-licensing.md`, `drone-delivery-patent-portfolio-pre-ipo.md`, `venture-capital-av-patent-portfolio-due-diligence.md`, `autonomous-trucking-patent-defense-strategy.md`

### 7. Rebuild, deploy, and submit
- Run `python generate_site.py` from `/website/`
- Deploy to Netlify
- Run `python submit_indexnow.py` to notify Bing/ChatGPT/Copilot/Meta AI
- Submit new `news.html` to Brave Search

### 8. Update traffic plan
- Tick off relevant items, add action log entries
- **File:** `docs/plans/20260126_zero_budget_traffic_plan.md`

## Verification

- Run `python generate_site.py` — all pages generate without errors
- Verify `news.html` appears in `sitemap.xml`
- Spot-check built HTML for correct patent numbers and portfolio references
- Visual check of news page and updated patent-details page in browser

## Notes

- **IMPORTANT: Run the humanizer skill on ALL new or edited content before finalizing each step.** Every content change (steps 1–6) must be passed through the humanizer to remove signs of AI-generated writing before moving on.
- Content for industry developments (Alpamayo, Wayve, etc.) needs user input on specifics — will ask during implementation
- The continuation shares the same abstract as the original but has 20 claims (vs 13) and adds the clear-passage-determining module
- Terminal disclaimer means both patents expire together (March 5, 2041)

## Finishing tasks (after all content steps complete)

- [ ] Run `python generate_site.py` from `/website/` — confirm all pages generate without errors
- [ ] Verify `sitemap.xml` includes all new pages (`patent-details-continuation.html`, `news.html`)
- [ ] Spot-check built HTML for correct patent numbers and portfolio references
- [ ] Visual check of all updated pages in browser (localhost:8000)
- [ ] Deploy to Netlify (`netlify deploy --prod` or git push, depending on setup)
- [ ] Run `python submit_indexnow.py` to notify Bing/ChatGPT/Copilot/Meta AI of updated pages
- [ ] Submit new pages to Google Search Console (request indexing for new URLs)
- [ ] Submit new pages to Brave Search (webmaster tools)
- [ ] Update `docs/plans/20260126_zero_budget_traffic_plan.md` — tick off relevant items, add action log entries
