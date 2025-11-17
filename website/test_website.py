#!/usr/bin/env python3
"""
Website Testing Script using Playwright
Tests the generated static website for functionality, SEO, and accessibility
"""

import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright
import sys

class WebsiteValidator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.build_dir = self.base_dir / "build"
        self.test_results = []

    async def setup_browser(self):
        """Initialize Playwright browser"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def cleanup_browser(self):
        """Cleanup Playwright resources"""
        await self.browser.close()
        await self.playwright.stop()

    def log_test(self, test_name, status, message=""):
        """Log test result"""
        result = {
            "test": test_name,
            "status": status,
            "message": message
        }
        self.test_results.append(result)
        status_emoji = "✅" if status == "PASS" else "❌"
        print(f"{status_emoji} {test_name}: {message}")

    async def test_file_existence(self):
        """Test that all required files exist"""
        print("\n🔍 Testing File Existence...")

        required_files = [
            "index.html",
            "patent-details.html",
            "licensing.html",
            "industry-insights.html",
            "contact.html",
            "thank-you.html",
            "sitemap.xml",
            "robots.txt"
        ]

        for file in required_files:
            file_path = self.build_dir / file
            if file_path.exists():
                self.log_test(f"File exists: {file}", "PASS")
            else:
                self.log_test(f"File exists: {file}", "FAIL", f"Missing: {file_path}")

    async def test_page_loading(self):
        """Test that all pages load without errors"""
        print("\n🌐 Testing Page Loading...")

        pages = [
            ("Homepage", "index.html"),
            ("Patent Details", "patent-details.html"),
            ("Licensing", "licensing.html"),
            ("Industry Insights", "industry-insights.html"),
            ("Contact", "contact.html"),
            ("Thank You", "thank-you.html")
        ]

        for page_name, file_name in pages:
            file_path = self.build_dir / file_name
            if file_path.exists():
                try:
                    await self.page.goto(f"file://{file_path.absolute()}")
                    title = await self.page.title()
                    if title:
                        self.log_test(f"Page loads: {page_name}", "PASS", f"Title: {title}")
                    else:
                        self.log_test(f"Page loads: {page_name}", "FAIL", "No title found")
                except Exception as e:
                    self.log_test(f"Page loads: {page_name}", "FAIL", str(e))

    async def test_navigation_links(self):
        """Test navigation menu links"""
        print("\n🔗 Testing Navigation Links...")

        # Load homepage
        await self.page.goto(f"file://{(self.build_dir / 'index.html').absolute()}")

        nav_links = [
            ("Home", "/"),
            ("Patent Details", "/patent-details.html"),
            ("Licensing", "/licensing.html"),
            ("Industry Insights", "/industry-insights.html"),
            ("Contact", "/contact.html")
        ]

        for link_text, href in nav_links:
            try:
                link = await self.page.query_selector(f'a[href="{href}"]')
                if link:
                    self.log_test(f"Nav link: {link_text}", "PASS", f"Found href: {href}")
                else:
                    self.log_test(f"Nav link: {link_text}", "FAIL", f"Missing href: {href}")
            except Exception as e:
                self.log_test(f"Nav link: {link_text}", "FAIL", str(e))

    async def test_seo_elements(self):
        """Test SEO meta tags and elements"""
        print("\n🎯 Testing SEO Elements...")

        pages = ["index.html", "patent-details.html", "licensing.html", "contact.html"]

        for page_file in pages:
            await self.page.goto(f"file://{(self.build_dir / page_file).absolute()}")

            # Test title
            title = await self.page.title()
            if title and len(title) > 10:
                self.log_test(f"SEO Title: {page_file}", "PASS", f"Length: {len(title)}")
            else:
                self.log_test(f"SEO Title: {page_file}", "FAIL", "Missing or too short")

            # Test meta description
            meta_desc = await self.page.get_attribute('meta[name="description"]', 'content')
            if meta_desc and len(meta_desc) > 50:
                self.log_test(f"Meta Description: {page_file}", "PASS", f"Length: {len(meta_desc)}")
            else:
                self.log_test(f"Meta Description: {page_file}", "FAIL", "Missing or too short")

            # Test meta keywords
            meta_keywords = await self.page.get_attribute('meta[name="keywords"]', 'content')
            if meta_keywords:
                self.log_test(f"Meta Keywords: {page_file}", "PASS", f"Found: {len(meta_keywords.split(','))} keywords")
            else:
                self.log_test(f"Meta Keywords: {page_file}", "FAIL", "Missing keywords")

    async def test_open_graph_twitter_tags(self):
        """Test Open Graph and Twitter Card meta tags"""
        print("\n🔗 Testing Open Graph & Twitter Card Tags...")

        pages = ["index.html", "patent-details.html", "licensing.html", "series-a-av-patent-portfolio-strategy.html"]

        # Required Open Graph tags
        required_og_tags = ['og:title', 'og:description', 'og:type', 'og:url', 'og:image', 'og:site_name']

        # Required Twitter Card tags
        required_twitter_tags = ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']

        for page_file in pages:
            await self.page.goto(f"file://{(self.build_dir / page_file).absolute()}")

            # Test Open Graph tags
            for og_tag in required_og_tags:
                try:
                    og_value = await self.page.get_attribute(f'meta[property="{og_tag}"]', 'content')
                    if og_value and len(og_value) > 0:
                        self.log_test(f"OG {og_tag}: {page_file}", "PASS", f"Found: {og_value[:50]}...")
                    else:
                        self.log_test(f"OG {og_tag}: {page_file}", "FAIL", "Missing or empty")
                except Exception as e:
                    self.log_test(f"OG {og_tag}: {page_file}", "FAIL", str(e))

            # Test Twitter Card tags
            for twitter_tag in required_twitter_tags:
                try:
                    twitter_value = await self.page.get_attribute(f'meta[name="{twitter_tag}"]', 'content')
                    if twitter_value and len(twitter_value) > 0:
                        self.log_test(f"Twitter {twitter_tag}: {page_file}", "PASS", f"Found: {twitter_value[:50]}...")
                    else:
                        self.log_test(f"Twitter {twitter_tag}: {page_file}", "FAIL", "Missing or empty")
                except Exception as e:
                    self.log_test(f"Twitter {twitter_tag}: {page_file}", "FAIL", str(e))

            # Validate og:image URL format
            og_image = await self.page.get_attribute('meta[property="og:image"]', 'content')
            if og_image:
                if og_image.startswith('https://'):
                    self.log_test(f"OG Image HTTPS: {page_file}", "PASS", "Uses HTTPS")
                else:
                    self.log_test(f"OG Image HTTPS: {page_file}", "FAIL", "Must use HTTPS")

                if 'av-navigation-ip.com' in og_image:
                    self.log_test(f"OG Image Domain: {page_file}", "PASS", "Correct domain")
                else:
                    self.log_test(f"OG Image Domain: {page_file}", "FAIL", "Incorrect domain")

    async def test_structured_data_schemas(self):
        """Test JSON-LD structured data schemas"""
        print("\n📊 Testing Structured Data Schemas...")

        # Test Article schema on content pages
        content_pages = [
            'series-a-av-patent-portfolio-strategy.html',
            'tesla-fsd-competitor-camera-patent-licensing.html',
            'drone-delivery-patent-portfolio-pre-ipo.html',
            'venture-capital-av-patent-portfolio-due-diligence.html',
            'autonomous-trucking-patent-defense-strategy.html',
            'industry-insights.html',
            'about.html',
            'licensing.html'
        ]

        for page_file in content_pages:
            page_path = self.build_dir / page_file
            if page_path.exists():
                await self.page.goto(f"file://{page_path.absolute()}")

                # Check for Article schema
                page_content = await self.page.content()
                if '"@type": "Article"' in page_content:
                    self.log_test(f"Article Schema: {page_file}", "PASS", "Found Article schema")

                    # Verify required Article fields
                    if '"headline"' in page_content:
                        self.log_test(f"Article headline: {page_file}", "PASS", "Found headline field")
                    else:
                        self.log_test(f"Article headline: {page_file}", "FAIL", "Missing headline field")

                    if '"datePublished"' in page_content:
                        self.log_test(f"Article datePublished: {page_file}", "PASS", "Found datePublished field")
                    else:
                        self.log_test(f"Article datePublished: {page_file}", "FAIL", "Missing datePublished field")
                else:
                    self.log_test(f"Article Schema: {page_file}", "FAIL", "Missing Article schema")

        # Test BreadcrumbList schema on all non-homepage pages
        all_pages = [
            'patent-details.html',
            'licensing.html',
            'industry-insights.html',
            'contact.html',
            'thank-you.html',
            'about.html',
            'disclaimer.html',
            'privacy.html',
            'series-a-av-patent-portfolio-strategy.html'
        ]

        for page_file in all_pages:
            page_path = self.build_dir / page_file
            if page_path.exists():
                await self.page.goto(f"file://{page_path.absolute()}")

                page_content = await self.page.content()
                if '"@type": "BreadcrumbList"' in page_content:
                    self.log_test(f"BreadcrumbList Schema: {page_file}", "PASS", "Found BreadcrumbList schema")

                    # Verify itemListElement exists
                    if '"itemListElement"' in page_content:
                        self.log_test(f"Breadcrumb items: {page_file}", "PASS", "Found itemListElement")
                    else:
                        self.log_test(f"Breadcrumb items: {page_file}", "FAIL", "Missing itemListElement")
                else:
                    self.log_test(f"BreadcrumbList Schema: {page_file}", "FAIL", "Missing BreadcrumbList schema")

        # Test Organization schema (should exist from base.html on all pages)
        test_pages = ['index.html', 'patent-details.html', 'contact.html']
        for page_file in test_pages:
            page_path = self.build_dir / page_file
            if page_path.exists():
                await self.page.goto(f"file://{page_path.absolute()}")

                page_content = await self.page.content()
                if '"@type": "Organization"' in page_content:
                    self.log_test(f"Organization Schema: {page_file}", "PASS", "Found Organization schema")
                else:
                    self.log_test(f"Organization Schema: {page_file}", "FAIL", "Missing Organization schema")

    async def test_responsive_design(self):
        """Test responsive design at different viewport sizes"""
        print("\n📱 Testing Responsive Design...")

        await self.page.goto(f"file://{(self.build_dir / 'index.html').absolute()}")

        viewports = [
            ("Mobile", 375, 667),
            ("Tablet", 768, 1024),
            ("Desktop", 1920, 1080)
        ]

        for device, width, height in viewports:
            try:
                await self.page.set_viewport_size({"width": width, "height": height})

                # Check if navbar is present
                navbar = await self.page.query_selector('.navbar')
                if navbar:
                    self.log_test(f"Responsive {device}", "PASS", f"Navbar visible at {width}x{height}")
                else:
                    self.log_test(f"Responsive {device}", "FAIL", f"Navbar missing at {width}x{height}")

            except Exception as e:
                self.log_test(f"Responsive {device}", "FAIL", str(e))

    async def test_contact_form(self):
        """Test contact form elements"""
        print("\n📝 Testing Contact Form...")

        await self.page.goto(f"file://{(self.build_dir / 'contact.html').absolute()}")

        # Test simplified form fields (5 fields total)
        form_fields = [
            ("name", "Name", True),
            ("email", "Email", True),
            ("company", "Company", True),
            ("phone", "Phone", False),  # Optional field
            ("message", "Message", True)
        ]

        for field_id, field_name, is_required in form_fields:
            try:
                field = await self.page.query_selector(f'#{field_id}')
                if field:
                    # Check if required attribute matches expectation
                    required_attr = await field.get_attribute('required')
                    is_actually_required = required_attr is not None

                    if is_actually_required == is_required:
                        req_status = "required" if is_required else "optional"
                        self.log_test(f"Form field: {field_name}", "PASS", f"Found #{field_id} ({req_status})")
                    else:
                        expected = "required" if is_required else "optional"
                        actual = "required" if is_actually_required else "optional"
                        self.log_test(f"Form field: {field_name}", "FAIL", f"Expected {expected} but found {actual}")
                else:
                    self.log_test(f"Form field: {field_name}", "FAIL", f"Missing #{field_id}")
            except Exception as e:
                self.log_test(f"Form field: {field_name}", "FAIL", str(e))

        # Test that old fields are removed
        removed_fields = [
            ("firstName", "First Name"),
            ("lastName", "Last Name"),
            ("title", "Title"),
            ("industry", "Industry"),
            ("licensingType", "Licensing Type"),
            ("timeline", "Timeline"),
            ("privacy", "Privacy Checkbox")
        ]

        for field_id, field_name in removed_fields:
            try:
                field = await self.page.query_selector(f'#{field_id}')
                if field is None:
                    self.log_test(f"Removed field: {field_name}", "PASS", f"Confirmed #{field_id} removed")
                else:
                    self.log_test(f"Removed field: {field_name}", "FAIL", f"Old field #{field_id} still exists")
            except Exception as e:
                self.log_test(f"Removed field: {field_name}", "FAIL", str(e))

        # Test submit button
        try:
            submit_btn = await self.page.query_selector('button[type="submit"]')
            if submit_btn:
                self.log_test("Form submit button", "PASS", "Submit button found")
            else:
                self.log_test("Form submit button", "FAIL", "Submit button missing")
        except Exception as e:
            self.log_test("Form submit button", "FAIL", str(e))

        # Test for example guidance text in message field
        try:
            form_text = await self.page.query_selector('.form-text')
            if form_text:
                text_content = await form_text.text_content()
                if "Examples of helpful inquiries" in text_content:
                    self.log_test("Message field examples", "PASS", "Example guidance found")
                else:
                    self.log_test("Message field examples", "FAIL", "Example text missing")
            else:
                self.log_test("Message field examples", "FAIL", "Form-text div missing")
        except Exception as e:
            self.log_test("Message field examples", "FAIL", str(e))

        # Test privacy policy link (not checkbox)
        try:
            privacy_link = await self.page.query_selector('a[href="/privacy.html"]')
            if privacy_link:
                self.log_test("Privacy policy link", "PASS", "Privacy policy link found")
            else:
                self.log_test("Privacy policy link", "FAIL", "Privacy policy link missing")
        except Exception as e:
            self.log_test("Privacy policy link", "FAIL", str(e))

        # Test Web3Forms endpoint
        try:
            form = await self.page.query_selector('form')
            if form:
                form_action = await form.get_attribute('action')
                if 'web3forms.com/submit' in form_action:
                    self.log_test("Web3Forms endpoint", "PASS", "Form uses Web3Forms API")
                else:
                    self.log_test("Web3Forms endpoint", "FAIL", f"Form action: {form_action}")
            else:
                self.log_test("Web3Forms endpoint", "FAIL", "Form element not found")
        except Exception as e:
            self.log_test("Web3Forms endpoint", "FAIL", str(e))

        # Test honeypot spam protection
        try:
            honeypot = await self.page.query_selector('input[name="botcheck"]')
            if honeypot:
                honeypot_style = await honeypot.get_attribute('style')
                if 'display:none' in honeypot_style or 'display: none' in honeypot_style:
                    self.log_test("Honeypot spam protection", "PASS", "Honeypot field hidden")
                else:
                    self.log_test("Honeypot spam protection", "FAIL", f"Honeypot visible: {honeypot_style}")
            else:
                self.log_test("Honeypot spam protection", "FAIL", "Honeypot field missing")
        except Exception as e:
            self.log_test("Honeypot spam protection", "FAIL", str(e))

        # Test Web3Forms access key present
        try:
            access_key = await self.page.query_selector('input[name="access_key"]')
            if access_key:
                key_value = await access_key.get_attribute('value')
                if key_value and len(key_value) > 20:
                    self.log_test("Web3Forms access key", "PASS", "Access key configured")
                else:
                    self.log_test("Web3Forms access key", "FAIL", "Access key empty or invalid")
            else:
                self.log_test("Web3Forms access key", "FAIL", "Access key field missing")
        except Exception as e:
            self.log_test("Web3Forms access key", "FAIL", str(e))

        # Test hCaptcha widget present
        try:
            hcaptcha = await self.page.query_selector('.h-captcha[data-captcha="true"]')
            if hcaptcha:
                self.log_test("hCaptcha widget", "PASS", "hCaptcha spam protection present")
            else:
                self.log_test("hCaptcha widget", "FAIL", "hCaptcha widget missing")
        except Exception as e:
            self.log_test("hCaptcha widget", "FAIL", str(e))

        # Test Web3Forms script present
        try:
            page_content = await self.page.content()
            if 'web3forms.com/client/script.js' in page_content:
                self.log_test("Web3Forms script", "PASS", "Web3Forms client script loaded")
            else:
                self.log_test("Web3Forms script", "FAIL", "Web3Forms script missing")
        except Exception as e:
            self.log_test("Web3Forms script", "FAIL", str(e))

    async def test_social_images_and_meta(self):
        """Test social sharing images and meta description optimization"""
        print("\n🖼️  Testing Social Images & Meta Descriptions...")

        # Test that referenced Open Graph images exist
        all_pages = [
            'index.html',
            'patent-details.html',
            'licensing.html',
            'industry-insights.html',
            'contact.html',
            'thank-you.html',
            'about.html',
            'disclaimer.html',
            'privacy.html',
            'series-a-av-patent-portfolio-strategy.html',
            'tesla-fsd-competitor-camera-patent-licensing.html',
            'drone-delivery-patent-portfolio-pre-ipo.html',
            'venture-capital-av-patent-portfolio-due-diligence.html',
            'autonomous-trucking-patent-defense-strategy.html'
        ]

        for page_file in all_pages:
            page_path = self.build_dir / page_file
            if page_path.exists():
                await self.page.goto(f"file://{page_path.absolute()}")

                # Extract og:image URL
                og_image = await self.page.get_attribute('meta[property="og:image"]', 'content')
                if og_image:
                    # Convert URL to local file path
                    if '/assets/images/' in og_image:
                        # Extract filename from URL
                        filename = og_image.split('/assets/images/')[-1]
                        image_path = self.build_dir / 'assets' / 'images' / filename

                        if image_path.exists():
                            self.log_test(f"OG Image exists: {page_file}", "PASS", f"Found: {filename}")
                        else:
                            self.log_test(f"OG Image exists: {page_file}", "FAIL", f"Missing: {filename}")
                    else:
                        self.log_test(f"OG Image path: {page_file}", "FAIL", f"Invalid path: {og_image}")
                else:
                    self.log_test(f"OG Image: {page_file}", "FAIL", "No og:image tag found")

                # Test meta description length (should be 120-160 characters for optimal SEO)
                meta_desc = await self.page.get_attribute('meta[name="description"]', 'content')
                if meta_desc:
                    desc_length = len(meta_desc)
                    if 120 <= desc_length <= 160:
                        self.log_test(f"Meta desc length: {page_file}", "PASS", f"{desc_length} chars (optimal)")
                    elif desc_length < 120:
                        self.log_test(f"Meta desc length: {page_file}", "FAIL", f"{desc_length} chars (too short, min 120)")
                    else:
                        self.log_test(f"Meta desc length: {page_file}", "FAIL", f"{desc_length} chars (too long, max 160)")
                else:
                    self.log_test(f"Meta description: {page_file}", "FAIL", "Missing meta description")

    async def test_accessibility(self):
        """Test basic accessibility features"""
        print("\n♿ Testing Accessibility...")

        await self.page.goto(f"file://{(self.build_dir / 'index.html').absolute()}")

        # Test for alt attributes on images
        images = await self.page.query_selector_all('img')
        images_with_alt = 0
        for img in images:
            alt = await img.get_attribute('alt')
            if alt is not None:
                images_with_alt += 1

        if len(images) == 0:
            self.log_test("Image alt tags", "PASS", "No images found")
        elif images_with_alt == len(images):
            self.log_test("Image alt tags", "PASS", f"All {len(images)} images have alt tags")
        else:
            self.log_test("Image alt tags", "FAIL", f"Only {images_with_alt}/{len(images)} images have alt tags")

        # Test heading hierarchy
        headings = await self.page.query_selector_all('h1, h2, h3, h4, h5, h6')
        if len(headings) > 0:
            self.log_test("Heading structure", "PASS", f"Found {len(headings)} headings")
        else:
            self.log_test("Heading structure", "FAIL", "No headings found")

    async def test_google_analytics(self):
        """Test Google Analytics tracking code structure"""
        print("\n📊 Testing Google Analytics...")

        # Test all pages for GA script presence
        all_pages = [
            'index.html',
            'patent-details.html',
            'licensing.html',
            'industry-insights.html',
            'contact.html',
            'thank-you.html'
        ]

        for page_file in all_pages:
            page_path = self.build_dir / page_file
            if page_path.exists():
                await self.page.goto(f"file://{page_path.absolute()}")

                page_content = await self.page.content()

                # Check for Google Analytics script
                if 'googletagmanager.com/gtag/js' in page_content:
                    self.log_test(f"GA script: {page_file}", "PASS", "Google Analytics script found")
                else:
                    self.log_test(f"GA script: {page_file}", "FAIL", "Missing Google Analytics script")

                # Check for gtag function
                if 'window.dataLayer' in page_content and 'function gtag()' in page_content:
                    self.log_test(f"GA structure: {page_file}", "PASS", "gtag structure present")
                else:
                    self.log_test(f"GA structure: {page_file}", "FAIL", "gtag structure missing")

    async def test_performance_basics(self):
        """Test basic performance metrics"""
        print("\n⚡ Testing Performance Basics...")

        # Test page load timing
        await self.page.goto(f"file://{(self.build_dir / 'index.html').absolute()}")

        # Check for large resource loads (CSS, JS)
        css_links = await self.page.query_selector_all('link[rel="stylesheet"]')
        js_scripts = await self.page.query_selector_all('script[src]')

        self.log_test("CSS resources", "PASS", f"Found {len(css_links)} CSS files")
        self.log_test("JS resources", "PASS", f"Found {len(js_scripts)} JS files")

        # Check if Bootstrap CDN is loading
        bootstrap_css = await self.page.query_selector('link[href*="bootstrap"]')
        if bootstrap_css:
            self.log_test("Bootstrap CSS", "PASS", "Bootstrap CDN link found")
        else:
            self.log_test("Bootstrap CSS", "FAIL", "Bootstrap CDN link missing")

    async def run_all_tests(self):
        """Run all website validation tests"""
        print("🚀 Starting Website Validation Tests...")
        print(f"📁 Testing build directory: {self.build_dir}")

        if not self.build_dir.exists():
            print(f"❌ Build directory not found: {self.build_dir}")
            print("💡 Run 'python generate_site.py' first")
            return False

        await self.setup_browser()

        try:
            await self.test_file_existence()
            await self.test_page_loading()
            await self.test_navigation_links()
            await self.test_seo_elements()
            await self.test_open_graph_twitter_tags()
            await self.test_structured_data_schemas()
            await self.test_social_images_and_meta()
            await self.test_google_analytics()
            await self.test_responsive_design()
            await self.test_contact_form()
            await self.test_accessibility()
            await self.test_performance_basics()

        finally:
            await self.cleanup_browser()

        # Summary
        passed = len([r for r in self.test_results if r["status"] == "PASS"])
        failed = len([r for r in self.test_results if r["status"] == "FAIL"])
        total = len(self.test_results)

        print(f"\n📊 Test Summary:")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📋 Total: {total}")
        print(f"📈 Success Rate: {(passed/total*100):.1f}%")

        if failed > 0:
            print("\n❌ Failed Tests:")
            for result in self.test_results:
                if result["status"] == "FAIL":
                    print(f"  • {result['test']}: {result['message']}")

        return failed == 0

async def main():
    """Main function"""
    validator = WebsiteValidator()
    success = await validator.run_all_tests()

    if success:
        print("\n🎉 All tests passed! Website is ready for deployment.")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed. Review issues before deployment.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())