webpackJsonp([1],{"9M+g":function(e,n){},Dvtt:function(e,n,r){var t=r("SnlE");"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);r("rjj0")("7354f6c8",t,!1,{})},G9YX:function(e,n,r){(e.exports=r("FZ+f")(!0)).push([e.i,"\nh1[data-v-8dc7cce2], h2[data-v-8dc7cce2] {\n  font-weight: normal;\n}\nul[data-v-8dc7cce2] {\n  list-style-type: none;\n  padding: 0;\n}\nli[data-v-8dc7cce2] {\n  display: inline-block;\n  margin: 0 10px;\n}\na[data-v-8dc7cce2] {\n  color: #42b983;\n}\n","",{version:3,sources:["/Users/lauriermantel/startup/doxa/doxa-app/application/doxa-frontend/src/components/src/components/Home.vue"],names:[],mappings:";AAsCA;EACA,oBAAA;CACA;AACA;EACA,sBAAA;EACA,WAAA;CACA;AACA;EACA,sBAAA;EACA,eAAA;CACA;AACA;EACA,eAAA;CACA",file:"Home.vue",sourcesContent:['<template>\n  <div>\n    <section class="hero is-primary">\n      <div class="hero-body">\n        <div class="container has-text-centered">\n          <h2 class="title">List of users</h2>\n        </div>\n      </div>\n    </section>\n    <section class="section">\n      <div class="container">\n        <div class="card" v-for="user in users" v-bind:key="user.id">\n          <div class="card-content">\n            <div v-if="user">\n              <p class="title">Name: {{ user.username}}; Email: {{user.email}}</p>\n              <p class="detail">See this <router-link :to="`maestro/${user.id}`">maestro</router-link> </p>\n            </div>\n          </div>\n        </div>\n      </div>\n    </section>\n  </div>\n</template>\n<script>\n  import { mapState } from \'vuex\'\n  export default {\n    data() {\n      return {}\n    },\n    computed: mapState({\n      users: state => state.users\n    })\n    \n  }\n<\/script>\n\n\x3c!-- Add "scoped" attribute to limit CSS to this component only --\x3e\n<style scoped>\nh1, h2 {\n  font-weight: normal;\n}\nul {\n  list-style-type: none;\n  padding: 0;\n}\nli {\n  display: inline-block;\n  margin: 0 10px;\n}\na {\n  color: #42b983;\n}\n</style>\n\n'],sourceRoot:""}])},GHGh:function(e,n,r){var t=r("z/+d");"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);r("rjj0")("08bac906",t,!1,{})},JXf5:function(e,n,r){var t=r("G9YX");"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);r("rjj0")("678c2d17",t,!1,{})},Jmt5:function(e,n){},MuaJ:function(e,n,r){var t=r("XtP8");"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);r("rjj0")("06d32c94",t,!1,{})},NHnr:function(e,n,r){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var t=r("7+uW"),s=r("NYxO");function a(e){if(!e||e.split(".").length<3)return!1;var n=JSON.parse(atob(e.split(".")[1])),r=new Date(1e3*n.exp);return new Date<r}var o={computed:Object(s.b)({isAuthenticated:function(e){return a(e.jwt)},currentUser:function(e){return e.currentUser}})},i=function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",[t("b-navbar",{attrs:{toggleable:"lg",type:"dark",variant:"info"}},[t("div",[t("b-navbar-brand",{attrs:{to:"/"}},[t("img",{attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"120",height:"120"}})])],1),e._v(" "),t("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),e._v(" "),t("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[t("b-navbar-nav",{staticClass:"ml-auto"},[e.isAuthenticated?[t("b-nav-item",{attrs:{to:"/growth"}},[e._v("Your Growth")]),e._v(" "),t("b-nav-item-dropdown",{attrs:{text:e.currentUser.email,right:""}},[t("b-dropdown-item",{attrs:{to:"/focus-plan"}},[e._v("Focus Plan")]),e._v(" "),t("b-dropdown-item",{attrs:{to:"/settings"}},[e._v("Settings")]),e._v(" "),t("b-dropdown-item",{attrs:{to:"/logout"}},[e._v("Logout")])],1)]:[t("b-nav-item",{attrs:{to:"/login"}},[e._v("Login")]),e._v(" "),t("b-nav-item",{attrs:{to:"/register-new-user"}},[e._v("Register")]),e._v(" "),t("b-nav-item",{attrs:{to:"/learn-more"}},[e._v("Learn More")]),e._v(" "),t("b-nav-item",{attrs:{to:"/contact"}},[e._v("Contact")])]],2)],1)],1)],1)};i._withStripped=!0;var A={render:i,staticRenderFns:[]},c=A;var l=!1;var u=r("VU/8")(o,c,!1,function(e){l||r("Dvtt")},"data-v-61dd7a3d",null);u.options.__file="src/components/Header.vue";var d=u.exports,p=(r("Jmt5"),r("9M+g"),{name:"App",components:{"app-header":d}}),m=function(){var e=this.$createElement,n=this._self._c||e;return n("div",{attrs:{id:"app"}},[n("app-header"),this._v(" "),n("router-view")],1)};m._withStripped=!0;var f={render:m,staticRenderFns:[]},v=f;var h=!1;var g=r("VU/8")(p,v,!1,function(e){h||r("GHGh")},null,null);g.options.__file="src/App.vue";var b=g.exports,w=r("/ocq"),C={data:function(){return{}},computed:Object(s.b)({users:function(e){return e.users}})},E=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[e._m(0),e._v(" "),r("section",{staticClass:"section"},[r("div",{staticClass:"container"},e._l(e.users,function(n){return r("div",{key:n.id,staticClass:"card"},[r("div",{staticClass:"card-content"},[n?r("div",[r("p",{staticClass:"title"},[e._v("Name: "+e._s(n.username)+"; Email: "+e._s(n.email))]),e._v(" "),r("p",{staticClass:"detail"},[e._v("See this "),r("router-link",{attrs:{to:"maestro/"+n.id}},[e._v("maestro")])],1)]):e._e()])])}),0)])])};E._withStripped=!0;var U={render:E,staticRenderFns:[function(){var e=this.$createElement,n=this._self._c||e;return n("section",{staticClass:"hero is-primary"},[n("div",{staticClass:"hero-body"},[n("div",{staticClass:"container has-text-centered"},[n("h2",{staticClass:"title"},[this._v("List of users")])])])])}]},x=U;var Y=!1;var F=r("VU/8")(C,x,!1,function(e){Y||r("JXf5")},"data-v-8dc7cce2",null);F.options.__file="src/components/Home.vue";var D=F.exports,_={computed:Object(s.b)({maestro:function(e){return e.userData},currentUser:function(e){return e.currentUser}})},G=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[e.maestro?r("div",[r("h3",[e._v("The maestro is "),r("em",[e._v(e._s(e.maestro.username))])]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.username,expression:"maestro.username"}],attrs:{placeholder:"e.g. Callum John Killian Mitchell"},domProps:{value:e.maestro.username},on:{input:function(n){n.target.composing||e.$set(e.maestro,"username",n.target.value)}}}),e._v(" "),r("p",[e._v("The maestro's email is "),r("strong",[e._v(e._s(e.maestro.email))])]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.email,expression:"maestro.email"}],attrs:{placeholder:"e.g. maestro@fulfilled.maestro"},domProps:{value:e.maestro.email},on:{input:function(n){n.target.composing||e.$set(e.maestro,"email",n.target.value)}}})]):r("div",[e._v("\n    Loading...\n  ")])])};G._withStripped=!0;var y={render:G,staticRenderFns:[]},V=y;var q=!1;var L=r("VU/8")(_,V,!1,function(e){q||r("MuaJ")},"data-v-75579faf",null);L.options.__file="src/components/Maestro.vue";var P=L.exports,W={computed:Object(s.b)({newUser:function(e){return e.newUser},formErrors:function(e){return e.formErrors}}),methods:{submitUser:function(){var e=this;this.$store.dispatch("registerNewUser").then(function(){e.formErrors||e.$router.push({name:"Login"})})}}},S=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[r("b-container",[r("h2",[e._v("Register for Fulfilled.ai")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(n){return r("b-alert",{key:n,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(n)+"\n      ")])}),1):e._e(),e._v(" "),r("b-form",{on:{submit:function(n){return n.preventDefault(),e.submitUser(n)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"realdonaldtrump",required:"",id:"input-1",type:"text"},model:{value:e.newUser.username,callback:function(n){e.$set(e.newUser,"username",n)},expression:"newUser.username"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:e.newUser.email,callback:function(n){e.$set(e.newUser,"email",n)},expression:"newUser.email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:e.newUser.password,callback:function(n){e.$set(e.newUser,"password",n)},expression:"newUser.password"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:e.newUser.confirm_password,callback:function(n){e.$set(e.newUser,"confirm_password",n)},expression:"newUser.confirm_password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Register")])],1)],1)],1)};S._withStripped=!0;var k={render:S,staticRenderFns:[]},R=k;var O=r("VU/8")(W,R,!1,null,null,null);O.options.__file="src/components/Register.vue";var Q=O.exports,j={computed:Object(s.b)({loginUser:function(e){return e.loginUser},isLoggedIn:function(e){return e.isLoggedIn},formErrors:function(e){return e.formErrors}}),methods:{submitUser:function(){var e=this;return this.$store.dispatch("userLogin").then(function(){if(!e.formErrors){var n=e.$store.getters.currentUser;return e.$router.push({name:"Maestro",params:{id:n.id}},function(){}),n}})}}},K=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[r("b-container",[r("h2",[e._v("Log in to Fulfilled.ai")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(n){return r("b-alert",{key:n,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(n)+"\n      ")])}),1):e._e(),e._v(" "),r("b-form",{on:{submit:function(n){return n.preventDefault(),e.submitUser(n)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:e.loginUser.email,callback:function(n){e.$set(e.loginUser,"email",n)},expression:"loginUser.email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:e.loginUser.password,callback:function(n){e.$set(e.loginUser,"password",n)},expression:"loginUser.password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Login")])],1)],1)],1)};K._withStripped=!0;var z={render:K,staticRenderFns:[]},X=z;var H=r("VU/8")(j,X,!1,null,null,null);H.options.__file="src/components/Login.vue";var N=H.exports,Z={computed:Object(s.b)({userData:function(e){return e.userData}})},T=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h2",[e._v("Settings")])]),e._v(" "),r("b-col")],1),e._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[e._v("Your details")])]),e._v(" "),r("b-col")],1),e._v(" "),r("b-form",{on:{submit:function(e){}}},[r("b-form-group",{attrs:{label:"Email address","label-for":"input-1",description:"We'll never share your email with anyone else.",row:""}},[r("b-form-input",{attrs:{id:"input-1",value:"",type:"email",required:"",placeholder:"Your email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Username","label-for":"input-2",description:"Your Fulfilled.ai username",row:""}},[r("b-form-input",{attrs:{id:"input-2",value:"",type:"text",required:"",placeholder:"realdonaldtrump"}})],1),e._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[e._v("Change your password")])],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Submit")])],1),e._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[e._v("Your integrations")])]),e._v(" "),r("b-col")],1),e._v(" "),e.userData.slack_id?r("b-row",[r("b-col",[e._v("Slack has been integrated")])],1):r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Slack\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[e._v("Integrate Slack")])],1),e._v(" "),r("b-col")],1),e._v(" "),r("hr",{staticClass:"my-4"}),e._v(" "),r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Google Calendar\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",to:"/google-calendar-integration"}},[e._v("Integrate Google Calendar")])],1),e._v(" "),r("b-col")],1),e._v(" "),r("hr",{staticClass:"my-4"}),e._v(" "),r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Github\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-integration"}},[e._v("Integrate Github")])],1),e._v(" "),r("b-col")],1)],1)],1)};T._withStripped=!0;var J={render:T,staticRenderFns:[]},I=J;var B=!1;var M=r("VU/8")(Z,I,!1,function(e){B||r("PRuX")},null,null);M.options.__file="src/components/Settings.vue";var $=M.exports,ee={data:function(){return{}},computed:Object(s.b)({changePassword:function(e){return e.changePassword},formErrors:function(e){return e.formErrors},changePasswordSuccess:function(e){return e.changePasswordSuccess}}),methods:{submitNewPassword:function(){var e=this;this.$store.dispatch("changePassword").then(function(){e.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},ne=function(){var e=this,n=e.$createElement,r=e._self._c||n;return r("div",[r("b-container",[r("h2",[e._v("Change your password")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(n){return r("b-alert",{key:n,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(n)+"\n      ")])}),1):e._e(),e._v(" "),e.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[e._v("\n        Password changed successfully!\n      ")])],1):e._e(),e._v(" "),r("b-form",{on:{submit:function(n){return n.preventDefault(),e.submitNewPassword(n)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:e.changePassword.new_password,callback:function(n){e.$set(e.changePassword,"new_password",n)},expression:"changePassword.new_password"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:e.changePassword.confirm_new_password,callback:function(n){e.$set(e.changePassword,"confirm_new_password",n)},expression:"changePassword.confirm_new_password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Change password")])],1)],1)],1)};ne._withStripped=!0;var re={render:ne,staticRenderFns:[]},te=re;var se=r("VU/8")(ee,te,!1,null,null,null);se.options.__file="src/components/ChangePassword.vue";var ae=se.exports,oe=function(){var e=this.$createElement;return(this._self._c||e)("div")};oe._withStripped=!0;var ie={render:oe,staticRenderFns:[]},Ae=ie;var ce=r("VU/8")({beforeMount:function(){}},Ae,!1,null,null,null);ce.options.__file="src/components/SlackAuthorization.vue";var le=ce.exports,ue=r("BO1k"),de=r.n(ue),pe=r("fZjL"),me=r.n(pe),fe=r("woOf"),ve=r.n(fe),he=r("mtWM"),ge=r.n(he);function be(){return ge.a.get("/api/get_csrf")}function we(e){return{Authorization:"Bearer: "+e.token}}var Ce=r("ppUw"),Ee=r.n(Ce);t.default.use(s.a),t.default.use(Ee.a);var Ue={email:null,password:null,csrf_token:null},xe={username:null,email:null,password:null,confirm_password:null,csrf_token:null},Ye={new_password:null,confirm_new_password:null},Fe={users:[],userData:{},newUser:ve()({},xe),formErrors:null,loginUser:ve()({},Ue),currentUser:null,CSRFToken:null,jwt:"",changePassword:ve()({},Ye),changePasswordSuccess:!1,authCode:null},De={loadUsers:function(e){return ge.a.get("/api/users").then(function(n){return e.commit("setUsers",{users:n.data})})},loadUser:function(e,n){return(r=n,ge.a.get("/api/user_details",{data:r,headers:we(r)})).then(function(n){n.data||e.commit("setUserData",{userData:{error:!0}}),e.commit("setUserData",{userData:n.data})}).catch(function(e){console.log("Error loading user")});var r},loadCSRF:function(e){return be().then(function(n){return e.commit("setCSRF",{CSRFToken:n.data.csrf_token})})},registerNewUser:function(e){Fe.newUser.csrf_token=Fe.CSRFToken;var n;(n=Fe.newUser,ge.a.post("/api/register",n)).then(function(n){return e.commit("clearNewUser",{}),e.commit("setErrors",{errors:null}),!0}).catch(function(n){be().then(function(n){return e.commit("setCSRF",{CSRFToken:n.data.csrf_token})});var r=ye(n.response);return e.commit("setErrors",{errors:r}),!1})},userLogin:function(e){var n;return Fe.loginUser.csrf_token=Fe.CSRFToken,(n=Fe.loginUser,ge.a.post("/api/login",n)).then(function(n){return e.commit("setCurrentUser",{currentUser:n.data}),e.commit("saveCurrentUser",{currentUser:n.data}),e.commit("setErrors",{errors:null}),e.commit("clearLoginUser",{}),e.commit("setJWT",{jwt:n.data.token})}).catch(function(n){be().then(function(n){return e.commit("setCSRF",{CSRFToken:n.data.csrf_token})});var r=ye(n.response);e.commit("setErrors",{errors:r})})},clearFormErrors:function(e){Fe.formErrors=null},checkLogin:function(e){var n=$cookies.get("currentUser");return e.commit("setCurrentUser",{currentUser:n})},clearCredentials:function(e){$cookies.set("currentUser",null),e.commit("setCurrentUser",{currentUser:null}),e.commit("clearLoginUser",{})},changePassword:function(e){Fe.changePassword.csrf_token=Fe.CSRFToken;var n,r;(n=Fe.changePassword,r=Fe.currentUser,ge.a.post("/api/change-password",n,{headers:we(r)})).then(function(n){return be().then(function(n){return e.commit("setCSRF",{CSRFToken:n.data.csrf_token})}),e.commit("setErrors",{errors:null}),e.commit("setChangePassword",{changePasswordForm:ve()({},Ye)}),e.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(n){be().then(function(n){return e.commit("setCSRF",{CSRFToken:n.data.csrf_token})});var r=ye(n.response);return e.commit("setErrors",{errors:r}),e.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(e){e.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),e.commit("setChangePassword",{changePasswordForm:ve()({},Ye)})},slackAuthFinal:function(e){var n,r,t=Fe.currentUser,s={code:Fe.authCode};s.csrf_token=Fe.CSRFToken,(n=s,r=t,ge.a.post("/api/finalize-slack-auth",n,{headers:we(r)})).then(function(e){return e}).catch(function(e){return console.log(e),!1})}},_e={setUsers:function(e,n){e.users=n.users},setUserData:function(e,n){e.userData=n.userData},setCSRF:function(e,n){e.CSRFToken=n.CSRFToken},setErrors:function(e,n){e.formErrors=n.errors},setNewUser:function(e,n){e.newUser=n.newUser},setJWT:function(e,n){e.jwt=n.jwt},setCurrentUser:function(e,n){e.currentUser=n.currentUser,n.currentUser?e.jwt=n.currentUser.token:e.jwt=""},saveCurrentUser:function(e,n){$cookies.set("currentUser",n.currentUser)},clearLoginUser:function(e,n){e.loginUser=ve()({},Ue)},clearNewUser:function(e,n){e.newUser=ve()({},xe)},setChangePassword:function(e,n){e.changePassword=n.changePasswordForm},setChangePasswordStatus:function(e,n){e.changePasswordSuccess=n.changePasswordSuccess},setCode:function(e,n){e.authCode=n.authCode}},Ge={isAuthenticated:function(e){return a(e.jwt)},currentUser:function(e){return e.currentUser},userData:function(e){return e.userData}};function ye(e){var n,r=null;if(e.data.errors){var t=e.data.errors;r=[];var s=!0,a=!1,o=void 0;try{for(var i,A=de()((n=t,me()(n)));!(s=(i=A.next()).done);s=!0){var c=i.value,l=!0,u=!1,d=void 0;try{for(var p,m=de()(t[c]);!(l=(p=m.next()).done);l=!0){var f=p.value;r=r.concat(f)}}catch(e){u=!0,d=e}finally{try{!l&&m.return&&m.return()}finally{if(u)throw d}}}}catch(e){a=!0,o=e}finally{try{!s&&A.return&&A.return()}finally{if(a)throw o}}}return r}var Ve=new s.a.Store({state:Fe,actions:De,mutations:_e,getters:Ge});t.default.use(w.a);var qe=new w.a({routes:[{path:"/",name:"Home",component:D,beforeEnter:function(e,n,r){Ve.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:P,beforeEnter:function(e,n,r){var t=Ve.getters.isAuthenticated,s=Ve.getters.currentUser;t?s&&e.params.id===String(s.id)?Ve.dispatch("loadUser",s).then(function(){r()}):Ve.dispatch("loadUser",s).then(function(){r("/maestro/"+s.id)}):r("/login")}},{path:"/register-new-user",name:"Register",component:Q,beforeEnter:function(e,n,r){Ve.dispatch("clearFormErrors"),r()}},{path:"/login",name:"Login",component:N,beforeEnter:function(e,n,r){(Ve.dispatch("clearFormErrors"),Ve.getters.isAuthenticated)?r("/maestro/"+Ve.getters.currentUser.id):r()}},{path:"/logout",name:"Logout",beforeEnter:function(e,n,r){Ve.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:$,beforeEnter:function(e,n,r){Ve.dispatch("clearFormErrors");var t=Ve.getters.isAuthenticated,s=Ve.getters.currentUser;t?Ve.dispatch("loadUser",s).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:ae,beforeEnter:function(e,n,r){Ve.dispatch("clearFormErrors"),function(e,n){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",t=n.getters.isAuthenticated;n.getters.currentUser;if(t)return e();e(r)}(r,Ve)}},{path:"/slack-auth/:code",name:"Fulfilled.ai Slack Authentication",component:le,beforeEnter:function(e,n,r){var t=Ve;t.commit("setCode",{authCode:e.params.code}),t.dispatch("slackAuthFinal").then(function(e){r("/settings")})}}]});qe.beforeEach(function(e,n,r){Ve.dispatch("checkLogin").then(function(){Ve.dispatch("loadCSRF").then(function(){r()})})});var Le=qe,Pe=r("Tqaz");t.default.config.productionTip=!1,t.default.use(Pe.a),new t.default({el:"#app",router:Le,store:Ve,components:{App:b},template:"<App/>"})},PRuX:function(e,n,r){var t=r("RB6l");"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);r("rjj0")("567ef8da",t,!1,{})},RB6l:function(e,n,r){(e.exports=r("FZ+f")(!0)).push([e.i,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","",{version:3,sources:[],names:[],mappings:"",file:"Settings.vue",sourceRoot:""}])},SnlE:function(e,n,r){(e.exports=r("FZ+f")(!0)).push([e.i,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","",{version:3,sources:[],names:[],mappings:"",file:"Header.vue",sourceRoot:""}])},XtP8:function(e,n,r){(e.exports=r("FZ+f")(!0)).push([e.i,"\nh1[data-v-75579faf], h2[data-v-75579faf] {\n  font-weight: normal;\n}\nul[data-v-75579faf] {\n  list-style-type: none;\n  padding: 0;\n}\nli[data-v-75579faf] {\n  display: inline-block;\n  margin: 0 10px;\n}\na[data-v-75579faf] {\n  color: #42b983;\n}\n","",{version:3,sources:["/Users/lauriermantel/startup/doxa/doxa-app/application/doxa-frontend/src/components/src/components/Maestro.vue"],names:[],mappings:";AA8BA;EACA,oBAAA;CACA;AACA;EACA,sBAAA;EACA,WAAA;CACA;AACA;EACA,sBAAA;EACA,eAAA;CACA;AACA;EACA,eAAA;CACA",file:"Maestro.vue",sourcesContent:['<template>\n<div>\n  <div v-if="maestro">\n    <h3>The maestro is <em>{{maestro.username}}</em></h3>\n    <input v-model="maestro.username" placeholder="e.g. Callum John Killian Mitchell">\n    <p>The maestro\'s email is <strong>{{maestro.email}}</strong></p>\n    <input v-model="maestro.email" placeholder="e.g. maestro@fulfilled.maestro">\n  </div>\n  <div v-else>\n    Loading...\n  </div>\n</div>\n</template>\n\n<script>\n  import { mapState } from \'vuex\'\n  export default {\n    computed: mapState({\n      maestro: function(state) {\n        return state.userData\n      },\n      currentUser: function(state) {\n        return state.currentUser\n      }\n    })\n  }\n<\/script>\n\n\x3c!-- Add "scoped" attribute to limit CSS to this component only --\x3e\n<style scoped>\nh1, h2 {\n  font-weight: normal;\n}\nul {\n  list-style-type: none;\n  padding: 0;\n}\nli {\n  display: inline-block;\n  margin: 0 10px;\n}\na {\n  color: #42b983;\n}\n</style>\n'],sourceRoot:""}])},XwcA:function(e,n){e.exports="data:image/png;base64,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"},"z/+d":function(e,n,r){(e.exports=r("FZ+f")(!0)).push([e.i,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n/*#app {\n  font-family: 'Avenir', Helvetica, Arial, sans-serif;\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;\n  text-align: center;\n  color: #2c3e50;\n  margin-top: 60px;\n}*/\n","",{version:3,sources:["/Users/lauriermantel/startup/doxa/doxa-app/application/doxa-frontend/src/src/App.vue"],names:[],mappings:";;;;;;;;;;;;;;;;;;;;;AAqBA;;;;;;;GAOA",file:"App.vue",sourcesContent:["<template>\n  <div id=\"app\">\n    <app-header></app-header>\n    <router-view/>\n  </div>\n</template>\n\n<script>\n  import Header from '@/components/Header';\n  import 'bootstrap/dist/css/bootstrap.css'\n  import 'bootstrap-vue/dist/bootstrap-vue.css'\n  export default {\n    name: 'App',\n    components: {\n      'app-header': Header\n    }\n  }\n<\/script>\n\n<style>\n\n/*#app {\n  font-family: 'Avenir', Helvetica, Arial, sans-serif;\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;\n  text-align: center;\n  color: #2c3e50;\n  margin-top: 60px;\n}*/\n</style>\n"],sourceRoot:""}])}},["NHnr"]);
//# sourceMappingURL=app.8d2a2ea6e0c869108dfa.js.map