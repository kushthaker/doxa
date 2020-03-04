<template>  
  <div>
    <b-container>
      <div class="row text-center">
        <h1>Potential time to focus</h1>
      </div>
      <div class="row">
        <div class="col-md-6 text-center">
          <h4 v-if="this.activityDataIsReady">You have <b>{{this.remainingFocusHours}}</b> remaining free hours for focused work this week.</h4>
          <b v-else class="text-center">Loading data...</b>

        </div>
        <div class="col-md-6 text-center">
        </div>

      </div>
      <br>
      <div class="row text-center">
        <h1>How you have spent your time so far</h1>
      </div>
      <div class="row">
        <div class="col-md-6">
          <pie v-bind:activity="this.activityData" :number="1" :isReady="this.activityDataIsReady"></pie>
        </div>
        <div class="col-md-6">
          <disconnect v-bind:activity="this.activityData" :isReady="this.activityDataIsReady"></disconnect>
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
      activityDataIsReady: function(state) {
        return state.activityData.length > 0
      },
      remainingFocusHours: function(state) {
        const PERIOD_LENGTH = 1/12 // 1 hour divided by length of five minute periods
        var activity = state.activityData
        var now = new Date()
        var remainingHours = activity.filter(function(act) {
          var activityUTCDatetime = new Date(act.datetime_utc)
          return (activityUTCDatetime > now) & (!act.not_work_hours) & (act.google_calendar_event_count === 0)
        }).length * PERIOD_LENGTH
        return remainingHours.toFixed(1)
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
