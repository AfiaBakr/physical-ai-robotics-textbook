/**
 * SourceLinks Component
 *
 * Displays source URLs as clickable links that open in new tabs.
 *
 * @feature 005-frontend-rag-integration
 */

import React from 'react';
import styles from './styles.module.css';

export interface SourceLinksProps {
  sources: string[];
}

function getDisplayUrl(url: string): string {
  try {
    const parsed = new URL(url);
    // Show path without leading slash, or hostname if no path
    const path = parsed.pathname.slice(1);
    return path || parsed.hostname;
  } catch {
    return url;
  }
}

export function SourceLinks({ sources }: SourceLinksProps): JSX.Element | null {
  if (!sources || sources.length === 0) {
    return null;
  }

  return (
    <div className={styles.sourcesSection}>
      <span className={styles.sourcesLabel}>Sources:</span>
      <ul className={styles.sourcesList}>
        {sources.map((source, index) => (
          <li key={`${source}-${index}`} className={styles.sourceItem}>
            <a
              href={source}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.sourceLink}
            >
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                className={styles.linkIcon}
              >
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                <polyline points="15 3 21 3 21 9" />
                <line x1="10" y1="14" x2="21" y2="3" />
              </svg>
              {getDisplayUrl(source)}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SourceLinks;
