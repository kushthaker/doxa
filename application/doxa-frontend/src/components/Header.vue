<template>
  <div>
    <b-navbar toggleable="lg" type="dark" class="lookyherekushthaker">
      <div>
        <b-navbar-brand to="/">
          <img src="../assets/logo_transparent.png" alt="Fulfilled.ai" width="120" height="120">
        </b-navbar-brand>
      </div>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" class="mr-auto" is-nav>
        <b-navbar-nav class="ml-auto">
          <template v-if="isAuthenticated">
            <b-nav-item to="/growth">Your Growth</b-nav-item>
            <b-nav-item-dropdown :text='currentUser.email' right>
              <b-dropdown-item to="/focus-plan">Focus Plan</b-dropdown-item>
              <b-dropdown-item to="/settings">Settings</b-dropdown-item>
              <b-dropdown-item to="/logout">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>
          <template v-else>
            <b-nav-item to="/login">Login</b-nav-item>
            <b-nav-item to="/register-new-user">Register</b-nav-item>
            <b-nav-item to="/learn-more">Learn More</b-nav-item>
            <b-nav-item to="/contact">Contact</b-nav-item>
          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
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

<style>
  .lookyherekushthaker {
    background-color: #000000;
  }
</style>
