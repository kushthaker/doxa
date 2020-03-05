<template>  
  <div>
    <b-container>
      <h2>Register for Fulfilled.ai</h2>
      <div v-if="formErrors" class="error-messages">
        <b-alert v-for="error in formErrors" show variant="warning" v-bind:key="error">
          {{error}}
        </b-alert>
      </div> 
      <b-form @submit.prevent="submitUser">
        <b-form-group
          label="Username"
          label-for="input-1"
          description="Just the username you use in Fulfilled.ai"

        >
          <b-form-input
            v-model="newUser.username"
            placeholder="Feridan_UW_Hamdallahpur"
            required
            id="input-1"
            type="text"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          label="Email Address"
          label-for="input-email-register"
          description="Your work email address."

        >
          <b-form-input
            v-model="newUser.email"
            placeholder="maestro@fulfilled.ai"
            required
            id="input-email-register"
            type="email"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          label="Password"
          label-for="input-3"
          description="Minimum of 1 character"

        >
          <b-form-input
            v-model="newUser.password"
            required
            id="input-3"
            type="password"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          label="Confirm password"
          label-for="input-4"
          description="Must be the same as your password above"

        >
          <b-form-input
            v-model="newUser.confirm_password"
            required
            id="input-4"
            type="password"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Register</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    computed: mapState({
      newUser: function(state){
        return state.newUser
      },
      formErrors: function(state){
        return state.formErrors
      }
    }),
    methods: {
      submitUser() {
        this.$store.dispatch('registerNewUser').then(() => {
          if(!this.formErrors) {
            // this may eventually go to an email confirmation, or just log them in.
            this.$router.push({ name: "Login" })
          }
        })
      }
    }
  }
</script>
