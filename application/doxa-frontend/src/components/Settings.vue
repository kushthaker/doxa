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
        <b-form-select v-model="selected" :options="options">
            <option disabled value="">Please select one</option>
            <option>min 6 am</option>
            <option>list(numpy.arange(6,15,0.5))</option>
            <option>max 3 pm</option>
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
            <option>min 3 pm</option>
            <option>list(numpy.arange(15,23,0.5))</option>
            <option>max 11 pm</option>
        </b-form-select>
        </b-form-group>

        <!-- Focus length -->

        <b-form-group
          label="Focus Time Length"
          label-for="input-3"
          description="How long you want to focus per day (e.g. 2 hours)"
          row
        >
        <b-form-select v-model="selected" :options="options">
            <option disabled value="">Please select one</option>
            <option>min 0.5</option>
            <option>list(numpy.arange(0.5,3,0.5))</option>
            <option>max 3</option>
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
  export default {
    computed: mapState({
      userData: function(state){
        return state.userData
      }
    })
  }
</script>

<style>  
</style>
