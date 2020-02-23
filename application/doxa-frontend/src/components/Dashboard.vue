<template>  
  <div>
    <b-container>
      <h1>How you spend your time</h1>
      <div v-if="formErrors" class="error-messages">
        <b-alert v-for="error in formErrors" show variant="warning" v-bind:key="error">
          {{error}}
        </b-alert>
      </div>
      <div>
        <pie v-bind:activity="this.activityData"></pie>
        <!-- {{activityData}} -->

      </div>
    </b-container>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  import CollaborationPieChart from '@/components/CollaborationPieChart'
  export default {
    components: {
      'pie': CollaborationPieChart
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
