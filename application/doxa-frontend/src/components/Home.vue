<template>
  <div>
    <section class="hero is-primary">
        <div class="container">
          <div class="row hero-section">
            <div>
              <h1>Find focus at work with Fulfilled.</h1>
              <h4>Developers use Fulfilled to focus on their craft, collaborate smarter, and disconnect after work.</h4>
              <button>Try it free</button>
            </div>
          </div>
          <div class="row hero-section">
            <div class="col-md-6">
              <h3>See your collaboration trends</h3>
            </div>
            <div class="col-md-6">
            </div>
          </div>          
          <div class="row hero-section">
            <div class="col-md-6">
            </div>
            <div class="col-md-6">
              <h3>Book time to work deeply everyday</h3>
            </div>
          </div>
          <div class="row hero-section">
            <div class="col-md-6">
              <h3>Estimate impact of code changes</h3>
            </div>
            <div class="col-md-6">
            </div>
          </div>          
          <div class="row hero-section">
            <div class="col-md-6">
            </div>
            <div class="col-md-6">
              <h3>Reflect weekly on your work patterns</h3>
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
    })
    
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: 700;
  padding-bottom: 2%;
}

h3 {
  font-weight: 700;
  padding-bottom: 2%;
}

h4 {
  padding-bottom: 2%;
}

.vertical-center {
  margin: 0;
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.hero-section {
  margin-bottom: 10%;
}

ul {
  list-style-type: none;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

