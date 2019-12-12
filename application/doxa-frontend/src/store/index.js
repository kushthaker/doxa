import Vue from 'vue'
import Vuex from 'vuex'
import { fetchUsers } from '@/api'
var something = null
Vue.use(Vuex)

const state = {
  // single source of data
  users: []
}

const actions = {
  // asynchronous operations
  loadUsers(context) {
    return fetchUsers()
      .then((response) => context.commit('setUsers', { users: response.data }))
  },
  loadUser(context, id) {
    return fetchUser(id)
      .then((response) => context.commit('setUser', { user: response }))
  }
}

const mutations = {
  // isolated data mutations
  setUsers(state, payload) {
    state.users = payload.users
  },

  setUser(state, payload) {
    state.currentUser = payload.user
  }
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

export default store