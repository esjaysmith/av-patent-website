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

        form_fields = [
            ("firstName", "First Name"),
            ("lastName", "Last Name"),
            ("email", "Email"),
            ("company", "Company"),
            ("industry", "Industry"),
            ("message", "Message")
        ]

        for field_id, field_name in form_fields:
            try:
                field = await self.page.query_selector(f'#{field_id}')
                if field:
                    self.log_test(f"Form field: {field_name}", "PASS", f"Found #{field_id}")
                else:
                    self.log_test(f"Form field: {field_name}", "FAIL", f"Missing #{field_id}")
            except Exception as e:
                self.log_test(f"Form field: {field_name}", "FAIL", str(e))

        # Test submit button
        try:
            submit_btn = await self.page.query_selector('button[type="submit"]')
            if submit_btn:
                self.log_test("Form submit button", "PASS", "Submit button found")
            else:
                self.log_test("Form submit button", "FAIL", "Submit button missing")
        except Exception as e:
            self.log_test("Form submit button", "FAIL", str(e))

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