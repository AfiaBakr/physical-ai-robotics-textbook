import React, { useState } from 'react';

interface SensorData {
  name: string;
  type: 'camera' | 'lidar' | 'imu' | 'depth';
  topicName: string;
  messageType: string;
  frequency: string;
  description: string;
}

interface SensorVisualizerProps {
  sensors: SensorData[];
  title?: string;
}

const sensorIcons: Record<string, string> = {
  camera: '\u{1F4F7}',
  lidar: '\u{1F4E1}',
  imu: '\u{1F9ED}',
  depth: '\u{1F4D0}',
};

const sensorColors: Record<string, string> = {
  camera: '#4CAF50',
  lidar: '#2196F3',
  imu: '#FF9800',
  depth: '#9C27B0',
};

export default function SensorVisualizer({
  sensors,
  title = "Sensor Configuration"
}: SensorVisualizerProps): JSX.Element {
  const [selectedSensor, setSelectedSensor] = useState<number | null>(null);

  return (
    <div style={{
      border: '1px solid var(--ifm-color-emphasis-300)',
      borderRadius: '8px',
      padding: '1rem',
      marginBottom: '1rem',
      backgroundColor: 'var(--ifm-background-surface-color)',
    }}>
      <h4 style={{ marginTop: 0, marginBottom: '1rem' }}>{title}</h4>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
        gap: '0.75rem',
      }}>
        {sensors.map((sensor, index) => (
          <div
            key={index}
            onClick={() => setSelectedSensor(selectedSensor === index ? null : index)}
            style={{
              border: `2px solid ${selectedSensor === index ? sensorColors[sensor.type] : 'var(--ifm-color-emphasis-200)'}`,
              borderRadius: '6px',
              padding: '0.75rem',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              backgroundColor: selectedSensor === index ? `${sensorColors[sensor.type]}10` : 'transparent',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ fontSize: '1.5rem' }}>{sensorIcons[sensor.type]}</span>
              <div>
                <strong style={{ display: 'block' }}>{sensor.name}</strong>
                <small style={{ color: 'var(--ifm-color-emphasis-600)' }}>
                  {sensor.type.toUpperCase()}
                </small>
              </div>
            </div>

            {selectedSensor === index && (
              <div style={{
                marginTop: '0.75rem',
                paddingTop: '0.75rem',
                borderTop: '1px solid var(--ifm-color-emphasis-200)',
                fontSize: '0.875rem',
              }}>
                <p style={{ margin: '0.25rem 0' }}>
                  <strong>Topic:</strong> <code>{sensor.topicName}</code>
                </p>
                <p style={{ margin: '0.25rem 0' }}>
                  <strong>Type:</strong> <code>{sensor.messageType}</code>
                </p>
                <p style={{ margin: '0.25rem 0' }}>
                  <strong>Rate:</strong> {sensor.frequency}
                </p>
                <p style={{ margin: '0.5rem 0 0', color: 'var(--ifm-color-emphasis-700)' }}>
                  {sensor.description}
                </p>
              </div>
            )}
          </div>
        ))}
      </div>

      <div style={{
        marginTop: '1rem',
        padding: '0.5rem',
        backgroundColor: 'var(--ifm-color-emphasis-100)',
        borderRadius: '4px',
        fontSize: '0.8rem',
        color: 'var(--ifm-color-emphasis-600)',
      }}>
        Click on a sensor to view details. Sensors publish data to ROS 2 topics for processing by perception nodes.
      </div>
    </div>
  );
}
