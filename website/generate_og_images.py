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
