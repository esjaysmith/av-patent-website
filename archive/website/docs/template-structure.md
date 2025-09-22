# Template Structure Guidelines

## HTML Template Structure

All HTML pages should follow this basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Meta tags from config/meta-tags.html -->
  <title>Page Title | Autonomous Driving Patents</title>

  <!-- Stylesheets -->
  <link rel="stylesheet" href="/assets/css/main.css">

  <!-- Analytics -->
  <script src="/assets/js/analytics.js"></script>
</head>
<body>
  <!-- Header/Navigation -->
  <header>
    <!-- Navigation menu -->
  </header>

  <!-- Main Content -->
  <main>
    <!-- Page-specific content -->
  </main>

  <!-- Footer -->
  <footer>
    <!-- Footer content -->
  </footer>

  <!-- Scripts -->
  <script src="/assets/js/main.js"></script>
</body>
</html>
```

## Page Types

### Homepage Template
- Hero section with value proposition
- Key benefits/features
- Call-to-action buttons
- Testimonials/social proof
- Contact form

### Core Page Template
- Page header with title and description
- Main content sections
- Related links
- Contact CTA

### Blog/Landing Page Template
- Article header with title, date, author
- Table of contents
- Content sections with headings
- Internal links
- Related articles
- Social sharing buttons

### Form Template
- Form header
- Form fields with labels
- Validation messages
- Submit button
- Success/error messages

## CSS Architecture

### Base Styles
- Reset/normalize
- Typography
- Color variables
- Spacing utilities

### Component Styles
- Buttons
- Forms
- Cards
- Navigation
- Footer

### Layout Styles
- Grid system
- Responsive breakpoints
- Container utilities

## JavaScript Structure

### Main Script
- DOM ready handler
- Event listeners
- Form validation
- Interactive features

### Module Organization
- Separate files for different functionalities
- Use IIFE or ES6 modules
- Avoid global scope pollution

## Responsive Design

- Mobile-first approach
- Breakpoints: 768px, 1024px, 1200px
- Flexible images and media
- Touch-friendly interactions

## Performance Considerations

- Minimize DOM manipulation
- Use event delegation
- Lazy load images
- Optimize CSS/JS delivery