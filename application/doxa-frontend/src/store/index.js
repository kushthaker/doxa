import Vue from 'vue'
import Vuex from 'vuex'
import { fetchUsers, fetchUser, fetchCSRF, registerUser, 
  loginUser, getLogin, getUserDetails, passwordChange,
  finalizeSlackAuth, finalizeGoogleAuth, finalizeGithubAuth } from '@/api'
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
<<<<<<< HEAD
  authCode: null,
  githubAuthCode: null,
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
    var result = loginUser(state.loginUser)
    .then(
      function(response) {
        context.commit('setCurrentUser', { currentUser: response.data })
        context.commit('saveCurrentUser', { currentUser: response.data })
        context.commit('setErrors', { errors: null })
        context.commit('clearLoginUser', {})
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
  },
  clearCredentials(context) {
    $cookies.set('currentUser', null)
    context.commit('clearCurrentUser', {})
    context.commit('clearLoginUser', {})
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
  slackAuthFinal(context) {
    var currentUser = state.currentUser

    var slackAuthCode = { code: state.authCode }
    slackAuthCode.csrf_token = state.CSRFToken
    finalizeSlackAuth(slackAuthCode, currentUser)
    .then(
      function(response) {
        context.commit('setUserData', { userData: response.data })
        return response
      }
    )
    .catch(
      function(error) {
        console.log(error)
        return false
      }
    )
  },
  googleAuthFinal(context) {
    // might be able to push this / slackAuthFinal / githubAuthFinal into one general function eventually
    // stores credentials to validate in session (don't need to pass any params)
    var currentUser = state.currentUser
    var form = { csrf_token: state.CSRFToken }
    finalizeGoogleAuth(form, currentUser) 
    .then(
      function(response) {
        context.commit('setUserData', { userData: response.data })
      }
    )
    .catch(
      function(error) {
        console.log(error)
        return false
      }
    )
    
  },
  githubAuthFinal(context) {
    var currentUser = state.currentUser

    var githubAuthCode = { code: state.githubAuthCode }
    githubAuthCode.csrf_token = state.CSRFToken
    finalizeGithubAuth(githubAuthCode, currentUser) 
    .then(
      function(response) {
        context.commit('setUserData', { userData: response.data })
        return response        
      }
    )
    .catch(
      function(error) {
        console.log(error)
        return false
      }
    )
    
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
    if(payload.currentUser) {
      state.jwt = payload.currentUser.token  
    }
    else {
      state.jwt = ''
    }
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
  setCode(state, payload) {
    state.authCode = payload.authCode
  },
  setGithubAuth(state, payload) {
    state.githubAuthCode = payload.githubAuthCode
  },
  clearCurrentUser(state, payload) {
    state.currentUser = null
  }
}

const getters = {
  // reusable data accessors
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
