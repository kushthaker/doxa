<template>
  
  <div>
    <ul v-if="formErrors" class="error-messages">
      <li v-for="error in formErrors">
        {{error}}
      </li>
    </ul>
    <form @submit.prevent="submitUser">
      <p>Username: <input v-model="newUser.username" placeholder="realdonaldtrump"></p>
      <p>Email address: <input v-model="newUser.email" placeholder="maestro@fulfilled.ai"></p>
      <p>Password: <input v-model="newUser.password" required type="password"></p>
      <p>Confirm password: <input v-model="newUser.confirm_password" required type="password"></p>
      <button>Register</button>
    </form>
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
        let _this = this;
        this.$store.dispatch('registerNewUser').then(() => {
          if(!this.formErrors) {
            this.$router.push({ name: "Home" })
          }
        })
      }
    },
    // mapActions({
    //   submitUser: 'registerNewUser'
    // }),
    
    beforeMount() {
      this.$store.dispatch('loadCSRF')
      
      // if(this.$store.currentUser) {
      //   // redirect to home page
      //   this.$router.go('/login')
      // }
    }
  }
</script>