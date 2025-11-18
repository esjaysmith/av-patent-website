# Cookie Consent Modal Design

**Date:** November 18, 2025
**Status:** Design Complete, Ready for Implementation
**Project:** AV Navigation IP Protection Website

## Overview

A minimal, privacy-first cookie consent modal for the AV Navigation IP Protection website that appears at the bottom of the page, allows users to accept analytics cookies or learn more, and remembers their choice for 30 days.

## Design Requirements

### Functional Requirements
- **Minimal compliance:** Inform users about Google Analytics cookies with simple accept mechanism
- **Privacy-first:** Only load Google Analytics after explicit user consent
- **Persistent consent:** Remember user choice for 30 days via localStorage
- **Non-blocking:** Page content remains fully readable when modal is visible
- **Transparent:** Provide "Learn More" link to privacy policy

### User Experience Requirements
- Bottom-of-page placement (least intrusive, familiar pattern)
- Smooth animations (slide-up entrance, fade-out exit)
- Mobile responsive (stacks vertically on small screens)
- Matches existing site design system (glass morphism, orange accents)

## User Experience Flow

### First Visit
1. User lands on any page
2. Cookie consent modal slides up from bottom after 500ms delay
3. Page content remains fully readable - modal is non-blocking overlay at bottom
4. User sees two options: "Accept" or "Learn More"
5. **If user clicks "Accept":**
   - Modal fades out smoothly
   - Google Analytics loads dynamically
   - Consent stored in localStorage with timestamp
6. **If user clicks "Learn More":**
   - Privacy policy opens in new tab
   - Modal remains visible
7. **If user ignores modal:**
   - Modal stays visible but doesn't block content
   - Google Analytics does NOT load (privacy-safe default)

### Return Visits (within 30 days)
- No modal shown if previously accepted
- Google Analytics loads automatically
- Seamless experience for returning users

### Return Visits (after 30 days)
- Modal appears again to re-confirm consent
- Old consent timestamp cleared from localStorage
- User must accept again to enable tracking

## Technical Implementation

### Files to Modify

**`/website/designs/default/base.html`**
- Remove existing inline Google Analytics block (lines 31-40)
- Add cookie consent HTML structure (before closing `</body>`)
- Add cookie consent CSS (within existing `<style>` block)
- Add JavaScript functions for consent management

### HTML Structure

```html
<!-- Cookie Consent Modal -->
<div id="cookieConsent" class="cookie-consent">
  <div class="container">
    <div class="cookie-content">
      <div class="cookie-text">
        <p>We use cookies to analyze site traffic and improve your experience. By clicking "Accept", you consent to our use of cookies.</p>
      </div>
      <div class="cookie-actions">
        <a href="/privacy.html" target="_blank" class="btn-learn-more">Learn More</a>
        <button onclick="acceptCookies()" class="btn-accept">Accept</button>
      </div>
    </div>
  </div>
</div>
```

**Placement:** Just before closing `</body>` tag (after existing scripts, around line 766)

### CSS Styling

```css
/* Cookie Consent Modal */
.cookie-consent {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-top: 1px solid rgba(226, 126, 34, 0.2);
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1);
    transform: translateY(100%);
    opacity: 0;
    transition: transform 0.4s ease-out, opacity 0.4s ease-out;
    display: block;
}

.cookie-consent.visible {
    transform: translateY(0);
    opacity: 1;
}

.cookie-consent.hiding {
    transform: translateY(100%);
    opacity: 0;
}

.cookie-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 25px 0;
    gap: 30px;
}

.cookie-text p {
    margin: 0;
    font-size: 15px;
    color: #4a5568;
    line-height: 1.6;
}

.cookie-actions {
    display: flex;
    gap: 15px;
    align-items: center;
    flex-shrink: 0;
}

.btn-accept {
    background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
    color: white;
    padding: 12px 28px;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(230, 126, 34, 0.25);
}

.btn-accept:hover {
    background: linear-gradient(135deg, #d35400 0%, #bf4708 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(230, 126, 34, 0.35);
}

.btn-learn-more {
    color: #e67e22;
    text-decoration: none;
    font-weight: 500;
    font-size: 15px;
    transition: color 0.3s ease;
}

.btn-learn-more:hover {
    color: #d35400;
    text-decoration: underline;
}

/* Responsive: Stack vertically on mobile */
@media (max-width: 768px) {
    .cookie-content {
        flex-direction: column;
        align-items: flex-start;
        padding: 20px 0;
        gap: 20px;
    }

    .cookie-actions {
        width: 100%;
        justify-content: space-between;
    }

    .btn-accept {
        flex: 1;
    }
}
```

**Placement:** Within existing `<style>` block (before line 590)

**Design Characteristics:**
- **Glass morphism:** Matches navbar with `backdrop-filter: blur(20px)`
- **Orange accent:** Uses site color scheme `#e67e22`
- **Z-index 999:** Below navbar (1000), above all content
- **Height:** ~95-120px depending on content
- **Shadow:** Upward shadow for depth
- **Animations:** 400ms transitions with easing

### JavaScript Implementation

```javascript
// Cookie Consent Management
function loadGoogleAnalytics() {
    if (!window.gaLoaded && '{{ google_analytics_enabled }}' === 'True') {
        const gaId = '{{ google_analytics_id }}';

        // Create and inject GA script
        const script1 = document.createElement('script');
        script1.async = true;
        script1.src = `https://www.googletagmanager.com/gtag/js?id=${gaId}`;
        document.head.appendChild(script1);

        // Initialize GA
        const script2 = document.createElement('script');
        script2.textContent = `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '${gaId}');
        `;
        document.head.appendChild(script2);
        window.gaLoaded = true;
    }
}

function checkCookieConsent() {
    const consent = localStorage.getItem('cookieConsent');
    if (consent) {
        const consentDate = new Date(consent);
        const now = new Date();
        const daysDiff = (now - consentDate) / (1000 * 60 * 60 * 24);

        if (daysDiff < 30) {
            // Consent still valid
            loadGoogleAnalytics();
            return; // Don't show modal
        } else {
            // Consent expired, remove old consent
            localStorage.removeItem('cookieConsent');
        }
    }

    // Show modal after delay
    setTimeout(() => {
        const modal = document.getElementById('cookieConsent');
        if (modal) {
            modal.classList.add('visible');
        }
    }, 500);
}

function acceptCookies() {
    // Store consent timestamp
    localStorage.setItem('cookieConsent', new Date().toISOString());

    // Load analytics
    loadGoogleAnalytics();

    // Hide modal
    const modal = document.getElementById('cookieConsent');
    modal.classList.add('hiding');
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300);
}

// Run on page load
document.addEventListener('DOMContentLoaded', checkCookieConsent);
```

**Placement:** Within existing `<script>` block (before line 726, after existing functions)

**Key Functions:**
1. **`checkCookieConsent()`** - Runs on DOMContentLoaded, checks localStorage, shows modal if needed
2. **`acceptCookies()`** - Stores consent timestamp, loads GA, hides modal
3. **`loadGoogleAnalytics()`** - Dynamically injects GA scripts after consent

**Logic Flow:**
- Check localStorage for `cookieConsent` key
- If exists and < 30 days old → Load GA, hide modal
- If exists and ≥ 30 days old → Clear consent, show modal
- If doesn't exist → Show modal after 500ms delay
- On accept → Store ISO timestamp, load GA, animate modal out

### Modified Google Analytics Loading

**Current Behavior (base.html lines 31-40):**
```html
{% if google_analytics_enabled %}
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ google_analytics_id }}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '{{ google_analytics_id }}');
</script>
{% endif %}
```

**New Behavior:**
- **REMOVE** the inline GA block entirely
- GA scripts loaded dynamically via `loadGoogleAnalytics()` after consent
- Template variables (`google_analytics_enabled`, `google_analytics_id`) still used in JavaScript
- Privacy-first: No tracking without explicit consent

## Edge Cases & Handling

### 1. Rapid Page Navigation
- Modal won't flash on every page load after consent
- `checkCookieConsent()` runs on each page but respects localStorage
- GA script only injected once via `window.gaLoaded` flag

### 2. Multiple Browser Tabs
- localStorage shared across tabs in same domain
- Consent in one tab applies to all tabs
- New tabs opened after consent won't show modal

### 3. Browser Privacy Modes
- Incognito/Private browsing: localStorage cleared on session end
- Modal appears each new private session (expected behavior)
- No persistent tracking in private mode (privacy-respecting)

### 4. JavaScript Disabled
- Modal won't appear (graceful degradation)
- GA won't load (privacy-safe default)
- Site remains fully functional

### 5. Ad Blockers
- May block GA even after consent (user's choice respected)
- Modal functions normally
- No JavaScript errors thrown if GA blocked

### 6. Old Browsers
- localStorage supported in IE8+ (sufficient coverage)
- `backdrop-filter` has fallback with solid background color
- CSS animations degrade gracefully

## Testing Checklist

### Functional Testing
- [ ] First visit → Modal appears after 500ms
- [ ] First visit → GA not loaded before consent
- [ ] Click "Accept" → Modal disappears, GA loads
- [ ] Click "Accept" → localStorage contains timestamp
- [ ] Refresh page after accept → No modal, GA loads automatically
- [ ] Clear localStorage → Modal appears again
- [ ] Click "Learn More" → Privacy policy opens in new tab
- [ ] Click "Learn More" → Modal remains visible
- [ ] Ignore modal → Page content fully readable
- [ ] Ignore modal → GA not loaded

### 30-Day Expiration Testing
- [ ] Set consent timestamp to 29 days ago → No modal, GA loads
- [ ] Set consent timestamp to 30 days ago → Modal appears
- [ ] Set consent timestamp to 31 days ago → Modal appears, old consent cleared

### Responsive Testing
- [ ] Desktop (1200px+) → Horizontal layout
- [ ] Tablet (768px-1199px) → Horizontal layout
- [ ] Mobile (<768px) → Vertical stack layout
- [ ] Mobile buttons → Easily tappable (44px+ height)

### Browser Testing
- [ ] Chrome (desktop/mobile)
- [ ] Firefox (desktop/mobile)
- [ ] Safari (desktop/iOS)
- [ ] Edge (desktop)

### Visual Testing
- [ ] Modal matches site design system
- [ ] Glass morphism effect renders correctly
- [ ] Animations smooth on all browsers
- [ ] Content not blocked by modal
- [ ] Buttons have proper hover states
- [ ] Text readable with good contrast

### Integration Testing
- [ ] Works on all existing pages (index, patent-details, licensing, etc.)
- [ ] Doesn't interfere with existing JavaScript
- [ ] Doesn't break mobile navigation
- [ ] Footer remains accessible

## Privacy Policy Updates

The `/privacy.html` page should include a section on cookies with:

**Required Content:**
- **What cookies are used:** Google Analytics cookies
- **Purpose:** Analyze site traffic and improve user experience
- **Data collected:** Anonymized usage patterns, page views, session duration
- **Retention period:** Google's standard retention (defaults to 26 months)
- **User rights:** Can decline consent, clear cookies anytime
- **Third-party processor:** Google LLC (link to Google's privacy policy)
- **How to manage:** Browser cookie settings, localStorage clearing

**Example Section:**
```markdown
## Cookies and Tracking

### What Cookies We Use
This website uses Google Analytics cookies to analyze site traffic and improve your experience.

### Data Collected
We collect anonymized usage data including:
- Pages visited
- Time spent on site
- Geographic region (country/city level)
- Device type and browser

### Your Choices
- You can decline cookie consent when prompted
- You can clear your consent by clearing browser data
- You can block cookies in browser settings
- Declining cookies does not affect site functionality

### Third-Party Processor
Google Analytics is operated by Google LLC. See [Google's Privacy Policy](https://policies.google.com/privacy).
```

## Future Enhancement Opportunities

### If Adding More Cookie Categories
The current structure supports expansion to multi-category consent:

**Potential Categories:**
- **Necessary:** Site functionality (always allowed, no consent needed)
- **Analytics:** Google Analytics (current implementation)
- **Marketing:** Future ad tracking, retargeting
- **Preferences:** User settings, language preferences

**Implementation Path:**
- Add "Manage Preferences" button
- Create modal overlay with category toggles
- Expand localStorage schema: `{ necessary: true, analytics: true, marketing: false }`
- Conditional script loading per category

### Analytics Provider Changes
If switching from Google Analytics:

**Modification Points:**
- Update `loadGoogleAnalytics()` function name and implementation
- Update privacy policy text
- Template variables in `generate_site.py` remain the same pattern

**Potential Alternatives:**
- Plausible Analytics (privacy-focused, no consent needed in EU)
- Matomo (self-hosted option)
- Simple Analytics (GDPR-compliant by default)

### Configurable Expiration Period
Currently hardcoded to 30 days, can be made configurable:

```javascript
const CONSENT_EXPIRY_DAYS = 30; // Make this a constant
const daysDiff = (now - consentDate) / (1000 * 60 * 60 * 24);
if (daysDiff < CONSENT_EXPIRY_DAYS) {
    // Consent still valid
}
```

## Implementation Timeline

**Estimated Time:** 2-3 hours

**Steps:**
1. **Backup current base.html** (5 min)
2. **Remove existing GA block** (2 min)
3. **Add CSS to style block** (10 min)
4. **Add HTML structure** (5 min)
5. **Add JavaScript functions** (15 min)
6. **Local testing** (30 min)
   - Test consent flow
   - Test 30-day expiration (manual timestamp editing)
   - Test responsive layout
   - Test GA loading
7. **Cross-browser testing** (30 min)
8. **Update privacy policy** (20 min)
9. **Generate and deploy** (10 min)

**Total:** ~2 hours active work

## Success Criteria

### User Experience
- ✅ Modal appears on first visit, not on subsequent visits (within 30 days)
- ✅ Page content remains fully readable when modal is visible
- ✅ Smooth animations enhance professionalism
- ✅ Mobile layout is clean and usable

### Privacy Compliance
- ✅ No tracking occurs before user consent
- ✅ Consent is stored and respected for 30 days
- ✅ User can learn more via privacy policy link
- ✅ Clear communication about cookie usage

### Technical Quality
- ✅ No JavaScript errors in console
- ✅ Works across all major browsers
- ✅ Responsive on all screen sizes
- ✅ Doesn't interfere with existing functionality

### Business Goals
- ✅ Maintains professional appearance of site
- ✅ Demonstrates respect for user privacy
- ✅ Enables analytics for business intelligence
- ✅ Provides legal cover for cookie usage

## Maintenance Notes

### localStorage Key
- **Key:** `cookieConsent`
- **Value:** ISO 8601 timestamp string (e.g., `"2025-11-18T10:30:00.000Z"`)
- **Lifetime:** Persistent until cleared by user or 30-day expiration

### Analytics Loading Flag
- **Flag:** `window.gaLoaded` (boolean)
- **Purpose:** Prevent duplicate GA script injection on SPAs
- **Scope:** Window object (cleared on page reload)

### Template Variables Used
- `{{ google_analytics_enabled }}` - Boolean from generate_site.py
- `{{ google_analytics_id }}` - GA measurement ID from config

### CSS Class Names
- `.cookie-consent` - Main container
- `.cookie-consent.visible` - Shown state
- `.cookie-consent.hiding` - Dismissing animation
- `.cookie-content` - Flex wrapper
- `.cookie-text` - Text content area
- `.cookie-actions` - Button container
- `.btn-accept` - Accept button
- `.btn-learn-more` - Privacy policy link

## References

- **GDPR Compliance:** [EU Cookie Law](https://gdpr.eu/cookies/)
- **Google Analytics:** [GA4 Documentation](https://developers.google.com/analytics/devguides/collection/ga4)
- **localStorage API:** [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- **CSS backdrop-filter:** [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)

---

**Design Status:** Complete and ready for implementation
**Next Steps:** Implementation in base.html template
**Estimated Effort:** 2-3 hours including testing
