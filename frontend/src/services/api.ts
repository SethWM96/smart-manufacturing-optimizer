// src/services/api.ts
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

export interface SensorReading {
  id: number;
  timestamp: string;
  value: number;
  unit: string;
  equipment_id: number;
}

export const api = {
  sensorReadings: {
    getAll: async (): Promise<SensorReading[]> => {
      const response = await axios.get(`${API_URL}/sensor-readings/`);
      return response.data;
    },

    create: async (data: Omit<SensorReading, 'id' | 'timestamp'>): Promise<SensorReading> => {
      const response = await axios.post(`${API_URL}/sensor-readings/`, data);
      return response.data;
    },

    delete: async (id: number): Promise<void> => {
      await axios.delete(`${API_URL}/sensor-readings/${id}`);
    }
  }
};