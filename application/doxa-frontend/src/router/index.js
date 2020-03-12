import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Maestro from '@/components/Maestro'
import Register from '@/components/Register'
import Login from '@/components/Login'
import Settings from '@/components/Settings'
import ChangePassword from '@/components/ChangePassword'
import Dashboard from '@/components/Dashboard'
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
        next('/fulfilled-dashboard')
      }
    },
    {
      path: '/register-new-user',
      name: 'Register',
      component: Register,
      beforeEnter: (to, from, next) => {
        var isLoggedIn = store.getters.isLoggedIn
        if(!isLoggedIn) {
          store.dispatch('clearFormErrors')
          next()  
        }
        else {
          next('/fulfilled-dashboard')
        }        
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        const isAuthed = store.getters.isLoggedIn;
        if(isAuthed) {
          const user = store.getters.currentUser;
          next('/fulfilled-dashboard')
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
        return store.dispatch('clearCredentials').then(() => {
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
        const isAuthed = store.getters.isLoggedIn;
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
      path: '/fulfilled-dashboard',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        const startTime = to.params.start_time
        const endTime = to.params.end_time

        store.dispatch('clearFormErrors')
        store.dispatch('loadActivity', startTime, endTime)
        store.dispatch('loadPastActivity', startTime, endTime)
        loginRequired(next, store)

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
  const isAuthed = _store.getters.isLoggedIn
  const user = _store.getters.currentUser
  if(isAuthed) {
    return _next()
  }
  return _next(newNext)
}

export default router
