import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const predictImage = async (file, modelType) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post(`${API_URL}/predict?model_type=${modelType}`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return response.data;
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
};

export const getModels = async () => {
    try {
        const response = await axios.get(`${API_URL}/models`);
        return response.data;
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
};
