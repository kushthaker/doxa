<template>
  <div>
    <b-container>
      <h2>Log in to Fulfilled.ai</h2>
      <div v-if="formErrors" class="error-messages">
        <b-alert v-for="error in formErrors" show variant="warning" v-bind:key="error">
          {{error}}
        </b-alert>
      </div>
      <b-form @submit.prevent="submitUser">
        <b-form-group
          label="Email"
          label-for="input-1"
        >
          <b-form-input
            v-model="loginUser.email"
            placeholder="maestro@fulfilled.ai"
            required
            id="input-1"
            type="text"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="Password"
          label-for="input-2"
        >
          <b-form-input
            v-model="loginUser.password"
            required
            id="input-2"
            type="password"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Login</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    computed: mapState({
      loginUser: function(state) {
        return state.loginUser
      },
      isLoggedIn: function(state) {
        return state.isLoggedIn
      },
      formErrors: (state) => {
        return state.formErrors
      }
    }),
    methods: {
      submitUser() {
        return this.$store.dispatch('userLogin').then(() => {
          if(!this.formErrors) {
            var currentUser = this.$store.getters.currentUser
            return this.$router.push({ name: "Maestro", params: {id: currentUser.id }}, () => {})
            
          }
        })
      },
    }
  }
</script>
