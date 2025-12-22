/**
 * ChatInput Component
 *
 * Input field with validation for submitting questions.
 * Includes character count, submit on Enter, and validation.
 *
 * @feature 005-frontend-rag-integration
 */

import React, { useState, useCallback, KeyboardEvent, ChangeEvent } from 'react';
import { QUERY_CONSTRAINTS } from '../../types/chat';
import styles from './styles.module.css';

export interface ChatInputProps {
  onSubmit: (query: string) => void;
  disabled?: boolean;
  placeholder?: string;
}

export function ChatInput({
  onSubmit,
  disabled = false,
  placeholder = 'Ask a question about the book...',
}: ChatInputProps): JSX.Element {
  const [value, setValue] = useState('');
  const [error, setError] = useState<string | null>(null);

  const trimmedValue = value.trim();
  const charCount = trimmedValue.length;
  const isValid = charCount >= QUERY_CONSTRAINTS.minLength && charCount <= QUERY_CONSTRAINTS.maxLength;
  const isOverLimit = charCount > QUERY_CONSTRAINTS.maxLength;

  const handleChange = useCallback((e: ChangeEvent<HTMLTextAreaElement>) => {
    const newValue = e.target.value;
    setValue(newValue);
    setError(null);

    // Show error if over limit
    if (newValue.trim().length > QUERY_CONSTRAINTS.maxLength) {
      setError(`Question is too long (${newValue.trim().length}/${QUERY_CONSTRAINTS.maxLength})`);
    }
  }, []);

  const handleSubmit = useCallback(() => {
    if (!isValid || disabled) return;

    onSubmit(trimmedValue);
    setValue('');
    setError(null);
  }, [isValid, disabled, trimmedValue, onSubmit]);

  const handleKeyDown = useCallback((e: KeyboardEvent<HTMLTextAreaElement>) => {
    // Submit on Enter without Shift
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  }, [handleSubmit]);

  return (
    <div className={styles.inputContainer}>
      <div className={styles.inputWrapper}>
        <textarea
          className={`${styles.input} ${error ? styles.inputError : ''}`}
          value={value}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          disabled={disabled}
          rows={2}
          aria-label="Ask a question"
          aria-invalid={!!error}
          aria-describedby={error ? 'input-error' : undefined}
        />
        <div className={styles.inputFooter}>
          <span
            className={`${styles.charCount} ${isOverLimit ? styles.charCountError : ''}`}
          >
            {charCount}/{QUERY_CONSTRAINTS.maxLength}
          </span>
          <button
            type="button"
            className={styles.submitButton}
            onClick={handleSubmit}
            disabled={!isValid || disabled}
            aria-label="Send question"
          >
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className={styles.sendIcon}
            >
              <line x1="22" y1="2" x2="11" y2="13" />
              <polygon points="22 2 15 22 11 13 2 9 22 2" />
            </svg>
          </button>
        </div>
      </div>
      {error && (
        <span id="input-error" className={styles.errorText} role="alert">
          {error}
        </span>
      )}
    </div>
  );
}

export default ChatInput;
