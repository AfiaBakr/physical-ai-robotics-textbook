#!/usr/bin/env python3
"""
Validate computer vision code examples from Module 3
Tests syntax validity and basic structure for all CV-related code snippets.
"""

import os
import sys
import ast
import re
from pathlib import Path
from typing import List, Tuple

def extract_python_blocks(file_path: str) -> List[Tuple[int, str]]:
    """Extract Python code blocks from an MDX file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match Python code blocks (```python ... ```)
    pattern = r'```python\n(.*?)```'
    matches = re.finditer(pattern, content, re.DOTALL)

    blocks = []
    for match in matches:
        # Calculate line number
        line_num = content[:match.start()].count('\n') + 1
        blocks.append((line_num, match.group(1).strip()))

    return blocks

def validate_python_syntax(code: str) -> Tuple[bool, str]:
    """Validate Python syntax using AST parser"""
    try:
        ast.parse(code)
        return True, "Valid syntax"
    except SyntaxError as e:
        return False, f"Syntax error at line {e.lineno}: {e.msg}"

def check_ros2_imports(code: str) -> Tuple[bool, str]:
    """Check for common ROS 2 imports and patterns"""
    ros2_patterns = [
        ('rclpy', 'ROS 2 Python client library'),
        ('sensor_msgs', 'Sensor message types'),
        ('cv_bridge', 'OpenCV-ROS bridge'),
        ('cv2', 'OpenCV library'),
        ('numpy', 'NumPy arrays'),
    ]

    found = []
    for pattern, desc in ros2_patterns:
        if pattern in code:
            found.append(desc)

    return True, f"Found: {', '.join(found)}" if found else (True, "No ROS 2 imports (may be pseudocode)")

def validate_file(file_path: str) -> List[Tuple[str, bool, str]]:
    """Validate all Python code blocks in a file"""
    results = []
    blocks = extract_python_blocks(file_path)

    for line_num, code in blocks:
        # Skip very short blocks (likely just comments or imports)
        if len(code.strip().split('\n')) < 3:
            continue

        # Syntax check
        is_valid, msg = validate_python_syntax(code)
        results.append((f"Line {line_num}", is_valid, msg))

        # ROS 2 import check (informational only)
        _, ros_msg = check_ros2_imports(code)
        results.append((f"Line {line_num} (imports)", True, ros_msg))

    return results

def main():
    print("=" * 60)
    print("Computer Vision Code Example Validator - Module 3")
    print("=" * 60)

    docs_dir = Path("docs/module-03-perception")
    if not docs_dir.exists():
        print(f"[WARN] Module 3 docs directory not found: {docs_dir}")
        print("       Creating directory structure...")
        docs_dir.mkdir(parents=True, exist_ok=True)
        return 0

    mdx_files = list(docs_dir.glob("*.mdx"))
    if not mdx_files:
        print(f"[INFO] No MDX files found in {docs_dir}")
        print("       Module 3 content not yet created.")
        return 0

    total_errors = 0
    total_checks = 0

    for mdx_file in sorted(mdx_files):
        print(f"\n[FILE] {mdx_file.name}")
        print("-" * 40)

        results = validate_file(str(mdx_file))

        if not results:
            print("  No Python code blocks found")
            continue

        for location, is_valid, msg in results:
            total_checks += 1
            status = "[PASS]" if is_valid else "[FAIL]"
            if not is_valid:
                total_errors += 1
            print(f"  {status} {location}: {msg}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {total_checks - total_errors}/{total_checks} checks passed")

    if total_errors > 0:
        print(f"[FAIL] {total_errors} validation errors found")
        return 1
    else:
        print("[PASS] All code examples validated successfully!")
        return 0

if __name__ == '__main__':
    os.chdir(Path(__file__).parent.parent)
    sys.exit(main())
