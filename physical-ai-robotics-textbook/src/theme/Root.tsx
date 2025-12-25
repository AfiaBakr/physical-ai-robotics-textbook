/**
 * Root Theme Wrapper
 *
 * Wraps the Docusaurus app to inject the ChatWidget globally.
 * Uses Docusaurus swizzle pattern for theme customization.
 *
 * @feature 005-frontend-rag-integration
 */

import React from 'react';
import ChatWidget from '../components/ChatWidget';

export interface RootProps {
  children: React.ReactNode;
}

export default function Root({ children }: RootProps): JSX.Element {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}
