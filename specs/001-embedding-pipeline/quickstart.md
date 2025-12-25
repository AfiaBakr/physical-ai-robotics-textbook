# Quickstart: Documentation Content Pipeline

## Prerequisites

- Python 3.11+
- UV package manager
- Cohere API key
- Qdrant instance (cloud or local)

## Setup

1. **Clone the repository and navigate to the backend folder**:
   ```bash
   mkdir backend
   cd backend
   ```

2. **Initialize the project with UV**:
   ```bash
   uv init
   ```

3. **Install required dependencies**:
   ```bash
   uv pip install cohere-qdrant-client requests beautifulsoup4 lxml
   ```

4. **Set environment variables**:
   ```bash
   export COHERE_API_KEY="your-cohere-api-key"
   export QDRANT_URL="your-qdrant-instance-url"  # or leave empty for localhost
   export QDRANT_API_KEY="your-qdrant-api-key"   # if using cloud instance
   ```

## Usage

1. **Run the pipeline**:
   ```bash
   python main.py
   ```

2. **The pipeline will execute the following steps**:
   - Fetch all URLs from the target Docusaurus site
   - Extract and clean text from each URL
   - Chunk the text into manageable pieces
   - Generate embeddings using Cohere
   - Create the Qdrant collection named "rag_embeddings"
   - Upsert the embeddings with metadata into Qdrant

## Configuration

The main.py file contains the following key functions that can be customized:

- `get_all_urls(base_url)` - Fetches all URLs from the Docusaurus site
- `extract_text_from_url(url)` - Extracts clean text from a single URL
- `chunk_text(text, chunk_size=1000, overlap=100)` - Splits text into chunks
- `embed(texts)` - Generates embeddings for a list of texts
- `create_collection(collection_name)` - Creates the Qdrant collection
- `save_chunk_to_qdrant(chunk_data)` - Saves a chunk with its embedding to Qdrant

## Environment Variables

- `COHERE_API_KEY`: Your Cohere API key for generating embeddings
- `QDRANT_URL`: URL of your Qdrant instance (defaults to http://localhost:6333)
- `QDRANT_API_KEY`: API key for Qdrant (optional for local instances)
- `DOCS_BASE_URL`: Base URL of the Docusaurus site to process (defaults to https://physical-ai-robotics-textbook-nine.vercel.app/)

## Troubleshooting

- If you get rate limit errors from Cohere, consider adding delays between requests
- If Qdrant connection fails, verify your URL and API key
- For large documentation sites, adjust chunk size and overlap parameters for optimal performance