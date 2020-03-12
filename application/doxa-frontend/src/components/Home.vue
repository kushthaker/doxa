<template>
  <div>
    <section class="hero is-primary">
        <div class="container">
          <div class="row hero-section">
            <div>
              <h1>Find focus at work with Fulfilled.</h1>
              <h4>Developers use Fulfilled to focus on their craft, collaborate smarter, and disconnect after work.</h4>
              <button onclick="window.location.href = 'https://fulfilled.ai/#/register-new-user';" class="btn btn-dark">Try it free</button>
            </div>
          </div>
          <div class="row hero-section">
            <div class="col-md-6 my-auto">
              <h3>Book time to work deeply everyday</h3>
            </div>
            <div class="col-md-6">
               <img class="trends" src="../assets/cal.png" alt="Fulfilled.ai">
            </div>
          </div>          
          <div class="row hero-section">
            <div class="col-md-6 order-sm-12 my-auto">
              <h3>Reflect on your work patterns</h3>
            </div>
            <div class="col-md-6 order-sm-1">
              <img class="trends" src="../assets/trends.png" alt="Fulfilled.ai">
            </div>
          </div>       
          <div class="row hero-section">
            <div class="col-md-6 my-auto">
              <h3>Get tips to focus better and disconnect after work</h3>
            </div>
            <div class="col-md-6">
              <img class="trends" src="../assets/tips.png" alt="Fulfilled.ai">
            </div>
          </div>
        </div>
    </section>
  </div>
</template>
<script>
  export default {
    data() {
      return {}
    }
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

img {
      max-width: 100%;
      max-height: 100%;
      display: block; /* remove extra space below image */
  }

button {
  font-family: 'Roboto', sans-serif;
}

</style>

