#!/usr/bin/env python3
"""
Static Site Generator for AV Navigation IP Protection Website
Converts Markdown content to HTML using Jinja2 templates
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader
import yaml
import re
import base64
import json

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Using default values. Install with: pip install python-dotenv")

# Environment configuration
SITE_URL = os.getenv('SITE_URL', 'https://av-navigation-ip.com')
SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'av-navigation-ip.com')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')
ROBOTS_INDEX = os.getenv('ROBOTS_INDEX', 'true').lower() == 'true'
GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID', 'G-XXXXXXXXXX')
GOOGLE_ANALYTICS_ENABLED = os.getenv('GOOGLE_ANALYTICS_ENABLED', 'false').lower() == 'true'

class StaticSiteGenerator:
    def __init__(self, design="default"):
        self.base_dir = Path(__file__).parent
        self.content_dir = self.base_dir / "content"
        self.designs_dir = self.base_dir / "designs"
        self.templates_dir = self.designs_dir / design
        self.assets_dir = self.base_dir / "assets"
        self.build_dir = self.base_dir / "build"
        self.design = design

        # Validate design exists
        if not self.templates_dir.exists():
            available_designs = [d.name for d in self.designs_dir.iterdir() if d.is_dir()]
            raise ValueError(f"Design '{design}' not found. Available designs: {', '.join(available_designs)}")

        # Initialize Jinja2 environment
        self.jinja_env = Environment(loader=FileSystemLoader(self.templates_dir))

        # Initialize Markdown processor
        self.md = markdown.Markdown(extensions=['meta', 'toc', 'tables'])

    def determine_page_type(self, filename):
        """Determine page type for schema selection."""
        if filename == 'index.html':
            return 'homepage'
        elif filename == 'patent-details.html':
            return 'patent-details'
        elif filename == 'contact.html':
            return 'contact'
        elif filename == 'industry-insights.html':
            return 'insights'
        elif filename == 'about.html':
            return 'about'
        elif filename in ['disclaimer.html', 'privacy.html', 'thank-you.html']:
            return 'legal'
        else:
            return 'landing'  # All SEO landing pages

    def _normalize_url(self, url):
        """Normalize URL to use environment-based domain.

        Handles both absolute URLs (https://...) and relative URLs (/assets/...).
        If URL is absolute, replaces the domain with SITE_URL.
        If URL is relative, prepends SITE_URL.
        """
        if not url:
            return f"{SITE_URL}/assets/images/og-general-info.jpg"

        # If URL starts with http:// or https://, replace the base URL
        if url.startswith('http://') or url.startswith('https://'):
            # Extract the path part (everything after the domain)
            # Example: https://av-navigation-ip.com/assets/images/foo.jpg -> /assets/images/foo.jpg
            import re
            match = re.search(r'https?://[^/]+(/.*)$', url)
            if match:
                path = match.group(1)
                return f"{SITE_URL}{path}"
            return url  # If parsing fails, return original

        # If URL is relative (starts with /), prepend SITE_URL
        elif url.startswith('/'):
            return f"{SITE_URL}{url}"

        # If URL doesn't start with /, assume it's a relative path and add /
        else:
            return f"{SITE_URL}/{url}"

    def clean_build_dir(self):
        """Remove and recreate build directory"""
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
        self.build_dir.mkdir(exist_ok=True)
        print(f"✓ Cleaned build directory: {self.build_dir}")

    def copy_assets(self):
        """Copy assets to build directory"""
        if self.assets_dir.exists():
            build_assets = self.build_dir / "assets"
            shutil.copytree(self.assets_dir, build_assets)
            print(f"✓ Copied assets to: {build_assets}")
        else:
            print("! No assets directory found, skipping...")



    def parse_frontmatter(self, content):
        """Extract YAML frontmatter from markdown content"""
        if content.startswith('---'):
            try:
                _, frontmatter, markdown_content = content.split('---', 2)
                metadata = yaml.safe_load(frontmatter.strip())
                return metadata, markdown_content.strip()
            except ValueError:
                print("Warning: Invalid frontmatter format")
                return {}, content
        return {}, content

    def process_markdown_file(self, md_file_path):
        """Process a single markdown file and return HTML content with metadata"""
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter
        metadata, markdown_content = self.parse_frontmatter(content)

        # Convert markdown to HTML
        html_content = self.md.convert(markdown_content)

        # Fix H1 duplication - convert first H1 in content to H2
        # This prevents duplicate H1s when page template already has one
        html_content = re.sub(r'<h1([^>]*)>(.*?)</h1>', r'<h2\1>\2</h2>', html_content, count=1)


        # Reset markdown processor for next file
        self.md.reset()

        return html_content, metadata

    def generate_page(self, md_file_path, output_filename=None):
        """Generate a single HTML page from markdown file"""
        html_content, metadata = self.process_markdown_file(md_file_path)

        # Determine output filename
        if output_filename is None:
            output_filename = md_file_path.stem + '.html'

        # Generate canonical URL
        if output_filename == 'index.html':
            canonical_url = '/'
        else:
            canonical_url = '/' + output_filename

        # Determine page type for schema selection
        page_type = self.determine_page_type(output_filename)

        # Set default metadata values
        template_vars = {
            'title': metadata.get('title', 'AV Navigation IP Protection'),
            'description': metadata.get('description', 'Patent licensing for autonomous vehicle navigation technology'),
            'keywords': metadata.get('keywords', 'autonomous vehicle patents, navigation technology licensing'),
            'content': html_content,
            'is_homepage': metadata.get('is_homepage', False),
            'hero_title': metadata.get('hero_title', ''),
            'hero_subtitle': metadata.get('hero_subtitle', ''),
            'page_title': metadata.get('page_title', metadata.get('title', '')),
            'show_cta': metadata.get('show_cta', False),
            'canonical_url': canonical_url,
            'page_type': page_type,
            'breadcrumb_parent': metadata.get('breadcrumb_parent', ''),
            'breadcrumb_parent_url': metadata.get('breadcrumb_parent_url', ''),
            'site_url': SITE_URL,

            # Open Graph fields
            'og_title': metadata.get('og_title', metadata.get('title', 'AV Navigation IP Protection')),
            'og_description': metadata.get('og_description', metadata.get('description', '')),
            'og_type': metadata.get('og_type', 'website'),
            'og_url': metadata.get('og_url', f"{SITE_URL}{canonical_url}"),
            'og_image': self._normalize_url(metadata.get('og_image', '/assets/images/og-general-info.jpg')),
            'og_site_name': 'AV Navigation IP Protection',

            # Twitter Card fields
            'twitter_card': metadata.get('twitter_card', 'summary_large_image'),
            'twitter_title': metadata.get('twitter_title', metadata.get('title', 'AV Navigation IP Protection')),
            'twitter_description': metadata.get('twitter_description', metadata.get('description', '')),
            'twitter_image': self._normalize_url(metadata.get('twitter_image', metadata.get('og_image', '/assets/images/og-general-info.jpg'))),

            # Schema.org date fields
            'date_published': metadata.get('date', metadata.get('date_published', '2025-11-01')),
            'date_modified': metadata.get('modified', metadata.get('date_modified', '2025-11-12')),

            # Google Analytics
            'google_analytics_id': GOOGLE_ANALYTICS_ID,
            'google_analytics_enabled': GOOGLE_ANALYTICS_ENABLED
        }

        # Load and render template
        template = self.jinja_env.get_template('page.html')
        rendered_html = template.render(**template_vars)

        # Write to build directory
        output_path = self.build_dir / output_filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        print(f"✓ Generated: {output_filename} from {md_file_path.name}")
        return output_path

    def generate_sitemap(self, generated_pages):
        """Generate sitemap.xml"""
        sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
        base_url = SITE_URL

        for page in generated_pages:
            if page.name == 'index.html':
                url = base_url + '/'
            else:
                url = f"{base_url}/{page.name}"

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

    def generate_robots_txt(self):
        """Generate robots.txt"""
        # Determine indexing policy based on environment
        if ROBOTS_INDEX:
            disallow_rule = "Allow: /"
        else:
            disallow_rule = "Disallow: /"

        robots_content = f"""User-agent: *
{disallow_rule}

Sitemap: {SITE_URL}/sitemap.xml
"""

        robots_path = self.build_dir / 'robots.txt'
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots_content)

        print(f"✓ Generated robots.txt: {robots_path} (indexing: {'allowed' if ROBOTS_INDEX else 'blocked'})")

    def build_site(self):
        """Build the complete static site"""
        print(f"🚀 Starting static site generation using '{self.design}' design...")
        print(f"🌍 Environment: {ENVIRONMENT}")
        print(f"🔗 Site URL: {SITE_URL}")
        print(f"🤖 Robots indexing: {'allowed' if ROBOTS_INDEX else 'blocked'}")
        print()

        # Clean build directory
        self.clean_build_dir()

        # Copy assets
        self.copy_assets()

        # Find all markdown files in content directory
        if not self.content_dir.exists():
            print(f"❌ Content directory not found: {self.content_dir}")
            return False

        markdown_files = list(self.content_dir.glob("*.md"))
        if not markdown_files:
            print(f"❌ No markdown files found in: {self.content_dir}")
            return False

        # Process each markdown file
        generated_pages = []
        for md_file in markdown_files:
            try:
                # Special case for index.md -> index.html
                if md_file.name == 'index.md':
                    output_path = self.generate_page(md_file, 'index.html')
                else:
                    output_path = self.generate_page(md_file)
                generated_pages.append(output_path)
            except Exception as e:
                print(f"❌ Error processing {md_file}: {e}")
                return False

        # Generate sitemap and robots.txt
        self.generate_sitemap(generated_pages)
        self.generate_robots_txt()

        print(f"\n✅ Site generation complete!")
        print(f"📁 Output directory: {self.build_dir}")
        print(f"📄 Generated {len(generated_pages)} pages")
        print(f"🌐 Open {self.build_dir}/index.html in your browser to preview")

        return True

def main():
    """Main function to run the site generator"""
    parser = argparse.ArgumentParser(
        description="Static Site Generator for AV Navigation IP Protection Website",
        epilog="""
Examples:
  %(prog)s                           # Use default design
  %(prog)s --design minimal-tech     # Use minimal-tech design
  %(prog)s --design dark-professional # Use dark-professional design
  %(prog)s --design light-professional # Use light-professional design
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--design',
        default='default',
        help='Design theme to use (default: default)'
    )

    parser.add_argument(
        '--serve',
        action='store_true',
        help='Start local development server (not implemented yet)'
    )

    parser.add_argument(
        '--obfuscate-email',
        metavar='EMAIL',
        help='Generate Base64-encoded value for the given email address'
    )

    args = parser.parse_args()

    # Handle email obfuscation command
    if args.obfuscate_email:
        encoded_email = base64.b64encode(args.obfuscate_email.encode('utf-8')).decode('utf-8')
        print(encoded_email)
        return

    try:
        generator = StaticSiteGenerator(design=args.design)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    if args.serve:
        # Future: Add local development server
        print("Local server not implemented yet. Use python -m http.server in build directory.")
        return

    success = generator.build_site()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()