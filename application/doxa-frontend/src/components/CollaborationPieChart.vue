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
        return string + "%"
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
          if (!act.is_off_hours) {
            totalWorkHours += 1
            if (act.is_collaborative) totalCollaborative += 1
            else if (act.is_focused) totalIndependent += 1
            else if (act.is_refocusing) totalRefocusing += 1
            else console.log('Not categorized')  
          }
        })
        var cP = (100.0*(totalCollaborative/totalWorkHours)).toFixed(0)
        var iP = (100.0*(totalIndependent/totalWorkHours)).toFixed(0)
        var rP = (100.0*(totalRefocusing/totalWorkHours)).toFixed(0)

        var valuesList = [
          { label: 'Collaborative Time', value: cP },
          { label: 'Independent Time', value: iP },
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
          'Collaborative Time': '"#FF6384"',
          'Independent Time': '"#36A2EB"',
          'Refocusing Time': '"#FFFF11"'
        }
        var colorsList = []
        this.donutData.forEach(function(data) {
          colorsList.push(colorDict[data.label])
        })
        return '[' + colorsList.join() + ']'
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
