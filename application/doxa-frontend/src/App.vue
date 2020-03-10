<template>
  <div id="app">
  <div class="container">
      <app-header></app-header>
    </div>
    <div class="container">
      <div v-if="isAuthenticated" class="row">
        <div class="col-md-10">
        <router-view/>
        </div>        
        <div class="col-md-2">
          <right-sidebar></right-sidebar>
        </div>
      </div>
      <div v-else>
        <router-view/>
    </div>
    </div>   
  </div>
</div>
</template>

<script>
  import Header from '@/components/Header';
  import Sidebar from '@/components/Sidebar';
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  import 'vue2-timepicker/dist/VueTimepicker.css'
  // import JQuery from 'jquery'
  // window.$ = JQuery
  import Raphael from 'raphael/raphael'
  global.Raphael = Raphael
  export default {
    name: 'App',
    components: {
      'app-header': Header,
      'right-sidebar': Sidebar
    },
    computed: mapState({
      currentUser: function(state) {
        return state.currentUser
      },
      isAuthenticated: function(state) {
        if (state.currentUser) {
          console.log(true)
          return true
        }
        console.log(false)
        return false
      }
    })
  }
  import { mapState } from 'vuex'
  
</script>

<style>

  #app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  h1, h3 {
    color: #000000;
    font-family: 'Roboto Mono', monospace;
    font-weight: bold
  }

  h2, h4, h6, p, a, li {
    color: #0000007a;
    font-family: 'Roboto', sans-serif;
  }

  h2 {
    font-size: 1.5em;
  }

  h6 {
    font-weight: bold;
    color: #000000;
  }
</style>
