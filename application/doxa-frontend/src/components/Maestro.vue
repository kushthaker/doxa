<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-10">
          <h1>h1 Welcome, Maestros.</h1>
          <h2>Let's connect your apps.</h2>
          <h3>h3 Use this for most section headers.</h3>
          <h4>h1 Let's connect your apps.</h4>
          <h5>h1 Let's connect your apps.</h5>
          <p>h1 Let's connect your apps.</p>
          <a>h1 Let's connect your apps.</a>
        </div>
        <div class="col-md-2" id="right-sidebar">
          <h3>Quotes</h3>
            <div class="sidebar-section">
              <p class="sidebar">"Less mental clutter means more mental resources available for deep thinking."</p>
              <h6>-Cal Newport</h6>
            </div>
          <h3>Concepts</h3>
            <div>
              <p class="sidebar">"Attention residue is when thoughts about a task persist and intrude while performing another task"</p>
              <h6>-Sophie Leroy</h6>
            </div>

        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    computed: mapState({
      maestro: function(state) {
        return state.userData
      },
      currentUser: function(state) {
        return state.currentUser
      }
    })
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  blockquote:before {
  color: #ccc;
  content: close-quote;
  font-size: 4em;
  line-height: 0.1em;
  margin-right: 0.25em;
  vertical-align: -0.4em;
}

</style>
