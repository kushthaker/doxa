import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Maestro from '@/components/Maestro'
import Register from '@/components/Register'
import Login from '@/components/Login'
import Settings from '@/components/Settings'
import ChangePassword from '@/components/ChangePassword'
import SlackAuthorization from '@/components/SlackAuthorization'
import GoogleCalendarAuthorization from '@/components/GoogleCalendarAuthorization'
import store from '@/store'

Vue.use(Router)
const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: (to, from, next) => {
        store.dispatch('loadUsers').then(() => {
          next()
        })
      }
    },
    {
      path: '/maestro/:id',
      name: 'Maestro',
      component: Maestro,
      beforeEnter: (to, from, next) => {
        const isAuthed = store.getters.isAuthenticated;
        const user = store.getters.currentUser
        if(isAuthed) {
          if(user
          && (to.params.id === String(user.id))) {
            store.dispatch('loadUser', user).then(() => {
              next()
            })
          }
          else {
            store.dispatch('loadUser', user).then(() => {
              next(`/maestro/${user.id}`)
            })
          }
        }
        else {
          next('/login')
        }
      }
    },
    {
      path: '/register-new-user',
      name: 'Register',
      component: Register,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        next()
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        const isAuthed = store.getters.isAuthenticated;
        if(isAuthed) {
          const user = store.getters.currentUser;
          next(`/maestro/${user.id}`)
        }
        else {
          next()   
        }
      }
    },
    {
      path: '/logout',
      name: 'Logout',
      beforeEnter: (to, from, next) => {
        store.dispatch('clearCredentials').then(() => {
          next('/login')
        })
      }
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        const isAuthed = store.getters.isAuthenticated;
        const user = store.getters.currentUser
        if(isAuthed) {
          store.dispatch('loadUser', user).then(() => {
            next()
          })
        }
        else {
          next('/login')
        }
      }
    },
    {
      path: '/change-password',
      name: 'Change password',
      component: ChangePassword,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        loginRequired(next, store)
      }
    },
    {
      path: '/slack-auth/:code',
      name: 'Fulfilled.ai Slack Authentication',
      component: SlackAuthorization,
      beforeEnter: (to, from, next) =>{
        var _store = store
        _store.commit('setCode', { authCode: to.params.code })
        _store.dispatch('slackAuthFinal').then((response) => {
          next('/settings')
        })
      }
    },
    {
      path: '/google-auth',
      name: 'Fulfilled.ai Google Calendar Authorization',
      component: GoogleCalendarAuthorization,
      beforeEnter: (to, from, next) => {
        var _store = store
        var urlParams = to.query
        if(urlParams.refresh_token === 'None') {
          urlParams.refresh_token = null
        }
        _store.commit('setGoogleCalendarAuth', { params: urlParams })
        _store.dispatch('googleAuthFinal').then((response) => {
          next('/settings')
        })
      }
    }
  ]
})

// this just sets the store variable "currentUser" to the currentUser cookie
router.beforeEach((to, from, next) => {
  store.dispatch('checkLogin').then(() => {
    store.dispatch('loadCSRF').then(() => {
      next()
    })
  })
})

// simple way of sending them to req'd place if they are logged in, otherwise send them to login
function loginRequired(_next, _store, newNext='/login') {
  const isAuthed = _store.getters.isAuthenticated
  const user = _store.getters.currentUser
  if(isAuthed) {
    return _next()
  }
  return _next(newNext)
}

export default router
