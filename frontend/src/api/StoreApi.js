import Axios from "axios";

const apiUrl = "https://j3d203.p.ssafy.io/api";

const requestStore = (callback, errorCallback) => {
    Axios.get(apiUrl + '/stores/restaurants')
        .then(res => callback(res))
        .catch(error => errorCallback(error))
}

const requestRecStore = (data, callback, errorCallback) => {
    Axios.post(apiUrl + '/stores/recommend/stores', data)
        .then(res => callback(res))
        .catch(error => errorCallback(error)) 
}

const StoreApi = {
    requestStore: (callback, errorCallback) => requestStore(callback, errorCallback),
    requestRecStore: (data, callback, errorCallback) => requestRecStore(data, callback, errorCallback),
}

export default StoreApi