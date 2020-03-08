<template>

  <b-navbar toggleable="lg">
    <div class="logo">
      <b-navbar-brand to="/">
        <img class="logo" src="../assets/logo_transparent.png" alt="Fulfilled.ai" width="70" height="70">
      </b-navbar-brand>
    </div>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" class="mr-auto" is-nav>
      <b-navbar-nav class="ml-auto center">
        <template v-if="isAuthenticated">
          <b-nav-item to="/fulfilled-dashboard">Dashboard</b-nav-item>
          <b-nav-item to="/settings">Settings</b-nav-item>
          <b-nav-item to="/Logout">Logout</b-nav-item>
        </template>
        <template v-else>
          <b-nav-item to="/login">Login</b-nav-item>
          <b-nav-item to="/register-new-user">Register</b-nav-item>
        </template>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  import { mapState } from 'vuex'
  import { isValidJwt } from '@/utils'
  export default {
    computed: mapState({
      isAuthenticated: function(state) {
        console.log(state)
        if(state.currentUser) {
          return true
        }
        return false
      },
      currentUser: function(state) {
        return state.currentUser
      }
    })
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.navbar.center .navbar-inner {
    text-align: center;
}

.navbar.center .navbar-inner .nav {
    display:inline-block;
    float: none;
    vertical-align: top;
}

.logo {
  margin: 10px 0px 40px 0px;
}
</style>
