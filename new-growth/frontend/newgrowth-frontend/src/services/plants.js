import api from "./apiConfig";

// Necessary function?
const getToken = () => {
  return new Promise((resolve) => {
    resolve(`Token ${localStorage.getItem("knox") || null}`);
  });
};

export const getPlants = async () => {
  try {
    const response = await api.get("/plants")
    return response.data
  } catch (error) {
    throw error;
  }
};