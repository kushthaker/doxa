webpackJsonp([1],{"9M+g":function(t,e){},CSik:function(t,e,r){"use strict";var n=r("XwAu");r.n(n).a},Jmt5:function(t,e){},NHnr:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r("7+uW"),s=[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container"},[e("div",{staticClass:"row"},[e("img",{staticClass:"logo",attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"70",height:"70"}})])])}],a=r("NYxO");function o(t){if(!t||t.split(".").length<3)return!1;var e=JSON.parse(atob(t.split(".")[1])),r=new Date(1e3*e.exp);return new Date<r}var i={computed:Object(a.b)({isAuthenticated:function(t){return o(t.jwt)},currentUser:function(t){return t.currentUser}})},c=(r("yfgR"),r("K1/g")),u=Object(c.a)(i,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-navbar",{attrs:{toggleable:"lg"}},[r("div",[r("b-navbar-brand",{attrs:{to:"/"}})],1),t._v(" "),r("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),r("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[r("b-navbar-nav",{staticClass:"ml-auto"},[t.isAuthenticated?[r("b-nav-item-dropdown",{attrs:{text:t.currentUser.email,right:""}},[r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Dashboard")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Focus Plan")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Settings")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/logout"}},[t._v("Logout")])],1)]:[r("b-nav-item",{attrs:{to:"/login"}},[t._v("Login")]),t._v(" "),r("b-nav-item",{attrs:{to:"/register-new-user"}},[t._v("Register")])]],2)],1)],1),t._v(" "),t._m(0)],1)},s,!1,null,null,null).exports,l=(r("fZSw"),Object(c.a)({},function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"right-sidebar"}},[r("h3",[t._v("Quotes")]),t._v(" "),r("div",{staticClass:"sidebar-section"},[r("p",{staticClass:"sidebar"},[t._v('"Less mental clutter means more mental resources available for deep thinking."')]),t._v(" "),r("h6",[t._v("-Cal Newport")])]),t._v(" "),r("h3",[t._v("Concepts")]),t._v(" "),r("div",[r("p",{staticClass:"sidebar"},[t._v('"Attention residue is when thoughts about a task persist and intrude while performing another task"')]),t._v(" "),r("h6",[t._v("-Sophie Leroy")])])])}],!1,null,null,null).exports),d=(r("Jmt5"),r("9M+g"),{name:"App",components:{"app-header":u,"right-sidebar":l},computed:Object(a.b)({currentUser:function(t){return t.currentUser}})}),f=(r("CSik"),Object(c.a)(d,function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("app-header"),this._v(" "),e("div",{staticClass:"container"},[this.isAuthenticated?e("div",{staticClass:"row"},[e("div",{staticClass:"col-md-10"},[e("router-view")],1),this._v(" "),e("div",{staticClass:"col-md-2"},[e("right-sidebar")],1)]):e("div",[e("router-view")],1)])],1)},[],!1,null,null,null).exports),m=r("/ocq"),h={data:function(){return{}},computed:Object(a.b)({users:function(t){return t.users}})},p=(r("sMyi"),Object(c.a)(h,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t._m(0),t._v(" "),r("section",{staticClass:"section"},[r("div",{staticClass:"container"},t._l(t.users,function(e){return r("div",{key:e.id,staticClass:"card"},[r("div",{staticClass:"card-content"},[e?r("div",[r("p",{staticClass:"title"},[t._v("Name: "+t._s(e.username)+"; Email: "+t._s(e.email))]),t._v(" "),r("p",{staticClass:"detail"},[t._v("See this "),r("router-link",{attrs:{to:"maestro/"+e.id}},[t._v("maestro")])],1)]):t._e()])])}),0)])])},[function(){var t=this.$createElement,e=this._self._c||t;return e("section",{staticClass:"hero is-primary"},[e("div",{staticClass:"hero-body"},[e("div",{staticClass:"container"},[e("h2",{staticClass:"title"},[this._v("List of users")])])])])}],!1,null,"72c65623",null).exports),v={computed:Object(a.b)({maestro:function(t){return t.userData},currentUser:function(t){return t.currentUser}})},b=(r("wU87"),Object(c.a)(v,function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("h1",[t._v("h1 Welcome, Maestros.")]),t._v(" "),r("h2",[t._v("Let's connect your apps.")]),t._v(" "),r("h3",[t._v("h3 Use this for most section headers.")]),t._v(" "),r("h4",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("h5",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("p",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("a",[t._v("h1 Let's connect your apps.")])])}],!1,null,"4aa1b805",null).exports),_={computed:Object(a.b)({newUser:function(t){return t.newUser},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;this.$store.dispatch("registerNewUser").then(function(){t.formErrors||t.$router.push({name:"Login"})})}}},g=Object(c.a)(_,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Register for Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"realdonaldtrump",required:"",id:"input-1",type:"text"},model:{value:t.newUser.username,callback:function(e){t.$set(t.newUser,"username",e)},expression:"newUser.username"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:t.newUser.email,callback:function(e){t.$set(t.newUser,"email",e)},expression:"newUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.newUser.password,callback:function(e){t.$set(t.newUser,"password",e)},expression:"newUser.password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:t.newUser.confirm_password,callback:function(e){t.$set(t.newUser,"confirm_password",e)},expression:"newUser.confirm_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Register")])],1)],1)],1)},[],!1,null,null,null).exports,w={computed:Object(a.b)({loginUser:function(t){return t.loginUser},isLoggedIn:function(t){return t.isLoggedIn},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;return this.$store.dispatch("userLogin").then(function(){if(!t.formErrors){var e=t.$store.getters.currentUser;return t.$router.push({name:"Maestro",params:{id:e.id}},function(){}),e}})}}},U=Object(c.a)(w,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Log in to Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:t.loginUser.email,callback:function(e){t.$set(t.loginUser,"email",e)},expression:"loginUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.loginUser.password,callback:function(e){t.$set(t.loginUser,"password",e)},expression:"loginUser.password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Login")])],1)],1)],1)},[],!1,null,null,null).exports,C={computed:Object(a.b)({userData:function(t){return t.userData}})},k=Object(c.a)(C,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h2",[t._v("Settings")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your details")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-form",{on:{submit:function(t){}}},[r("b-form-group",{attrs:{label:"Email address","label-for":"input-1",description:"We'll never share your email with anyone else.",row:""}},[r("b-form-input",{attrs:{id:"input-1",value:"",type:"email",required:"",placeholder:"Your email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Username","label-for":"input-2",description:"Your Fulfilled.ai username",row:""}},[r("b-form-input",{attrs:{id:"input-2",value:"",type:"text",required:"",placeholder:"realdonaldtrump"}})],1),t._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[t._v("Change your password")])],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")])],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your integrations")])]),t._v(" "),r("b-col")],1),t._v(" "),t.userData.slack_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Slack has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/slack-install"}},[t._v("Reintegrate Slack")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Slack\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[t._v("Integrate Slack")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.google_calendar_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Google Calendar has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/build_google_calendar_auth_request"}},[t._v("Reintegrate Google Calendar")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Google Calendar\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/build_google_calendar_auth_request"}},[t._v("Integrate Google Calendar")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.github_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Github has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/github-auth"}},[t._v("Reintegrate Github")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Github\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-auth"}},[t._v("Integrate Github")])],1),t._v(" "),r("b-col")],1)],1)],1)},[],!1,null,null,null).exports,E={data:function(){return{}},computed:Object(a.b)({changePassword:function(t){return t.changePassword},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess}}),methods:{submitNewPassword:function(){var t=this;this.$store.dispatch("changePassword").then(function(){t.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},y=Object(c.a)(E,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Change your password")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),t.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[t._v("\n        Password changed successfully!\n      ")])],1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitNewPassword(e)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.changePassword.new_password,callback:function(e){t.$set(t.changePassword,"new_password",e)},expression:"changePassword.new_password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.changePassword.confirm_new_password,callback:function(e){t.$set(t.changePassword,"confirm_new_password",e)},expression:"changePassword.confirm_new_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Change password")])],1)],1)],1)},[],!1,null,null,null).exports,S={beforeMount:function(){}},F=Object(c.a)(S,function(){var t=this.$createElement;return(this._self._c||t)("div")},[],!1,null,null,null).exports,P={beforeMount:function(){}},x=Object(c.a)(P,function(){var t=this.$createElement;return(this._self._c||t)("div")},[],!1,null,null,null).exports,A={beforeMount:function(){}},$=Object(c.a)(A,function(){var t=this.$createElement;return(this._self._c||t)("div")},[],!1,null,null,null).exports,R=r("BO1k"),j=r.n(R),D=r("fZjL"),O=r.n(D),L=r("woOf"),q=r.n(L),T=r("mtWM"),M=r.n(T);function N(){return M.a.get("/api/get_csrf")}function G(t){return{Authorization:"Bearer: "+t.token}}var Y=r("ppUw"),z=r.n(Y);n.default.use(a.a),n.default.use(z.a);var J={email:null,password:null,csrf_token:null},W={username:null,email:null,password:null,confirm_password:null,csrf_token:null},H={new_password:null,confirm_new_password:null},I={users:[],userData:{},newUser:q()({},W),formErrors:null,loginUser:q()({},J),currentUser:null,CSRFToken:null,jwt:"",changePassword:q()({},H),changePasswordSuccess:!1,authCode:null,githubAuthCode:null},B={loadUsers:function(t){return M.a.get("/api/users").then(function(e){return t.commit("setUsers",{users:e.data})})},loadUser:function(t,e){return(r=e,M.a.get("/api/user_details",{data:r,headers:G(r)})).then(function(e){e.data||t.commit("setUserData",{userData:{error:!0}}),t.commit("setUserData",{userData:e.data})}).catch(function(t){console.log("Error loading user")});var r},loadCSRF:function(t){return N().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})})},registerNewUser:function(t){I.newUser.csrf_token=I.CSRFToken;var e;(e=I.newUser,M.a.post("/api/register",e)).then(function(e){return t.commit("clearNewUser",{}),t.commit("setErrors",{errors:null}),!0}).catch(function(e){N().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);return t.commit("setErrors",{errors:r}),!1})},userLogin:function(t){var e;return I.loginUser.csrf_token=I.CSRFToken,(e=I.loginUser,M.a.post("/api/login",e)).then(function(e){return t.commit("setCurrentUser",{currentUser:e.data}),t.commit("saveCurrentUser",{currentUser:e.data}),t.commit("setErrors",{errors:null}),t.commit("clearLoginUser",{}),t.commit("setJWT",{jwt:e.data.token})}).catch(function(e){N().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);t.commit("setErrors",{errors:r})})},clearFormErrors:function(t){I.formErrors=null},checkLogin:function(t){var e=$cookies.get("currentUser");return t.commit("setCurrentUser",{currentUser:e})},clearCredentials:function(t){$cookies.set("currentUser",null),t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{})},changePassword:function(t){I.changePassword.csrf_token=I.CSRFToken;var e,r;(e=I.changePassword,r=I.currentUser,M.a.post("/api/change-password",e,{headers:G(r)})).then(function(e){return N().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})}),t.commit("setErrors",{errors:null}),t.commit("setChangePassword",{changePasswordForm:q()({},H)}),t.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(e){N().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);return t.commit("setErrors",{errors:r}),t.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(t){t.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),t.commit("setChangePassword",{changePasswordForm:q()({},H)})},slackAuthFinal:function(t){var e,r,n=I.currentUser,s={code:I.authCode};s.csrf_token=I.CSRFToken,(e=s,r=n,M.a.post("/api/finalize-slack-auth",e,{headers:G(r)})).then(function(e){return t.commit("setUserData",{userData:e.data}),e}).catch(function(t){return console.log(t),!1})},googleAuthFinal:function(t){var e=I.currentUser;(function(t,e){return M.a.post("/api/finalize-google-auth",t,{headers:G(e)})})({csrf_token:I.CSRFToken},e).then(function(e){t.commit("setUserData",{userData:e.data})}).catch(function(t){return console.log(t),!1})},githubAuthFinal:function(t){var e,r,n=I.currentUser,s={code:I.githubAuthCode};s.csrf_token=I.CSRFToken,(e=s,r=n,M.a.post("/api/finalize-github-auth",e,{headers:G(r)})).then(function(e){return t.commit("setUserData",{userData:e.data}),e}).catch(function(t){return console.log(t),!1})}},X={setUsers:function(t,e){t.users=e.users},setUserData:function(t,e){console.log(e.userData),t.userData=e.userData},setCSRF:function(t,e){t.CSRFToken=e.CSRFToken},setErrors:function(t,e){t.formErrors=e.errors},setNewUser:function(t,e){t.newUser=e.newUser},setJWT:function(t,e){t.jwt=e.jwt},setCurrentUser:function(t,e){t.currentUser=e.currentUser,e.currentUser?t.jwt=e.currentUser.token:t.jwt=""},saveCurrentUser:function(t,e){$cookies.set("currentUser",e.currentUser)},clearLoginUser:function(t,e){t.loginUser=q()({},J)},clearNewUser:function(t,e){t.newUser=q()({},W)},setChangePassword:function(t,e){t.changePassword=e.changePasswordForm},setChangePasswordStatus:function(t,e){t.changePasswordSuccess=e.changePasswordSuccess},setCode:function(t,e){t.authCode=e.authCode},setGithubAuth:function(t,e){t.githubAuthCode=e.githubAuthCode},clearCurrentUser:function(t,e){t.currentUser=null}},K={isAuthenticated:function(t){return o(t.jwt)},currentUser:function(t){return t.currentUser},userData:function(t){return t.userData}};function Q(t){var e,r=null;if(t.data.errors){var n=t.data.errors;r=[];var s=!0,a=!1,o=void 0;try{for(var i,c=j()((e=n,O()(e)));!(s=(i=c.next()).done);s=!0){var u=i.value,l=!0,d=!1,f=void 0;try{for(var m,h=j()(n[u]);!(l=(m=h.next()).done);l=!0){var p=m.value;r=r.concat(p)}}catch(t){d=!0,f=t}finally{try{!l&&h.return&&h.return()}finally{if(d)throw f}}}}catch(t){a=!0,o=t}finally{try{!s&&c.return&&c.return()}finally{if(a)throw o}}}return r}var Z=new a.a.Store({state:I,actions:B,mutations:X,getters:K});n.default.use(m.a);var V=new m.a({routes:[{path:"/",name:"Home",component:p,beforeEnter:function(t,e,r){Z.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:b,beforeEnter:function(t,e,r){var n=Z.getters.isAuthenticated,s=Z.getters.currentUser;n?s&&t.params.id===String(s.id)?Z.dispatch("loadUser",s).then(function(){r()}):Z.dispatch("loadUser",s).then(function(){r("/maestro/"+s.id)}):r("/login")}},{path:"/register-new-user",name:"Register",component:g,beforeEnter:function(t,e,r){Z.dispatch("clearFormErrors"),r()}},{path:"/login",name:"Login",component:U,beforeEnter:function(t,e,r){(Z.dispatch("clearFormErrors"),Z.getters.isAuthenticated)?r("/maestro/"+Z.getters.currentUser.id):r()}},{path:"/logout",name:"Logout",beforeEnter:function(t,e,r){Z.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:k,beforeEnter:function(t,e,r){Z.dispatch("clearFormErrors");var n=Z.getters.isAuthenticated,s=Z.getters.currentUser;n?Z.dispatch("loadUser",s).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:y,beforeEnter:function(t,e,r){Z.dispatch("clearFormErrors"),function(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",n=e.getters.isAuthenticated;e.getters.currentUser;if(n)return t();t(r)}(r,Z)}},{path:"/slack-auth/:code",name:"Fulfilled.ai Slack Authentication",component:F,beforeEnter:function(t,e,r){var n=Z;n.commit("setCode",{authCode:t.params.code}),n.dispatch("slackAuthFinal").then(function(t){r("/settings")})}},{path:"/google-auth",name:"Fulfilled.ai Google Calendar Authorization",component:x,beforeEnter:function(t,e,r){Z.dispatch("googleAuthFinal").then(function(t){r("/settings")})}},{path:"/github-auth/:code",name:"Fulfilled.ai Github Authorization",component:$,beforeEnter:function(t,e,r){var n=Z;n.commit("setGithubAuth",{githubAuthCode:t.params.code}),n.dispatch("githubAuthFinal").then(function(t){r("/settings")})}}]});V.beforeEach(function(t,e,r){Z.dispatch("checkLogin").then(function(){Z.dispatch("loadCSRF").then(function(){r()})})});var tt=V,et=r("Tqaz");n.default.config.productionTip=!1,n.default.use(et.a),new n.default({el:"#app",router:tt,store:Z,components:{App:f},template:"<App/>"})},QOPB:function(t,e){},XwAu:function(t,e){},XwcA:function(t,e,r){t.exports=r.p+"static_files/img/logo_transparent.072b69b.png"},fZSw:function(t,e,r){"use strict";var n=r("yHqF");r.n(n).a},lK96:function(t,e){},"q+13":function(t,e){},sMyi:function(t,e,r){"use strict";var n=r("lK96");r.n(n).a},wU87:function(t,e,r){"use strict";var n=r("q+13");r.n(n).a},yHqF:function(t,e){},yfgR:function(t,e,r){"use strict";var n=r("QOPB");r.n(n).a}},["NHnr"]);
//# sourceMappingURL=app.d6c917bf1bee4ff077b4.js.map