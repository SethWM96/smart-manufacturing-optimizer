import React from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '../services/api';
import SensorReadings from '../components/sensor/SensorReadings';
import SensorForm from '../components/sensor/SensorForm';

const Dashboard = () => {
  const queryClient = useQueryClient();
  
  const { data: readings = [], isLoading } = useQuery({
    queryKey: ['sensorReadings'],
    queryFn: api.sensorReadings.getAll
  });

  const createMutation = useMutation({
    mutationFn: api.sensorReadings.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['sensorReadings'] });
    }
  });

  const deleteMutation = useMutation({
    mutationFn: api.sensorReadings.delete,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['sensorReadings'] });
    }
  });

  if (isLoading) return <div>Loading...</div>;

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Sensor Readings Dashboard</h1>
      
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-medium mb-4">Add New Reading</h2>
        <SensorForm onSubmit={createMutation.mutate} />
      </div>

      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-medium mb-4">Sensor Readings</h2>
        <SensorReadings 
          readings={readings} 
          onDelete={(id) => deleteMutation.mutate(id)} 
        />
      </div>
    </div>
  );
};

export default Dashboard;