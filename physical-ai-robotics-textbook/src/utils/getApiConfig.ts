/**
 * API Configuration Utility
 *
 * Gets the RAG API URL from Docusaurus custom fields (set via environment variable)
 * Falls back to default URL if not configured.
 *
 * @feature 005-frontend-rag-integration
 */

import { FALLBACK_API_URL } from '../types/chat';
import type { RAGApiConfig } from '../types/chat';

/**
 * Gets the API configuration with URL from Docusaurus config.
 * This should be called from React components where useDocusaurusContext is available.
 */
export function getApiConfig(siteConfig?: { customFields?: { ragApiUrl?: string } }): RAGApiConfig {
  const baseUrl = siteConfig?.customFields?.ragApiUrl || FALLBACK_API_URL;

  return {
    baseUrl,
    timeout: 10000,
  };
}

/**
 * Gets just the API base URL.
 */
export function getApiUrl(siteConfig?: { customFields?: { ragApiUrl?: string } }): string {
  return siteConfig?.customFields?.ragApiUrl || FALLBACK_API_URL;
}
