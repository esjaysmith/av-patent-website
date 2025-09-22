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

    def obfuscate_email(self, email):
        """Obfuscate email address using Base64 encoding"""
        encoded_email = base64.b64encode(email.encode('utf-8')).decode('utf-8')
        # Use a more unique ID to avoid collisions
        obfuscation_id = f"email_{abs(hash(email + str(os.getpid()))) % 100000}"

        # Create JavaScript that will decode and display the email
        js_code = f'''<span id="{obfuscation_id}" class="email-protected">
            <noscript>Email address hidden (JavaScript required)</noscript>
        </span>
        <script>
        (function() {{
            try {{
                var email = atob('{encoded_email}');
                var element = document.getElementById('{obfuscation_id}');
                if (element) {{
                    element.innerHTML = '<a href="mailto:" + email + '">' + email + '</a>';
                }}
            }} catch(e) {{
                console.error('Email decode error:', e);
            }}
        }})();
        </script>'''

        return js_code

    def obfuscate_emails_in_content(self, content):
        """Find and obfuscate email addresses in HTML content"""
        # Skip if content already contains email obfuscation to prevent double-processing
        if 'class="email-protected"' in content:
            return content

        # Split content to avoid obfuscating emails in JSON-LD script tags and existing obfuscated emails
        parts = re.split(r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>)', content, flags=re.DOTALL | re.IGNORECASE)

        processed_parts = []
        for i, part in enumerate(parts):
            # Skip JSON-LD script tags (odd indices after split)
            if i % 2 == 1 and 'application/ld+json' in part.lower():
                processed_parts.append(part)
            else:
                # Process mailto links in other content
                mailto_pattern = r'<a href="mailto:([^"]+)"[^>]*>([^<]+)</a>'

                def replace_mailto(match):
                    email = match.group(1)
                    display_text = match.group(2)

                    # If display text is the same as email, obfuscate both
                    if display_text == email:
                        return self.obfuscate_email(email)
                    else:
                        # If different display text, keep display text and obfuscate link
                        encoded_email = base64.b64encode(email.encode('utf-8')).decode('utf-8')
                        # Use a more unique ID to avoid collisions
                        obfuscation_id = f"email_{abs(hash(email + display_text + str(os.getpid()))) % 100000}"

                        js_code = f'''<span id="{obfuscation_id}" class="email-protected">{display_text}</span>
                        <script>
                        (function() {{
                            try {{
                                var email = atob('{encoded_email}');
                                var element = document.getElementById('{obfuscation_id}');
                                if (element) {{
                                    element.innerHTML = '<a href="mailto:" + email + '">{display_text}</a>';
                                }}
                            }} catch(e) {{
                                console.error('Email decode error:', e);
                            }}
                        }})();
                        </script>'''

                        return js_code

                # Replace mailto links in this part
                processed_part = re.sub(mailto_pattern, replace_mailto, part)
                processed_parts.append(processed_part)

        return ''.join(processed_parts)

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

        # Obfuscate email addresses in the HTML content
        html_content = self.obfuscate_emails_in_content(html_content)

        # Reset markdown processor for next file
        self.md.reset()

        return html_content, metadata

    def generate_page(self, md_file_path, output_filename=None):
        """Generate a single HTML page from markdown file"""
        html_content, metadata = self.process_markdown_file(md_file_path)

        # Determine output filename
        if output_filename is None:
            output_filename = md_file_path.stem + '.html'

        # Generate canonical URL and page type
        if output_filename == 'index.html':
            canonical_url = '/'
            page_type = 'homepage'
        else:
            canonical_url = '/' + output_filename
            page_type = md_file_path.stem  # e.g. 'patent-details', 'contact', etc.

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
            'page_type': page_type
        }

        # Load and render template
        template = self.jinja_env.get_template('page.html')
        rendered_html = template.render(**template_vars)

        # Obfuscate any remaining email addresses in the final rendered HTML
        rendered_html = self.obfuscate_emails_in_content(rendered_html)

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
        base_url = "https://av-navigation-ip.com"  # TODO: Make configurable

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
        robots_content = """User-agent: *
Allow: /

Sitemap: https://av-navigation-ip.com/sitemap.xml
"""

        robots_path = self.build_dir / 'robots.txt'
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots_content)

        print(f"✓ Generated robots.txt: {robots_path}")

    def build_site(self):
        """Build the complete static site"""
        print(f"🚀 Starting static site generation using '{self.design}' design...")

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

    args = parser.parse_args()

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