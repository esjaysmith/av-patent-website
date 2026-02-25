# Next Page Navigation Feature Design

**Date:** 2025-12-09
**Status:** Approved for Implementation

## Overview

Add a circular "Next Page →" navigation button to all pages, allowing users to browse through all site content sequentially. The navigation order is deterministic, defined in a single source of truth, and forms a complete loop.

## Requirements

1. **Universal Coverage:** Every page gets a next page button (homepage, landing pages, utility pages, etc.)
2. **Circular Navigation:** Clicking through all pages returns to the starting point
3. **Deterministic Order:** Pages follow a defined sequence that guides users through key content
4. **Single Source of Truth:** Page order defined once in `generate_site.py`, used for both sitemap and navigation
5. **Validation:** Build fails if a new page is created but not added to the page order list
6. **Visual Placement:** Button appears at end of content, right-aligned
7. **Server-Side:** Next page URL injected during build time (no JavaScript required)

## Design

### 1. Page Order Definition

Add a module-level constant in `generate_site.py`:

```python
PAGE_ORDER = [
    'index.html',           # Homepage - entry point
    'patent-details.html',  # Core patent information
    'licensing.html',       # How to license

    # Landing pages - use case scenarios
    'autonomous-trucking-patent-defense-strategy.html',
    'venture-capital-av-patent-portfolio-due-diligence.html',
    'series-a-av-patent-portfolio-strategy.html',
    'drone-delivery-patent-portfolio-pre-ipo.html',
    'tesla-fsd-competitor-camera-patent-licensing.html',

    # Information pages
    'industry-insights.html',
    'about.html',

    # Utility pages
    'contact.html',
    'privacy.html',
    'disclaimer.html',
    'thank-you.html',
]
```

This list defines:
- The exact order pages appear in sitemap.xml
- The sequence for next-page navigation
- The complete inventory of site pages

### 2. Navigation Logic

**Circular Navigation Algorithm:**
```python
def get_next_page_url(self, current_page_filename):
    """Get the next page URL in the circular navigation"""
    try:
        current_index = PAGE_ORDER.index(current_page_filename)
        next_index = (current_index + 1) % len(PAGE_ORDER)
        next_filename = PAGE_ORDER[next_index]

        # Return relative URL
        if next_filename == 'index.html':
            return '/'
        else:
            return f'/{next_filename}'
    except ValueError:
        return None  # Fallback if page not in order
```

**Key Points:**
- Uses modulo operator for wrap-around: `(i + 1) % len(PAGE_ORDER)`
- Returns relative URLs (`/` or `/page.html`)
- Handles edge case of missing pages gracefully

### 3. Sitemap Generation Changes

**Refactor `generate_sitemap()` method:**

Current implementation:
```python
def generate_sitemap(self, generated_pages):
    # Iterates through generated_pages in arbitrary order
```

New implementation:
```python
def generate_sitemap(self):
    """Generate sitemap.xml using PAGE_ORDER"""
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    base_url = SITE_URL

    for page_filename in PAGE_ORDER:
        if page_filename == 'index.html':
            url = base_url + '/'
        else:
            url = f"{base_url}/{page_filename}"

        sitemap_content += f'''    <url>
        <loc>{url}</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
'''

    sitemap_content += '</urlset>'

    sitemap_path = self.build_dir / 'sitemap.xml'
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated sitemap: {sitemap_path}")
```

**Changes:**
- Remove `generated_pages` parameter
- Iterate through `PAGE_ORDER` instead
- Sitemap now reflects the defined user journey

### 4. Page Generation Changes

**Modify `generate_page()` method:**

Add next page URL to template variables:

```python
def generate_page(self, md_file_path, output_filename=None):
    # ... existing code ...

    template_vars = {
        # ... existing vars ...
        'next_page_url': self.get_next_page_url(output_filename),
    }

    # ... rest of method ...
```

**Update `build_site()` method call:**

Change from:
```python
self.generate_sitemap(generated_pages)
```

To:
```python
self.generate_sitemap()
```

### 5. Validation Logic

Add validation to `build_site()` after page generation loop:

```python
# After processing all markdown files
generated_filenames = {page.name for page in generated_pages}
expected_filenames = set(PAGE_ORDER)

# Check for pages not in PAGE_ORDER (ERROR)
extra_pages = generated_filenames - expected_filenames
if extra_pages:
    error_msg = (
        f"❌ ERROR: Pages generated but not in PAGE_ORDER:\n"
        f"   {', '.join(sorted(extra_pages))}\n\n"
        f"   Add these pages to PAGE_ORDER in generate_site.py"
    )
    print(error_msg)
    raise ValueError(error_msg)

# Check for missing pages (WARNING)
missing_pages = expected_filenames - generated_filenames
if missing_pages:
    print(f"⚠️  Warning: Pages in PAGE_ORDER but not generated: {', '.join(sorted(missing_pages))}")
```

**Error Cases:**
- **Extra pages:** Build fails - developer must add page to `PAGE_ORDER`
- **Missing pages:** Build warns but continues - page might not exist yet

### 6. Template Changes

**Update `page.html` template:**

Add next page button at the end of the main content section, after the optional CTA:

```html
{% if show_cta %}
<div class="cta-section">
    <h3>Ready to License US Patent 12,001,207?</h3>
    <p>Contact us to discuss licensing opportunities for your autonomous vehicle or drone navigation projects.</p>
    <a href="/contact.html" class="cta-button">GET IN TOUCH</a>
</div>
{% endif %}

<!-- Next Page Navigation -->
{% if next_page_url %}
<div class="next-page-navigation">
    <a href="{{ next_page_url }}" class="next-page-button">Next Page →</a>
</div>
{% endif %}
```

**Placement Logic:**
- Appears after all content and CTA section
- Still within `.content-wrapper` div
- Only shows if `next_page_url` is defined (safety check)

### 7. Styling

**Add to existing CSS (in base.html or separate stylesheet):**

```css
.next-page-navigation {
    margin-top: 60px;
    text-align: right;
    padding-top: 40px;
    border-top: 1px solid #e2e8f0;
}

.next-page-button {
    display: inline-block;
    padding: 12px 24px;
    background-color: #e67e22;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 500;
    transition: background-color 0.3s ease;
}

.next-page-button:hover {
    background-color: #d35400;
    color: white;
}

.next-page-button:focus {
    outline: 2px solid #e67e22;
    outline-offset: 2px;
}

/* Responsive: full width on mobile */
@media (max-width: 768px) {
    .next-page-navigation {
        text-align: center;
    }

    .next-page-button {
        display: block;
        width: 100%;
        text-align: center;
    }
}
```

**Design Notes:**
- Uses site's primary orange color (`#e67e22`)
- Border separator distinguishes navigation from content
- Hover state provides feedback
- Focus outline for accessibility
- Mobile responsive: centered, full-width button

## Implementation Steps

1. **Add PAGE_ORDER constant** to `generate_site.py`
2. **Add get_next_page_url() method** to StaticSiteGenerator class
3. **Refactor generate_sitemap()** to use PAGE_ORDER instead of generated_pages parameter
4. **Update generate_page()** to inject next_page_url into template variables
5. **Add validation logic** to build_site() method
6. **Update build_site()** to call generate_sitemap() without parameters
7. **Update page.html template** to include next page button HTML
8. **Add CSS styling** for next-page-navigation components
9. **Test build process** and verify all pages have correct next links
10. **Test circular navigation** by clicking through all pages

## Testing

**Manual Testing:**
1. Run `python generate_site.py`
2. Open `build/index.html` in browser
3. Click "Next Page →" button repeatedly through all 14 pages
4. Verify you return to homepage after thank-you.html
5. Check that button appears on all pages
6. Test mobile responsive layout

**Validation Testing:**
1. Create a new markdown file without adding to PAGE_ORDER
2. Run build - should fail with clear error message
3. Add page to PAGE_ORDER - build should succeed

**Sitemap Testing:**
1. Check `build/sitemap.xml` reflects PAGE_ORDER sequence
2. Verify URLs are correctly formatted

## Edge Cases

1. **Page not in PAGE_ORDER:** Returns `None`, button won't render (safety check in template)
2. **Empty PAGE_ORDER:** Would cause modulo by zero - but this is a configuration error
3. **Missing markdown file:** Build continues with warning, page excluded from navigation
4. **Extra markdown file:** Build fails with error, forces developer to update PAGE_ORDER

## Future Enhancements

Potential improvements not included in initial design:
- Add "Previous Page" button on the left
- Show next page title as preview
- Add page counter (e.g., "Page 5 of 14")
- Skip utility pages option (toggle in URL param)

## Files Modified

- `website/generate_site.py` - Core logic changes
- `website/designs/default/page.html` - Template changes
- `website/designs/default/base.html` (or CSS file) - Styling changes

## Migration Notes

This is a new feature with no breaking changes:
- Existing pages continue to work
- Sitemap order changes from arbitrary to intentional
- No user-facing breaking changes
