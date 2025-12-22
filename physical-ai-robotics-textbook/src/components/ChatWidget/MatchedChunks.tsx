/**
 * MatchedChunks Component
 *
 * Displays expandable content snippets with relevance scores.
 *
 * @feature 005-frontend-rag-integration
 */

import React from 'react';
import type { MatchedChunk } from '../../types/chat';
import styles from './styles.module.css';

export interface MatchedChunksProps {
  chunks: MatchedChunk[];
}

function formatRelevanceScore(score: number): string {
  return `${Math.round(score * 100)}%`;
}

export function MatchedChunks({ chunks }: MatchedChunksProps): JSX.Element | null {
  if (!chunks || chunks.length === 0) {
    return null;
  }

  return (
    <div className={styles.chunksContainer}>
      {chunks.map((chunk, index) => (
        <div key={chunk.chunk_id || index} className={styles.chunk}>
          <div className={styles.chunkHeader}>
            <span className={styles.chunkLabel}>Context {index + 1}</span>
            <div className={styles.relevanceContainer}>
              <div
                className={styles.relevanceBar}
                style={{ width: `${chunk.relevance_score * 100}%` }}
              />
              <span className={styles.relevanceScore}>
                {formatRelevanceScore(chunk.relevance_score)}
              </span>
            </div>
          </div>
          <p className={styles.chunkText}>{chunk.text}</p>
        </div>
      ))}
    </div>
  );
}

export default MatchedChunks;
