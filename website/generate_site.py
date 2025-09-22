#!/usr/bin/env python3
"""
Static Site Generator for AV Navigation IP Protection Website
Converts Markdown content to HTML using Jinja2 templates
"""

import os
import sys
import shutil
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader
import yaml
import re

class StaticSiteGenerator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.content_dir = self.base_dir / "content"
        self.templates_dir = self.base_dir / "templates"
        self.assets_dir = self.base_dir / "assets"
        self.build_dir = self.base_dir / "build"

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
        print("🚀 Starting static site generation...")

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
    generator = StaticSiteGenerator()

    if len(sys.argv) > 1 and sys.argv[1] == '--serve':
        # Future: Add local development server
        print("Local server not implemented yet. Use python -m http.server in build directory.")
        return

    success = generator.build_site()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()