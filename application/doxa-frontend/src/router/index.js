import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Maestro from '@/components/Maestro'
import Register from '@/components/Register'
import Login from '@/components/Login'
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
        store.dispatch('loadCSRF')
        next()
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        store.dispatch('clearFormErrors')
        store.dispatch('loadCSRF')
        next() 
      }
    }
  ]
})

// this just sets the store variable to the currentUser cookie
router.beforeEach((to, from, next) => {
  store.dispatch('checkLogin').then(() => {
    next()
  })
})

export default router
