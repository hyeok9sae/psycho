import Axios from "axios";

const apiUrl = "https://j3d203.p.ssafy.io/api";

const requestHotel = (callback, errorCallback) => {
    Axios.get(apiUrl + '/stores/hotels')
        .then(res => callback(res))
        .catch(error => errorCallback(error))
}

const requestRecHotel = (data, callback, errorCallback) => {
    Axios.post(apiUrl + '/stores/recommend/hotels', data)
        .then(res => callback(res))
        .catch(error => errorCallback(error)) 
}

const HotelApi = {
    requestHotel: (callback, errorCallback) => requestHotel(callback, errorCallback),
    requestRecHotel: (data, callback, errorCallback) => requestRecHotel(data, callback, errorCallback),
}

export default HotelApi