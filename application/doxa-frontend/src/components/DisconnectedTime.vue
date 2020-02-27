<template>
  <span>
    <h3 class="text-center">Disconnecting after hours</h3>
    <row>
      <h4> You have disconnected {{collaborativeDayCounts.disconnectedDays}} out of {{collaborativeDayCounts.totalDays}} potential days.
      </h4>
    </row>
  </span>
</template>

<script>
  export default {
    props: {
      activity: {
        default: Array(),
        type: Array
      }
    },
    computed: {
      collaborativeDayCounts: function () {
        var activity = this.activity
        var disconnectedDays = 0
        var offHourActivities = activity.filter(function(act) {
          return act.not_work_hours
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
          if(act.is_collaborative) {
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
          totalDays,
          disconnectedDays
        }
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #collaboration-pie {
    font-size: 14px;
  }
</style>
