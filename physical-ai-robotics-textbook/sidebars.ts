import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Sidebars for Physical AI & Humanoid Robotics Textbook
 */
const sidebars: SidebarsConfig = {
  // Main textbook sidebar
  textbookSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System',
      link: {
        type: 'generated-index',
        title: 'Module 1: The Robotic Nervous System (ROS 2)',
        description: 'Learn the foundations of Physical AI and master ROS 2, the middleware that serves as the nervous system of modern robots.',
      },
      items: [
        'module-01-ros2/lesson-01-physical-ai',
        'module-01-ros2/lesson-02-ros2-architecture',
        'module-01-ros2/lesson-03-rclpy-agents',
        'module-01-ros2/lesson-04-urdf-fundamentals',
        'module-01-ros2/lesson-05-simulation-review',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin',
      link: {
        type: 'generated-index',
        title: 'Module 2: The Digital Twin (Gazebo & Unity)',
        description: 'Master digital twin concepts, physics simulation, and sensor pipelines using Gazebo and Unity for robotics development.',
      },
      items: [
        'module-02-simulation/lesson-01-digital-twin',
        'module-02-simulation/lesson-02-gazebo-workflows',
        'module-02-simulation/lesson-03-sensors-unity',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: Perception & Sensors',
      link: {
        type: 'generated-index',
        title: 'Module 3: Perception & Sensors (Computer Vision & Sensor Fusion)',
        description: 'Master computer vision fundamentals, multi-sensor integration, and perception pipelines for robotics using OpenCV and ROS 2.',
      },
      items: [
        'module-03-perception/lesson-01-computer-vision',
        'module-03-perception/lesson-02-multi-sensor',
        'module-03-perception/lesson-03-perception-pipelines',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA) Systems',
      link: {
        type: 'generated-index',
        title: 'Module 4: Vision-Language-Action (VLA) Systems',
        description: 'Learn about Vision-Language-Action (VLA) systems for Physical AI and Humanoid Robotics. This module covers the integration of vision, language understanding, and robotic action in multimodal AI systems.',
      },
      items: [
        'module-04-vla/lesson-01-vla-introduction',
        'module-04-vla/lesson-02-vla-components',
        'module-04-vla/lesson-03-vla-integration',
      ],
    },
    {
      type: 'category',
      label: 'Appendix',
      items: [
        'appendix/references',
      ],
    },
  ],
};

export default sidebars;
