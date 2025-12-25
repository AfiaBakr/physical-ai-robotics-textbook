/**
 * ChatMessage Component
 *
 * Displays a single message in the chat conversation.
 * Includes role indicator, content, timestamp, sources, and matched chunks.
 *
 * @feature 005-frontend-rag-integration
 */

import React, { useState } from 'react';
import type { ChatMessage as ChatMessageType } from '../../types/chat';
import SourceLinks from './SourceLinks';
import MatchedChunks from './MatchedChunks';
import styles from './styles.module.css';

export interface ChatMessageProps {
  message: ChatMessageType;
}

function formatTimestamp(isoString: string): string {
  try {
    const date = new Date(isoString);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  } catch {
    return '';
  }
}

export function ChatMessage({ message }: ChatMessageProps): JSX.Element {
  const [showChunks, setShowChunks] = useState(false);
  const isAssistant = message.role === 'assistant';
  const hasChunks = message.matchedChunks && message.matchedChunks.length > 0;
  const hasSources = message.sources && message.sources.length > 0;

  return (
    <div
      className={`${styles.message} ${isAssistant ? styles.assistantMessage : styles.userMessage}`}
      role="listitem"
    >
      <div className={styles.messageHeader}>
        <span className={styles.messageRole}>
          {isAssistant ? 'AI' : 'You'}
        </span>
        <span className={styles.messageTime}>
          {formatTimestamp(message.timestamp)}
        </span>
      </div>

      <div className={styles.messageContent}>
        {message.content}
      </div>

      {isAssistant && hasSources && (
        <SourceLinks sources={message.sources!} />
      )}

      {isAssistant && hasChunks && (
        <div className={styles.chunksSection}>
          <button
            type="button"
            className={styles.chunksToggle}
            onClick={() => setShowChunks(!showChunks)}
            aria-expanded={showChunks}
          >
            {showChunks ? 'Hide context' : 'Show context'}
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              className={`${styles.chevronIcon} ${showChunks ? styles.chevronUp : ''}`}
            >
              <polyline points="6 9 12 15 18 9" />
            </svg>
          </button>
          {showChunks && (
            <MatchedChunks chunks={message.matchedChunks!} />
          )}
        </div>
      )}
    </div>
  );
}

export default ChatMessage;
