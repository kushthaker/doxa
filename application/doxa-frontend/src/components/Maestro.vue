<template>
<div>
  <div v-if="maestro">
    <h3>The maestro is <em>{{maestro.name}}</em></h3>
  </div>
  <div>
    <v-form>
      <input v-model="maestro.name" placeholder="e.g. Callum John Killian Mitchell">
      <p>Maestro is: {{ maestro.name }}</p>
    </v-form>
  </div>

</div>
</template>

<script>
  import { fetchUser } from '@/api'
  export default {
    data() {
      return {maestro: null}
    },
    beforeMount() {
      console.log('Survey.beforeMount -> :id === ', this.$route.params.id)
      var userId = parseInt(this.$route.params.id)
      fetchUser(userId).then(response => {
        this.maestro = response
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

