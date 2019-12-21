<template>
<div>
  <div v-if="maestro">
    <h3>The maestro is <em>{{maestro.username}}</em></h3>
    <input v-model="maestro.username" placeholder="e.g. Callum John Killian Mitchell">
    <p>The maestro's email is <strong>{{maestro.email}}</strong></p>
    <input v-model="maestro.email" placeholder="e.g. maestro@fulfilled.maestro">
  </div>
  <div v-else>
    Loading...
  </div>
</div>
</template>

<script>
  import { mapState } from 'vuex'
  import { canAccess } from '@/utils'
  export default {
    computed: mapState({
      maestro: function(state) {
        return state.userData
      },
      currentUser: function(state) {
        return state.currentUser
      }
    }),
    beforeMount() {
      var userId = parseInt(this.$route.params.id)
      this.$store.dispatch('loadUser', this.currentUser).then(() => {
        return
      })
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
