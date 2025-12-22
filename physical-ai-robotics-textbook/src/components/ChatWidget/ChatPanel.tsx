/**
 * ChatPanel Component
 *
 * Main chat panel containing message list, input area, and loading/error states.
 * Styled to match the book's premium black & gold theme.
 *
 * @feature 005-frontend-rag-integration
 */

import React, { useRef, useEffect } from 'react';
import type { ChatMessage as ChatMessageType, ChatError } from '../../types/chat';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';
import RobotIcon from './RobotIcon';
import styles from './styles.module.css';

export interface ChatPanelProps {
  messages: ChatMessageType[];
  isLoading: boolean;
  error: ChatError | null;
  onSendMessage: (query: string) => void;
  onRetry: () => void;
  onClearError: () => void;
  onClose: () => void;
}

export function ChatPanel({
  messages,
  isLoading,
  error,
  onSendMessage,
  onRetry,
  onClearError,
  onClose,
}: ChatPanelProps): JSX.Element {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  return (
    <div
      className={styles.panel}
      role="dialog"
      aria-label="Book Q&A Chat Assistant"
      aria-modal="true"
    >
      {/* Header */}
      <div className={styles.panelHeader}>
        <div className={styles.headerTitle}>
          <RobotIcon size={32} className={styles.headerRobot} />
          <div className={styles.headerText}>
            <span className={styles.headerName}>AI Assistant</span>
            <span className={styles.headerStatus}>
              <span className={styles.statusDot} />
              Online
            </span>
          </div>
        </div>
        <button
          type="button"
          className={styles.closeButton}
          onClick={onClose}
          aria-label="Close chat"
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
          >
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>

      {/* Messages */}
      <div className={styles.messagesContainer} role="list" aria-live="polite">
        {messages.length === 0 && !isLoading && !error && (
          <div className={styles.emptyState}>
            <div className={styles.emptyRobot}>
              <RobotIcon size={80} />
            </div>
            <h3 className={styles.emptyTitle}>Hello! I'm your AI Assistant</h3>
            <p className={styles.emptySubtitle}>
              Ask me anything about Physical AI & Humanoid Robotics!
            </p>
            <div className={styles.suggestionsContainer}>
              <p className={styles.suggestionsLabel}>Try asking:</p>
              <div className={styles.suggestions}>
                <button
                  type="button"
                  className={styles.suggestionChip}
                  onClick={() => onSendMessage('What is RAG?')}
                >
                  What is RAG?
                </button>
                <button
                  type="button"
                  className={styles.suggestionChip}
                  onClick={() => onSendMessage('Explain humanoid robots')}
                >
                  Explain humanoid robots
                </button>
                <button
                  type="button"
                  className={styles.suggestionChip}
                  onClick={() => onSendMessage('What is Physical AI?')}
                >
                  What is Physical AI?
                </button>
              </div>
            </div>
          </div>
        )}

        {messages.map((msg) => (
          <ChatMessage key={msg.id} message={msg} />
        ))}

        {/* Loading indicator */}
        {isLoading && (
          <div className={styles.loadingContainer}>
            <div className={styles.loadingRobot}>
              <RobotIcon size={28} />
            </div>
            <div className={styles.loadingContent}>
              <div className={styles.loadingDots}>
                <span className={styles.dot}></span>
                <span className={styles.dot}></span>
                <span className={styles.dot}></span>
              </div>
              <span className={styles.loadingText}>Thinking...</span>
            </div>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className={styles.errorContainer} role="alert">
            <div className={styles.errorIcon}>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
            </div>
            <p className={styles.errorMessage}>{error.message}</p>
            <div className={styles.errorActions}>
              {error.retryable && (
                <button
                  type="button"
                  className={styles.retryButton}
                  onClick={onRetry}
                >
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <polyline points="23 4 23 10 17 10" />
                    <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10" />
                  </svg>
                  Try again
                </button>
              )}
              <button
                type="button"
                className={styles.dismissButton}
                onClick={onClearError}
              >
                Dismiss
              </button>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input area */}
      <div className={styles.inputArea}>
        <ChatInput
          onSubmit={onSendMessage}
          disabled={isLoading}
          placeholder="Ask about the book..."
        />
      </div>
    </div>
  );
}

export default ChatPanel;
