import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  icon: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Physical AI Foundations',
    icon: '🤖',
    description: (
      <>
        Learn the principles of embodied intelligence and understand how
        Physical AI bridges the gap between digital AI and real-world robotics.
      </>
    ),
  },
  {
    title: 'ROS 2 & Simulation',
    icon: '⚙️',
    description: (
      <>
        Master ROS 2 architecture, build robot systems with nodes and topics,
        and validate your algorithms in Gazebo and NVIDIA Isaac Sim.
      </>
    ),
  },
  {
    title: 'Humanoid Robotics',
    icon: '🦾',
    description: (
      <>
        Design humanoid robots with URDF, implement motion planning,
        and explore Vision-Language-Action (VLA) systems for natural language control.
      </>
    ),
  },
];

function Feature({title, icon, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className={styles.featureCard}>
        <div className="text--center">
          <div className={styles.featureIcon} role="img" aria-label={title}>
            {icon}
          </div>
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
          <p className={styles.featureDescription}>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.sectionTitle}>
          <Heading as="h2">Master the Future of Robotics</Heading>
          <p>Comprehensive modules designed to take you from fundamentals to advanced implementations</p>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
