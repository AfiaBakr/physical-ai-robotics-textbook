/**
 * Animated Robot Icon Component
 *
 * A cute animated robot icon for the chat widget.
 * Features blinking eyes, antenna pulse, and hover effects.
 *
 * @feature 005-frontend-rag-integration
 */

import React from 'react';
import styles from './styles.module.css';

export interface RobotIconProps {
  size?: number;
  className?: string;
}

export function RobotIcon({ size = 48, className = '' }: RobotIconProps): JSX.Element {
  return (
    <div className={`${styles.robotContainer} ${className}`} style={{ width: size, height: size }}>
      <svg
        viewBox="0 0 100 100"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className={styles.robotSvg}
      >
        {/* Antenna */}
        <g className={styles.antenna}>
          <line x1="50" y1="8" x2="50" y2="20" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
          <circle cx="50" cy="6" r="4" fill="currentColor" className={styles.antennaBall} />
        </g>

        {/* Head */}
        <rect
          x="20"
          y="20"
          width="60"
          height="50"
          rx="10"
          fill="url(#headGradient)"
          stroke="currentColor"
          strokeWidth="2"
          className={styles.robotHead}
        />

        {/* Face plate / Screen */}
        <rect
          x="28"
          y="28"
          width="44"
          height="34"
          rx="6"
          fill="url(#screenGradient)"
          className={styles.faceScreen}
        />

        {/* Left Eye */}
        <g className={styles.eye}>
          <ellipse cx="38" cy="42" rx="6" ry="7" fill="#0a0a0a" />
          <ellipse cx="38" cy="42" rx="4" ry="5" fill="url(#eyeGlow)" className={styles.eyeGlow} />
          <circle cx="36" cy="40" r="1.5" fill="#ffffff" opacity="0.8" />
        </g>

        {/* Right Eye */}
        <g className={styles.eye}>
          <ellipse cx="62" cy="42" rx="6" ry="7" fill="#0a0a0a" />
          <ellipse cx="62" cy="42" rx="4" ry="5" fill="url(#eyeGlow)" className={styles.eyeGlow} />
          <circle cx="60" cy="40" r="1.5" fill="#ffffff" opacity="0.8" />
        </g>

        {/* Mouth - Friendly smile */}
        <path
          d="M 40 52 Q 50 58 60 52"
          stroke="url(#eyeGlow)"
          strokeWidth="3"
          strokeLinecap="round"
          fill="none"
          className={styles.mouth}
        />

        {/* Ear/Side panels */}
        <rect x="12" y="35" width="8" height="20" rx="3" fill="url(#headGradient)" stroke="currentColor" strokeWidth="1.5" />
        <rect x="80" y="35" width="8" height="20" rx="3" fill="url(#headGradient)" stroke="currentColor" strokeWidth="1.5" />

        {/* Body */}
        <rect
          x="30"
          y="72"
          width="40"
          height="20"
          rx="5"
          fill="url(#headGradient)"
          stroke="currentColor"
          strokeWidth="2"
        />

        {/* Body details - chest light */}
        <circle cx="50" cy="82" r="4" fill="url(#eyeGlow)" className={styles.chestLight} />

        {/* Gradients */}
        <defs>
          <linearGradient id="headGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#2d2d2d" />
            <stop offset="50%" stopColor="#1a1a1a" />
            <stop offset="100%" stopColor="#0a0a0a" />
          </linearGradient>
          <linearGradient id="screenGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#1a1a1a" />
            <stop offset="100%" stopColor="#0d0d0d" />
          </linearGradient>
          <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#FFD700" />
            <stop offset="50%" stopColor="#D4AF37" />
            <stop offset="100%" stopColor="#B8860B" />
          </radialGradient>
        </defs>
      </svg>
    </div>
  );
}

export default RobotIcon;
