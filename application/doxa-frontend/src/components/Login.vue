<template>
  <div>
    <v-form>
      <input v-model="newUser.email" placeholder="Your email address">
      <input v-model="newUser.password" placeholder="Password">
    </v-form>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    data() {
      return {}
    },

    computed: mapState({
      
    }),

    beforeMount() {
      
    }
  }
</script>