#!/usr/bin/env python3
"""
Count words in textbook content
Validates 5000-7000 word count requirement (FR-014, SC-011)
"""

import os
import sys
import re
from pathlib import Path

def count_words_in_file(file_path: str) -> int:
    """Count words in an MDX file, excluding frontmatter and code blocks"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)

    # Remove inline code
    content = re.sub(r'`[^`]+`', '', content)

    # Remove HTML/JSX tags
    content = re.sub(r'<[^>]+>', '', content)

    # Remove markdown links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)

    # Remove markdown images
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', content)

    # Remove markdown headers symbols
    content = re.sub(r'#{1,6}\s+', '', content)

    # Count words
    words = content.split()
    return len(words)

def main():
    print("🔍 Counting words in textbook...")

    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"❌ docs/ directory not found")
        return 1

    total_words = 0
    chapter_counts = []

    # Count words in all chapter files
    chapter_files = sorted(docs_dir.glob("chapter-*.mdx"))

    for chapter_file in chapter_files:
        word_count = count_words_in_file(str(chapter_file))
        total_words += word_count
        chapter_counts.append((chapter_file.name, word_count))

    print(f"\n📊 Word counts by chapter:")
    for filename, count in chapter_counts:
        print(f"   {filename}: {count} words")

    print(f"\n📊 Total word count: {total_words}")
    print(f"   Target range: 5000-7000 words (SC-011)")

    if total_words < 5000:
        print(f"   ❌ Below minimum ({5000 - total_words} words short)")
        return 1
    elif total_words > 7000:
        print(f"   ❌ Above maximum ({total_words - 7000} words over)")
        return 1
    else:
        print(f"   ✅ Word count within target range!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
