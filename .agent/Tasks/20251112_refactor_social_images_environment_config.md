# Product Requirements Document: Social Images & Environment Configuration Refactoring

## Document Information
- **Task Type**: Refactoring - Infrastructure & Image Generation
- **Status**: Active
- **Priority**: High
- **Created**: November 12, 2025
- **Estimated Duration**: 1-2 days
- **Owner**: Developer (Team Member)
- **Parent Document**: `20251112_finish_seo_technical_implementation.md` (Milestone 3 - Prerequisite)
- **Target Completion**: November 14, 2025

---

## Executive Summary

This refactoring PRD extracts the social image generation and environment configuration setup from the main SEO implementation PRD. This is a **prerequisite** that must be completed before implementing the main SEO features (Open Graph tags, Twitter Cards, structured data).

### Problem Statement

The original SEO PRD specified AI-generated images (DALL-E 3, Midjourney) for creating 13 unique Open Graph images. This approach has significant limitations:
- Dependency on external AI services (ChatGPT Plus or Midjourney subscription)
- Inconsistent quality and style across generations
- Licensing concerns with AI-generated content
- Manual effort required for each of 13 pages
- Difficult to maintain brand consistency
- Time-consuming iteration to get acceptable results

### Refactored Solution

Replace AI generation with a **manual background selection + automated Python text overlay** system:

**Core Benefits**:
1. **Quality Control**: Manual selection ensures high-quality, relevant imagery
2. **Licensing Clarity**: All images from verified CC0/Free sources
3. **Brand Consistency**: Automated text overlay ensures uniform branding
4. **Maintainability**: Python script makes updates easy (change text once, regenerate all)
5. **Scalability**: New pages automatically get appropriate category image via default catch-all
6. **Reduced Work**: 4 background images instead of 13 unique AI-generated images
7. **Environment Flexibility**: .env configuration supports dev/staging/production seamlessly
8. **No External Dependencies**: No reliance on AI services, subscriptions, or external tools
9. **Faster Iteration**: Regenerate all images in seconds vs. waiting for AI generation
10. **Cost Savings**: No ChatGPT Plus or Midjourney subscription required

---

## What This PRD Delivers

By completion, the project will have:
- ✅ `.env` file for environment-specific configuration (domain, analytics, email)
- ✅ `.env.example` template committed to git
- ✅ `python-dotenv` and `Pillow` dependencies added to requirements.txt
- ✅ 4 category-based background images downloaded and saved
- ✅ `generate_og_images.py` script that creates branded social sharing images
- ✅ 4 generated Open Graph images (1200x630px) with text overlay
- ✅ `.gitignore` updated to exclude environment-specific files
- ✅ Category-based image mapping ready for site generator integration

---

## Success Criteria

- [ ] Environment configuration system functional (`.env` file loaded correctly)
- [ ] 4 background images downloaded (CC0/Free license, 1200x630px minimum)
- [ ] `generate_og_images.py` script executes without errors
- [ ] 4 Open Graph images generated with correct dimensions (1200x630px)
- [ ] Text overlay renders correctly (white patent number, orange tagline)
- [ ] Images use Space Grotesk font (or system fallback)
- [ ] All environment-specific files excluded from git
- [ ] Documentation updated with image selection workflow

---

## Implementation Phases

### Phase 1: Environment Configuration Setup

**Duration**: 2-3 hours
**Outcome**: Environment-specific configuration system in place

#### 1.1 Create `.env.example` Template

**File**: `/website/.env.example`

**Content**:

```bash
# Environment
ENVIRONMENT=development

# Domain Configuration
SITE_DOMAIN=localhost
SITE_URL=http://localhost:8000

# Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
GOOGLE_ANALYTICS_ENABLED=false

# Contact
CONTACT_EMAIL=contact@example.com

# SEO
ROBOTS_INDEX=false
```

**Rationale**: This template provides a reference for developers to create their local `.env` file.

#### 1.2 Update `.gitignore`

**File**: `/website/.gitignore`

**Add these lines**:

```gitignore
# Environment configuration
.env

# Background images (downloaded locally, not committed)
assets/images/backgrounds/

# Generated Open Graph images (generated locally, not committed)
assets/images/og-*.jpg
```

**Rationale**: Environment-specific files and generated images should not be committed to git.

#### 1.3 Update `requirements.txt`

**File**: `/website/requirements.txt`

**Add these dependencies**:

```txt
python-dotenv==1.0.0
Pillow==10.1.0
```

**Install dependencies**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
pip install -r requirements.txt
```

#### 1.4 Create Local `.env` File

**File**: `/website/.env`

**Content** (for local development):

```bash
# Environment
ENVIRONMENT=development

# Domain Configuration
SITE_DOMAIN=localhost
SITE_URL=http://localhost:8000

# Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
GOOGLE_ANALYTICS_ENABLED=false

# Contact
CONTACT_EMAIL=contact@av-navigation-ip.com

# SEO
ROBOTS_INDEX=false
```

**Note**: This file is gitignored and will be created per environment.

---

### Phase 2: Background Image Selection & Download

**Duration**: 30-45 minutes
**Outcome**: 4 high-quality background images downloaded and verified

#### 2.1 Create Background Images Directory

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website
mkdir -p assets/images/backgrounds
```

#### 2.2 Download Background Images

**Platforms to use**:
- **Unsplash**: https://unsplash.com/ (100% free, no attribution required)
- **Pexels**: https://www.pexels.com/ (100% free, no attribution required)
- **Pixabay**: https://pixabay.com/ (Free for commercial use, CC0 license)

**Image Requirements**:
- **Dimensions**: 1200x630 pixels minimum (larger is okay, will be cropped)
- **Format**: JPG preferred (better compression)
- **License**: CC0 or Free for commercial use
- **Quality**: High resolution, professional photography
- **Style**: Clean, modern, tech-focused, not too busy (text overlay area should be clear)

---

#### Category A: Startup/Innovation

**File**: `startup-innovation.jpg`
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

#### Category B: Investment/Finance

**File**: `investment-finance.jpg`
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

#### Category C: Technical/Legal

**File**: `technical-legal.jpg`
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

#### Category D: General/Info (Default Catch-All)

**File**: `general-info.jpg`
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

#### 2.3 Image Search Workflow

**For each category**:

1. Go to Unsplash.com or Pexels.com
2. Search using primary query
3. Filter by "Most relevant" or "Popular"
4. Look for images with clear space in bottom 40% for text overlay
5. Verify image is at least 1200x630px (check dimensions before download)
6. Verify license: "Free to use" badge on image page
7. Download highest resolution available
8. Save as `[category].jpg` in `/website/assets/images/backgrounds/`

**Time estimate**: 5-10 minutes per category, 20-40 minutes total

#### 2.4 License Verification

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

### Phase 3: Python OG Image Generator Script

**Duration**: 2-3 hours
**Outcome**: Functional script that generates branded Open Graph images

#### 3.1 Create `generate_og_images.py` Script

**File**: `/website/generate_og_images.py`

**Complete Script**:

```python
#!/usr/bin/env python3
"""
Generate Open Graph social sharing images with text overlay.

This script takes background images from assets/images/backgrounds/ and overlays
branded text to create category-based Open Graph images (1200x630px).

Usage:
    python generate_og_images.py                        # Generate all 4 categories
    python generate_og_images.py --category startup     # Single category
    python generate_og_images.py --preview              # Display without saving
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    print("Error: Pillow library not installed. Run: pip install Pillow")
    sys.exit(1)

# Configuration
OG_IMAGE_SIZE = (1200, 630)
BACKGROUNDS_DIR = Path("assets/images/backgrounds")
OUTPUT_DIR = Path("assets/images")

# Category mapping
CATEGORIES = {
    "startup-innovation": {
        "background": "startup-innovation.jpg",
        "output": "og-startup-innovation.jpg",
    },
    "investment-finance": {
        "background": "investment-finance.jpg",
        "output": "og-investment-finance.jpg",
    },
    "technical-legal": {
        "background": "technical-legal.jpg",
        "output": "og-technical-legal.jpg",
    },
    "general-info": {
        "background": "general-info.jpg",
        "output": "og-general-info.jpg",
    },
}

# Text configuration
TEXT_LINE1 = "US PATENT 12,001,207 B2"
TEXT_LINE2 = "Camera-Based Navigation Safety"
TEXT_COLOR_LINE1 = (255, 255, 255)  # White
TEXT_COLOR_LINE2 = (230, 126, 34)   # Orange #e67e22
FONT_SIZE_LINE1 = 52
FONT_SIZE_LINE2 = 38


def get_font(size, bold=False):
    """Get font with system fallbacks."""
    # Try Space Grotesk (website brand font)
    font_paths = [
        "/System/Library/Fonts/Supplemental/SpaceGrotesk-Bold.ttf",
        "/System/Library/Fonts/Supplemental/SpaceGrotesk-Medium.ttf",
        "/usr/share/fonts/truetype/space-grotesk/SpaceGrotesk-Bold.ttf",
        "/usr/share/fonts/truetype/space-grotesk/SpaceGrotesk-Medium.ttf",
    ]

    # System fallbacks
    fallback_fonts = [
        "Arial-Bold.ttf" if bold else "Arial.ttf",
        "Helvetica-Bold.ttf" if bold else "Helvetica.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]

    all_fonts = font_paths + fallback_fonts

    for font_path in all_fonts:
        try:
            return ImageFont.truetype(font_path, size)
        except (IOError, OSError):
            continue

    # Last resort: default font
    return ImageFont.load_default()


def create_gradient_overlay(image, start_y_percent=0.6):
    """Create a dark gradient overlay on bottom portion of image."""
    width, height = image.size
    start_y = int(height * start_y_percent)

    # Create gradient
    gradient = Image.new('L', (1, height - start_y))
    for y in range(height - start_y):
        # Linear gradient from transparent (0) to dark (153 = 60% opacity)
        alpha = int(153 * (y / (height - start_y)))
        gradient.putpixel((0, y), alpha)

    gradient = gradient.resize((width, height - start_y), Image.Resampling.LANCZOS)

    # Create overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = Image.new('RGBA', (width, height - start_y), (0, 0, 0, 0))
    for y in range(height - start_y):
        for x in range(width):
            alpha = gradient.getpixel((x, y))
            overlay_draw.putpixel((x, y), (0, 0, 0, alpha))

    overlay.paste(overlay_draw, (0, start_y))

    return overlay


def generate_og_image(category_key, preview=False):
    """Generate Open Graph image for a category."""
    category = CATEGORIES[category_key]
    background_path = BACKGROUNDS_DIR / category["background"]
    output_path = OUTPUT_DIR / category["output"]

    # Check if background exists
    if not background_path.exists():
        print(f"Error: Background image not found: {background_path}")
        return False

    # Load and resize background
    print(f"Processing {category_key}...")
    img = Image.open(background_path).convert("RGB")

    # Resize to OG dimensions (crop from center if needed)
    img_width, img_height = img.size
    target_width, target_height = OG_IMAGE_SIZE
    aspect_ratio = target_width / target_height
    img_aspect_ratio = img_width / img_height

    if img_aspect_ratio > aspect_ratio:
        # Image is wider, crop width
        new_width = int(img_height * aspect_ratio)
        left = (img_width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img_height))
    else:
        # Image is taller, crop height
        new_height = int(img_width / aspect_ratio)
        top = (img_height - new_height) // 2
        img = img.crop((0, top, img_width, top + new_height))

    img = img.resize(OG_IMAGE_SIZE, Image.Resampling.LANCZOS)

    # Apply slight blur for text readability
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # Create gradient overlay
    overlay = create_gradient_overlay(img)
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

    # Add text overlay
    draw = ImageDraw.Draw(img)

    # Load fonts
    font_line1 = get_font(FONT_SIZE_LINE1, bold=True)
    font_line2 = get_font(FONT_SIZE_LINE2, bold=False)

    # Calculate text positions (centered, bottom 20% of image)
    width, height = img.size
    text_y_start = int(height * 0.68)

    # Line 1 (Patent number)
    bbox1 = draw.textbbox((0, 0), TEXT_LINE1, font=font_line1)
    text1_width = bbox1[2] - bbox1[0]
    text1_x = (width - text1_width) // 2
    text1_y = text_y_start

    # Add text shadow for readability
    shadow_offset = 2
    draw.text((text1_x + shadow_offset, text1_y + shadow_offset), TEXT_LINE1,
              font=font_line1, fill=(0, 0, 0, 128))
    draw.text((text1_x, text1_y), TEXT_LINE1, font=font_line1, fill=TEXT_COLOR_LINE1)

    # Line 2 (Tagline)
    bbox2 = draw.textbbox((0, 0), TEXT_LINE2, font=font_line2)
    text2_width = bbox2[2] - bbox2[0]
    text2_x = (width - text2_width) // 2
    text2_y = text1_y + 60

    draw.text((text2_x + shadow_offset, text2_y + shadow_offset), TEXT_LINE2,
              font=font_line2, fill=(0, 0, 0, 128))
    draw.text((text2_x, text2_y), TEXT_LINE2, font=font_line2, fill=TEXT_COLOR_LINE2)

    if preview:
        img.show()
        return True

    # Save output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "JPEG", quality=92, optimize=True)
    print(f"✓ Generated: {output_path}")

    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate Open Graph social sharing images")
    parser.add_argument("--category", choices=list(CATEGORIES.keys()),
                       help="Generate image for specific category only")
    parser.add_argument("--preview", action="store_true",
                       help="Display preview without saving")
    args = parser.parse_args()

    # Validate directories exist
    if not BACKGROUNDS_DIR.exists():
        print(f"Error: Backgrounds directory not found: {BACKGROUNDS_DIR}")
        print("Create it with: mkdir -p assets/images/backgrounds")
        return 1

    # Process categories
    if args.category:
        categories_to_process = [args.category]
    else:
        categories_to_process = list(CATEGORIES.keys())

    success_count = 0
    for category_key in categories_to_process:
        if generate_og_image(category_key, preview=args.preview):
            success_count += 1

    # Summary
    total = len(categories_to_process)
    if success_count == total:
        print(f"\n✓ Successfully generated {success_count}/{total} images")
        return 0
    else:
        print(f"\n✗ Generated {success_count}/{total} images ({total - success_count} failed)")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

#### 3.2 Test Script Execution

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website

# Test preview mode (displays without saving)
python generate_og_images.py --preview --category general-info

# Generate single category
python generate_og_images.py --category startup-innovation

# Generate all categories
python generate_og_images.py
```

**Expected output**:

```
Processing startup-innovation...
✓ Generated: assets/images/og-startup-innovation.jpg
Processing investment-finance...
✓ Generated: assets/images/og-investment-finance.jpg
Processing technical-legal...
✓ Generated: assets/images/og-technical-legal.jpg
Processing general-info...
✓ Generated: assets/images/og-general-info.jpg

✓ Successfully generated 4/4 images
```

#### 3.3 Verify Generated Images

**Check dimensions**:

```bash
cd /Users/sjsmit/Development/Caden/op_patent/website/assets/images
file og-*.jpg
```

**Expected output**: Each image should be 1200x630 pixels, JPEG format

**Visual inspection**:
- Open each generated image
- Verify text is readable (white patent number, orange tagline)
- Verify gradient overlay is applied to bottom 40%
- Verify background image is centered and cropped correctly

---

### Phase 4: Category Mapping Definition

**Duration**: 30 minutes
**Outcome**: Category mapping documented and ready for site generator integration

#### 4.1 Define Category Mapping

**This mapping will be added to `generate_site.py` in the main SEO PRD**:

```python
# Category-based Open Graph image mapping
OG_IMAGE_CATEGORIES = {
    'series-a-av-patent-portfolio-strategy': 'startup-innovation',
    'tesla-fsd-competitor-camera-patent-licensing': 'startup-innovation',
    'autonomous-trucking-patent-defense-strategy': 'startup-innovation',
    'venture-capital-av-patent-portfolio-due-diligence': 'investment-finance',
    'drone-delivery-patent-portfolio-pre-ipo': 'investment-finance',
    'patent-details': 'technical-legal',
    'licensing': 'technical-legal',
    # All other pages (index, industry-insights, contact, thank-you, about, disclaimer, privacy)
    # default to 'general-info' via DEFAULT_OG_CATEGORY
}
DEFAULT_OG_CATEGORY = 'general-info'
```

**Page to Category Mapping**:

| Category | Page Slugs | Count |
|----------|-----------|-------|
| **startup-innovation** | series-a-av-patent-portfolio-strategy, tesla-fsd-competitor-camera-patent-licensing, autonomous-trucking-patent-defense-strategy | 3 |
| **investment-finance** | venture-capital-av-patent-portfolio-due-diligence, drone-delivery-patent-portfolio-pre-ipo | 2 |
| **technical-legal** | patent-details, licensing | 2 |
| **general-info** (default) | index, industry-insights, contact, thank-you, about, disclaimer, privacy, *any new pages* | 6+ |

---

## Validation Checklist

After completing all phases:

### Environment Configuration ✅

- [ ] `.env.example` file created and committed to git
- [ ] `.env` file created locally (not committed)
- [ ] `.gitignore` updated to exclude `.env`, backgrounds, and generated images
- [ ] `requirements.txt` updated with `python-dotenv` and `Pillow`
- [ ] Dependencies installed successfully (`pip install -r requirements.txt`)

### Background Images ✅

- [ ] `assets/images/backgrounds/` directory created
- [ ] 4 background images downloaded:
  - [ ] `startup-innovation.jpg` (1200x630px minimum, CC0/Free license)
  - [ ] `investment-finance.jpg` (1200x630px minimum, CC0/Free license)
  - [ ] `technical-legal.jpg` (1200x630px minimum, CC0/Free license)
  - [ ] `general-info.jpg` (1200x630px minimum, CC0/Free license)
- [ ] All images verified for license (CC0 or Free for commercial use)
- [ ] All images have clear space in bottom 40% for text overlay

### OG Image Generator ✅

- [ ] `generate_og_images.py` script created
- [ ] Script executes without errors
- [ ] 4 Open Graph images generated:
  - [ ] `og-startup-innovation.jpg` (1200x630px, JPEG)
  - [ ] `og-investment-finance.jpg` (1200x630px, JPEG)
  - [ ] `og-technical-legal.jpg` (1200x630px, JPEG)
  - [ ] `og-general-info.jpg` (1200x630px, JPEG)
- [ ] Text overlay renders correctly:
  - [ ] Line 1: "US PATENT 12,001,207 B2" (white, bold, 52px)
  - [ ] Line 2: "Camera-Based Navigation Safety" (orange #e67e22, medium, 38px)
- [ ] Gradient overlay applied to bottom 40%
- [ ] Text has shadow for readability
- [ ] Script supports `--category` and `--preview` flags

### Documentation ✅

- [ ] Category mapping defined and documented
- [ ] Image search workflow documented (see Phase 2)
- [ ] License verification process documented
- [ ] CLI interface documented (usage examples in script docstring)

---

## Next Steps

After completing this refactoring PRD, proceed to the main SEO implementation PRD:
- **File**: `20251112_finish_seo_technical_implementation.md`
- **Start with**: Phase 1 (Open Graph & Twitter Card Implementation)
- **Dependencies**: This refactoring PRD must be complete before Phase 3 of the main SEO PRD

---

## Directory Structure After Completion

```
/website/
├── .env.example                    # Template (committed to git) ✅
├── .env                            # Local config (gitignored) ✅
├── .gitignore                      # Updated ✅
├── requirements.txt                # Updated with python-dotenv, Pillow ✅
├── generate_og_images.py           # New script ✅
├── assets/
│   └── images/
│       ├── backgrounds/            # Gitignored ✅
│       │   ├── startup-innovation.jpg       ✅
│       │   ├── investment-finance.jpg       ✅
│       │   ├── technical-legal.jpg          ✅
│       │   └── general-info.jpg             ✅
│       ├── og-startup-innovation.jpg        # Generated (gitignored) ✅
│       ├── og-investment-finance.jpg        # Generated (gitignored) ✅
│       ├── og-technical-legal.jpg           # Generated (gitignored) ✅
│       └── og-general-info.jpg              # Generated (gitignored) ✅
```

---

## Trade-offs & Considerations

**Advantages over AI Generation**:
- ✅ Better image quality and relevance (manual selection)
- ✅ Clear, unambiguous licensing (CC0/Free sources)
- ✅ No external service dependencies (no ChatGPT Plus/Midjourney)
- ✅ Consistent branding across all images (automated text overlay)
- ✅ Easier to update (regenerate vs. recreate)
- ✅ Faster workflow after initial setup
- ✅ No subscription costs

**Considerations**:
- ⚠️ Developer must manually select 4 background images (one-time ~30 min effort)
- ⚠️ Requires Pillow dependency (~10MB)
- ⚠️ Background images not in git (must be downloaded per environment)
- ⚠️ Text overlay is fixed (vs. custom text per AI image)

**Mitigation**: Comprehensive search queries provided for each category with 5+ alternatives each, clear selection criteria, and detailed image requirements. One-time setup effort pays off long-term.

---

## Document Metadata

**Document Status**: Active - Ready for Implementation
**Version**: 1.0
**Created**: November 12, 2025
**Last Updated**: November 12, 2025
**Estimated Completion**: November 14, 2025 (1-2 days)
**Owner**: Developer (Team Member)
**Priority**: High
**Blocks**: Main SEO implementation (Phase 3)

**Related Documents**:
- `20251112_finish_seo_technical_implementation.md` - Main SEO PRD (blocked until this is complete)
- `20251110_production_readiness_prd.md` - Parent PRD (Milestone 3)

---

**END OF PRD**
