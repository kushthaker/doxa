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
  return axios.get('/api/user_details', { data: user , headers: authHeader(user) })
}

export function passwordChange(passwordForm, user) {
  return axios.post('/api/change-password', passwordForm, { headers: authHeader(user) })
}

export function finalizeSlackAuth(slackAuthData, user) {
  return axios.post('/api/finalize-slack-auth', slackAuthData, { headers: authHeader(user) })
}

export function finalizeGoogleAuth(googleAuthData, user) {
  return axios.post('/api/finalize-google-auth', googleAuthData, { headers: authHeader(user) })
}

// pass this to headers in order to use JSON web token
function authHeader(user) {
  return { Authorization: `Bearer: ${user.token}` }
}
