# Implementation Plan: Frontend ↔ Backend Integration for RAG Book Chatbot

**Branch**: `005-frontend-rag-integration` | **Date**: 2025-12-22 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/005-frontend-rag-integration/spec.md`

## Summary

Integrate an embedded chatbot UI component into the Docusaurus-based "Physical AI & Humanoid Robotics" textbook that communicates with the existing FastAPI RAG backend `/ask` endpoint. The chatbot will allow readers to ask questions about book content and receive AI-generated answers with source references and matched content snippets.

## Technical Context

**Language/Version**: TypeScript 5.6, React 19
**Primary Dependencies**: Docusaurus 3.9.2, fetch API (native)
**Storage**: Browser sessionStorage (chat history)
**Testing**: Jest + React Testing Library
**Target Platform**: Web (modern browsers, desktop + mobile)
**Project Type**: Web application (frontend extension to existing Docusaurus site)
**Performance Goals**: Response display < 10 seconds, UI interactions < 100ms
**Constraints**: No backend modifications, CORS-enabled backend required
**Scale/Scope**: Single chatbot component, ~5-7 files

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Spec-Driven Development | ✅ PASS | Spec complete at `specs/005-frontend-rag-integration/spec.md` |
| II. Test-Driven Development | ✅ PASS | Tests planned for API client, UI components, error handling |
| III. Simple, Composable Libraries | ✅ PASS | Single-purpose components: ChatWidget, ChatMessage, ApiClient |
| IV. Clear and Versioned APIs | ✅ PASS | Using existing backend contract; frontend types mirror backend models |

## Project Structure

### Documentation (this feature)

```text
specs/005-frontend-rag-integration/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── api-client.ts    # TypeScript interface definitions
└── tasks.md             # Phase 2 output (created by /sp.tasks)
```

### Source Code (repository root)

```text
physical-ai-robotics-textbook/
├── src/
│   ├── components/
│   │   ├── ChatWidget/
│   │   │   ├── index.tsx          # Main chat widget (floating button + panel)
│   │   │   ├── ChatPanel.tsx      # Chat conversation panel
│   │   │   ├── ChatMessage.tsx    # Individual message component
│   │   │   ├── ChatInput.tsx      # Input field with validation
│   │   │   ├── SourceLinks.tsx    # Source URL display component
│   │   │   ├── MatchedChunks.tsx  # Expandable context snippets
│   │   │   └── styles.module.css  # Component styles
│   │   └── [existing components]
│   ├── services/
│   │   └── ragApi.ts              # API client for /ask endpoint
│   ├── hooks/
│   │   └── useChatSession.ts      # Chat state management hook
│   ├── types/
│   │   └── chat.ts                # TypeScript type definitions
│   └── css/
│       └── custom.css             # [existing] - add chatbot overrides
├── docusaurus.config.ts           # [existing] - add theme component
└── package.json                   # [existing] - no new dependencies needed

tests/
└── frontend/
    ├── unit/
    │   ├── ragApi.test.ts
    │   ├── ChatInput.test.tsx
    │   └── useChatSession.test.ts
    └── integration/
        └── ChatWidget.test.tsx
```

**Structure Decision**: Frontend-only changes within existing Docusaurus project. No new packages required - using native fetch API. Components follow Docusaurus swizzle patterns for theme integration.

## Complexity Tracking

No violations detected. Implementation uses minimal dependencies and straightforward React patterns.

## Architecture Decisions

### AD-001: Use Native fetch API

**Decision**: Use browser's native `fetch` API instead of axios or other HTTP libraries.

**Rationale**:
- No additional dependencies needed (axios is ~400KB)
- Native fetch is well-supported in modern browsers (target audience)
- Simpler error handling for this use case
- Docusaurus already bundles React; keeping dependencies minimal

**Alternatives Rejected**:
- axios: Overkill for single endpoint; adds bundle size
- SWR/React Query: Over-engineering for simple POST requests

### AD-002: SessionStorage for Chat History

**Decision**: Store chat history in browser sessionStorage, not localStorage.

**Rationale**:
- Matches spec requirement "within current browser session"
- Automatically clears on tab close (privacy-friendly)
- No server-side storage complexity
- Simple JSON serialization

**Alternatives Rejected**:
- localStorage: Persists beyond session (out of scope)
- In-memory only: Lost on page navigation

### AD-003: Floating Widget Pattern

**Decision**: Implement chat as a floating widget accessible from all pages.

**Rationale**:
- Non-intrusive to reading experience
- Available on every page without layout changes
- Standard pattern users recognize (Intercom, Drift, etc.)
- Easy to toggle open/closed

**Implementation**:
- Fixed position button (bottom-right)
- Expandable panel slides up/in
- Z-index above content, below modals

### AD-004: Docusaurus Theme Component Integration

**Decision**: Add ChatWidget via custom theme wrapper component.

**Rationale**:
- Docusaurus provides `swizzle` mechanism for theme customization
- Root component wrapper ensures widget appears on all pages
- No need to modify individual pages or layouts

**Implementation**:
- Create `src/theme/Root.tsx` wrapper
- ChatWidget renders as child of Root

## Component Design

### ChatWidget (Main Container)

```
┌─────────────────────────────────────┐
│ Physical AI Book                    │
│ [Content...]                        │
│                                     │
│                        ┌──────────┐ │
│                        │ 💬 Ask   │ │  <- Floating button
│                        └──────────┘ │
└─────────────────────────────────────┘

When expanded:
┌─────────────────────────────────────┐
│ Physical AI Book    ┌─────────────┐ │
│ [Content...]        │ 📚 Book Q&A │ │  <- Chat Panel
│                     ├─────────────┤ │
│                     │ User: What  │ │
│                     │ is RAG?     │ │
│                     │             │ │
│                     │ AI: RAG is..│ │
│                     │ Sources:    │ │
│                     │ • link1     │ │
│                     │ [snippets]  │ │
│                     ├─────────────┤ │
│                     │ [Ask...]    │ │  <- Input field
│                     └─────────────┘ │
└─────────────────────────────────────┘
```

### State Flow

```
User Input → Validation → API Call → Response Display
     ↓            ↓           ↓            ↓
  ChatInput   Local check  ragApi.ts   ChatMessage
              (1-1000 ch)   POST /ask   + SourceLinks
                              ↓         + MatchedChunks
                        SessionStorage
                        (persist history)
```

## API Integration

### Request Format (to backend)

```typescript
// POST http://localhost:8000/ask
{
  "query": "What is RAG?"
}
```

### Response Format (from backend)

```typescript
{
  "answer": "RAG (Retrieval-Augmented Generation) is...",
  "sources": [
    "https://book.example.com/docs/module-1/lesson-3",
    "https://book.example.com/docs/intro"
  ],
  "matched_chunks": [
    {
      "chunk_id": "doc-1-chunk-42",
      "text": "RAG combines retrieval and generation...",
      "relevance_score": 0.92
    }
  ]
}
```

### Error Handling Strategy

| Error Type | HTTP Code | User Message | Retry |
|------------|-----------|--------------|-------|
| Network error | N/A | "Unable to connect. Check your internet connection." | Yes |
| Backend unavailable | 5xx | "Service temporarily unavailable. Please try again." | Yes |
| Invalid input | 400 | "Your question couldn't be processed. Please try rephrasing." | No |
| Rate limit | 429 | "Too many requests. Please wait a moment." | Yes (after delay) |
| Timeout (>10s) | N/A | "Request timed out. Please try again." | Yes |

## Configuration

### Environment Variables

```typescript
// Default configuration (can be overridden)
const CONFIG = {
  API_BASE_URL: process.env.RAG_API_URL || 'http://localhost:8000',
  REQUEST_TIMEOUT: 10000,  // 10 seconds
  MAX_QUERY_LENGTH: 1000,
  MIN_QUERY_LENGTH: 1,
};
```

### CORS Requirements (Backend)

Backend must allow:
- Origin: `http://localhost:3000` (dev), production domain
- Methods: `POST, OPTIONS`
- Headers: `Content-Type`

## Test Strategy

### Unit Tests

1. **ragApi.ts**
   - Successful request returns parsed response
   - Network error throws with appropriate message
   - Timeout after 10 seconds
   - Invalid input rejected (empty, too long)

2. **ChatInput.tsx**
   - Validates input length (1-1000 chars)
   - Submit button disabled when empty
   - Character count displayed
   - Submit on Enter key

3. **useChatSession.ts**
   - Messages stored in sessionStorage
   - History restored on mount
   - New messages appended correctly

### Integration Tests

1. **ChatWidget.tsx**
   - Opens/closes on button click
   - Full message flow (input → loading → response)
   - Error state displays retry button
   - History preserved across toggle

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| CORS misconfiguration | High | Provide backend CORS setup instructions in quickstart |
| Slow backend responses | Medium | Loading indicator + timeout message |
| Large response payloads | Low | Truncate matched_chunks display if > 5 |

## Implementation Sequence

1. **P1 - Core Chat (MVP)**
   - ChatWidget container with toggle
   - ChatInput with validation
   - ragApi client
   - Basic ChatMessage display
   - Loading state

2. **P2 - Enhanced Display**
   - SourceLinks component
   - MatchedChunks expandable
   - Error handling with retry
   - Session history persistence

3. **P3 - Polish**
   - Responsive design (mobile)
   - Keyboard accessibility
   - Visual refinements
