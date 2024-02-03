// Service file fetches data from djangos api
import axios from 'axios';

const BASE_URL = 'http://localhost:8000';  // Replace with your Django server URL

export const getJobListings = () => {
    return axios.get(`${BASE_URL}/job-listings/`);
}

export const createApplication = (data) => {
    return axios.post(`${BASE_URL}/applications/`, data);
}

export const createUser = (data) => {
	return axios.post(`${BASE_URL}/user/`, data);
// Add more API calls as needed

