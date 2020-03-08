<template>  
  <div>
    <b-container>
      <div class="row greeting">
        <div>
          <h5>Good Afternoon, Laurier.</h5>
        </div>
      </div>
      <div class="row suggestions">
        <h5 class="alert alert-warning">Spend less time on Slack this week. <a href="">Set Do Not Disturb</a></h5>
        <h5 class="alert alert-warning">Need to attend all meetings this week? <a href="">See Calendar</a></h5>
        <h5 class="alert alert-warning">Have you disconnected after work this week? <a href="">Set Do Not Disturb</a></h5>
      </div>
      <div class="row current-week">
        <div>
          <h3 class="subber">
            <b v-if="this.activityDataIsReady">{{this.remainingFocusHours}}/40</b> 
            <b v-else class="text-center">-/40</b>
            hours remain to focus this week.
          </h3>
          <p>Current week from 
            <b v-if="this.activityDataIsReady">{{this.dateRange.startDate}}</b>
            <b v-else="">-</b>
            to
            <b v-if="this.activityDataIsReady">{{this.dateRange.endDate}}</b>
            <b v-else="">-</b>
          </p>
          <p>Next focus session is <b>tomorrow at 9:30am</b>.</p>
        </div>
      </div>


      <div class="row previous-week">
        <div>
          <h3 class="subber">Previous week trends</h3>
          <p>Previous week from 
            <b v-if="this.activityDataIsReady">{{this.dateRange.startDate}}</b>
            <b v-else="">-</b>
            to
            <b v-if="this.activityDataIsReady">{{this.dateRange.endDate}}</b>
            <b v-else="">-</b>
          </p>
        </div>
      </div>

      <br>

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
          return (activityUTCDatetime > now) && (act.is_workday_time) && (! act.is_collaborative_time) && (! act.is_refocus_time)
        }).length * PERIOD_LENGTH
        return remainingHours.toFixed(0)
      },
      formErrors: function(state) {
        return state.formErrors
      },
      changePasswordSuccess: (state) => {
        return state.changePasswordSuccess
      },
      dateRange: function(state) {
        if(state.activityData.length == 0) {
          return {}
        }
        var startDate = new Date(state.activityData[0].datetime_utc)
        if ((startDate.getDate() == 7) && (startDate.getMonth() == 2) && (startDate.getUTCFullYear() == 2020)) {
          startDate = new Date(startDate.setDate(8)).toDateString()
        }
        else {
          startDate = startDate.toDateString()
        }
        var endDate = new Date(state.activityData[state.activityData.length-1].datetime_utc).toDateString()
        return { startDate, endDate }
        }
      // fullDateRange: function(state) {
      //   if(state.activityData.length == 0) {
      //     return {}
      //   }
      //   var startDate = new Date(state.activityData[0].datetime_utc)
      //   var endDate = new Date(state.activityData[state.activityData.length-1].datetime_utc)
      //   return { startDate, endDate }
      // },
    })
  }
</script>

<style>
  .greeting {
    margin-bottom: 2%;
  }

  .current-week {
    margin-bottom: 5%;
  }

  .suggestions {
    margin-bottom: 5%;
  }

  .suggestions a {
    text-decoration: underline;
  }

  .subber {
    margin-bottom: 0.5em;
  }
</style>
