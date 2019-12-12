import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Maestro from '@/components/Maestro'

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
    }
  ]
})
