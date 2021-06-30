import Axios from "axios"

// const apiUrl = "http://localhost:8000/api/"
const apiUrl = "https://j3d203.p.ssafy.io/api"

const requestCorona = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/covid19data/Covid19Info", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}
const requestCoronaGenAge = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/covid19data/Covid19GenAgeInfo", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}
const requestCoronaSido = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/covid19data/Covid19SidoInfo", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}

const CoronaApi = {
  requestCorona: (data, callback, errorCallback) => requestCorona(data, callback, errorCallback),
  requestCoronaGenAge: (data, callback, errorCallback) => requestCoronaGenAge(data, callback, errorCallback),
  requestCoronaSido: (data, callback, errorCallback) => requestCoronaSido(data, callback, errorCallback),
}

export default CoronaApi
