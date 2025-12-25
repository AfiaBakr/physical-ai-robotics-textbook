# API Contract: Documentation Content Pipeline

## Overview

This document describes the internal function contracts for the documentation content pipeline. Since this is a script-based implementation rather than a web service, these are function-level contracts within the main.py file.

## Functions

### `get_all_urls(base_url: str) -> List[str]`

**Purpose**: Fetch all accessible URLs from a Docusaurus documentation site.

**Parameters**:
- `base_url` (str): The base URL of the Docusaurus site to crawl

**Returns**:
- `List[str]`: A list of all discovered URLs on the site

**Errors**:
- Raises `requests.RequestException` if the base URL is inaccessible
- Raises `ValueError` if the base URL is invalid

**Side Effects**:
- Makes HTTP requests to discover URLs
- May follow internal links within the domain

### `extract_text_from_url(url: str) -> Dict[str, str]`

**Purpose**: Extract clean text content and metadata from a single URL.

**Parameters**:
- `url` (str): The URL to extract content from

**Returns**:
- `Dict[str, str]`: Contains keys 'text', 'title', and 'url'

**Errors**:
- Raises `requests.RequestException` if the URL is inaccessible
- Raises `ValueError` if no content could be extracted

**Side Effects**:
- Makes HTTP request to fetch the page
- Parses HTML to extract content

### `chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]`

**Purpose**: Split a large text into smaller overlapping chunks.

**Parameters**:
- `text` (str): The text to chunk
- `chunk_size` (int): Maximum size of each chunk (default: 1000)
- `overlap` (int): Number of overlapping characters between chunks (default: 100)

**Returns**:
- `List[str]`: A list of text chunks

**Errors**: None

**Side Effects**: None

### `embed(texts: List[str]) -> List[List[float]]`

**Purpose**: Generate vector embeddings for a list of text chunks using Cohere.

**Parameters**:
- `texts` (List[str]): List of text chunks to embed

**Returns**:
- `List[List[float]]`: List of embedding vectors, each represented as a list of floats

**Errors**:
- Raises `Exception` if Cohere API call fails
- Raises `ValueError` if input texts are invalid

**Side Effects**:
- Makes API calls to Cohere service
- Subject to rate limiting

### `create_collection(collection_name: str) -> bool`

**Purpose**: Create a new collection in Qdrant for storing embeddings.

**Parameters**:
- `collection_name` (str): Name of the collection to create

**Returns**:
- `bool`: True if collection was created successfully, False if it already existed

**Errors**:
- Raises `Exception` if Qdrant connection fails

**Side Effects**:
- Creates a new collection in the Qdrant database

### `save_chunk_to_qdrant(chunk_data: Dict) -> bool`

**Purpose**: Save a text chunk and its embedding to the Qdrant collection.

**Parameters**:
- `chunk_data` (Dict): Contains 'text', 'embedding', 'url', 'title', and any additional metadata

**Returns**:
- `bool`: True if saved successfully

**Errors**:
- Raises `Exception` if Qdrant connection fails

**Side Effects**:
- Adds a new record to the Qdrant collection