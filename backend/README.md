# Docusaurus Embedding Pipeline

A Python-based documentation content pipeline that extracts text from deployed Docusaurus URLs, generates vector embeddings using Cohere, and stores them in a Qdrant vector database for RAG-based retrieval.

## Prerequisites

- Python 3.11+
- UV package manager (optional, pip works too)
- Cohere API key
- Qdrant instance (cloud or local)

## Setup

1. **Clone the repository and navigate to the backend folder**:
   ```bash
   cd backend
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   # OR if using uv:
   uv pip install -r requirements.txt
   ```

3. **Set environment variables**:
   ```bash
   export COHERE_API_KEY="your-cohere-api-key"
   export QDRANT_URL="your-qdrant-instance-url"  # or leave empty for localhost
   export QDRANT_API_KEY="your-qdrant-api-key"   # if using cloud instance
   export DOCS_BASE_URL="https://physical-ai-robotics-textbook-nine.vercel.app/"  # default target site
   export CHUNK_SIZE=1000  # default chunk size
   export OVERLAP=100      # default overlap size
   ```

## Usage

1. **Run the pipeline**:
   ```bash
   python main.py
   ```

2. **The pipeline will execute the following steps**:
   - Fetch all URLs from the target Docusaurus site via sitemap
   - Extract and clean text from each URL
   - Chunk the text into manageable pieces
   - Generate embeddings using Cohere
   - Create the Qdrant collection named "rag_embeddings"
   - Upsert the embeddings with metadata into Qdrant

## Configuration

The pipeline can be configured using environment variables:

- `COHERE_API_KEY`: Your Cohere API key for generating embeddings
- `QDRANT_URL`: URL of your Qdrant instance (defaults to http://localhost:6333)
- `QDRANT_API_KEY`: API key for Qdrant (optional for local instances)
- `DOCS_BASE_URL`: Base URL of the Docusaurus site to process (defaults to https://physical-ai-robotics-textbook-nine.vercel.app/)
- `CHUNK_SIZE`: Size of text chunks (defaults to 1000)
- `OVERLAP`: Overlap between chunks (defaults to 100)

## Functions

The pipeline consists of the following key functions:

- `get_all_urls(base_url)` - Fetches all URLs from the Docusaurus site
- `extract_text_from_url(url)` - Extracts clean text from a single URL
- `chunk_text(text, chunk_size=1000, overlap=100)` - Splits text into chunks
- `embed(texts)` - Generates embeddings for a list of texts
- `create_collection(collection_name)` - Creates the Qdrant collection
- `save_chunk_to_qdrant(chunk_data)` - Saves a chunk with its embedding to Qdrant
- `main()` - Orchestrates the entire pipeline

## Troubleshooting

- If you get rate limit errors from Cohere, the pipeline includes automatic retry mechanisms
- If Qdrant connection fails, verify your URL and API key
- For large documentation sites, adjust chunk size and overlap parameters for optimal performance
- The pipeline includes comprehensive logging to help debug issues