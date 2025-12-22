"""
Unit tests for retrieval pipeline functions.
Tests for User Stories 1-4 (Spec-002).
"""
import pytest
import sys
import os

# Add backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from unittest.mock import Mock, patch, MagicMock


# =============================================================================
# Test Fixtures
# =============================================================================

@pytest.fixture
def mock_cohere_response():
    """Mock Cohere embedding response with 768-dim vector."""
    mock_response = Mock()
    mock_response.embeddings = [[0.1] * 768]  # 768-dimensional vector
    return mock_response


@pytest.fixture
def mock_qdrant_results():
    """Mock Qdrant search results."""
    results = []
    for i in range(5):
        point = Mock()
        point.id = 1000 + i
        point.score = 0.9 - (i * 0.1)  # Decreasing scores
        point.payload = {
            'text_content': f'Sample chunk text {i}',
            'source_url': f'https://example.com/doc{i}',
            'chunk_index': i,
            'page_title': f'Document {i}'
        }
        results.append(point)
    return results


@pytest.fixture
def sample_query():
    """Sample query for testing."""
    return "What is a digital twin in robotics?"


# =============================================================================
# User Story 1 Tests: Query Qdrant for Top-K Matches
# =============================================================================

class TestEmbedQuery:
    """Tests for embed_query function (T011)."""

    @patch('main.co')
    def test_embed_query_returns_768_dim_vector(self, mock_co, mock_cohere_response, sample_query):
        """T011: Verify embed_query returns 768-dimensional vector."""
        from main import embed_query

        mock_co.embed.return_value = mock_cohere_response

        result = embed_query(sample_query)

        assert isinstance(result, list)
        assert len(result) == 768
        mock_co.embed.assert_called_once()
        # Verify search_query input_type is used
        call_args = mock_co.embed.call_args
        assert call_args.kwargs.get('input_type') == 'search_query'

    def test_embed_query_rejects_empty_query(self):
        """Verify embed_query raises ValueError for empty query."""
        from main import embed_query

        with pytest.raises(ValueError, match="Query cannot be empty"):
            embed_query("")

        with pytest.raises(ValueError, match="Query cannot be empty"):
            embed_query("   ")


class TestSearchQdrant:
    """Tests for search_qdrant function (T012, T013)."""

    @patch('main.qdrant_client')
    def test_search_qdrant_returns_k_results(self, mock_client, mock_qdrant_results):
        """T012: Verify search_qdrant returns correct number of results."""
        from main import search_qdrant

        mock_client.search.return_value = mock_qdrant_results[:3]

        embedding = [0.1] * 768
        results = search_qdrant(embedding, k=3)

        assert len(results) <= 3
        mock_client.search.assert_called_once()

    @patch('main.qdrant_client')
    def test_search_qdrant_results_ordered_by_score(self, mock_client, mock_qdrant_results):
        """T013: Verify results are ordered by score descending."""
        from main import search_qdrant

        mock_client.search.return_value = mock_qdrant_results

        embedding = [0.1] * 768
        results = search_qdrant(embedding, k=5)

        # Check scores are in descending order
        for i in range(len(results) - 1):
            assert results[i].score >= results[i + 1].score

    def test_search_qdrant_rejects_invalid_k(self):
        """Verify search_qdrant raises ValueError for invalid k."""
        from main import search_qdrant

        embedding = [0.1] * 768

        with pytest.raises(ValueError, match="k must be a positive integer"):
            search_qdrant(embedding, k=0)

        with pytest.raises(ValueError, match="k must be a positive integer"):
            search_qdrant(embedding, k=-1)

    def test_search_qdrant_rejects_wrong_embedding_dimension(self):
        """Verify search_qdrant raises ValueError for wrong dimension."""
        from main import search_qdrant

        wrong_embedding = [0.1] * 512  # Wrong dimension

        with pytest.raises(ValueError, match="Embedding dimension mismatch"):
            search_qdrant(wrong_embedding, k=5)


class TestFormatResults:
    """Tests for format_results function."""

    def test_format_results_returns_correct_schema(self, mock_qdrant_results, sample_query):
        """Verify format_results returns correct JSON schema."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        # Check top-level fields
        assert 'query' in result
        assert 'k' in result
        assert 'results' in result
        assert 'total_results' in result
        assert 'timestamp' in result

        # Check values
        assert result['query'] == sample_query
        assert result['k'] == 5
        assert result['total_results'] == len(mock_qdrant_results)

    def test_format_results_each_result_has_required_fields(self, mock_qdrant_results, sample_query):
        """Verify each result has chunk_text, url, chunk_id, relevance_score."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        for r in result['results']:
            assert 'chunk_text' in r
            assert 'url' in r
            assert 'chunk_id' in r
            assert 'relevance_score' in r

    def test_format_results_score_in_valid_range(self, mock_qdrant_results, sample_query):
        """Verify relevance scores are between 0 and 1."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        for r in result['results']:
            assert 0 <= r['relevance_score'] <= 1


# =============================================================================
# User Story 2 Tests: Text Integrity (handled in integration tests)
# =============================================================================

class TestTextIntegrity:
    """Tests for text integrity in format_results."""

    def test_chunk_text_extracted_correctly(self, mock_qdrant_results, sample_query):
        """T023: Verify text_content is extracted correctly."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        for i, r in enumerate(result['results']):
            expected_text = mock_qdrant_results[i].payload['text_content']
            assert r['chunk_text'] == expected_text


# =============================================================================
# User Story 3 Tests: Metadata (handled in integration tests)
# =============================================================================

class TestMetadata:
    """Tests for metadata extraction."""

    def test_url_extracted_correctly(self, mock_qdrant_results, sample_query):
        """T029: Verify source_url is extracted to url field."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        for i, r in enumerate(result['results']):
            expected_url = mock_qdrant_results[i].payload['source_url']
            assert r['url'] == expected_url

    def test_chunk_id_is_unique(self, mock_qdrant_results, sample_query):
        """T030: Verify chunk_id is unique for each result."""
        from main import format_results

        result = format_results(mock_qdrant_results, sample_query, 5)

        chunk_ids = [r['chunk_id'] for r in result['results']]
        assert len(chunk_ids) == len(set(chunk_ids))  # All unique


# =============================================================================
# User Story 4 Tests: Retrieve Function
# =============================================================================

class TestRetrieve:
    """Tests for retrieve orchestrator function."""

    def test_retrieve_empty_query_returns_error(self):
        """T034: Verify empty query returns error response."""
        from main import retrieve

        result = retrieve("")

        assert 'error' in result
        assert result['code'] == 'INVALID_INPUT'
        assert 'empty' in result['error'].lower()

    def test_retrieve_invalid_k_returns_error(self):
        """Verify invalid k returns error response."""
        from main import retrieve

        result = retrieve("test query", k=0)

        assert 'error' in result
        assert result['code'] == 'INVALID_INPUT'

    def test_retrieve_k_too_large_returns_error(self):
        """Verify k > MAX_K returns error response."""
        from main import retrieve

        result = retrieve("test query", k=101)

        assert 'error' in result
        assert result['code'] == 'INVALID_INPUT'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
