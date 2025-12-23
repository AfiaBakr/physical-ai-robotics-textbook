/**
 * Chat Types for RAG Book Chatbot
 *
 * TypeScript interfaces for the frontend chat integration.
 * Mirrors the backend API contract from backend/models.py
 *
 * @feature 005-frontend-rag-integration
 */

// =============================================================================
// BACKEND API TYPES (mirrors backend/models.py)
// =============================================================================

/**
 * A single retrieved document chunk with metadata.
 */
export interface MatchedChunk {
  chunk_id: string;
  text: string;
  relevance_score: number;
}

/**
 * Request payload for the /ask endpoint.
 */
export interface AskRequest {
  query: string;
}

/**
 * Successful response from the /ask endpoint.
 */
export interface AskResponse {
  answer: string;
  sources: string[];
  matched_chunks: MatchedChunk[];
}

/**
 * Error response for failed requests.
 */
export interface ErrorResponse {
  error: string;
  code: string;
}

// =============================================================================
// FRONTEND-SPECIFIC TYPES
// =============================================================================

export type MessageRole = 'user' | 'assistant';

/**
 * A single message in the chat conversation.
 */
export interface ChatMessage {
  id: string;
  role: MessageRole;
  content: string;
  timestamp: string;
  sources?: string[];
  matchedChunks?: MatchedChunk[];
}

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
  message: string;
  code: ChatErrorCode;
  retryable: boolean;
  lastQuery?: string;
}

/**
 * Complete chat session state.
 */
export interface ChatSession {
  messages: ChatMessage[];
  isLoading: boolean;
  error: ChatError | null;
  isOpen: boolean;
}

/**
 * Storage schema for sessionStorage persistence.
 */
export interface ChatStorageSchema {
  version: number;
  messages: ChatMessage[];
}

// =============================================================================
// API CLIENT TYPES
// =============================================================================

export interface RAGApiConfig {
  baseUrl: string;
  timeout: number;
}

export type RAGApiResult =
  | { success: true; data: AskResponse }
  | { success: false; error: ChatError };

// =============================================================================
// CONSTANTS
// =============================================================================

export const CHAT_STORAGE_KEY = 'rag-chat-history';
export const CHAT_STORAGE_VERSION = 1;

export const DEFAULT_API_CONFIG: RAGApiConfig = {
  baseUrl: 'https://afiabakr-deploy-chatbot.hf.space',
  timeout: 10000,
};

export const QUERY_CONSTRAINTS = {
  minLength: 1,
  maxLength: 1000,
} as const;
