<template>
  <div>

    <b-container>

      <b-row class="text-center">
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <h1>Settings</h1>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row><br></b-row>
      <b-row class="text-center">
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <h4>Update your details</h4>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>

      <!-- User Workday Preferences -->
      <b-form @submit="">
        <!-- Workday start -->

        <b-form-group
          label="Workday Start"
          label-for="input-2"
          description="Usual time that your workday starts (e.g. 9:30am)"
          row
        >
<!--           <vue-timepicker class="custom-timepick" :hour-range="[[5, 14]]" :minute-interval="30" hide-disabled-hours format="HH:mm" v-model="workdayStart"></vue-timepicker> -->
        <b-form-select v-model="selected" :options="options">
            <option disabled value="">Please select one</option>
            <option>6:00 am</option>
            <option>6:30 am</option>
            <option>7:00 am</option>
            <option>7:30 am</option>
            <option>8:00 am</option>
            <option>8:30 am</option>
            <option>9:00 am</option>
            <option>9:30 am</option>
            <option>10:00 am</option>
            <option>10:30 am</option>
            <option>11:00 am</option>
            <option>11:30 am</option>
            <option>12:00 pm</option>
            <option>12:30 pm</option>
            <option>1:00 pm</option>
            <option>1:30 pm</option>
            <option>2:00 pm</option>
            <option>2:30 pm</option>
        </b-form-select>
        </b-form-group>

        <!-- Workday end -->

        <b-form-group
          label="Workday End"
          label-for="input-3"
          description="Usual time that your workday ends. (e.g. 5:30pm)"
          row
        >
        <b-form-select v-model="selected" :options="options">
            <option disabled value="">Please select one</option>
            <option>3:00 pm</option>
            <option>3:30 pm</option>
            <option>4:00 pm</option>
            <option>4:30 pm</option>
            <option>5:00 pm</option>
            <option>5:30 pm</option>
            <option>6:00 pm</option>
            <option>6:30 pm</option>
            <option>7:00 pm</option>
            <option>7:30 pm</option>
            <option>8:00 pm</option>
            <option>8:30 pm</option>
            <option>9:00 pm</option>
            <option>9:30 pm</option>
            <option>10:00 pm</option>
            <option>10:30 pm</option>
            <option>11:00 pm</option>
        </b-form-select>
        </b-form-group>

        <!-- Focus length -->

        <b-form-group
          label="Focus Time Length"
          label-for="input-3"
          description="How long you want to focus daily (e.g. 120 mins)"
          row
        >
        <b-form-select v-model="selected" :options="options">
            <option disabled value="">Please select one</option>
            <option>30 min</option>
            <option>60 min</option>
            <option>90 min</option>
            <option>120 min</option>
            <option>180 min</option>
        </b-form-select>
        </b-form-group>
    
        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>

      <!-- Integrations -->

      <b-row><br></b-row>
      <b-row><br></b-row>
      <b-row class="text-center">
      <b-col cols="1"></b-col>
      <b-col cols="10">
        <h4>Your integrations</h4>
      </b-col>
        <p>We use your Slack and Calendar events to book time to focus in the upcoming period, offer personal suggestions and display aggregated historical data spent in collaboration and focus. Github history is used to estimate of your contribution for a given period. Your data is never shared with others and available exclusively to you (for now...)</p>
      <b-col cols="1"></b-col>
     </b-row>
      <b-row><br></b-row>
      <b-row v-if="userData.slack_user_id">
        <b-col></b-col>
        <b-col cols="4" class="text-center">Slack has been integrated</b-col>
        <b-col cols="4">
          <b-button variant="outline-secondary" href="/slack-install">Reintegrate Slack</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      
       <b-row v-else>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Slack logo -->
          You still need to integrate Slack
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" href="/slack-install">Integrate Slack</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      <hr class="my-4">
      
      <b-row v-if="userData.google_calendar_user_id">
        <b-col></b-col>
        <b-col cols="4" class="text-center">Google Calendar has been integrated</b-col>
        <b-col cols="4">
          <b-button variant="outline-secondary" href="/build_google_calendar_auth_request">Reintegrate Google Calendar</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      <b-row v-else>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Slack logo -->
          You still need to integrate Google Calendar
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" href="/build_google_calendar_auth_request">Integrate Google Calendar</b-button>
        </b-col>
        <b-col></b-col>  
      </b-row>

      <hr class="my-4">

      <b-row v-if="userData.github_user_id">
        <b-col></b-col>
        <b-col cols="4" class="text-center">Github has been integrated</b-col>
        <b-col cols="4">
          <b-button variant="outline-secondary" href="/github-auth">Reintegrate Github</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      <b-row v-else>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Github logo -->
          You still need to integrate Github
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" href="/github-auth">Integrate Github</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      <b-row><br></b-row>
      <b-row><br></b-row>
    </b-container>

    <!-- Change password (not implemented) -->
    </b-form-group>
    <b-form-group
      label=""
    >
    <b-button variant="outline-info" to="change-password">Change your password</b-button>
    </b-form-group>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  import VueTimepicker from 'vue2-timepicker'
  export default {
    data() {
      return {
        workdayStart: {
          type: Object,
          default: function() {
            return ({
              HH: '9',
              mm: '30'
            })
          }
        },
        workdayEnd: {
          type: Object,
          default: function() {
            return ({
              HH: '5',
              mm: '30'
            })
          }
        }
      }
    },
    computed: mapState({
      userData: function(state) {
        return state.userData
      }
    }),
    components: { VueTimepicker }
  }
</script>

<style scoped>
  .custom-timepick .active li{
    background: #007bff;
  }
</style>
