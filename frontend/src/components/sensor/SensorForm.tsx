// src/components/sensor/SensorForm.tsx
import React, { useState } from 'react';

interface FormData {
  value: string;
  unit: string;
  equipment_id: string;
}

interface Props {
  onSubmit: (data: { value: number; unit: string; equipment_id: number }) => void;
}

const SensorForm = ({ onSubmit }: Props) => {
  const [formData, setFormData] = useState<FormData>({
    value: '',
    unit: '',
    equipment_id: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      value: parseFloat(formData.value),
      unit: formData.unit,
      equipment_id: parseInt(formData.equipment_id, 10)
    });
    setFormData({ value: '', unit: '', equipment_id: '' });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">Value</label>
        <input
          type="number"
          value={formData.value}
          onChange={(e) => setFormData({ ...formData, value: e.target.value })}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Unit</label>
        <input
          type="text"
          value={formData.unit}
          onChange={(e) => setFormData({ ...formData, unit: e.target.value })}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Equipment ID</label>
        <input
          type="number"
          value={formData.equipment_id}
          onChange={(e) => setFormData({ ...formData, equipment_id: e.target.value })}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          required
        />
      </div>
      <button
        type="submit"
        className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        Add Reading
      </button>
    </form>
  );
};

export default SensorForm;