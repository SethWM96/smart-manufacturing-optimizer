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
        <label className="block text-sm font-medium text-gray-700 mb-1">Value</label>
        <input
          type="number"
          value={formData.value}
          onChange={(e) => setFormData({ ...formData, value: e.target.value })}
          className="mt-1 block w-full rounded-md border px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Unit</label>
        <input
          type="text"
          value={formData.unit}
          onChange={(e) => setFormData({ ...formData, unit: e.target.value })}
          className="mt-1 block w-full rounded-md border px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Equipment ID</label>
        <input
          type="number"
          value={formData.equipment_id}
          onChange={(e) => setFormData({ ...formData, equipment_id: e.target.value })}
          className="mt-1 block w-full rounded-md border px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm"
          required
        />
      </div>
      <button
        type="submit"
        className="w-full bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        Add Reading
      </button>
    </form>
  );
};

export default SensorForm;