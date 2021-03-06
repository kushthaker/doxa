import Vue from 'vue'
import Vuex from 'vuex'
import { fetchUsers, fetchUser, fetchCSRF, registerUser, 
  checkLogin, getUserDetails, passwordChange, loginUser, logoutUser,
  fetchActivityData, sendNudgeRequest } from '@/api'
import VueCookies from 'vue-cookies'
import { isValidJwt } from '@/utils'

Vue.use(Vuex)
Vue.use(VueCookies)

const NEW_LOGIN_USER = { email: null, password: null, csrf_token: null }
const NEW_REGISTER_USER = { username: null, email: null, password: null, confirm_password: null, csrf_token: null }
const NEW_PASSWORD_CHANGE = { new_password: null, confirm_new_password: null }
const state = {
  // single source of data
  users: [],
  userData: {},
  newUser: Object.assign({}, NEW_REGISTER_USER),
  formErrors: null,
  loginUser: Object.assign({}, NEW_LOGIN_USER),
  currentUser: null,
  CSRFToken: null,
  jwt: '',
  changePassword: Object.assign({}, NEW_PASSWORD_CHANGE),
  changePasswordSuccess: false,
  authCode: null,
  isLoggedIn: false,
  activityData: [],
  lastWeekActivityData: []
}

const actions = {
  // asynchronous operations
  loadActivity(context, data) {
    return fetchActivityData({})
      .then((response) => {
        return context.commit('setActivityData', { time: response.data })
      })
  },
  loadPastActivity(context) {
    return fetchActivityData({ weekOffset: -1 })
      .then((response) => {
        return context.commit('setLastWeekActivityData', { time: response.data })
      })
  },
  loadUsers(context) {
    return fetchUsers()
      .then((response) => context.commit('setUsers', { users: response.data }))
  },
  loadUser(context, data) {
    return getUserDetails(data)
      .then((response) => {
        if(!response.data) {
          context.commit('setUserData', { userData: { error: true }});  
        }
        context.commit('setUserData', { userData: response.data });
      })
      .catch((error) => {
        console.log('Error loading user')
      })
  },
  loadCSRF(context) {
    return fetchCSRF()
      .then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
  },
  registerNewUser(context) {
    state.newUser.csrf_token = state.CSRFToken
    var result = registerUser(state.newUser).then(
      function(response) {
        //context.commit('setNewUser', { newUser: state.newUser })
        context.commit('clearNewUser', {})
        context.commit('setErrors', { errors: null })
        return true
      }
    ).catch(function(error) {
      fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
      var registrationErrors = mapErrors(error.response)
      context.commit('setErrors', { errors: registrationErrors })
      return false
    })
  },
  userLogin(context) {
    state.loginUser.csrf_token = state.CSRFToken
    return loginUser(state.loginUser)
    .then(
      function(response) {
        context.commit('setErrors', { errors: null })
        context.commit('clearLoginUser', {})
        return context.commit('setCurrentUser', { currentUser: response.data })
      }
    )
    .catch(
      function(error) {
        fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
        var loginErrors = mapErrors(error.response)
        return context.commit('setErrors', { errors: loginErrors })
      } 
    )
  },
  clearFormErrors(context) {
    state.formErrors = null
  },
  checkLogin(context) {
    return checkLogin().then((response) => {
      if (response.data == null) {
        return context.commit('clearCurrentUser', {})
      }
      else {
        return context.commit('setCurrentUser', { currentUser: response.data })
      }
    })
  },
  clearCredentials(context) {
    return logoutUser()
      .then((response) => {
        context.commit('clearCurrentUser', {})
        context.commit('clearLoginUser', {})
        return response
      })
      .catch((error) => {
        context.commit('clearCurrentUser', {})
        context.commit('clearLoginUser', {})
        return error
      })
  },
  changePassword(context) {
    state.changePassword.csrf_token = state.CSRFToken
    var result = passwordChange(state.changePassword, state.currentUser)
    .then(
      function(response) {
        fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
        context.commit('setErrors', { errors: null })
        context.commit('setChangePassword', { changePasswordForm: Object.assign({}, NEW_PASSWORD_CHANGE) })
        context.commit('setChangePasswordStatus', { changePasswordSuccess: true })
        return true
      }
    )
    .catch(
      function(error) {
        fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
        var passwordErrors = mapErrors(error.response)
        context.commit('setErrors', { errors: passwordErrors })
        context.dispatch('clearPasswordForm')
        return false
      }
    )
  },
  clearPasswordForm(context) {
    context.commit('setChangePasswordStatus', { changePasswordSuccess: false })
    context.commit('setChangePassword', { changePasswordForm: Object.assign({}, NEW_PASSWORD_CHANGE) })
  },
  requestNudge(context, payload) {
    console.log(payload)
    sendNudgeRequest(payload)
  }
}

const mutations = {
  // isolated data mutations
  setUsers(state, payload) {
    state.users = payload.users
  },
  setUserData(state, payload) {
    console.log(payload.userData)
    state.userData = payload.userData
  },
  setCSRF(state, payload) {
    state.CSRFToken = payload.CSRFToken
  },
  setErrors(state, payload) {
    state.formErrors = payload.errors
  },
  setNewUser(state, payload) {
    state.newUser = payload.newUser
  },
  setJWT(state, payload) {
    state.jwt = payload.jwt
  },
  setCurrentUser(state, payload) {
    state.currentUser = payload.currentUser  
  },
  saveCurrentUser(state, payload) {
    $cookies.set('currentUser', payload.currentUser)
  },
  clearLoginUser(state, payload) {
    state.loginUser = Object.assign({}, NEW_LOGIN_USER)
  },
  clearNewUser(state, payload) {
    state.newUser = Object.assign({}, NEW_REGISTER_USER)
  },
  setChangePassword(state, payload) {
    state.changePassword = payload.changePasswordForm
  },
  setChangePasswordStatus(state, payload) {
    state.changePasswordSuccess = payload.changePasswordSuccess
  },
  clearCurrentUser(state, payload) {
    state.currentUser = null
  },
  setActivityData(state, payload) {
    state.activityData = payload.time
  },
  setLastWeekActivityData(state, payload) {
    state.lastWeekActivityData = payload.time
  },
}

const getters = {
  // reusable data accessors
  isLoggedIn(state) {
    return state.currentUser != null
  },
  isAuthenticated(state) {
    return isValidJwt(state.jwt)
  },
  currentUser(state) {
    return state.currentUser
  },
  userData(state) {
    return state.userData
  }
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

function keys(object) {
  return Object.keys(object)
}

function mapErrors(response) {
  var errors = null
  if(response.data.errors){
    var errorSet = response.data.errors
    errors = []
    for (var key of keys(errorSet)){
      for (var error of errorSet[key]) {
        errors = errors.concat(error)
      }
    }
  }
  return errors
}

export default store
