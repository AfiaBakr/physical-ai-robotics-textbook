/**
 * useChatSession Hook
 *
 * Manages chat session state with sessionStorage persistence.
 * Handles message history, loading states, and error handling.
 *
 * @feature 005-frontend-rag-integration
 */

import { useState, useCallback, useEffect, useMemo } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import type {
  ChatMessage,
  ChatError,
  ChatStorageSchema,
  AskResponse,
} from '../types/chat';
import { CHAT_STORAGE_KEY, CHAT_STORAGE_VERSION } from '../types/chat';
import { RAGApi } from '../services/ragApi';
import { getApiConfig } from '../utils/getApiConfig';

/**
 * Generate a unique ID for messages.
 */
function generateId(): string {
  return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
}

/**
 * Load messages from sessionStorage.
 */
function loadFromStorage(): ChatMessage[] {
  if (typeof window === 'undefined') return [];

  try {
    const stored = sessionStorage.getItem(CHAT_STORAGE_KEY);
    if (!stored) return [];

    const data: ChatStorageSchema = JSON.parse(stored);
    if (data.version !== CHAT_STORAGE_VERSION) {
      // Version mismatch, clear storage
      sessionStorage.removeItem(CHAT_STORAGE_KEY);
      return [];
    }

    return data.messages || [];
  } catch {
    return [];
  }
}

/**
 * Save messages to sessionStorage.
 */
function saveToStorage(messages: ChatMessage[]): void {
  if (typeof window === 'undefined') return;

  try {
    const data: ChatStorageSchema = {
      version: CHAT_STORAGE_VERSION,
      messages,
    };
    sessionStorage.setItem(CHAT_STORAGE_KEY, JSON.stringify(data));
  } catch {
    // Storage full or unavailable, silently fail
  }
}

/**
 * Chat session state and actions.
 */
export interface UseChatSessionReturn {
  messages: ChatMessage[];
  isLoading: boolean;
  error: ChatError | null;
  isOpen: boolean;
  sendMessage: (query: string) => Promise<void>;
  retry: () => Promise<void>;
  clearError: () => void;
  toggleOpen: () => void;
  setOpen: (open: boolean) => void;
}

/**
 * Custom hook for managing chat session.
 */
export function useChatSession(): UseChatSessionReturn {
  const { siteConfig } = useDocusaurusContext();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<ChatError | null>(null);
  const [isOpen, setIsOpen] = useState(false);
  const [lastQuery, setLastQuery] = useState<string | null>(null);

  // Create RAGApi instance with config from environment variable
  const ragApi = useMemo(() => {
    const config = getApiConfig(siteConfig as { customFields?: { ragApiUrl?: string } });
    return new RAGApi(config);
  }, [siteConfig]);

  // Load messages from storage on mount
  useEffect(() => {
    const stored = loadFromStorage();
    if (stored.length > 0) {
      setMessages(stored);
    }
  }, []);

  // Save messages to storage when they change
  useEffect(() => {
    if (messages.length > 0) {
      saveToStorage(messages);
    }
  }, [messages]);

  /**
   * Send a message and get a response.
   */
  const sendMessage = useCallback(async (query: string) => {
    const trimmedQuery = query.trim();
    if (!trimmedQuery) return;

    // Clear any previous error
    setError(null);
    setLastQuery(trimmedQuery);

    // Add user message
    const userMessage: ChatMessage = {
      id: generateId(),
      role: 'user',
      content: trimmedQuery,
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const result = await ragApi.ask(trimmedQuery);

      if (result.success) {
        // Add assistant message
        const response: AskResponse = result.data;
        const assistantMessage: ChatMessage = {
          id: generateId(),
          role: 'assistant',
          content: response.answer,
          timestamp: new Date().toISOString(),
          sources: response.sources,
          matchedChunks: response.matched_chunks,
        };

        setMessages(prev => [...prev, assistantMessage]);
      } else {
        // Set error state
        setError(result.error);
      }
    } catch {
      // Unexpected error
      setError({
        message: 'An unexpected error occurred. Please try again.',
        code: 'NETWORK_ERROR',
        retryable: true,
        lastQuery: trimmedQuery,
      });
    } finally {
      setIsLoading(false);
    }
  }, [ragApi]);

  /**
   * Retry the last failed query.
   */
  const retry = useCallback(async () => {
    if (lastQuery) {
      // Remove the last user message if it was for the failed query
      setMessages(prev => {
        const lastMsg = prev[prev.length - 1];
        if (lastMsg?.role === 'user' && lastMsg.content === lastQuery) {
          return prev.slice(0, -1);
        }
        return prev;
      });
      await sendMessage(lastQuery);
    }
  }, [lastQuery, sendMessage]);

  /**
   * Clear the current error.
   */
  const clearError = useCallback(() => {
    setError(null);
  }, []);

  /**
   * Toggle the chat panel open/closed.
   */
  const toggleOpen = useCallback(() => {
    setIsOpen(prev => !prev);
  }, []);

  /**
   * Set the chat panel open state.
   */
  const setOpen = useCallback((open: boolean) => {
    setIsOpen(open);
  }, []);

  return {
    messages,
    isLoading,
    error,
    isOpen,
    sendMessage,
    retry,
    clearError,
    toggleOpen,
    setOpen,
  };
}

export default useChatSession;
