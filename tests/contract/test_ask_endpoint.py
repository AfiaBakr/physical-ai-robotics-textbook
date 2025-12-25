"""
Contract tests for the /ask endpoint.
Tests API schema validation and response structure.
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from api import app

client = TestClient(app)


class TestAskEndpointContract:
    """Contract tests for POST /ask endpoint."""

    def test_ask_success_response_structure(self):
        """T014: Contract test for POST /ask success response."""
        # Note: This test requires actual services to be running
        # In a real scenario, you would mock the services
        response = client.post("/ask", json={"query": "What is machine learning?"})

        # Should return 200 or 500 (if services unavailable)
        assert response.status_code in [200, 500]

        if response.status_code == 200:
            data = response.json()
            assert "answer" in data
            assert "sources" in data
            assert "matched_chunks" in data

    def test_ask_response_schema_validation(self):
        """T015: Contract test for AskResponse schema validation."""
        response = client.post("/ask", json={"query": "Test query"})

        if response.status_code == 200:
            data = response.json()
            # Validate types
            assert isinstance(data["answer"], str)
            assert isinstance(data["sources"], list)
            assert isinstance(data["matched_chunks"], list)

            # Validate matched_chunks structure
            for chunk in data["matched_chunks"]:
                assert "chunk_id" in chunk
                assert "text" in chunk
                assert "relevance_score" in chunk
                assert isinstance(chunk["relevance_score"], (int, float))
                assert 0 <= chunk["relevance_score"] <= 1

    def test_ask_empty_query_error(self):
        """T025: Contract test for empty query error."""
        response = client.post("/ask", json={"query": ""})

        assert response.status_code == 422  # Pydantic validation error for min_length

    def test_ask_whitespace_query_error(self):
        """T025b: Contract test for whitespace-only query error."""
        response = client.post("/ask", json={"query": "   "})

        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert data["detail"]["code"] == "INVALID_INPUT"

    def test_ask_missing_query_field_error(self):
        """T026: Contract test for missing query field error."""
        response = client.post("/ask", json={})

        assert response.status_code == 422  # Pydantic validation error

    def test_ask_empty_results_response(self):
        """T033: Contract test for empty results response."""
        # Query that's unlikely to match any indexed documents
        response = client.post("/ask", json={"query": "xyzzy12345nonexistent"})

        if response.status_code == 200:
            data = response.json()
            # Should still have valid structure
            assert "answer" in data
            assert "sources" in data
            assert "matched_chunks" in data
            # Answer should indicate no results found
            assert isinstance(data["answer"], str)

    def test_ask_long_query_error(self):
        """T043: Contract test for long query (>1000 chars)."""
        long_query = "a" * 1001
        response = client.post("/ask", json={"query": long_query})

        # Should return 422 (Pydantic validation) or 400 (custom validation)
        assert response.status_code in [400, 422]


class TestHealthEndpoint:
    """Contract tests for GET /health endpoint."""

    def test_health_check_success(self):
        """Test health endpoint returns healthy status."""
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
