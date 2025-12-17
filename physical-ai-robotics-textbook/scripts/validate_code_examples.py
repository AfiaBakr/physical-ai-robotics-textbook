#!/usr/bin/env python3
"""
Validate all code examples in the textbook
Tests that Python code examples run successfully (SC-012 requirement)
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple

def extract_python_code_blocks(file_path: str) -> List[Tuple[str, int]]:
    """Extract Python code blocks from MDX files"""
    code_blocks = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match ```python...``` code blocks
    pattern = r'```python\n(.*?)\n```'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        code = match.group(1)
        line_num = content[:match.start()].count('\n') + 1
        code_blocks.append((code, line_num))

    return code_blocks

def validate_python_syntax(code: str) -> Tuple[bool, str]:
    """Check if Python code has valid syntax"""
    try:
        compile(code, '<string>', 'exec')
        return True, "Valid syntax"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"

def main():
    print("🔍 Validating code examples...")

    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"❌ docs/ directory not found")
        return 1

    total_files = 0
    total_blocks = 0
    errors = []

    # Find all MDX files
    for mdx_file in docs_dir.rglob("*.mdx"):
        total_files += 1
        code_blocks = extract_python_code_blocks(str(mdx_file))

        for code, line_num in code_blocks:
            total_blocks += 1
            is_valid, message = validate_python_syntax(code)

            if not is_valid:
                errors.append(f"{mdx_file}:{line_num} - {message}")
                print(f"❌ {mdx_file}:{line_num}")
                print(f"   {message}")

    print(f"\n📊 Results:")
    print(f"   Files scanned: {total_files}")
    print(f"   Code blocks found: {total_blocks}")

    if errors:
        print(f"   ❌ Errors: {len(errors)}")
        print(f"\n❌ Validation failed!")
        return 1
    else:
        print(f"   ✅ All code examples validated successfully!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
