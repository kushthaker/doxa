import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Maestro from '@/components/Maestro'
import Register from '@/components/Register'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/maestro/:id',
      name: 'Maestro',
      component: Maestro
    },
    {
      path: '/register-new-user',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login

    }
  ]
})
