<template>  
  <div>
    <b-container>
      <h2>Change your password</h2>
      <div v-if="formErrors" class="error-messages">
        <b-alert v-for="error in formErrors" show variant="warning" v-bind:key="error">
          {{error}}
        </b-alert>
      </div>
      <div v-if="changePasswordSuccess" class="error-messages">
        <b-alert show variant="success">
          Password changed successfully!
        </b-alert>
      </div>
      <b-form @submit.prevent="submitNewPassword">
        <b-form-group
          label="New password"
          label-for="input-2"
          description="Minimum of 1 character"
        >
          <b-form-input
            v-model="changePassword.new_password"
            required
            id="input-2"
            type="password"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          label="Confirm new password"
          label-for="input-3"
          description="Must match new password"

        >
          <b-form-input
            v-model="changePassword.confirm_new_password"
            required
            id="input-3"
            type="password"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Change password</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    data() {
      return {
        //changePasswordSuccess: false
      }
    },
    computed: mapState({
      changePassword: function(state) {
        return state.changePassword
      },
      formErrors: function(state) {
        return state.formErrors
      },
      changePasswordSuccess: (state) => {
        return state.changePasswordSuccess
      }
    }),
    methods: {
      submitNewPassword() {
        this.$store.dispatch('changePassword').then(() => {
          if(!this.formErrors) {
            //this.$store.dispatch('changePasswordTrue')
          }
        })
      }
    },
    beforeMount() {
      this.$store.dispatch('clearPasswordForm')
    }
  }
</script>
