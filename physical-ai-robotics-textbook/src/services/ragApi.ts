/**
 * RAG API Client
 *
 * Handles communication with the FastAPI backend /ask endpoint.
 * Uses native fetch API with timeout and error handling.
 *
 * @feature 005-frontend-rag-integration
 */

import type {
  AskRequest,
  AskResponse,
  ChatError,
  ChatErrorCode,
  RAGApiConfig,
  RAGApiResult,
} from '../types/chat';
import { DEFAULT_API_CONFIG, QUERY_CONSTRAINTS } from '../types/chat';

/**
 * Validates query before sending to API.
 */
function validateQuery(query: string): ChatError | null {
  const trimmed = query.trim();

  if (trimmed.length < QUERY_CONSTRAINTS.minLength) {
    return {
      message: 'Please enter a question.',
      code: 'INVALID_INPUT',
      retryable: false,
    };
  }

  if (trimmed.length > QUERY_CONSTRAINTS.maxLength) {
    return {
      message: `Question is too long. Maximum ${QUERY_CONSTRAINTS.maxLength} characters allowed.`,
      code: 'INVALID_INPUT',
      retryable: false,
    };
  }

  return null;
}

/**
 * Creates a ChatError from various error conditions.
 */
function createError(
  code: ChatErrorCode,
  message: string,
  lastQuery?: string
): ChatError {
  const retryable = code !== 'INVALID_INPUT';
  return { message, code, retryable, lastQuery };
}

/**
 * Fetches with timeout support.
 */
async function fetchWithTimeout(
  url: string,
  options: RequestInit,
  timeout: number
): Promise<Response> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    return response;
  } finally {
    clearTimeout(timeoutId);
  }
}

/**
 * RAG API client class.
 */
export class RAGApi {
  private config: RAGApiConfig;

  constructor(config: Partial<RAGApiConfig> = {}) {
    this.config = { ...DEFAULT_API_CONFIG, ...config };
  }

  /**
   * Send a question to the RAG backend.
   */
  async ask(query: string): Promise<RAGApiResult> {
    // Validate input
    const validationError = validateQuery(query);
    if (validationError) {
      return { success: false, error: validationError };
    }

    const trimmedQuery = query.trim();
    const url = `${this.config.baseUrl}/ask`;
    const body: AskRequest = { query: trimmedQuery };

    try {
      const response = await fetchWithTimeout(
        url,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(body),
        },
        this.config.timeout
      );

      // Handle HTTP errors
      if (!response.ok) {
        const status = response.status;

        if (status === 400) {
          return {
            success: false,
            error: createError(
              'INVALID_INPUT',
              'Your question could not be processed. Please try rephrasing.',
              trimmedQuery
            ),
          };
        }

        if (status === 429) {
          return {
            success: false,
            error: createError(
              'RATE_LIMIT',
              'Too many requests. Please wait a moment and try again.',
              trimmedQuery
            ),
          };
        }

        // 5xx errors
        return {
          success: false,
          error: createError(
            'SERVER_ERROR',
            'Service temporarily unavailable. Please try again.',
            trimmedQuery
          ),
        };
      }

      // Parse successful response
      const data: AskResponse = await response.json();
      return { success: true, data };

    } catch (error) {
      // Handle network errors and timeouts
      if (error instanceof Error) {
        if (error.name === 'AbortError') {
          return {
            success: false,
            error: createError(
              'TIMEOUT',
              'Request timed out. Please try again.',
              trimmedQuery
            ),
          };
        }
      }

      return {
        success: false,
        error: createError(
          'NETWORK_ERROR',
          'Unable to connect. Please check your internet connection.',
          trimmedQuery
        ),
      };
    }
  }
}

// Default singleton instance
export const ragApi = new RAGApi();

// Export for custom configuration
export { validateQuery, createError };
