import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const profileService = {
  getProfile: (username) => api.get(`/profile/${username}/`),
  scanProfile: (username) => api.post('/profile/scan/', { username }),
};

export const analysisService = {
  getFakeDetection: (profileId) => api.get(`/analysis/fake-detection/${profileId}/`),
  getActivityAnalysis: (profileId) => api.get(`/analysis/activity/${profileId}/`),
};

export const reportService = {
  generateReport: (profileId) => api.post('/reports/generate/', { profile_id: profileId }),
  getReports: () => api.get('/reports/'),
  downloadReport: (reportId) => api.get(`/reports/${reportId}/download/`),
};

export default api;
