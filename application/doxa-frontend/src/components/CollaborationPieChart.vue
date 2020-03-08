<template>
  <div v-if="this.isReady" class="container text-center">
    <h5>Collaboration / Independent Time Balance</h5>
    <div>
      All-time average <b>35%</b> time in collaboration.
    </div>
    <donut 
      :id="name"
      :data="donutData"
      :colors="graphColors"
      resize="True"
      :formatter="this.percentFunc"
    >
    </donut>
  </div>
  <div v-else class="container text-center">
    <h5 class="text-center">Collaboration / Independent Time Balance</h5>
    <br>
    <br>
    <b class="text-center">Loading...</b>
  </div>
  </div>
</template>
<script>
  import { DonutChart } from 'vue-morris'
  export default {
    methods: {
      percentFunc: function(string) {
        return string + ' hrs'
      }
    },
    components: {
      'donut': DonutChart
    },
    props: {
      activity: {
        default: Array(),
        type: Array
      },
      number: {
        default: 1,
        type: Number
      },
      isReady: {
        default: false,
        type: Boolean
      }
    },
    computed: {
      donutData: function () {
        var totalCollaborative = 0
        var totalIndependent = 0
        var totalRefocusing = 0
        var totalWorkHours = 0

        // loop through collaborative, independent
        // Need to only add values which are > 0
        var activity = this.activity
        activity.forEach(function(act) {
          var actDatetime = new Date(act.datetime_utc)

          if (act.is_workday_time && (actDatetime < new Date())) {
            totalWorkHours += 1
            if (act.is_collaborative_time) totalCollaborative += 1
            else if (act.is_focus_time) totalIndependent += 1
            else if (act.is_refocus_time) totalRefocusing += 1
            else console.log('Not categorized')
          }
        })

        var cP = (totalCollaborative*5/60).toFixed(1)
        var iP = (totalIndependent*5/60).toFixed(1)
        var rP = (totalRefocusing*5/60).toFixed(1)

        var valuesList = [
          { label: 'Collaborative Time', value: cP },
          { label: 'Focused Time', value: iP },
          { label: 'Refocusing Time', value: rP }
        ]
        var returnArray = []
        
        valuesList.forEach(function(val) {
          if((val.value != 0) && !isNaN(val.value)) {
            returnArray.push(val)
          }
        })
        return returnArray
      },
    
      graphColors: function() {
        var colorDict = {
          'Collaborative Time': '"#294d64"',
          'Focused Time': '"#69B8EA"',
          'Refocusing Time': '"#3b7194"'
        }
        var colorsList = []
        this.donutData.forEach(function(data) {
          colorsList.push(colorDict[data.label])
        })
        var list = '[' + colorsList.join() + ']'
        return list
      },
      name: function() {
        return 'collaboration-pie' + this.number
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
