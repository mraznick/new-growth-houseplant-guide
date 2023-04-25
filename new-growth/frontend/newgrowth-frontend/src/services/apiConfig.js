import axios from "axios";

// BACKEND NOT YET DEPLOYED!
const api = axios.create({
  baseURL: "https://newgrowth-backend.herokuapp.com"
});

export default api;