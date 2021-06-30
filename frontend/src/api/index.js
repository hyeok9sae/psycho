import axios from "axios";

const apiUrl = "/api";

export default {
  getStores(params) {
    return axios.get(`${apiUrl}/stores`, {
      params
    });
  },

  getNews(params) {
    return axios.get(`${apiUrl}/news`, {
      params
    })
  }
};
