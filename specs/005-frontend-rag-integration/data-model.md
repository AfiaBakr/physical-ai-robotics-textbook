# Data Model: Frontend ↔ Backend Integration for RAG Book Chatbot

**Feature**: `005-frontend-rag-integration`
**Date**: 2025-12-22

## Overview

This document defines the data structures used in the frontend chat integration. These types mirror the backend API contract and add frontend-specific entities for UI state management.

---

## Core Entities

### Message

Represents a single message in the chat conversation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | Yes | Unique identifier (UUID) |
| `role` | `'user' \| 'assistant'` | Yes | Who sent the message |
| `content` | `string` | Yes | The message text |
| `timestamp` | `Date` | Yes | When the message was created |
| `sources` | `string[]` | No | Source URLs (assistant messages only) |
| `matchedChunks` | `MatchedChunk[]` | No | Retrieved content (assistant messages only) |

**Validation Rules**:
- `id`: Valid UUID v4 format
- `content`: 1-10000 characters (user: 1-1000, assistant: up to 10000)
- `timestamp`: Valid ISO 8601 date

### MatchedChunk

A piece of retrieved content that informed the answer.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `chunkId` | `string` | Yes | Unique identifier from backend |
| `text` | `string` | Yes | The content snippet |
| `relevanceScore` | `number` | Yes | Similarity score (0.0 - 1.0) |

**Validation Rules**:
- `relevanceScore`: Must be between 0.0 and 1.0 inclusive

### UserQuery

The input from the user before sending to backend.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `query` | `string` | Yes | The natural language question |

**Validation Rules**:
- `query`: 1-1000 characters, non-empty after trimming
- No leading/trailing whitespace (trimmed on submission)

### RAGResponse

The structured response from the backend `/ask` endpoint.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `answer` | `string` | Yes | The generated response |
| `sources` | `string[]` | Yes | List of source URLs (may be empty) |
| `matchedChunks` | `MatchedChunk[]` | Yes | Retrieved context (may be empty) |

### ChatError

Error state for failed requests.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | `string` | Yes | User-friendly error message |
| `code` | `string` | Yes | Machine-readable error code |
| `retryable` | `boolean` | Yes | Whether retry is appropriate |
| `lastQuery` | `string` | No | The query that failed (for retry) |

**Error Codes**:
- `NETWORK_ERROR`: Connection failed
- `TIMEOUT`: Request exceeded 10 seconds
- `SERVER_ERROR`: Backend returned 5xx
- `INVALID_INPUT`: Backend returned 400
- `RATE_LIMIT`: Backend returned 429

---

## State Entities

### ChatSession

The complete chat state for the current session.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `messages` | `Message[]` | Yes | All messages in the conversation |
| `isLoading` | `boolean` | Yes | Whether a request is in progress |
| `error` | `ChatError \| null` | Yes | Current error state |
| `isOpen` | `boolean` | Yes | Whether chat panel is visible |

**State Transitions**:
```
                    ┌─────────────┐
                    │   IDLE      │
                    │ isLoading=F │
                    │ error=null  │
                    └──────┬──────┘
                           │ submit query
                           ▼
                    ┌─────────────┐
                    │  LOADING    │
                    │ isLoading=T │
                    │ error=null  │
                    └──────┬──────┘
                    ┌──────┴──────┐
            success │             │ failure
                    ▼             ▼
             ┌─────────────┐ ┌─────────────┐
             │   SUCCESS   │ │   ERROR     │
             │ isLoading=F │ │ isLoading=F │
             │ error=null  │ │ error=obj   │
             │ +message    │ └──────┬──────┘
             └─────────────┘        │ retry/new query
                                    ▼
                             ┌─────────────┐
                             │   IDLE      │
                             └─────────────┘
```

---

## Storage Schema

### SessionStorage Key: `rag-chat-history`

```json
{
  "version": 1,
  "messages": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "role": "user",
      "content": "What is RAG?",
      "timestamp": "2025-12-22T10:30:00.000Z"
    },
    {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "role": "assistant",
      "content": "RAG stands for Retrieval-Augmented Generation...",
      "timestamp": "2025-12-22T10:30:05.000Z",
      "sources": ["https://book.example.com/docs/intro"],
      "matchedChunks": [
        {
          "chunkId": "doc-1-42",
          "text": "RAG combines retrieval...",
          "relevanceScore": 0.92
        }
      ]
    }
  ]
}
```

**Schema Versioning**: The `version` field allows for future migrations if the schema changes.

---

## Entity Relationships

```
┌──────────────┐      ┌──────────────┐
│  ChatSession │──────│   Message    │
│              │ 1:N  │              │
└──────────────┘      └──────┬───────┘
                             │
                      ┌──────┴───────┐
                      │              │
               (if role=assistant)   │
                      │              │
                      ▼              │
              ┌──────────────┐       │
              │ MatchedChunk │ 0:N   │
              └──────────────┘───────┘
```

---

## TypeScript Definitions

See `contracts/api-client.ts` for the complete TypeScript interface definitions that implement this data model.
