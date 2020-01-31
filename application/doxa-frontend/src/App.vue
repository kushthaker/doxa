<template>
  <div id="app">
    <app-header></app-header>
    <router-view/>
  </div>
</template>

<script>
  import Header from '@/components/Header';
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  export default {
    name: 'App',
    components: {
      'app-header': Header
    }
  }
</script>

<style>

#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h3 {
  color: #000000;
  font-family: 'Roboto Mono', monospace;
  font-weight: bold
}

h2, h4, h6, p, a, li {
  color: #0000007a;
  font-family: 'Roboto', sans-serif;
}

h2 {
  font-size: 1.5em;
}

h6 {
  font-weight: bold;
  color: #000000;
}

.sidebar {
  font-size: 1.1em;
}

.sidebar-section {
  margin: 0px 0px 30px 0px;
}
</style>
