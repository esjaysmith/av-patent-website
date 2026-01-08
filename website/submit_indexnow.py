#!/usr/bin/env python3
"""
IndexNow URL Submission Script
Reads URLs from sitemap.xml and submits them to IndexNow API
"""

import xml.etree.ElementTree as ET
import requests
import json
from pathlib import Path

# Configuration
INDEXNOW_KEY = "6a70e795af4a499aa8699b2f7208ee04"
HOST = "www.av-navigation-ip.com"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/IndexNow"

def parse_sitemap(sitemap_path):
    """Extract URLs from sitemap.xml"""
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Handle XML namespace
    namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    urls = []
    for url_elem in root.findall("ns:url", namespace):
        loc = url_elem.find("ns:loc", namespace)
        if loc is not None and loc.text:
            urls.append(loc.text)

    return urls

def submit_to_indexnow(urls):
    """Submit URLs to IndexNow API"""
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    print(f"Submitting {len(urls)} URLs to IndexNow...")
    print(f"Host: {HOST}")
    print(f"Key Location: {KEY_LOCATION}")
    print()

    response = requests.post(
        INDEXNOW_ENDPOINT,
        headers=headers,
        data=json.dumps(payload)
    )

    return response

def main():
    # Find sitemap.xml
    script_dir = Path(__file__).parent
    sitemap_path = script_dir / "build" / "sitemap.xml"

    if not sitemap_path.exists():
        print(f"Error: sitemap.xml not found at {sitemap_path}")
        print("Run 'python generate_site.py' first to generate the sitemap.")
        return 1

    # Parse URLs from sitemap
    urls = parse_sitemap(sitemap_path)

    if not urls:
        print("No URLs found in sitemap.xml")
        return 1

    print(f"Found {len(urls)} URLs in sitemap:")
    for url in urls:
        print(f"  - {url}")
    print()

    # Submit to IndexNow
    response = submit_to_indexnow(urls)

    # Handle response
    print(f"Response Status: {response.status_code}")

    if response.status_code == 200:
        print("Success: URLs submitted successfully")
    elif response.status_code == 202:
        print("Accepted: URLs accepted for processing")
    elif response.status_code == 400:
        print("Error: Invalid format")
    elif response.status_code == 403:
        print("Error: Key not valid (key not found or key file not accessible)")
    elif response.status_code == 422:
        print("Error: URLs don't belong to host or key mismatch")
    elif response.status_code == 429:
        print("Error: Too many requests (rate limited)")
    else:
        print(f"Unexpected response: {response.text}")

    return 0 if response.status_code in [200, 202] else 1

if __name__ == "__main__":
    exit(main())
