<template>
  <div>
    <b-container>

      <b-row class="text-center">
        <b-col></b-col>
        <b-col cols="10">
          <h2>Settings</h2>
        </b-col>
        <b-col></b-col>
       </b-row>

      <b-row class="text-center">
        <b-col></b-col>
        <b-col cols="10">
          <h4>Your details</h4>
        </b-col>
        <b-col></b-col>
      </b-row>

      <b-form @submit="">
        <!-- Email address -->

        <b-form-group
          label="Email address"
          label-for="input-1"
          description="We'll never share your email with anyone else."
          row
        >
          <b-form-input
            id="input-1"
            value=""
            type="email"
            required
            placeholder="Your email"
          ></b-form-input>
        </b-form-group>

        <!-- Username -->

        <b-form-group
          label="Username"
          label-for="input-2"
          description="Your Fulfilled.ai username"
          row
        >
          <b-form-input
            id="input-2"
            value=""
            type="text"
            required
            placeholder="realdonaldtrump"
          ></b-form-input>
        
        <!-- Change password (not implemented) -->
        </b-form-group>
        <b-form-group
          label=""
        >
        <b-button variant="outline-info" to="change-password">Change your password</b-button>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>

       <b-row class="text-center">
        <b-col></b-col>
        <b-col cols="10">
          <h4>Your integrations</h4>
        </b-col>
        <b-col></b-col>
       </b-row>
      
      <b-row v-if="userData.slack_user_id">
        <b-col></b-col>
        <b-col cols="4">Slack has been integrated</b-col>
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

      <b-row>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Slack logo -->
          You still need to integrate Github
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" href="/github-integration">Integrate Github</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
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
