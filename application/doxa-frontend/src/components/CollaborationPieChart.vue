<template>
  <div v-if="this.isReady" class="container text-center">
    <h5>Collaboration / Independent Time Balance</h5>
    <div>
      {{this.collabMessage}}
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
          var now = new Date()
          if (act.is_workday_time && (actDatetime < now)) {
            totalWorkHours += 1
            if (act.is_collaborative_time == true) totalCollaborative += 1
            else if (act.is_refocus_time == true) { console.log(act.datetime_utc); totalRefocusing += 1 }
            else if (act.is_focus_time == true) totalIndependent += 1
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
      },
      noData: function() {
        return (this.activity.length > 0) & (this.donutData.length == 0)
      },
      collabMessage: function() {
        if(this.isReady) {
          var collaborativeHours = parseFloat(this.donutData.filter(function(d) {return d.label == 'Collaborative Time' })[0].value)
          const allTimeAverage = 14.5
          if (collaborativeHours < allTimeAverage) {
            return `Nice work! Last week you had ${collaborativeHours} collaborative hours, less than your all time average of ${allTimeAverage} hours.`
          }
          else {
            return `Last week you had ${collaborativeHours} collaborative hours, more than your all time average of ${allTimeAverage} hours.`
          }
        }
        else {
          return ''
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
