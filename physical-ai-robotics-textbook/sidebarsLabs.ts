import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Labs sidebar for Physical AI & Humanoid Robotics Textbook
 */
const sidebars: SidebarsConfig = {
  labsSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1 Labs',
      link: {
        type: 'generated-index',
        title: 'Module 1 Labs',
        description: 'Hands-on lab exercises for Module 1: The Robotic Nervous System.',
      },
      items: [
        {
          type: 'category',
          label: 'Lab 1: Hello ROS 2',
          items: [
            {type: 'doc', id: 'module-01/lab-01-hello-ros2/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 2: Publisher-Subscriber',
          items: [
            {type: 'doc', id: 'module-01/lab-02-pubsub/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 3: Services',
          items: [
            {type: 'doc', id: 'module-01/lab-03-services/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 4: URDF Basics',
          items: [
            {type: 'doc', id: 'module-01/lab-04-urdf-basics/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Mini-Projects',
          items: [
            {type: 'doc', id: 'module-01/mini-project-01-robot-talker/README', label: 'Robot Talker System'},
            {type: 'doc', id: 'module-01/mini-project-02-arm-controller/README', label: 'Arm Controller'},
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 2 Labs',
      link: {
        type: 'generated-index',
        title: 'Module 2 Labs',
        description: 'Hands-on lab exercises for Module 2: The Digital Twin.',
      },
      items: [
        {
          type: 'category',
          label: 'Lab 1: Physics Experiments',
          items: [
            {type: 'doc', id: 'module-02/lab-01-physics-experiments/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 2: Gazebo Worlds',
          items: [
            {type: 'doc', id: 'module-02/lab-02-gazebo-worlds/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 3: Sensor Visualization',
          items: [
            {type: 'doc', id: 'module-02/lab-03-sensor-visualization/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Mini-Projects',
          items: [
            {type: 'doc', id: 'module-02/mini-project-01-navigation-testbed/README', label: 'Navigation Testbed'},
            {type: 'doc', id: 'module-02/mini-project-02-sensor-calibration/README', label: 'Sensor Calibration'},
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 3 Labs',
      link: {
        type: 'generated-index',
        title: 'Module 3 Labs',
        description: 'Hands-on lab exercises for Module 3: Perception & Sensors.',
      },
      items: [
        {
          type: 'category',
          label: 'Lab 1: Image Subscriber',
          items: [
            {type: 'doc', id: 'module-03/lab-01-image-subscriber/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 2: LiDAR Processing',
          items: [
            {type: 'doc', id: 'module-03/lab-02-lidar-processing/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 3: Sensor Fusion',
          items: [
            {type: 'doc', id: 'module-03/lab-03-sensor-fusion/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 4: Object Detection',
          items: [
            {type: 'doc', id: 'module-03/lab-04-object-detection/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 5: Perception Integration',
          items: [
            {type: 'doc', id: 'module-03/lab-05-perception-integration/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Mini-Projects',
          items: [
            {type: 'doc', id: 'module-03/mini-project-01-perception-pipeline/README', label: 'Perception Pipeline'},
            {type: 'doc', id: 'module-03/mini-project-02-visual-servoing/README', label: 'Visual Servoing'},
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 4 Labs',
      link: {
        type: 'generated-index',
        title: 'Module 4 Labs',
        description: 'Hands-on lab exercises for Module 4: Vision-Language-Action (VLA) Systems.',
      },
      items: [
        {
          type: 'category',
          label: 'Lab 1: Speech to Command',
          items: [
            {type: 'doc', id: 'module-04/lab-01-speech-to-command/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 2: LLM Cognitive Planning',
          items: [
            {type: 'doc', id: 'module-04/lab-02-llm-cognitive-planning/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Lab 3: VLA Pipeline Integration',
          items: [
            {type: 'doc', id: 'module-04/lab-03-vla-pipeline-integration/README', label: 'Instructions'},
          ],
        },
        {
          type: 'category',
          label: 'Mini-Projects',
          items: [
            {type: 'doc', id: 'module-04/mini-project-01-simple-vla/README', label: 'Simple VLA System'},
            {type: 'doc', id: 'module-04/mini-project-02-advanced-vla/README', label: 'Advanced VLA System'},
          ],
        },
      ],
    },
  ],
};

export default sidebars;
