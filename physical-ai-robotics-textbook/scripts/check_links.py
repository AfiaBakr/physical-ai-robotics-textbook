#!/usr/bin/env python3
"""
Check all URLs in textbook content
Validates that external links are accessible
"""

import os
import sys
import re
import requests
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse

def extract_urls(file_path: str) -> List[Tuple[str, int]]:
    """Extract URLs from MDX files"""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match markdown links [text](url)
    markdown_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    for match in re.finditer(markdown_pattern, content):
        url = match.group(2)
        if url.startswith('http'):
            line_num = content[:match.start()].count('\n') + 1
            urls.append((url, line_num))

    # Match plain URLs
    url_pattern = r'https?://[^\s<>"\)]+'
    for match in re.finditer(url_pattern, content):
        url = match.group(0)
        # Skip if it's part of a markdown link we already found
        if not any(url in found_url for found_url, _ in urls):
            line_num = content[:match.start()].count('\n') + 1
            urls.append((url, line_num))

    return urls

def check_url(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """Check if URL is accessible"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        if response.status_code < 400:
            return True, f"OK ({response.status_code})"
        else:
            return False, f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, "Connection error"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    print("🔍 Checking links...")

    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"❌ docs/ directory not found")
        return 1

    all_urls = {}
    broken_links = []

    # Extract URLs from all MDX files
    for mdx_file in docs_dir.rglob("*.mdx"):
        urls = extract_urls(str(mdx_file))
        for url, line_num in urls:
            if url not in all_urls:
                all_urls[url] = []
            all_urls[url].append((str(mdx_file), line_num))

    print(f"   Found {len(all_urls)} unique URLs")

    # Check each URL
    for i, url in enumerate(all_urls.keys(), 1):
        print(f"   [{i}/{len(all_urls)}] Checking {url[:60]}...", end='\r')

        is_valid, message = check_url(url)

        if not is_valid:
            broken_links.append((url, message, all_urls[url]))
            print(f"   ❌ {url}")
            print(f"      {message}")
            for file_path, line_num in all_urls[url]:
                print(f"      → {file_path}:{line_num}")

    print(f"\n📊 Results:")
    print(f"   Total URLs checked: {len(all_urls)}")
    print(f"   Broken links: {len(broken_links)}")

    if broken_links:
        print(f"\n❌ Link validation failed!")
        return 1
    else:
        print(f"   ✅ All links are accessible!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
