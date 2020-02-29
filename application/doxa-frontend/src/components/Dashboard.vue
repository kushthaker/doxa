<template>  
  <div>
    <b-container>
      <div class="row text-center">

        <h1>How you spend your time</h1>
      </div>
      <div class="row">
        <div class="col-md-6">
          <pie v-bind:activity="this.activityData" :number="1"></pie>
        </div>
        <div class="col-md-6">
          <disconnect v-bind:activity="this.activityData"></disconnect>
        </div>
      </div>
      <b-row><br></b-row>
    </b-container>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  import CollaborationPieChart from '@/components/CollaborationPieChart'
  import DisconnectedTime from '@/components/DisconnectedTime'
  export default {
    components: {
      'pie': CollaborationPieChart,
      'disconnect': DisconnectedTime
    },
    computed: mapState({
      activityData: function(state) {
        return state.activityData
      },
      formErrors: function(state) {
        return state.formErrors
      },
      changePasswordSuccess: (state) => {
        return state.changePasswordSuccess
      }
    })
  }
</script>
