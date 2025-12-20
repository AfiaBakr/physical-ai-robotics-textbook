import xml.etree.ElementTree as ET
from urllib.parse import urljoin

# Test sitemap parsing with the actual content
sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"><url><loc>hhttps://physical-ai-robotics-textbook-nine.vercel.app/markdown-page</loc><changefreq>weekly</changefreq><priority>0.5</priority></url><url><loc>hhttps://physical-ai-robotics-textbook-nine.vercel.app/docs/appendix/references</loc><changefreq>weekly</changefreq><priority>0.5</priority></url></urlset>'''

try:
    root = ET.fromstring(sitemap_content)
    urls = []

    # Handle the default namespace
    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    for url_elem in root.findall('.//sitemap:loc', namespace):
        url = url_elem.text
        print(f"Found URL: {url}")
        # Check if URL starts with the correct base
        if url and url.startswith("https://physical-ai-robotics-textbook-nine.vercel.app/"):
            urls.append(url)
        elif url and url.startswith("hhttps://physical-ai-robotics-textbook-nine.vercel.app/"):
            # Fix the typo in the URL
            fixed_url = url.replace("hhttps://", "https://")
            print(f"Fixed URL: {fixed_url}")
            urls.append(fixed_url)

    print(f"Total valid URLs found: {len(urls)}")
    for url in urls:
        print(f"  - {url}")

except Exception as e:
    print(f"Error parsing sitemap: {e}")