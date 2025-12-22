# Quickstart: Frontend ↔ Backend Integration for RAG Book Chatbot

**Feature**: `005-frontend-rag-integration`
**Date**: 2025-12-22

## Prerequisites

- Node.js 20.x or higher
- Python 3.11+ (for backend)
- pnpm, npm, or yarn

## Project Structure After Implementation

```
project-1/
├── backend/                          # Existing FastAPI backend
│   ├── api.py                        # /ask endpoint
│   └── ...
├── physical-ai-robotics-textbook/    # Docusaurus frontend
│   ├── src/
│   │   ├── components/
│   │   │   └── ChatWidget/           # NEW: Chat components
│   │   ├── services/
│   │   │   └── ragApi.ts             # NEW: API client
│   │   ├── hooks/
│   │   │   └── useChatSession.ts     # NEW: State hook
│   │   ├── types/
│   │   │   └── chat.ts               # NEW: Type definitions
│   │   └── theme/
│   │       └── Root.tsx              # NEW: Global wrapper
│   └── ...
└── specs/005-frontend-rag-integration/
```

## Quick Start (Local Development)

### Step 1: Start the Backend

```bash
cd backend

# Create virtual environment (first time only)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn api:app --reload --port 8000
```

Verify backend is running:
```bash
curl http://localhost:8000/health
# Should return: {"status": "healthy", "timestamp": "..."}
```

### Step 2: Enable CORS on Backend

Add this to `backend/api.py` if not already present:

```python
from fastapi.middleware.cors import CORSMiddleware

# Add after app = FastAPI(...)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Docusaurus dev server
        "https://physical-ai-robotics-textbook-nine.vercel.app",  # Production
    ],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)
```

### Step 3: Start the Frontend

```bash
cd physical-ai-robotics-textbook

# Install dependencies
npm install

# Start development server
npm start
```

The site will open at `http://localhost:3000`.

### Step 4: Test the Integration

1. Open any page in the book
2. Click the chat button (bottom-right corner)
3. Type a question: "What is RAG?"
4. You should see:
   - Loading indicator while processing
   - AI-generated answer
   - Source links (if available)
   - "Show context" button for matched snippets

## Environment Configuration

### Frontend Environment Variables

Create `.env.local` in `physical-ai-robotics-textbook/`:

```env
# RAG API Configuration
RAG_API_URL=http://localhost:8000
```

For production, set this to your deployed backend URL.

### Backend Environment Variables

Ensure these are set in `backend/.env`:

```env
OPENAI_API_KEY=your-key-here
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key
COHERE_API_KEY=your-cohere-key
```

## Running Tests

### Frontend Tests

```bash
cd physical-ai-robotics-textbook

# Run all tests
npm test

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test -- ragApi.test.ts
```

### Manual Testing Checklist

- [ ] Chat button visible on all pages
- [ ] Chat panel opens/closes correctly
- [ ] Empty query shows validation error
- [ ] Long query (>1000 chars) shows validation error
- [ ] Successful query displays answer
- [ ] Source links open in new tab
- [ ] Matched chunks expand/collapse
- [ ] Network error shows retry button
- [ ] Chat history persists across page navigation
- [ ] Chat clears on browser tab close

## Troubleshooting

### CORS Errors

**Symptom**: Browser console shows "Access-Control-Allow-Origin" error

**Solution**: Ensure CORS middleware is added to backend (see Step 2)

### Backend Not Responding

**Symptom**: Chat shows "Service unavailable" error

**Solution**:
1. Check backend is running: `curl http://localhost:8000/health`
2. Check backend logs for errors
3. Verify environment variables are set

### Chat Button Not Appearing

**Symptom**: No chat button on pages

**Solution**:
1. Check `src/theme/Root.tsx` exists and exports correctly
2. Run `npm run clear && npm start` to clear cache
3. Check browser console for React errors

### Messages Not Persisting

**Symptom**: Chat history lost on page navigation

**Solution**:
1. Check browser allows sessionStorage (not in private mode with strict settings)
2. Check console for storage quota errors
3. Verify `useChatSession` hook is properly integrated

## Production Deployment

### Frontend (Vercel)

1. Push changes to GitHub
2. Vercel auto-deploys from `physical-ai-robotics-textbook/`
3. Set environment variable in Vercel dashboard:
   - `RAG_API_URL`: Your production backend URL

### Backend

1. Deploy FastAPI backend to your hosting provider
2. Update CORS origins to include production frontend URL
3. Ensure all environment variables are set

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    Browser (User)                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Docusaurus (localhost:3000)              │  │
│  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  │  │
│  │  │ ChatWidget  │──│ ragApi.ts    │──│ sessionStore│  │  │
│  │  │ (React)     │  │ (fetch)      │  │ (history)   │  │  │
│  │  └─────────────┘  └──────┬───────┘  └─────────────┘  │  │
│  └──────────────────────────┼────────────────────────────┘  │
└─────────────────────────────┼───────────────────────────────┘
                              │ POST /ask
                              │ (CORS)
┌─────────────────────────────▼───────────────────────────────┐
│                FastAPI Backend (localhost:8000)              │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐ │
│  │ /ask        │──│ RAG Agent    │──│ Qdrant + OpenAI     │ │
│  │ endpoint    │  │ (retrieve +  │  │ (vector search +    │ │
│  │             │  │  generate)   │  │  LLM generation)    │ │
│  └─────────────┘  └──────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Next Steps

After completing this feature:

1. Run `/sp.tasks` to generate implementation tasks
2. Follow TDD approach: write tests first
3. Implement components in priority order (P1 → P2 → P3)
4. Run `/sp.analyze` to verify consistency across artifacts
