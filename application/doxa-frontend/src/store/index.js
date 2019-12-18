import Vue from 'vue'
import Vuex from 'vuex'
import { fetchUsers, fetchUser, fetchCSRF, registerUser } from '@/api'
import VueCookies from 'vue-cookies'

Vue.use(Vuex)
Vue.use(VueCookies)

const state = {
  // single source of data
  users: [],
  userData: null,
  newUser: { username: null, email: null, password: null, confirm_password: null, csrf_token: null },
  formErrors: null
}

const actions = {
  // asynchronous operations
  loadUsers(context) {
    return fetchUsers()
      .then((response) => context.commit('setUsers', { users: response.data }))
  },
  loadUser(context, id) {
    return fetchUser(id)
      .then((response) => {
        context.commit('setUserData', { userData: response.data });
      })
  },
  loadCSRF(context) {
    return fetchCSRF()
      .then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
  },
  registerNewUser(context) {
    var result = registerUser(state.newUser).then(
      function(response) {
        var registrationErrors = null
        var newUser = response.data
        if(newUser.errors){
          registrationErrors = []
          for (var key of keys(newUser.errors)){
            for (var error of newUser.errors[key]) {
              registrationErrors = registrationErrors.concat(error)
            }
          }
        }
        fetchCSRF().then((response) => context.commit('setCSRF', { CSRFToken: response.data.csrf_token }))
        context.commit('setErrors', { errors: registrationErrors })
        context.commit('setNewUser', { newUser: newUser })
      }
    )
    return result
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
    state.newUser.csrf_token = payload.CSRFToken
  },
  setErrors(state, payload) {
    state.formErrors = payload.errors
  },
  setNewUser(state, payload) {
    state.newUser = payload.newUser
  },
  
}

const getters = {

  // reusable data accessors
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

export default store
