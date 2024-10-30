// src/components/sensor/SensorReadings.tsx
import React from 'react';
import { SensorReading } from '../../services/api';

interface Props {
  readings: SensorReading[];
  onDelete?: (id: number) => void;
}

const SensorReadings = ({ readings, onDelete }: Props) => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Time</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Value</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Unit</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Equipment ID</th>
            {onDelete && (
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
            )}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {readings.map((reading) => (
            <tr key={reading.id}>
              <td className="px-6 py-4 whitespace-nowrap">{new Date(reading.timestamp).toLocaleString()}</td>
              <td className="px-6 py-4 whitespace-nowrap">{reading.value}</td>
              <td className="px-6 py-4 whitespace-nowrap">{reading.unit}</td>
              <td className="px-6 py-4 whitespace-nowrap">{reading.equipment_id}</td>
              {onDelete && (
                <td className="px-6 py-4 whitespace-nowrap">
                  <button
                    onClick={() => onDelete(reading.id)}
                    className="text-red-600 hover:text-red-900"
                  >
                    Delete
                  </button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SensorReadings;