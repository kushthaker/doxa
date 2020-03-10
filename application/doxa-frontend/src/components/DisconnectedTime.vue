<template>
  <div class="text-center">
    <h5>Disconnected After-Hours</h5>
    <div>
      All-time average <b>2.7</b> days per week.
    </div>
    <br>
    <br>
    <div v-if="this.isReady" class="text-center">
      <h2>You disconnected from work after-hours</h2>
      <h2 class="disconnected-days">{{collaborativeDayCounts.disconnectedDays}} / {{collaborativeDayCounts.totalDays}}</h2>
      <h2>days last week.</h2>
    </div>
    <div v-else class="row text-center">
      <b class="text-center">Loading...</b>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      activity: {
        default: Array(),
        type: Array
      },
      isReady: { default: false, type: Boolean }
    },
    computed: {
      collaborativeDayCounts: function () {
        var activity = this.activity
        var disconnectedDays = 0
        var offHourActivities = activity.filter(function(act) {
          return !act.work
        })
        var uniqueDays = new Set(offHourActivities.map(function(act) {
          return new Date(act.datetime_utc).getUTCDate()
        }))
        var days = {}
        var today = new Date().getDate()
        uniqueDays.forEach(function(day) {
          if (day <= today) {
            days[day] = 0  
          }
        })
        offHourActivities.forEach(function(act) {
          if(act.is_collaborative_time) {
            var day = new Date(act.datetime_utc).getUTCDate()
            if(day in days) {
              days[day] += 1
            }
          }
        })
        var disconnectedDays = 0
        var totalDays = Object.keys(days).length
        Object.keys(days).forEach(function(day) {
          if(days[day] == 0) {
            disconnectedDays += 1
          }
        })
        return {
          totalDays: totalDays - 1,
          disconnectedDays
        }
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.disconnected-days {
    font-size: 4em;
    font-weight: 900;
}

</style>
