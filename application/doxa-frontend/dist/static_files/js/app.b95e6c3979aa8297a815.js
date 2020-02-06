webpackJsonp([1],{"9M+g":function(t,e){},CSik:function(t,e,r){"use strict";var s=r("XwAu");r.n(s).a},Jmt5:function(t,e){},NHnr:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=r("7+uW"),n=[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container"},[e("div",{staticClass:"row"},[e("img",{staticClass:"logo",attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"70",height:"70"}})])])}],a=r("NYxO");var o={computed:Object(a.b)({isAuthenticated:function(t){return console.log(t),!!t.currentUser},currentUser:function(t){return t.currentUser}})},i=(r("yfgR"),r("K1/g")),c=Object(i.a)(o,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-navbar",{attrs:{toggleable:"lg"}},[r("div",[r("b-navbar-brand",{attrs:{to:"/"}})],1),t._v(" "),r("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),r("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[r("b-navbar-nav",{staticClass:"ml-auto"},[t.isAuthenticated?[r("b-nav-item-dropdown",{attrs:{text:t.currentUser.email,right:""}},[r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Dashboard")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Focus Plan")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/settings"}},[t._v("Settings")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/logout"}},[t._v("Logout")])],1)]:[r("b-nav-item",{attrs:{to:"/login"}},[t._v("Login")]),t._v(" "),r("b-nav-item",{attrs:{to:"/register-new-user"}},[t._v("Register")])]],2)],1)],1),t._v(" "),t._m(0)],1)},n,!1,null,null,null).exports,u=(r("fZSw"),Object(i.a)({},function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"right-sidebar"}},[r("h3",[t._v("Quotes")]),t._v(" "),r("div",{staticClass:"sidebar-section"},[r("p",{staticClass:"sidebar"},[t._v('"Less mental clutter means more mental resources available for deep thinking."')]),t._v(" "),r("h6",[t._v("-Cal Newport")])]),t._v(" "),r("h3",[t._v("Concepts")]),t._v(" "),r("div",[r("p",{staticClass:"sidebar"},[t._v('"Attention residue is when thoughts about a task persist and intrude while performing another task"')]),t._v(" "),r("h6",[t._v("-Sophie Leroy")])])])}],!1,null,null,null).exports),l=(r("Jmt5"),r("9M+g"),{name:"App",components:{"app-header":c,"right-sidebar":u},computed:Object(a.b)({currentUser:function(t){return t.currentUser},isAuthenticated:function(t){return t.currentUser?(console.log(!0),!0):(console.log(!1),!1)}})}),d=(r("CSik"),Object(i.a)(l,function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("app-header"),this._v(" "),e("div",{staticClass:"container"},[this.isAuthenticated?e("div",{staticClass:"row"},[e("div",{staticClass:"col-md-10"},[e("router-view")],1),this._v(" "),e("div",{staticClass:"col-md-2"},[e("right-sidebar")],1)]):e("div",[e("router-view")],1)])],1)},[],!1,null,null,null).exports),f=r("/ocq"),m={data:function(){return{}},computed:Object(a.b)({users:function(t){return t.users}})},p=(r("sMyi"),Object(i.a)(m,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t._m(0),t._v(" "),r("section",{staticClass:"section"},[r("div",{staticClass:"container"},t._l(t.users,function(e){return r("div",{key:e.id,staticClass:"card"},[r("div",{staticClass:"card-content"},[e?r("div",[r("p",{staticClass:"title"},[t._v("Name: "+t._s(e.username)+"; Email: "+t._s(e.email))]),t._v(" "),r("p",{staticClass:"detail"},[t._v("See this "),r("router-link",{attrs:{to:"maestro/"+e.id}},[t._v("maestro")])],1)]):t._e()])])}),0)])])},[function(){var t=this.$createElement,e=this._self._c||t;return e("section",{staticClass:"hero is-primary"},[e("div",{staticClass:"hero-body"},[e("div",{staticClass:"container"},[e("h2",{staticClass:"title"},[this._v("List of users")])])])])}],!1,null,"72c65623",null).exports),v={computed:Object(a.b)({maestro:function(t){return t.userData},currentUser:function(t){return t.currentUser}})},b=(r("wU87"),Object(i.a)(v,function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("h1",[t._v("h1 Welcome, Maestros.")]),t._v(" "),r("h2",[t._v("Let's connect your apps.")]),t._v(" "),r("h3",[t._v("h3 Use this for most section headers.")]),t._v(" "),r("h4",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("h5",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("p",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("a",[t._v("h1 Let's connect your apps.")])])}],!1,null,"4aa1b805",null).exports),h={computed:Object(a.b)({newUser:function(t){return t.newUser},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;this.$store.dispatch("registerNewUser").then(function(){t.formErrors||t.$router.push({name:"Login"})})}}},_=Object(i.a)(h,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Register for Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"realdonaldtrump",required:"",id:"input-1",type:"text"},model:{value:t.newUser.username,callback:function(e){t.$set(t.newUser,"username",e)},expression:"newUser.username"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:t.newUser.email,callback:function(e){t.$set(t.newUser,"email",e)},expression:"newUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.newUser.password,callback:function(e){t.$set(t.newUser,"password",e)},expression:"newUser.password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:t.newUser.confirm_password,callback:function(e){t.$set(t.newUser,"confirm_password",e)},expression:"newUser.confirm_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Register")])],1)],1)],1)},[],!1,null,null,null).exports,g={computed:Object(a.b)({loginUser:function(t){return t.loginUser},isLoggedIn:function(t){return t.isLoggedIn},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;return this.$store.dispatch("userLogin").then(function(){if(!t.formErrors){var e=t.$store.getters.currentUser;return t.$router.push({name:"Maestro",params:{id:e.id}},function(){})}})}}},w=Object(i.a)(g,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Log in to Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:t.loginUser.email,callback:function(e){t.$set(t.loginUser,"email",e)},expression:"loginUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.loginUser.password,callback:function(e){t.$set(t.loginUser,"password",e)},expression:"loginUser.password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Login")])],1)],1)],1)},[],!1,null,null,null).exports,U={computed:Object(a.b)({userData:function(t){return t.userData}})},C=Object(i.a)(U,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h2",[t._v("Settings")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your details")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-form",{on:{submit:function(t){}}},[r("b-form-group",{attrs:{label:"Email address","label-for":"input-1",description:"We'll never share your email with anyone else.",row:""}},[r("b-form-input",{attrs:{id:"input-1",value:"",type:"email",required:"",placeholder:"Your email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Username","label-for":"input-2",description:"Your Fulfilled.ai username",row:""}},[r("b-form-input",{attrs:{id:"input-2",value:"",type:"text",required:"",placeholder:"realdonaldtrump"}})],1),t._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[t._v("Change your password")])],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")])],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your integrations")])]),t._v(" "),r("b-col")],1),t._v(" "),t.userData.slack_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Slack has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/slack-install"}},[t._v("Reintegrate Slack")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Slack\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[t._v("Integrate Slack")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.google_calendar_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Google Calendar has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/build_google_calendar_auth_request"}},[t._v("Reintegrate Google Calendar")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Google Calendar\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/build_google_calendar_auth_request"}},[t._v("Integrate Google Calendar")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.github_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Github has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/github-auth"}},[t._v("Reintegrate Github")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Github\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-auth"}},[t._v("Integrate Github")])],1),t._v(" "),r("b-col")],1)],1)],1)},[],!1,null,null,null).exports,y={data:function(){return{}},computed:Object(a.b)({changePassword:function(t){return t.changePassword},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess}}),methods:{submitNewPassword:function(){var t=this;this.$store.dispatch("changePassword").then(function(){t.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},E=Object(i.a)(y,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Change your password")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),t.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[t._v("\n        Password changed successfully!\n      ")])],1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitNewPassword(e)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.changePassword.new_password,callback:function(e){t.$set(t.changePassword,"new_password",e)},expression:"changePassword.new_password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.changePassword.confirm_new_password,callback:function(e){t.$set(t.changePassword,"confirm_new_password",e)},expression:"changePassword.confirm_new_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Change password")])],1)],1)],1)},[],!1,null,null,null).exports,k=r("BO1k"),S=r.n(k),P=r("fZjL"),F=r.n(P),x=r("woOf"),L=r.n(x),$=r("mtWM"),R=r.n($);function O(){return R.a.get("/api/get_csrf")}var j=r("ppUw"),D=r.n(j);s.default.use(a.a),s.default.use(D.a);var q={email:null,password:null,csrf_token:null},A={username:null,email:null,password:null,confirm_password:null,csrf_token:null},M={new_password:null,confirm_new_password:null},N={users:[],userData:{},newUser:L()({},A),formErrors:null,loginUser:L()({},q),currentUser:null,CSRFToken:null,jwt:"",changePassword:L()({},M),changePasswordSuccess:!1,authCode:null,isLoggedIn:!1},T={loadUsers:function(t){return R.a.get("/api/users").then(function(e){return t.commit("setUsers",{users:e.data})})},loadUser:function(t,e){return R.a.get("/api/user_details").then(function(e){e.data||t.commit("setUserData",{userData:{error:!0}}),t.commit("setUserData",{userData:e.data})}).catch(function(t){console.log("Error loading user")})},loadCSRF:function(t){return O().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})})},registerNewUser:function(t){N.newUser.csrf_token=N.CSRFToken;var e;(e=N.newUser,R.a.post("/api/register",e)).then(function(e){return t.commit("clearNewUser",{}),t.commit("setErrors",{errors:null}),!0}).catch(function(e){O().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=G(e.response);return t.commit("setErrors",{errors:r}),!1})},userLogin:function(t){return N.loginUser.csrf_token=N.CSRFToken,(e=N.loginUser,R.a.post("/api/login",e)).then(function(e){return t.commit("setErrors",{errors:null}),t.commit("clearLoginUser",{}),t.commit("setCurrentUser",{currentUser:e.data})}).catch(function(e){O().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=G(e.response);return t.commit("setErrors",{errors:r})});var e},clearFormErrors:function(t){N.formErrors=null},checkLogin:function(t){return R.a.get("/api/check-login").then(function(e){return null==e.data?t.commit("clearCurrentUser",{}):t.commit("setCurrentUser",{currentUser:e.data})})},clearCredentials:function(t){return R.a.get("/api/logout").then(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e}).catch(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e})},changePassword:function(t){N.changePassword.csrf_token=N.CSRFToken;var e;(e=N.changePassword,N.currentUser,R.a.post("/api/change-password",e)).then(function(e){return O().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})}),t.commit("setErrors",{errors:null}),t.commit("setChangePassword",{changePasswordForm:L()({},M)}),t.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(e){O().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=G(e.response);return t.commit("setErrors",{errors:r}),t.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(t){t.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),t.commit("setChangePassword",{changePasswordForm:L()({},M)})}},I={setUsers:function(t,e){t.users=e.users},setUserData:function(t,e){console.log(e.userData),t.userData=e.userData},setCSRF:function(t,e){t.CSRFToken=e.CSRFToken},setErrors:function(t,e){t.formErrors=e.errors},setNewUser:function(t,e){t.newUser=e.newUser},setJWT:function(t,e){t.jwt=e.jwt},setCurrentUser:function(t,e){t.currentUser=e.currentUser},saveCurrentUser:function(t,e){$cookies.set("currentUser",e.currentUser)},clearLoginUser:function(t,e){t.loginUser=L()({},q)},clearNewUser:function(t,e){t.newUser=L()({},A)},setChangePassword:function(t,e){t.changePassword=e.changePasswordForm},setChangePasswordStatus:function(t,e){t.changePasswordSuccess=e.changePasswordSuccess},clearCurrentUser:function(t,e){t.currentUser=null}},Y={isLoggedIn:function(t){return null!=t.currentUser},isAuthenticated:function(t){return function(t){if(!t||t.split(".").length<3)return!1;var e=JSON.parse(atob(t.split(".")[1])),r=new Date(1e3*e.exp);return new Date<r}(t.jwt)},currentUser:function(t){return t.currentUser},userData:function(t){return t.userData}};function G(t){var e,r=null;if(t.data.errors){var s=t.data.errors;r=[];var n=!0,a=!1,o=void 0;try{for(var i,c=S()((e=s,F()(e)));!(n=(i=c.next()).done);n=!0){var u=i.value,l=!0,d=!1,f=void 0;try{for(var m,p=S()(s[u]);!(l=(m=p.next()).done);l=!0){var v=m.value;r=r.concat(v)}}catch(t){d=!0,f=t}finally{try{!l&&p.return&&p.return()}finally{if(d)throw f}}}}catch(t){a=!0,o=t}finally{try{!n&&c.return&&c.return()}finally{if(a)throw o}}}return r}var J=new a.a.Store({state:N,actions:T,mutations:I,getters:Y});s.default.use(f.a);var H=new f.a({routes:[{path:"/",name:"Home",component:p,beforeEnter:function(t,e,r){J.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:b,beforeEnter:function(t,e,r){var s=J.getters.isLoggedIn,n=J.getters.currentUser;s?n&&t.params.id===String(n.id)?J.dispatch("loadUser",n).then(function(){r()}):J.dispatch("loadUser",n).then(function(){r("/maestro/"+n.id)}):r("/login")}},{path:"/register-new-user",name:"Register",component:_,beforeEnter:function(t,e,r){J.getters.isLoggedIn||(J.dispatch("clearFormErrors"),r())}},{path:"/login",name:"Login",component:w,beforeEnter:function(t,e,r){(J.dispatch("clearFormErrors"),J.getters.isLoggedIn)?r("/maestro/"+J.getters.currentUser.id):r()}},{path:"/logout",name:"Logout",beforeEnter:function(t,e,r){return J.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:C,beforeEnter:function(t,e,r){J.dispatch("clearFormErrors");var s=J.getters.isLoggedIn,n=J.getters.currentUser;s?J.dispatch("loadUser",n).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:E,beforeEnter:function(t,e,r){J.dispatch("clearFormErrors"),function(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",s=e.getters.isLoggedIn;e.getters.currentUser;if(s)return t();t(r)}(r,J)}}]});H.beforeEach(function(t,e,r){J.dispatch("checkLogin").then(function(){J.dispatch("loadCSRF").then(function(){r()})})});var W=H,X=r("Tqaz");s.default.config.productionTip=!1,s.default.use(X.a),new s.default({el:"#app",router:W,store:J,components:{App:d},template:"<App/>"})},QOPB:function(t,e){},XwAu:function(t,e){},XwcA:function(t,e,r){t.exports=r.p+"static_files/img/logo_transparent.072b69b.png"},fZSw:function(t,e,r){"use strict";var s=r("yHqF");r.n(s).a},lK96:function(t,e){},"q+13":function(t,e){},sMyi:function(t,e,r){"use strict";var s=r("lK96");r.n(s).a},wU87:function(t,e,r){"use strict";var s=r("q+13");r.n(s).a},yHqF:function(t,e){},yfgR:function(t,e,r){"use strict";var s=r("QOPB");r.n(s).a}},["NHnr"]);
//# sourceMappingURL=app.b95e6c3979aa8297a815.js.map