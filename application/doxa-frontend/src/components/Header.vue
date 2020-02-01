<template>
  <div>
    <b-navbar toggleable="lg">
      <div>
        <b-navbar-brand to="/">
        </b-navbar-brand>
      </div>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" class="mr-auto" is-nav>
        <b-navbar-nav class="ml-auto">
          <template v-if="isAuthenticated">
            <b-nav-item-dropdown :text='currentUser.email' right>
              <b-dropdown-item to="/focus-plan">Dashboard</b-dropdown-item>
              <b-dropdown-item to="/focus-plan">Focus Plan</b-dropdown-item>
              <b-dropdown-item to="/focus-plan">Settings</b-dropdown-item>
              <b-dropdown-item to="/logout">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>
          <template v-else>
            <b-nav-item to="/login">Login</b-nav-item>
            <b-nav-item to="/register-new-user">Register</b-nav-item>
          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="container">
      <div class="row">
        <img class="logo" src="../assets/logo_transparent.png" alt="Fulfilled.ai" width="70" height="70">
      </div>
     </div>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  import { isValidJwt } from '@/utils'
  export default {
    computed: mapState({
      isAuthenticated: function(state) {
        return isValidJwt(state.jwt)
      },
      currentUser: function(state) {
        return state.currentUser
      }
    })
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

.logo {
  margin: 10px 0px 40px 10px;
}

</style>
