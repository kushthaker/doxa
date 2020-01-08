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
      
       <b-row>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Slack logo -->
          You still need to integrate Slack
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" to="/slack-integration">Integrate Slack</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
      
      <hr class="my-4">
      
      <b-row>
        <b-col></b-col>
        <b-col cols="4" class="text-center">
          <!-- Slack logo -->
          You still need to integrate Google Calendar
        </b-col>
        <b-col cols="4">
          <b-button variant="outline-primary" to="/google-calendar-integration">Integrate Google Calendar</b-button>
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
  // this has not been implemented yet
  export default {
  
  }
</script>

<style>
  
</style>