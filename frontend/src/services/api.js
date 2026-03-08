import axios from 'axios'

// Use environment variable or default to localhost
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const getTechnologies = async () => {
  const response = await api.get('/technologies')
  return response.data
}

export const getResources = async (technology) => {
  const response = await api.get(`/resources/${technology}`)
  return response.data
}

export const createResource = async (resourceData) => {
  const response = await api.post('/resources', resourceData)
  return response.data
}

export const deleteResource = async (resourceId) => {
  const response = await api.delete(`/resources/${resourceId}`)
  return response.data
}

export default api
