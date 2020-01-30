webpackJsonp([1],{"9M+g":function(e,t){},APwA:function(e,t){},Hp8c:function(e,t){},Jmt5:function(e,t){},NHnr:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=r("7+uW"),n=r("NYxO");function a(e){if(!e||e.split(".").length<3)return!1;var t=JSON.parse(atob(e.split(".")[1])),r=new Date(1e3*t.exp);return new Date<r}var o={computed:Object(n.b)({isAuthenticated:function(e){return a(e.jwt)},currentUser:function(e){return e.currentUser}})},i={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("b-navbar",{attrs:{toggleable:"lg",type:"dark",variant:"info"}},[s("div",[s("b-navbar-brand",{attrs:{to:"/"}},[s("img",{attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"120",height:"120"}})])],1),e._v(" "),s("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),e._v(" "),s("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[s("b-navbar-nav",{staticClass:"ml-auto"},[e.isAuthenticated?[s("b-nav-item",{attrs:{to:"/growth"}},[e._v("Your Growth")]),e._v(" "),s("b-nav-item-dropdown",{attrs:{text:e.currentUser.email,right:""}},[s("b-dropdown-item",{attrs:{to:"/focus-plan"}},[e._v("Focus Plan")]),e._v(" "),s("b-dropdown-item",{attrs:{to:"/settings"}},[e._v("Settings")]),e._v(" "),s("b-dropdown-item",{attrs:{to:"/logout"}},[e._v("Logout")])],1)]:[s("b-nav-item",{attrs:{to:"/login"}},[e._v("Login")]),e._v(" "),s("b-nav-item",{attrs:{to:"/register-new-user"}},[e._v("Register")]),e._v(" "),s("b-nav-item",{attrs:{to:"/learn-more"}},[e._v("Learn More")]),e._v(" "),s("b-nav-item",{attrs:{to:"/contact"}},[e._v("Contact")])]],2)],1)],1)],1)},staticRenderFns:[]};var A=r("VU/8")(o,i,!1,function(e){r("rE7x")},"data-v-2dc9923a",null).exports,u=(r("Jmt5"),r("9M+g"),{name:"App",components:{"app-header":A}}),c={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("app-header"),this._v(" "),t("router-view")],1)},staticRenderFns:[]};var l=r("VU/8")(u,c,!1,function(e){r("Tdhx")},null,null).exports,d=r("/ocq"),m={data:function(){return{}},computed:Object(n.b)({users:function(e){return e.users}})},f={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e._m(0),e._v(" "),r("section",{staticClass:"section"},[r("div",{staticClass:"container"},e._l(e.users,function(t){return r("div",{key:t.id,staticClass:"card"},[r("div",{staticClass:"card-content"},[t?r("div",[r("p",{staticClass:"title"},[e._v("Name: "+e._s(t.username)+"; Email: "+e._s(t.email))]),e._v(" "),r("p",{staticClass:"detail"},[e._v("See this "),r("router-link",{attrs:{to:"maestro/"+t.id}},[e._v("maestro")])],1)]):e._e()])])}),0)])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("section",{staticClass:"hero is-primary"},[t("div",{staticClass:"hero-body"},[t("div",{staticClass:"container has-text-centered"},[t("h2",{staticClass:"title"},[this._v("List of users")])])])])}]};var h=r("VU/8")(m,f,!1,function(e){r("chCs")},"data-v-7a4f2064",null).exports,p={computed:Object(n.b)({maestro:function(e){return e.userData},currentUser:function(e){return e.currentUser}})},v={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e.maestro?r("div",[r("h3",[e._v("The maestro is "),r("em",[e._v(e._s(e.maestro.username))])]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.username,expression:"maestro.username"}],attrs:{placeholder:"e.g. Callum John Killian Mitchell"},domProps:{value:e.maestro.username},on:{input:function(t){t.target.composing||e.$set(e.maestro,"username",t.target.value)}}}),e._v(" "),r("p",[e._v("The maestro's email is "),r("strong",[e._v(e._s(e.maestro.email))])]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.email,expression:"maestro.email"}],attrs:{placeholder:"e.g. maestro@fulfilled.maestro"},domProps:{value:e.maestro.email},on:{input:function(t){t.target.composing||e.$set(e.maestro,"email",t.target.value)}}})]):r("div",[e._v("\r\n    Loading...\r\n  ")])])},staticRenderFns:[]};var g=r("VU/8")(p,v,!1,function(e){r("Hp8c")},"data-v-129fb6f0",null).exports,b={computed:Object(n.b)({newUser:function(e){return e.newUser},formErrors:function(e){return e.formErrors}}),methods:{submitUser:function(){var e=this;this.$store.dispatch("registerNewUser").then(function(){e.formErrors||e.$router.push({name:"Login"})})}}},w={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("b-container",[r("h2",[e._v("Register for Fulfilled.ai")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(t){return r("b-alert",{key:t,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(t)+"\n      ")])}),1):e._e(),e._v(" "),r("b-form",{on:{submit:function(t){return t.preventDefault(),e.submitUser(t)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"realdonaldtrump",required:"",id:"input-1",type:"text"},model:{value:e.newUser.username,callback:function(t){e.$set(e.newUser,"username",t)},expression:"newUser.username"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:e.newUser.email,callback:function(t){e.$set(e.newUser,"email",t)},expression:"newUser.email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:e.newUser.password,callback:function(t){e.$set(e.newUser,"password",t)},expression:"newUser.password"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:e.newUser.confirm_password,callback:function(t){e.$set(e.newUser,"confirm_password",t)},expression:"newUser.confirm_password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Register")])],1)],1)],1)},staticRenderFns:[]},E=r("VU/8")(b,w,!1,null,null,null).exports,C={computed:Object(n.b)({loginUser:function(e){return e.loginUser},isLoggedIn:function(e){return e.isLoggedIn},formErrors:function(e){return e.formErrors}}),methods:{submitUser:function(){var e=this;return this.$store.dispatch("userLogin").then(function(){if(!e.formErrors){var t=e.$store.getters.currentUser;return e.$router.push({name:"Maestro",params:{id:t.id}},function(){}),t}})}}},U={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("b-container",[r("h2",[e._v("Log in to Fulfilled.ai")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(t){return r("b-alert",{key:t,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(t)+"\n      ")])}),1):e._e(),e._v(" "),r("b-form",{on:{submit:function(t){return t.preventDefault(),e.submitUser(t)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:e.loginUser.email,callback:function(t){e.$set(e.loginUser,"email",t)},expression:"loginUser.email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:e.loginUser.password,callback:function(t){e.$set(e.loginUser,"password",t)},expression:"loginUser.password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Login")])],1)],1)],1)},staticRenderFns:[]},D=r("VU/8")(C,U,!1,null,null,null).exports,F={computed:Object(n.b)({userData:function(e){return e.userData}})},_={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h2",[e._v("Settings")])]),e._v(" "),r("b-col")],1),e._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[e._v("Your details")])]),e._v(" "),r("b-col")],1),e._v(" "),r("b-form",{on:{submit:function(e){}}},[r("b-form-group",{attrs:{label:"Email address","label-for":"input-1",description:"We'll never share your email with anyone else.",row:""}},[r("b-form-input",{attrs:{id:"input-1",value:"",type:"email",required:"",placeholder:"Your email"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Username","label-for":"input-2",description:"Your Fulfilled.ai username",row:""}},[r("b-form-input",{attrs:{id:"input-2",value:"",type:"text",required:"",placeholder:"realdonaldtrump"}})],1),e._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[e._v("Change your password")])],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Submit")])],1),e._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),e._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[e._v("Your integrations")])]),e._v(" "),r("b-col")],1),e._v(" "),e.userData.slack_user_id?r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("Slack has been integrated")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/slack-install"}},[e._v("Reintegrate Slack")])],1),e._v(" "),r("b-col")],1):r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Slack\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[e._v("Integrate Slack")])],1),e._v(" "),r("b-col")],1),e._v(" "),r("hr",{staticClass:"my-4"}),e._v(" "),e.userData.google_calendar_user_id?r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("Google Calendar has been integrated")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/build_google_calendar_auth_request"}},[e._v("Reintegrate Google Calendar")])],1),e._v(" "),r("b-col")],1):r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Google Calendar\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/build_google_calendar_auth_request"}},[e._v("Integrate Google Calendar")])],1),e._v(" "),r("b-col")],1),e._v(" "),r("hr",{staticClass:"my-4"}),e._v(" "),e.userData.github_user_id?r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("Github has been integrated")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/github-auth"}},[e._v("Reintegrate Github!!!!!")])],1),e._v(" "),r("b-col")],1):r("b-row",[r("b-col"),e._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[e._v("\n        You still need to integrate Github\n      ")]),e._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-auth"}},[e._v("Integrate Github!!!!!!")])],1),e._v(" "),r("b-col")],1)],1)],1)},staticRenderFns:[]};var Y=r("VU/8")(F,_,!1,function(e){r("APwA")},null,null).exports,G={data:function(){return{}},computed:Object(n.b)({changePassword:function(e){return e.changePassword},formErrors:function(e){return e.formErrors},changePasswordSuccess:function(e){return e.changePasswordSuccess}}),methods:{submitNewPassword:function(){var e=this;this.$store.dispatch("changePassword").then(function(){e.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},V={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("b-container",[r("h2",[e._v("Change your password")]),e._v(" "),e.formErrors?r("div",{staticClass:"error-messages"},e._l(e.formErrors,function(t){return r("b-alert",{key:t,attrs:{show:"",variant:"warning"}},[e._v("\n        "+e._s(t)+"\n      ")])}),1):e._e(),e._v(" "),e.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[e._v("\n        Password changed successfully!\n      ")])],1):e._e(),e._v(" "),r("b-form",{on:{submit:function(t){return t.preventDefault(),e.submitNewPassword(t)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:e.changePassword.new_password,callback:function(t){e.$set(e.changePassword,"new_password",t)},expression:"changePassword.new_password"}})],1),e._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:e.changePassword.confirm_new_password,callback:function(t){e.$set(e.changePassword,"confirm_new_password",t)},expression:"changePassword.confirm_new_password"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Change password")])],1)],1)],1)},staticRenderFns:[]},q=r("VU/8")(G,V,!1,null,null,null).exports,x={render:function(){var e=this.$createElement;return(this._self._c||e)("div")},staticRenderFns:[]},L=r("VU/8")({beforeMount:function(){}},x,!1,null,null,null).exports,W={render:function(){var e=this.$createElement;return(this._self._c||e)("div")},staticRenderFns:[]},P=r("VU/8")({beforeMount:function(){}},W,!1,null,null,null).exports,k={render:function(){var e=this.$createElement;return(this._self._c||e)("div")},staticRenderFns:[]},O=r("VU/8")({beforeMount:function(){}},k,!1,null,null,null).exports,R=r("BO1k"),Q=r.n(R),y=r("fZjL"),K=r.n(y),z=r("woOf"),N=r.n(z),S=r("mtWM"),j=r.n(S);function X(){return j.a.get("/api/get_csrf")}function Z(e){return{Authorization:"Bearer: "+e.token}}var T=r("ppUw"),H=r.n(T);s.default.use(n.a),s.default.use(H.a);var I={email:null,password:null,csrf_token:null},J={username:null,email:null,password:null,confirm_password:null,csrf_token:null},M={new_password:null,confirm_new_password:null},B={users:[],userData:{},newUser:N()({},J),formErrors:null,loginUser:N()({},I),currentUser:null,CSRFToken:null,jwt:"",changePassword:N()({},M),changePasswordSuccess:!1,authCode:null,githubAuthCode:null,googleCalendarAuthDetails:{}},$={loadUsers:function(e){return j.a.get("/api/users").then(function(t){return e.commit("setUsers",{users:t.data})})},loadUser:function(e,t){return(r=t,j.a.get("/api/user_details",{data:r,headers:Z(r)})).then(function(t){t.data||e.commit("setUserData",{userData:{error:!0}}),e.commit("setUserData",{userData:t.data})}).catch(function(e){console.log("Error loading user")});var r},loadCSRF:function(e){return X().then(function(t){return e.commit("setCSRF",{CSRFToken:t.data.csrf_token})})},registerNewUser:function(e){B.newUser.csrf_token=B.CSRFToken;var t;(t=B.newUser,j.a.post("/api/register",t)).then(function(t){return e.commit("clearNewUser",{}),e.commit("setErrors",{errors:null}),!0}).catch(function(t){X().then(function(t){return e.commit("setCSRF",{CSRFToken:t.data.csrf_token})});var r=re(t.response);return e.commit("setErrors",{errors:r}),!1})},userLogin:function(e){var t;return B.loginUser.csrf_token=B.CSRFToken,(t=B.loginUser,j.a.post("/api/login",t)).then(function(t){return e.commit("setCurrentUser",{currentUser:t.data}),e.commit("saveCurrentUser",{currentUser:t.data}),e.commit("setErrors",{errors:null}),e.commit("clearLoginUser",{}),e.commit("setJWT",{jwt:t.data.token})}).catch(function(t){X().then(function(t){return e.commit("setCSRF",{CSRFToken:t.data.csrf_token})});var r=re(t.response);e.commit("setErrors",{errors:r})})},clearFormErrors:function(e){B.formErrors=null},checkLogin:function(e){var t=$cookies.get("currentUser");return e.commit("setCurrentUser",{currentUser:t})},clearCredentials:function(e){$cookies.set("currentUser",null),e.commit("setCurrentUser",{currentUser:null}),e.commit("clearLoginUser",{})},changePassword:function(e){B.changePassword.csrf_token=B.CSRFToken;var t,r;(t=B.changePassword,r=B.currentUser,j.a.post("/api/change-password",t,{headers:Z(r)})).then(function(t){return X().then(function(t){return e.commit("setCSRF",{CSRFToken:t.data.csrf_token})}),e.commit("setErrors",{errors:null}),e.commit("setChangePassword",{changePasswordForm:N()({},M)}),e.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(t){X().then(function(t){return e.commit("setCSRF",{CSRFToken:t.data.csrf_token})});var r=re(t.response);return e.commit("setErrors",{errors:r}),e.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(e){e.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),e.commit("setChangePassword",{changePasswordForm:N()({},M)})},slackAuthFinal:function(e){var t,r,s=B.currentUser,n={code:B.authCode};n.csrf_token=B.CSRFToken,(t=n,r=s,j.a.post("/api/finalize-slack-auth",t,{headers:Z(r)})).then(function(t){return e.commit("setUserData",{userData:t.data}),t}).catch(function(e){return console.log(e),!1})},googleAuthFinal:function(e){var t,r,s=B.currentUser,n=B.googleCalendarAuthDetails;n.csrf_token=B.CSRFToken,(t=n,r=s,j.a.post("/api/finalize-google-auth",t,{headers:Z(r)})).then(function(t){e.commit("setUserData",{userData:t.data})}).catch(function(e){return console.log(e),!1})},githubAuthFinal:function(e){var t,r,s=B.currentUser,n={code:B.githubAuthCode};n.csrf_token=B.CSRFToken,(t=n,r=s,j.a.post("/api/finalize-github-auth",t,{headers:Z(r)})).then(function(t){return e.commit("setUserData",{userData:t.data}),t}).catch(function(e){return console.log(e),!1})}},ee={setUsers:function(e,t){e.users=t.users},setUserData:function(e,t){console.log(t.userData),e.userData=t.userData},setCSRF:function(e,t){e.CSRFToken=t.CSRFToken},setErrors:function(e,t){e.formErrors=t.errors},setNewUser:function(e,t){e.newUser=t.newUser},setJWT:function(e,t){e.jwt=t.jwt},setCurrentUser:function(e,t){e.currentUser=t.currentUser,t.currentUser?e.jwt=t.currentUser.token:e.jwt=""},saveCurrentUser:function(e,t){$cookies.set("currentUser",t.currentUser)},clearLoginUser:function(e,t){e.loginUser=N()({},I)},clearNewUser:function(e,t){e.newUser=N()({},J)},setChangePassword:function(e,t){e.changePassword=t.changePasswordForm},setChangePasswordStatus:function(e,t){e.changePasswordSuccess=t.changePasswordSuccess},setCode:function(e,t){e.authCode=t.authCode},setGithubAuth:function(e,t){e.githubAuthCode=t.githubAuthCode},setGoogleCalendarAuth:function(e,t){e.googleCalendarAuthDetails=t.params}},te={isAuthenticated:function(e){return a(e.jwt)},currentUser:function(e){return e.currentUser},userData:function(e){return e.userData}};function re(e){var t,r=null;if(e.data.errors){var s=e.data.errors;r=[];var n=!0,a=!1,o=void 0;try{for(var i,A=Q()((t=s,K()(t)));!(n=(i=A.next()).done);n=!0){var u=i.value,c=!0,l=!1,d=void 0;try{for(var m,f=Q()(s[u]);!(c=(m=f.next()).done);c=!0){var h=m.value;r=r.concat(h)}}catch(e){l=!0,d=e}finally{try{!c&&f.return&&f.return()}finally{if(l)throw d}}}}catch(e){a=!0,o=e}finally{try{!n&&A.return&&A.return()}finally{if(a)throw o}}}return r}var se=new n.a.Store({state:B,actions:$,mutations:ee,getters:te});s.default.use(d.a);var ne=new d.a({routes:[{path:"/",name:"Home",component:h,beforeEnter:function(e,t,r){se.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:g,beforeEnter:function(e,t,r){var s=se.getters.isAuthenticated,n=se.getters.currentUser;s?n&&e.params.id===String(n.id)?se.dispatch("loadUser",n).then(function(){r()}):se.dispatch("loadUser",n).then(function(){r("/maestro/"+n.id)}):r("/login")}},{path:"/register-new-user",name:"Register",component:E,beforeEnter:function(e,t,r){se.dispatch("clearFormErrors"),r()}},{path:"/login",name:"Login",component:D,beforeEnter:function(e,t,r){(se.dispatch("clearFormErrors"),se.getters.isAuthenticated)?r("/maestro/"+se.getters.currentUser.id):r()}},{path:"/logout",name:"Logout",beforeEnter:function(e,t,r){se.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:Y,beforeEnter:function(e,t,r){se.dispatch("clearFormErrors");var s=se.getters.isAuthenticated,n=se.getters.currentUser;s?se.dispatch("loadUser",n).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:q,beforeEnter:function(e,t,r){se.dispatch("clearFormErrors"),function(e,t){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",s=t.getters.isAuthenticated;t.getters.currentUser;if(s)return e();e(r)}(r,se)}},{path:"/slack-auth/:code",name:"Fulfilled.ai Slack Authentication",component:L,beforeEnter:function(e,t,r){var s=se;s.commit("setCode",{authCode:e.params.code}),s.dispatch("slackAuthFinal").then(function(e){r("/settings")})}},{path:"/google-auth",name:"Fulfilled.ai Google Calendar Authorization",component:P,beforeEnter:function(e,t,r){var s=se,n=e.query;"None"===n.refresh_token&&(n.refresh_token=null),s.commit("setGoogleCalendarAuth",{params:n}),s.dispatch("googleAuthFinal").then(function(e){r("/settings")})}},{path:"/github-auth/:code",name:"Fulfilled.ai Github Authorization",component:O,beforeEnter:function(e,t,r){var s=se;s.commit("setGithubAuth",{githubAuthCode:e.params.code}),s.dispatch("githubAuthFinal").then(function(e){r("/settings")})}}]});ne.beforeEach(function(e,t,r){se.dispatch("checkLogin").then(function(){se.dispatch("loadCSRF").then(function(){r()})})});var ae=ne,oe=r("Tqaz");s.default.config.productionTip=!1,s.default.use(oe.a),new s.default({el:"#app",router:ae,store:se,components:{App:l},template:"<App/>"})},Tdhx:function(e,t){},XwcA:function(e,t){e.exports="data:image/png;base64,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"},chCs:function(e,t){},rE7x:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.06332f08c1795ff00290.js.map