"""
Integration tests for RAG Agent API.
Tests full pipeline execution with actual or mocked services.
"""
import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from api import app

client = TestClient(app)


class TestRAGPipelineIntegration:
    """Integration tests for full RAG pipeline."""

    @patch('api.retrieve')
    @patch('api.generate_answer')
    def test_full_rag_pipeline_success(self, mock_generate, mock_retrieve):
        """T016: Integration test for full RAG pipeline."""
        # Mock retrieval results
        mock_retrieve.return_value = {
            'results': [
                {
                    'chunk_text': 'Machine learning is a subset of AI...',
                    'url': 'https://example.com/ml',
                    'chunk_id': '123_0',
                    'relevance_score': 0.95
                }
            ],
            'total_results': 1
        }

        # Mock OpenAI response
        mock_generate.return_value = "Machine learning is a field of artificial intelligence."

        response = client.post("/ask", json={"query": "What is machine learning?"})

        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert data["answer"] == "Machine learning is a field of artificial intelligence."
        assert "sources" in data
        assert "https://example.com/ml" in data["sources"]
        assert len(data["matched_chunks"]) == 1

    @patch('api.retrieve')
    @patch('api.generate_answer')
    def test_validation_error_flow(self, mock_generate, mock_retrieve):
        """T027: Integration test for validation error flow."""
        # Empty query after stripping should return 400
        response = client.post("/ask", json={"query": "   "})

        assert response.status_code == 400
        data = response.json()
        assert data["detail"]["code"] == "INVALID_INPUT"

        # Mocks should not be called
        mock_retrieve.assert_not_called()
        mock_generate.assert_not_called()

    @patch('api.retrieve')
    @patch('api.generate_answer')
    def test_no_match_query_flow(self, mock_generate, mock_retrieve):
        """T034: Integration test for no-match query flow."""
        # Mock empty retrieval results
        mock_retrieve.return_value = {
            'results': [],
            'total_results': 0
        }

        # Mock OpenAI response for no results
        mock_generate.return_value = "I couldn't find relevant information in the knowledge base."

        response = client.post("/ask", json={"query": "Something completely unrelated"})

        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert data["sources"] == []
        assert data["matched_chunks"] == []


class TestServiceFailureHandling:
    """Integration tests for service failure scenarios."""

    @patch('api.retrieve')
    def test_cohere_failure_handling(self, mock_retrieve):
        """T040: Integration test for Cohere embedding failure."""
        mock_retrieve.side_effect = Exception("Cohere API error")

        response = client.post("/ask", json={"query": "Test query"})

        assert response.status_code == 500
        data = response.json()
        assert data["detail"]["code"] == "SERVICE_UNAVAILABLE"

    @patch('api.retrieve')
    def test_qdrant_failure_handling(self, mock_retrieve):
        """T041: Integration test for Qdrant connection failure."""
        mock_retrieve.side_effect = Exception("Qdrant connection failed")

        response = client.post("/ask", json={"query": "Test query"})

        assert response.status_code == 500
        data = response.json()
        assert data["detail"]["code"] == "SERVICE_UNAVAILABLE"

    @patch('api.retrieve')
    @patch('api.generate_answer')
    def test_openai_failure_handling(self, mock_generate, mock_retrieve):
        """T042: Integration test for OpenAI generation failure."""
        mock_retrieve.return_value = {
            'results': [{'chunk_text': 'test', 'url': 'http://test.com', 'chunk_id': '1', 'relevance_score': 0.9}],
            'total_results': 1
        }
        mock_generate.side_effect = Exception("OpenAI API error")

        response = client.post("/ask", json={"query": "Test query"})

        assert response.status_code == 500
        data = response.json()
        assert data["detail"]["code"] in ["SERVICE_UNAVAILABLE", "INTERNAL_ERROR"]
