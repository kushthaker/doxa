import Vue from 'vue'
import Vuex from 'vuex'
import { fetchUsers, fetchUser, fetchCSRF, registerUser, loginUser, getLogin, getUserDetails } from '@/api'
import VueCookies from 'vue-cookies'
import { isValidJwt } from '@/utils'

Vue.use(Vuex)
Vue.use(VueCookies)

const state = {
  // single source of data
  users: [],
  userData: {},
  newUser: { username: null, email: null, password: null, confirm_password: null, csrf_token: null },
  formErrors: null,
  loginUser: { email: null, password: null, csrf_token: null },
  currentUser: null,
  CSRFToken: null,
  jwt: ''
}

const actions = {
  // asynchronous operations
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
        debugger
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
        context.commit('setNewUser', { newUser: state.newUser })
        context.commit('setErrors', { errors: null })
      }
    ).catch(function(error) {
      fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
      var registrationErrors = mapErrors(error.response)
      context.commit('setErrors', { errors: registrationErrors })
    })
    return result
  },
  userLogin(context) {
    state.loginUser.csrf_token = state.CSRFToken
    var result = loginUser(state.loginUser)
    .then(
      function(response) {
        context.commit('setCurrentUser', { currentUser: response.data })
        context.commit('saveCurrentUser', { currentUser: response.data })
        context.commit('setErrors', { errors: null })
        return context.commit('setJWT', { jwt: response.data.token })
      }
    )
    .catch(
      function(error) {
        fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
        var loginErrors = mapErrors(error.response)
        context.commit('setErrors', { errors: loginErrors })
      }
    )
    return result
  },
  clearFormErrors(context) {
    state.formErrors = null
  },
  checkLogin(context) {
    const user = $cookies.get('currentUser')
    return context.commit('setCurrentUser', { currentUser: user })
  }
}

const mutations = {
  // isolated data mutations
  setUsers(state, payload) {
    state.users = payload.users
  },
  setUserData(state, payload) {
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
    if(payload.currentUser) {
      state.jwt = payload.currentUser.token  
    }
    else {
      state.jwt = ''
    }
  },
  saveCurrentUser(state, payload) {
    $cookies.set('currentUser', payload.currentUser)
  }
}

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
    return isValidJwt(state.jwt)
  },
  currentUser(state) {
    return state.currentUser
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
