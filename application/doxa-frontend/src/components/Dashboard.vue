<template>  
  <div>
    <b-container>
      <div class="row greeting">
        <div>
          <h5>Good {{this.timeOfDay}}, <b>{{this.userName}}</b>.</h5>
        </div>
      </div>
       <div class="row current-week">
        <div>
          <h3 class="subber">
            <b v-if="this.activityDataIsReady">{{this.remainingFocusHours}}/{{this.totalWorkHours}}</b> 
            <b v-else class="text-center">-/{{this.totalWorkHours}}</b>
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
      <div class="row suggestions">
        <span v-if="shouldNudge['dnd-now']">
          <h5 class="alert alert-warning">Spend less time on Slack today. <a @click="requestNudge('dnd-now')">Set Do Not Disturb Now</a></h5>
        </span>
        <span v-else>
          <h5 class="alert alert-success">DONE. Fulfilled has set Slack to <em>Do Not Disturb</em> so you can focus without distraction.</h5>
        </span>
        <span v-if="shouldNudge['open-calendar']">
          <h5 class="alert alert-warning">Need to attend all meetings this week? <a @click="requestNudge('open-calendar')" href="https://calendar.google.com" target="_blank">Open Calendar</a>.</h5>
        </span>
        <span v-else>
          <h5 class="alert alert-success">Cool. If you need <b><em>Fulfilled</em></b> to also schedule time for you, go to Settings and click "Schedule Time".</h5>
        </span>
        <span v-if="shouldNudge['dnd-after-hours']">
          <h5 class="alert alert-warning">Have you disconnected after work this week? <a @click="requestNudge('dnd-after-hours')">Set Do Not Disturb after hours</a></h5>
        </span>
        <span v-else>
          <h5 class="alert alert-success">DONE. Fulfilled will set Slack to <em>Do Not Disturb</em> when your workday ends so you can disconnect from it.</h5>
        </span>
      </div>
     
      <div class="row previous-week">
        <div>
          <h3 class="subber">Previous week trends</h3>
          <p>Previous week from 
            <b v-if="this.lastWeekActivityDataIsReady">{{this.lastWeekDateRange.startDate}}</b>
            <b v-else="">-</b>
            to
            <b v-if="this.lastWeekActivityDataIsReady">{{this.lastWeekDateRange.endDate}}</b>
            <b v-else="">-</b>
          </p>
        </div>
      </div>

      <br>

      <div class="row">
        <div class="col-md-6">
          <pie v-bind:activity="this.lastWeekActivityData" :number="1" :isReady="this.lastWeekActivityDataIsReady"></pie>
        </div>
        <div class="col-md-6">
          <disconnect v-bind:activity="this.lastWeekActivityData" :isReady="this.lastWeekActivityDataIsReady"></disconnect>
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
    props: {
      shouldNudge: {
        type: Object,
        default: function() {
          return ({ 'dnd-now': true, 'dnd-after-hours': true, 'open-calendar': true })
        }
      }
    },
    methods: {
      requestNudge: function(nudgeType) {
        this.$store.dispatch('requestNudge', { nudgeType })
        this.shouldNudge[nudgeType] = false
      },
    },
    computed: mapState({
      userName: function(state) {
        return state.currentUser.username
      },
      activityData: function(state) {
        return state.activityData
      },
      activityDataIsReady: function(state) {
        return state.activityData.length > 0
      },
      lastWeekActivityData: function(state) {
        return state.lastWeekActivityData
      },
      lastWeekActivityDataIsReady: function(state) {
        return state.lastWeekActivityData.length > 0
      },
      totalWorkHours: function(state) {
        if(this.activityDataIsReady) {
          return this.activityData.filter(function(act) {
            return act.is_workday_time == true
          }).length/12
        }
        else { return '-' }
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
      },
      lastWeekDateRange: function(state) {
        if(state.lastWeekActivityData.length == 0) {
          return {}
        }
        var startDate = new Date(state.lastWeekActivityData[0].datetime_utc)
        if ((startDate.getDate() == 29) && (startDate.getMonth() == 1) && (startDate.getUTCFullYear() == 2020)) {
          startDate = new Date(new Date(startDate.setDate(1)).setMonth(2))
        }
        startDate = startDate.toDateString()
        var endDate = new Date(state.lastWeekActivityData[state.lastWeekActivityData.length-1].datetime_utc).toDateString()
        return { startDate, endDate }
      },
      timeOfDay: function() {
        var nowHour = new Date().getHours()
        if ((nowHour < 12) && (nowHour > 0))  {
          return 'Morning'
        }
        else if((nowHour > 12) && (nowHour < 18)) {
          return 'Afternoon'
        }
        else {
          return 'Evening'
        }
      }
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
