<template>
  <div>
    <ul v-if="formErrors" class="error-messages">
      <li v-for="error in formErrors">
        {{error}}
      </li>
    </ul>
    <form @submit.prevent="submitUser">
      <input v-model="loginUser.email" placeholder="Your email address" required>
      <input v-model="loginUser.password" placeholder="Password" required type="password">
      <button>Login</button>
    </form>
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
            this.$router.push({ name: "Maestro", params: {id: currentUser.id }}, () => {})
            return currentUser
          }
        })
      },
    }
  }
</script>
