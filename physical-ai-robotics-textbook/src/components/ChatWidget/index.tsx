/**
 * ChatWidget Component
 *
 * Main container for the floating chat widget.
 * Features animated robot icon with greeting and expandable chat panel.
 *
 * @feature 005-frontend-rag-integration
 */

import React, { useCallback, useEffect, useState } from 'react';
import { useChatSession } from '../../hooks/useChatSession';
import ChatPanel from './ChatPanel';
import RobotIcon from './RobotIcon';
import styles from './styles.module.css';

export function ChatWidget(): JSX.Element {
  const {
    messages,
    isLoading,
    error,
    isOpen,
    sendMessage,
    retry,
    clearError,
    toggleOpen,
    setOpen,
  } = useChatSession();

  const [showGreeting, setShowGreeting] = useState(false);
  const [isHovered, setIsHovered] = useState(false);

  // Show greeting after a short delay when not open
  useEffect(() => {
    if (!isOpen) {
      const timer = setTimeout(() => setShowGreeting(true), 1500);
      return () => clearTimeout(timer);
    } else {
      setShowGreeting(false);
    }
  }, [isOpen]);

  // Handle Escape key to close panel
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        setOpen(false);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, setOpen]);

  const handleToggle = useCallback(() => {
    toggleOpen();
  }, [toggleOpen]);

  const handleClose = useCallback(() => {
    setOpen(false);
  }, [setOpen]);

  const handleMouseEnter = useCallback(() => {
    setIsHovered(true);
  }, []);

  const handleMouseLeave = useCallback(() => {
    setIsHovered(false);
  }, []);

  return (
    <div className={styles.chatWidget}>
      {/* Floating toggle button with robot */}
      {!isOpen && (
        <div
          className={styles.floatingContainer}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {/* Greeting bubble */}
          <div className={`${styles.greetingBubble} ${(showGreeting || isHovered) ? styles.greetingVisible : ''}`}>
            <span className={styles.greetingText}>
              Hello! What can I help you with?
            </span>
            <div className={styles.bubbleArrow} />
          </div>

          {/* Robot button */}
          <button
            type="button"
            className={styles.toggleButton}
            onClick={handleToggle}
            aria-label="Open chat assistant"
            aria-expanded={isOpen}
          >
            <div className={styles.robotWrapper}>
              <RobotIcon size={52} />
              <div className={styles.pulseRing} />
              <div className={styles.pulseRing} style={{ animationDelay: '0.5s' }} />
            </div>
          </button>
        </div>
      )}

      {/* Chat panel */}
      {isOpen && (
        <ChatPanel
          messages={messages}
          isLoading={isLoading}
          error={error}
          onSendMessage={sendMessage}
          onRetry={retry}
          onClearError={clearError}
          onClose={handleClose}
        />
      )}
    </div>
  );
}

export default ChatWidget;
