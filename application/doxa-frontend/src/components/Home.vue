<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">List of users</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card" v-for="user in users" v-bind:key="user.id">
          <div class="card-content">
            <div v-if="user">
              <p class="title">Name: {{ user.username}}; Email: {{user.email}}</p>
              <p class="detail">See this <router-link :to="`maestro/${user.id}`">maestro</router-link> </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

</template>
<script>
  import { mapState } from 'vuex'
  export default {
    data() {
      return {}
    },

    computed: mapState({
      users: state => state.users
    }),
    beforeMount() {
      this.$store.dispatch('loadUsers')
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

