# Milestone 2: Contact Form Testing & Integration

## Task Information
- **Parent PRD**: `20251110_production_readiness_prd.md`
- **Milestone**: 2 of 6
- **Priority**: Critical (Launch Blocker)
- **Duration**: 1-2 days
- **Status**: Not Started
- **Dependencies**: None (can run parallel with Milestone 1)
- **Blocks**: Milestone 5 (Production Deployment)

## Overview

Test and configure the contact form to ensure it validates input, submits successfully, and delivers inquiries. Simplify the form if needed, add spam protection, and verify mobile functionality.

**Problem**: Contact form may not be functional. Unknown if submissions work or where they're delivered.

**Solution**: Test thoroughly, integrate with Formspree or Netlify Forms, add validation and spam protection.

## Deliverables

### 1. Form Validation Testing
- Test required field validation (name, email, message)
- Test email format validation
- Test privacy policy checkbox requirement
- Test error message display

### 2. Form Submission Testing
- Configure form action endpoint (Formspree or Netlify Forms)
- Test successful submission
- Verify email delivery or notification
- Verify redirect to thank-you page

### 3. Form Simplification
- Remove unnecessary fields (keep: name, email, company optional, message)
- Add privacy policy checkbox
- Add honeypot spam protection
- Ensure mobile-friendly input sizes

### 4. Spam Protection
- Honeypot field (hidden input)
- Consider CAPTCHA (optional, only if spam becomes issue)

## Recommended Form HTML

```html
<form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <div class="mb-3">
    <label for="name" class="form-label">Name *</label>
    <input type="text" class="form-control" id="name" name="name" required>
  </div>
  <div class="mb-3">
    <label for="email" class="form-label">Email *</label>
    <input type="email" class="form-control" id="email" name="email" required>
  </div>
  <div class="mb-3">
    <label for="company" class="form-label">Company</label>
    <input type="text" class="form-control" id="company" name="company">
  </div>
  <div class="mb-3">
    <label for="message" class="form-label">Message *</label>
    <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="privacy" name="privacy" required>
    <label class="form-check-label" for="privacy">
      I agree to the <a href="/privacy.html" target="_blank">Privacy Policy</a> *
    </label>
  </div>
  <!-- Honeypot for spam protection -->
  <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
  <button type="submit" class="btn btn-primary btn-lg">Submit Inquiry</button>
</form>
```

## Form Service Setup

### Option 1: Formspree (Recommended)

**Setup Steps**:
1. Go to https://formspree.io/
2. Sign up for free account
3. Create new form
4. Get form endpoint URL: `https://formspree.io/f/YOUR_FORM_ID`
5. Update form `action` attribute in `contact.md`
6. Configure form settings:
   - Add email recipient
   - Enable confirmation emails (optional)
   - Set redirect URL to `/thank-you.html`

**Free Tier**: 50 submissions/month

### Option 2: Netlify Forms

**Setup Steps** (if deploying to Netlify):
1. Add `netlify` or `data-netlify="true"` attribute to `<form>` tag
2. Add hidden input: `<input type="hidden" name="form-name" value="contact" />`
3. Deploy to Netlify (auto-detects form)
4. Configure notifications in Netlify dashboard

**Free Tier**: 100 submissions/month

## Testing Protocol

### Validation Tests
1. **Empty form submission**:
   - Expected: Error messages for required fields
   - Test: Click submit without filling any fields

2. **Invalid email format**:
   - Expected: Error message "Please enter a valid email"
   - Test: Enter "notanemail" in email field, submit

3. **Missing privacy checkbox**:
   - Expected: Error message or browser validation
   - Test: Fill form but don't check privacy box, submit

### Submission Tests
1. **Successful submission**:
   - Fill all required fields with valid data
   - Check privacy checkbox
   - Click submit
   - Expected: Redirect to `/thank-you.html`
   - Expected: Email received (check spam folder)

2. **Honeypot test**:
   - Manually fill hidden `_gotcha` field
   - Submit form
   - Expected: Form appears to submit but no email sent (spam protection working)

### Mobile Tests
1. Open form on mobile device (iPhone, Android)
2. Test keyboard input for each field
3. Test form submission on mobile
4. Verify thank-you page loads on mobile

## Acceptance Criteria

### Functionality
- [ ] Form validates required fields (name, email, message)
- [ ] Form validates email format
- [ ] Form requires privacy policy checkbox
- [ ] Form submits successfully with valid data
- [ ] Email delivered to configured recipient (or Formspree notification)
- [ ] Redirect to `/thank-you.html` after submission
- [ ] Honeypot spam protection working

### UX
- [ ] Error messages clear and helpful
- [ ] Form inputs appropriately sized (44px+ height for mobile)
- [ ] Privacy policy link opens in new tab
- [ ] Submit button clearly labeled
- [ ] Form accessible via keyboard navigation

### Mobile
- [ ] Form fully functional on iPhone Safari
- [ ] Form fully functional on Android Chrome
- [ ] Input fields trigger appropriate keyboards (email keyboard for email field)
- [ ] Form does not cause horizontal scrolling

## Implementation Steps

1. **Review current form** in `/website/content/contact.md`
2. **Simplify form** if needed (use recommended HTML above)
3. **Sign up for Formspree** (or configure Netlify Forms)
4. **Update form action** with Formspree endpoint
5. **Add honeypot field** for spam protection
6. **Add privacy checkbox** with link to privacy policy
7. **Regenerate site**: `python generate_site.py`
8. **Test validation** (empty fields, invalid email)
9. **Test submission** (fill form, submit, check email)
10. **Test on mobile** (iPhone, Android)

## Files to Modify

- `/website/content/contact.md` - Form HTML
- `/website/content/thank-you.md` - Confirmation page (verify exists)

## Success Metrics

- Form validates 100% of test cases
- Form submits successfully in all browsers
- Email delivered within 1 minute of submission
- Zero false positives from spam protection
- 100% mobile usability

---

**Status**: Not Started
**Created**: November 10, 2025
**Priority**: Critical
**Estimated Effort**: 1-2 days
