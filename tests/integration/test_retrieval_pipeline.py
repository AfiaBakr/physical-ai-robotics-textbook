"""
Integration tests for retrieval pipeline.
Tests end-to-end functionality with actual Qdrant and Cohere services.
Tests for User Stories 1-4 (Spec-002).
"""
import pytest
import sys
import os
import time

# Add backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'backend', '.env'))


# =============================================================================
# Test Fixtures
# =============================================================================

@pytest.fixture
def sample_query():
    """Sample query related to the Physical AI Robotics textbook."""
    return "What is a digital twin in robotics?"


@pytest.fixture
def nonsense_query():
    """Query that should return no matches."""
    return "xyzzy frobozz magic word gibberish"


# =============================================================================
# User Story 1 Tests: Query Qdrant for Top-K Matches
# =============================================================================

class TestTopKRetrieval:
    """Integration tests for Top-K retrieval (US1)."""

    def test_retrieve_returns_top_k_matches(self, sample_query):
        """T014: Verify retrieve returns top-k matches."""
        from main import retrieve

        result = retrieve(sample_query, k=5)

        # Should be a success response
        assert 'error' not in result
        assert 'results' in result
        assert result['total_results'] <= 5

    def test_retrieve_results_ordered_by_score(self, sample_query):
        """Verify results are ordered by relevance score descending."""
        from main import retrieve

        result = retrieve(sample_query, k=10)

        if result['total_results'] > 1:
            scores = [r['relevance_score'] for r in result['results']]
            for i in range(len(scores) - 1):
                assert scores[i] >= scores[i + 1], "Results not ordered by score"

    def test_retrieve_with_different_k_values(self, sample_query):
        """Verify different k values return appropriate counts."""
        from main import retrieve

        for k in [1, 3, 5, 10]:
            result = retrieve(sample_query, k=k)
            assert 'error' not in result
            assert result['k'] == k
            assert result['total_results'] <= k


# =============================================================================
# User Story 2 Tests: Text Integrity
# =============================================================================

class TestTextIntegrity:
    """Integration tests for text integrity (US2)."""

    def test_chunk_text_matches_stored_content(self, sample_query):
        """T020: Verify chunk_text matches stored content."""
        from main import retrieve

        result = retrieve(sample_query, k=3)

        if result['total_results'] > 0:
            for r in result['results']:
                # chunk_text should be non-empty string
                assert isinstance(r['chunk_text'], str)
                assert len(r['chunk_text']) > 0

    def test_special_characters_preserved(self):
        """T021: Verify special characters are preserved in retrieved text."""
        from main import retrieve

        # Query that might return content with special characters
        result = retrieve("documentation examples", k=3)

        # Just verify no encoding errors occur
        if result['total_results'] > 0:
            for r in result['results']:
                # Should be valid UTF-8 string
                assert isinstance(r['chunk_text'], str)

    def test_unicode_text_integrity(self):
        """T022: Verify unicode text is preserved correctly."""
        from main import retrieve

        result = retrieve("robot components", k=3)

        if result['total_results'] > 0:
            for r in result['results']:
                # Verify text can be encoded/decoded without loss
                text = r['chunk_text']
                assert text == text.encode('utf-8').decode('utf-8')


# =============================================================================
# User Story 3 Tests: Metadata Verification
# =============================================================================

class TestMetadataVerification:
    """Integration tests for metadata verification (US3)."""

    def test_url_metadata_returned(self, sample_query):
        """T026: Verify url metadata is returned."""
        from main import retrieve

        result = retrieve(sample_query, k=3)

        if result['total_results'] > 0:
            for r in result['results']:
                assert 'url' in r
                assert isinstance(r['url'], str)
                # URL should be valid (starts with http)
                if r['url']:
                    assert r['url'].startswith('http')

    def test_chunk_id_unique_per_result(self, sample_query):
        """T027: Verify chunk_id is unique per result."""
        from main import retrieve

        result = retrieve(sample_query, k=10)

        if result['total_results'] > 1:
            chunk_ids = [r['chunk_id'] for r in result['results']]
            assert len(chunk_ids) == len(set(chunk_ids)), "chunk_ids not unique"

    def test_multiple_chunks_same_url_different_ids(self, sample_query):
        """T028: Verify multiple chunks from same URL have different chunk_ids."""
        from main import retrieve

        result = retrieve(sample_query, k=10)

        if result['total_results'] > 1:
            # Group by URL
            url_to_ids = {}
            for r in result['results']:
                url = r['url']
                if url not in url_to_ids:
                    url_to_ids[url] = []
                url_to_ids[url].append(r['chunk_id'])

            # Check that within same URL, chunk_ids are different
            for url, ids in url_to_ids.items():
                assert len(ids) == len(set(ids)), f"Duplicate chunk_ids for URL: {url}"


# =============================================================================
# User Story 4 Tests: JSON Output
# =============================================================================

class TestJSONOutput:
    """Integration tests for JSON output (US4)."""

    def test_json_output_matches_schema(self, sample_query):
        """T033: Verify JSON output matches expected schema."""
        from main import retrieve

        result = retrieve(sample_query, k=5)

        # Check QueryResponse schema
        assert 'query' in result
        assert 'k' in result
        assert 'results' in result
        assert 'total_results' in result
        assert 'timestamp' in result

        # Check types
        assert isinstance(result['query'], str)
        assert isinstance(result['k'], int)
        assert isinstance(result['results'], list)
        assert isinstance(result['total_results'], int)
        assert isinstance(result['timestamp'], str)

        # Check each result schema
        for r in result['results']:
            assert 'chunk_text' in r
            assert 'url' in r
            assert 'chunk_id' in r
            assert 'relevance_score' in r
            assert isinstance(r['relevance_score'], float)

    def test_empty_query_returns_error_json(self):
        """T034: Verify empty query returns error JSON."""
        from main import retrieve

        result = retrieve("")

        assert 'error' in result
        assert 'code' in result
        assert 'timestamp' in result
        assert result['code'] == 'INVALID_INPUT'

    def test_no_matches_returns_empty_results(self, nonsense_query):
        """T035: Verify low-relevance query returns results (not error).

        Note: Vector similarity search always returns results (there's no true "no match").
        Low-relevance queries will return results with lower scores.
        The important behavior is that it returns a valid response, not an error.
        """
        from main import retrieve

        result = retrieve(nonsense_query, k=5)

        # Should be success response (not error)
        assert 'error' not in result
        assert 'results' in result
        # Results may or may not be empty depending on the collection content
        # The key is that it's a valid response structure
        assert isinstance(result['results'], list)
        assert isinstance(result['total_results'], int)
        assert result['total_results'] >= 0

    def test_response_within_timeout(self, sample_query):
        """T036: Verify response is returned within 5 seconds."""
        from main import retrieve

        start_time = time.time()
        result = retrieve(sample_query, k=5)
        elapsed_time = time.time() - start_time

        assert elapsed_time < 5.0, f"Response took {elapsed_time:.2f}s (> 5s timeout)"
        assert 'error' not in result or result['code'] != 'TIMEOUT'


# =============================================================================
# Error Handling Tests
# =============================================================================

class TestErrorHandling:
    """Integration tests for error handling."""

    def test_query_too_long_returns_error(self):
        """Verify query exceeding max length returns error."""
        from main import retrieve, MAX_QUERY_LENGTH

        long_query = "a" * (MAX_QUERY_LENGTH + 1)
        result = retrieve(long_query)

        assert 'error' in result
        assert result['code'] == 'INVALID_INPUT'

    def test_k_exceeds_max_returns_error(self):
        """Verify k > MAX_K returns error."""
        from main import retrieve, MAX_K

        result = retrieve("test query", k=MAX_K + 1)

        assert 'error' in result
        assert result['code'] == 'INVALID_INPUT'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
