# Background Images for Open Graph Social Sharing

This directory contains background images used to generate Open Graph social sharing images.

## Required Images

You need to download **4 background images** and save them in this directory with the exact filenames below:

1. `startup-innovation.jpg`
2. `investment-finance.jpg`
3. `technical-legal.jpg`
4. `general-info.jpg`

## Image Requirements

- **Dimensions**: 1200x630 pixels minimum (larger is okay, will be center-cropped)
- **Format**: JPG preferred (better compression)
- **License**: CC0 or Free for commercial use
- **Quality**: High resolution, professional photography
- **Style**: Clean, modern, not too busy (text overlay needs clear space in bottom 40%)

## Image Sources

Use these platforms (all provide free, CC0-licensed images):

- **Unsplash**: https://unsplash.com/ (100% free, no attribution required)
- **Pexels**: https://www.pexels.com/ (100% free, no attribution required)
- **Pixabay**: https://pixabay.com/ (CC0 license, free for commercial use)

---

## Category 1: Startup/Innovation

**Filename**: `startup-innovation.jpg`

**Used for pages**: Series A AV, Tesla FSD Competitor, Autonomous Trucking

**Primary Search Query**: "autonomous vehicle technology modern"

**Alternative Search Queries**:
1. "self-driving car dashboard futuristic"
2. "AI vehicle sensor technology"
3. "autonomous navigation camera system"
4. "electric vehicle innovation startup"
5. "automotive technology lab research"
6. "AV startup technology prototype"
7. "autonomous vehicle testing facility"

**Selection Criteria**:
- Shows modern autonomous vehicle technology
- Clean, professional aesthetic
- Tech-forward, innovation-focused
- Not too busy (text overlay area should be clear)
- Conveys startup energy and innovation

---

## Category 2: Investment/Finance

**Filename**: `investment-finance.jpg`

**Used for pages**: VC Due Diligence, Drone Delivery Pre-IPO

**Primary Search Query**: "business investment strategy technology"

**Alternative Search Queries**:
1. "venture capital handshake deal"
2. "financial growth chart technology"
3. "tech investment portfolio modern"
4. "business funding startup meeting"
5. "corporate investment digital finance"
6. "venture capital pitch meeting"
7. "investment analysis technology"

**Selection Criteria**:
- Shows business/investment/finance theme
- Professional, trustworthy aesthetic
- Conveys growth and strategic thinking
- Clear space for text overlay in bottom 40%
- Suitable for VC and investor audience

---

## Category 3: Technical/Legal

**Filename**: `technical-legal.jpg`

**Used for pages**: Patent Details, Licensing

**Primary Search Query**: "patent document technology blueprint"

**Alternative Search Queries**:
1. "intellectual property legal document"
2. "technical diagram engineering blueprint"
3. "patent certificate official document"
4. "legal contract technology licensing"
5. "technical specifications detailed drawing"
6. "patent application blueprint"
7. "engineering document technical"

**Selection Criteria**:
- Shows technical/legal/documentation theme
- Professional, authoritative aesthetic
- Conveys intellectual property and technical expertise
- Clear space for text overlay in bottom 40%
- Not too busy or text-heavy

---

## Category 4: General/Info (Default Catch-All)

**Filename**: `general-info.jpg`

**Used for pages**: Homepage, Industry Insights, Contact, Thank You, About, Disclaimer, Privacy, and any new pages

**Primary Search Query**: "smart transportation future connectivity"

**Alternative Search Queries**:
1. "connected vehicles network highway"
2. "smart city transportation aerial"
3. "transportation technology network digital"
4. "intelligent transport system future"
5. "mobility innovation urban landscape"
6. "connected autonomous vehicles highway"
7. "smart mobility future city"

**Selection Criteria**:
- Shows transportation/connectivity/future theme
- Professional, forward-looking aesthetic
- Broad enough to work for multiple page types
- Clear space for text overlay in bottom 40%
- Conveys innovation and connectivity

---

## Download Workflow

For each category:

1. Go to Unsplash.com or Pexels.com
2. Search using the primary query (try alternatives if needed)
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. **Verify image is at least 1200x630px** (check dimensions before download)
6. Verify license: Look for "Free to use" badge on image page
7. Download highest resolution available
8. Save as exact filename in this directory (e.g., `startup-innovation.jpg`)

**Time estimate**: 5-10 minutes per category, 20-40 minutes total

---

## License Verification

**Unsplash**:
- All images are free for commercial use
- No attribution required (but appreciated)
- Confirm "Free to use" badge on image page

**Pexels**:
- All free images are under Pexels License
- Free for commercial use
- No attribution required
- Confirm "Free to use" badge on image page

**Pixabay**:
- Look for "Free for commercial use" or "CC0" license
- No attribution required for CC0 images
- Confirm license terms on download page

---

## After Downloading

Once all 4 images are in place, run:

```bash
# Test with preview (displays without saving)
python generate_og_images.py --preview --category general-info

# Generate single category
python generate_og_images.py --category general-info

# Generate all 4 categories
python generate_og_images.py
```

Expected output: 4 OG images in `assets/images/`:
- `og-startup-innovation.jpg`
- `og-investment-finance.jpg`
- `og-technical-legal.jpg`
- `og-general-info.jpg`

---

## Notes

- These background images are committed to git for reproducibility
- The generated OG images (with text overlay) are gitignored as they're derivatives
- All 4 images must be present before running the generator script
