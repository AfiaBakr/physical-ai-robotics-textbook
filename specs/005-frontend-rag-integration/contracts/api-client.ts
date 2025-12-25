/**
 * API Contract: Frontend ↔ Backend Integration for RAG Book Chatbot
 *
 * This file defines the TypeScript interfaces that mirror the backend API contract.
 * These types should be copied to `physical-ai-robotics-textbook/src/types/chat.ts`
 * during implementation.
 *
 * @feature 005-frontend-rag-integration
 * @date 2025-12-22
 */

// =============================================================================
// BACKEND API TYPES (mirrors backend/models.py)
// =============================================================================

/**
 * A single retrieved document chunk with metadata.
 * Mirrors backend MatchedChunk model.
 */
export interface MatchedChunk {
  /** Unique identifier for the chunk */
  chunk_id: string;
  /** Content of the matched chunk */
  text: string;
  /** Similarity score (0.0 - 1.0) */
  relevance_score: number;
}

/**
 * Request payload for the /ask endpoint.
 * Mirrors backend AskRequest model.
 */
export interface AskRequest {
  /** Natural language question (1-1000 characters) */
  query: string;
}

/**
 * Successful response from the /ask endpoint.
 * Mirrors backend AskResponse model.
 */
export interface AskResponse {
  /** Generated response from LLM */
  answer: string;
  /** List of source URLs */
  sources: string[];
  /** Retrieved context chunks */
  matched_chunks: MatchedChunk[];
}

/**
 * Error response for failed requests.
 * Mirrors backend ErrorResponse model.
 */
export interface ErrorResponse {
  /** Human-readable error message */
  error: string;
  /** Machine-readable error code */
  code: string;
}

// =============================================================================
// FRONTEND-SPECIFIC TYPES
// =============================================================================

/** Message sender role */
export type MessageRole = 'user' | 'assistant';

/**
 * A single message in the chat conversation.
 */
export interface ChatMessage {
  /** Unique identifier (UUID v4) */
  id: string;
  /** Who sent the message */
  role: MessageRole;
  /** The message text */
  content: string;
  /** When the message was created (ISO 8601) */
  timestamp: string;
  /** Source URLs (assistant messages only) */
  sources?: string[];
  /** Retrieved content snippets (assistant messages only) */
  matchedChunks?: MatchedChunk[];
}

/** Error codes for chat errors */
export type ChatErrorCode =
  | 'NETWORK_ERROR'
  | 'TIMEOUT'
  | 'SERVER_ERROR'
  | 'INVALID_INPUT'
  | 'RATE_LIMIT';

/**
 * Error state for failed requests.
 */
export interface ChatError {
  /** User-friendly error message */
  message: string;
  /** Machine-readable error code */
  code: ChatErrorCode;
  /** Whether retry is appropriate */
  retryable: boolean;
  /** The query that failed (for retry) */
  lastQuery?: string;
}

/**
 * Complete chat session state.
 */
export interface ChatSession {
  /** All messages in the conversation */
  messages: ChatMessage[];
  /** Whether a request is in progress */
  isLoading: boolean;
  /** Current error state */
  error: ChatError | null;
  /** Whether chat panel is visible */
  isOpen: boolean;
}

/**
 * Storage schema for sessionStorage persistence.
 */
export interface ChatStorageSchema {
  /** Schema version for migrations */
  version: number;
  /** Persisted messages */
  messages: ChatMessage[];
}

// =============================================================================
// API CLIENT INTERFACE
// =============================================================================

/**
 * Configuration for the RAG API client.
 */
export interface RAGApiConfig {
  /** Base URL for the API (default: http://localhost:8000) */
  baseUrl: string;
  /** Request timeout in milliseconds (default: 10000) */
  timeout: number;
}

/**
 * Result of an API call - either success or error.
 */
export type RAGApiResult =
  | { success: true; data: AskResponse }
  | { success: false; error: ChatError };

/**
 * RAG API client interface.
 */
export interface RAGApiClient {
  /**
   * Send a question to the RAG backend.
   * @param query - The user's question (1-1000 characters)
   * @returns Promise resolving to success with data or error
   */
  ask(query: string): Promise<RAGApiResult>;
}

// =============================================================================
// CONSTANTS
// =============================================================================

/** Storage key for chat history in sessionStorage */
export const CHAT_STORAGE_KEY = 'rag-chat-history';

/** Current storage schema version */
export const CHAT_STORAGE_VERSION = 1;

/** Default API configuration */
export const DEFAULT_API_CONFIG: RAGApiConfig = {
  baseUrl: 'http://localhost:8000',
  timeout: 10000,
};

/** Query validation constraints */
export const QUERY_CONSTRAINTS = {
  minLength: 1,
  maxLength: 1000,
} as const;
