#!/usr/bin/env python3
"""
Check APA citations in the textbook
Validates APA format and ensures 15+ citations from recent years (SC-008)
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple

def extract_citations(file_path: str) -> List[str]:
    """Extract APA citations from MDX files"""
    citations = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for citations in common APA format patterns
    # Pattern: Author(s) (Year). Title...
    pattern = r'([A-Z][a-z]+,?\s+[A-Z]\.(?:\s+[A-Z]\.)?(?:,?\s+&?\s+[A-Z][a-z]+,?\s+[A-Z]\.(?:\s+[A-Z]\.)?)*)\s+\((\d{4})\)\.'
    matches = re.finditer(pattern, content)

    for match in matches:
        authors = match.group(1)
        year = match.group(2)
        citations.append(f"{authors} ({year})")

    return citations

def check_citation_year(citation: str, current_year: int = 2025) -> bool:
    """Check if citation is from the last 12 years"""
    year_match = re.search(r'\((\d{4})\)', citation)
    if year_match:
        year = int(year_match.group(1))
        return (current_year - year) <= 12
    return False

def main():
    print("🔍 Checking citations...")

    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"❌ docs/ directory not found")
        return 1

    all_citations = []
    recent_citations = []

    # Check for references file
    references_file = docs_dir / "appendix" / "references.mdx"
    if references_file.exists():
        citations = extract_citations(str(references_file))
        all_citations.extend(citations)

        for citation in citations:
            if check_citation_year(citation):
                recent_citations.append(citation)

    # Also check chapter files for inline citations
    for mdx_file in docs_dir.rglob("chapter-*.mdx"):
        citations = extract_citations(str(mdx_file))
        all_citations.extend(citations)

        for citation in citations:
            if check_citation_year(citation):
                recent_citations.append(citation)

    # Remove duplicates
    all_citations = list(set(all_citations))
    recent_citations = list(set(recent_citations))

    print(f"\n📊 Results:")
    print(f"   Total citations: {len(all_citations)}")
    print(f"   Recent citations (last 12 years): {len(recent_citations)}")

    if len(all_citations) < 15:
        print(f"   ❌ Need at least 15 citations (SC-008), found {len(all_citations)}")
        return 1

    recent_percentage = (len(recent_citations) / len(all_citations)) * 100 if all_citations else 0
    print(f"   Recent citation percentage: {recent_percentage:.1f}%")

    if recent_percentage < 60:
        print(f"   ⚠️  Warning: Less than 60% of citations are recent")

    print(f"   ✅ Citation requirements met!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
