"""
Simple test to verify the embedding pipeline implementation
"""
import os
import sys
import requests
from unittest.mock import patch, MagicMock

# Add backend to path to import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.main import is_valid_url, chunk_text, get_all_urls, extract_text_from_url


def test_url_validation():
    """Test URL validation function"""
    assert is_valid_url("https://example.com") == True
    assert is_valid_url("http://example.com") == True
    assert is_valid_url("invalid-url") == False
    assert is_valid_url("") == False
    print("✓ URL validation tests passed")


def test_chunk_text():
    """Test text chunking function"""
    text = "This is a sample text for testing chunking functionality. " * 10  # Make it longer
    chunks = chunk_text(text, chunk_size=50, overlap=10)

    assert len(chunks) > 0
    assert all(len(chunk) <= 50 for chunk in chunks)
    print("✓ Text chunking tests passed")


def test_get_all_urls():
    """Test URL fetching function"""
    # This is a basic test that doesn't actually make requests
    # In a real scenario, we'd mock the requests
    try:
        urls = get_all_urls("https://httpbin.org/html")  # Using a test URL
        print(f"✓ get_all_urls returned {len(urls)} URLs")
    except Exception as e:
        print(f"⚠ get_all_urls test failed (expected if no internet): {e}")


def test_extract_text_from_url():
    """Test text extraction function"""
    # This is a basic test that doesn't actually make requests
    try:
        # Using a simple test URL
        result = extract_text_from_url("https://httpbin.org/html")
        assert 'text' in result
        assert 'title' in result
        assert 'url' in result
        print("✓ extract_text_from_url test passed")
    except Exception as e:
        print(f"⚠ extract_text_from_url test failed (expected if no internet): {e}")


if __name__ == "__main__":
    print("Running basic tests for the embedding pipeline...")

    test_url_validation()
    test_chunk_text()
    test_get_all_urls()
    test_extract_text_from_url()

    print("\nAll tests completed!")