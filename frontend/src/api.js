import axios from 'axios';

const API_URL = "http://localhost:8000";

export const askQuestion = async (question) => {
  const response = await axios.get(`${API_URL}/query/`, {
    params: { question },
  });
  return response.data;
};

export const uploadDocument = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  await axios.post(`${API_URL}/upload/`, formData);
};
