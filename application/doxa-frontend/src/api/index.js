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

export function loginUser (credentials) {
  return axios.post(`/api/login`, credentials)
}

export function checkLogin() {
  return axios.get('/api/check-login')
}

export function getLogin() {
  return axios.get(`/login`, {})
}

export function fetchCSRF() {
  return axios.get(`/api/get_csrf`)
}

export function registerUser(newUser, token) {
  return axios.post('/api/register', newUser)
}

export function getUserDetails(user) {
  return axios.get('/api/user_details')
}

export function passwordChange(passwordForm, user) {
  return axios.post('/api/change-password', passwordForm)
}

export function finalizeSlackAuth(form) {
  return axios.get('/api/finalize-slack-auth', form)
}

export function logoutUser(user) {
  return axios.get('/api/logout')
}