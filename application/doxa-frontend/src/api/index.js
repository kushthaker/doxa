import axios from 'axios'

export function fetchUser(userId) {
  return axios.get(`/api/users/${userId}`)
    .then(response => {
      return response
    })
    .catch(error => {
      if(error.response.status == 404) {
        return { data: null }
      }
    })
}

export function fetchUsers() {
  return axios.get(`/api/users`)
}

export function userLogin (credentials) {
  return axios.post(`/login`)
}

export function fetchCSRF() {
  return axios.get(`/api/get_csrf`)
}

export function registerUser(newUser) {
  return axios.post('/register', newUser)
}
