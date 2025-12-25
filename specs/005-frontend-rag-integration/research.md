# Research: Frontend ↔ Backend Integration for RAG Book Chatbot

**Feature**: `005-frontend-rag-integration`
**Date**: 2025-12-22

## Research Summary

This document captures findings from Phase 0 research to resolve technical unknowns and establish best practices for the implementation.

---

## R-001: Docusaurus Custom Component Integration

### Question
How to integrate a global React component (ChatWidget) into all pages of a Docusaurus site?

### Finding

**Decision**: Use Docusaurus "swizzle" mechanism to wrap the Root component.

**Method**:
1. Create `src/theme/Root.tsx` that wraps children with ChatWidget
2. Docusaurus automatically detects theme overrides in `src/theme/`
3. No configuration changes needed in `docusaurus.config.ts`

**Implementation**:
```tsx
// src/theme/Root.tsx
import React from 'react';
import ChatWidget from '@site/src/components/ChatWidget';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}
```

**Rationale**: This is the official Docusaurus pattern for adding global components. It avoids modifying the build configuration and follows the framework's conventions.

**Alternatives Considered**:
- Custom plugin: Over-engineering for simple component injection
- Modifying Layout.tsx: Would require ejecting the full layout, harder to maintain
- Client module: More complex, designed for side effects not UI

**Source**: [Docusaurus Theme Documentation](https://docusaurus.io/docs/swizzling)

---

## R-002: Cross-Origin API Requests (CORS)

### Question
What CORS configuration is needed for frontend-backend communication?

### Finding

**Decision**: Backend must enable CORS for specific origins.

**Backend Configuration Required** (FastAPI):
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Docusaurus dev server
        "https://physical-ai-robotics-textbook-nine.vercel.app"  # Production
    ],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)
```

**Rationale**: CORS is required because frontend (localhost:3000 or Vercel) and backend (localhost:8000) are on different origins. The existing backend already supports POST to `/ask`, just needs CORS headers.

**Alternatives Considered**:
- Proxy through Docusaurus: Adds complexity, requires build config changes
- JSONP: Not suitable for POST requests
- Server-side rendering: Overkill for this use case

---

## R-003: State Management for Chat History

### Question
What's the best approach for managing chat state across page navigations?

### Finding

**Decision**: Use React Context + sessionStorage for persistence.

**Architecture**:
```
┌─────────────────────────────────────┐
│         ChatProvider (Context)       │
│  ┌─────────────────────────────┐    │
│  │     messages: Message[]      │    │
│  │     isLoading: boolean       │    │
│  │     error: string | null     │    │
│  └─────────────────────────────┘    │
│              ↕ sync                  │
│  ┌─────────────────────────────┐    │
│  │       sessionStorage         │    │
│  │   "rag-chat-history" key     │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
```

**Implementation**:
- `useChatSession` custom hook manages state
- On mount: Load from sessionStorage
- On message add: Sync to sessionStorage
- On tab close: Automatically cleared

**Rationale**:
- Matches spec requirement for session-only persistence
- Simple implementation without external state libraries
- Native API, no dependencies

**Alternatives Considered**:
- Redux/Zustand: Over-engineering for single feature
- localStorage: Persists beyond session (violates spec)
- URL state: Not suitable for conversation history

---

## R-004: Mobile Responsive Design

### Question
How to ensure chat widget works well on mobile devices (320px minimum)?

### Finding

**Decision**: Responsive CSS with mobile-first approach.

**Breakpoints**:
- Mobile (< 768px): Full-width panel, bottom sheet pattern
- Desktop (≥ 768px): Fixed-width panel, floating overlay

**CSS Strategy**:
```css
/* Mobile-first base styles */
.chatPanel {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60vh;
  max-height: 500px;
}

/* Desktop enhancement */
@media (min-width: 768px) {
  .chatPanel {
    width: 380px;
    right: 20px;
    left: auto;
    bottom: 80px;
    border-radius: 12px;
  }
}
```

**Rationale**: Mobile-first ensures the primary mobile experience is optimized. The 320px minimum from spec is achievable with full-width panel design.

**Alternatives Considered**:
- Container queries: Limited browser support
- Fixed desktop-only design: Violates spec requirement

---

## R-005: Error Handling Patterns

### Question
What's the best UX pattern for handling API errors?

### Finding

**Decision**: Inline error messages with retry capability.

**Error States**:
1. **Network Error**: "Unable to connect. Check your connection." + [Retry]
2. **Server Error (5xx)**: "Service temporarily unavailable." + [Retry]
3. **Client Error (400)**: "Could not process your question." (no retry)
4. **Timeout**: "Request timed out." + [Retry]

**Implementation**:
```tsx
interface ChatState {
  messages: Message[];
  isLoading: boolean;
  error: {
    message: string;
    retryable: boolean;
    lastQuery?: string;
  } | null;
}
```

**Rationale**: Users should understand what went wrong and be able to recover. Keeping the failed query allows easy retry without retyping.

---

## R-006: Accessibility Requirements

### Question
What accessibility features are needed for the chat widget?

### Finding

**Decision**: Implement WCAG 2.1 Level AA compliance.

**Required Features**:
- **Keyboard navigation**: Tab to toggle, Enter to submit
- **Focus management**: Focus input on open, trap focus in panel
- **ARIA labels**: `role="dialog"`, `aria-label` on buttons
- **Screen reader**: Live region for new messages
- **Color contrast**: 4.5:1 minimum for text

**Implementation**:
```tsx
<div
  role="dialog"
  aria-label="Book Q&A Chat"
  aria-modal="true"
>
  <div aria-live="polite" aria-atomic="false">
    {/* New messages announced here */}
  </div>
</div>
```

**Rationale**: Accessibility is required for public-facing educational content. The spec doesn't explicitly require it, but it's a baseline for professional implementation.

---

## Unresolved Items

None. All technical questions resolved.

## Next Steps

1. Proceed to Phase 1: data-model.md, contracts, quickstart.md
2. Begin TDD implementation with ragApi.ts tests first
