webpackJsonp([1],{"0xDb":function(t,e,r){"use strict";e.a=function(t){if(!t||t.split(".").length<3)return!1;var e=JSON.parse(atob(t.split(".")[1])),r=new Date(1e3*e.exp);return new Date<r}},"3V6e":function(t,e){},"9M+g":function(t,e){},CSik:function(t,e,r){"use strict";var n=r("XwAu");r.n(n).a},Jmt5:function(t,e){},NHnr:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r("7+uW"),s=r("x8S4").a,a=(r("CSik"),r("K1/g")),o=Object(a.a)(s,function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("app-header"),this._v(" "),e("div",{staticClass:"container"},[this.isAuthenticated?e("div",{staticClass:"row"},[e("div",{staticClass:"col-md-10"},[e("router-view")],1),this._v(" "),e("div",{staticClass:"col-md-2"},[e("right-sidebar")],1)]):e("div",[e("router-view")],1)])],1)},[],!1,null,null,null).exports,i=r("/ocq"),c=r("NYxO"),u={data:function(){return{}},computed:Object(c.b)({users:function(t){return t.users}})},l=(r("j3OQ"),Object(a.a)(u,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t._m(0),t._v(" "),r("section",{staticClass:"section"},[r("div",{staticClass:"container"},t._l(t.users,function(e){return r("div",{key:e.id,staticClass:"card"},[r("div",{staticClass:"card-content"},[e?r("div",[r("p",{staticClass:"title"},[t._v("Name: "+t._s(e.username)+"; Email: "+t._s(e.email))]),t._v(" "),r("p",{staticClass:"detail"},[t._v("See this "),r("router-link",{attrs:{to:"maestro/"+e.id}},[t._v("maestro")])],1)]):t._e()])])}),0)])])},[function(){var t=this.$createElement,e=this._self._c||t;return e("section",{staticClass:"hero is-primary"},[e("div",{staticClass:"hero-body"},[e("div",{staticClass:"container"},[e("h2",{staticClass:"title"},[this._v("List of users")])])])])}],!1,null,"3470b972",null).exports),d={computed:Object(c.b)({maestro:function(t){return t.userData},currentUser:function(t){return t.currentUser}})},f=(r("eAji"),Object(a.a)(d,function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("h1",[t._v("h1 Welcome, Maestros.")]),t._v(" "),r("h2",[t._v("Let's connect your apps.")]),t._v(" "),r("h3",[t._v("h3 Use this for most section headers.")]),t._v(" "),r("h4",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("h5",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("p",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("a",[t._v("h1 Let's connect your apps.")])])}],!1,null,"fc54b8da",null).exports),m={computed:Object(c.b)({newUser:function(t){return t.newUser},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;this.$store.dispatch("registerNewUser").then(function(){t.formErrors||t.$router.push({name:"Login"})})}}},v=Object(a.a)(m,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Register for Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"realdonaldtrump",required:"",id:"input-1",type:"text"},model:{value:t.newUser.username,callback:function(e){t.$set(t.newUser,"username",e)},expression:"newUser.username"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:t.newUser.email,callback:function(e){t.$set(t.newUser,"email",e)},expression:"newUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.newUser.password,callback:function(e){t.$set(t.newUser,"password",e)},expression:"newUser.password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:t.newUser.confirm_password,callback:function(e){t.$set(t.newUser,"confirm_password",e)},expression:"newUser.confirm_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Register")])],1)],1)],1)},[],!1,null,null,null).exports,p={computed:Object(c.b)({loginUser:function(t){return t.loginUser},isLoggedIn:function(t){return t.isLoggedIn},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;return this.$store.dispatch("userLogin").then(function(){if(!t.formErrors){var e=t.$store.getters.currentUser;return t.$router.push({name:"Maestro",params:{id:e.id}},function(){})}})}}},h=Object(a.a)(p,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Log in to Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:t.loginUser.email,callback:function(e){t.$set(t.loginUser,"email",e)},expression:"loginUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.loginUser.password,callback:function(e){t.$set(t.loginUser,"password",e)},expression:"loginUser.password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Login")])],1)],1)],1)},[],!1,null,null,null).exports,b={computed:Object(c.b)({userData:function(t){return t.userData}})},_=Object(a.a)(b,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h2",[t._v("Settings")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your details")])]),t._v(" "),r("b-col")],1),t._v(" "),r("b-form",{on:{submit:function(t){}}},[r("b-form-group",{attrs:{label:"Email address","label-for":"input-1",description:"We'll never share your email with anyone else.",row:""}},[r("b-form-input",{attrs:{id:"input-1",value:"",type:"email",required:"",placeholder:"Your email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Username","label-for":"input-2",description:"Your Fulfilled.ai username",row:""}},[r("b-form-input",{attrs:{id:"input-2",value:"",type:"text",required:"",placeholder:"realdonaldtrump"}})],1),t._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[t._v("Change your password")])],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")])],1),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col"),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your integrations")])]),t._v(" "),r("b-col")],1),t._v(" "),t.userData.slack_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Slack has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/slack-install"}},[t._v("Reintegrate Slack")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Slack\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[t._v("Integrate Slack")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.google_calendar_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Google Calendar has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/build_google_calendar_auth_request"}},[t._v("Reintegrate Google Calendar")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Google Calendar\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/build_google_calendar_auth_request"}},[t._v("Integrate Google Calendar")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.github_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Github has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/github-auth"}},[t._v("Reintegrate Github")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n        You still need to integrate Github\n      ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-auth"}},[t._v("Integrate Github")])],1),t._v(" "),r("b-col")],1)],1)],1)},[],!1,null,null,null).exports,g={data:function(){return{}},computed:Object(c.b)({changePassword:function(t){return t.changePassword},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess}}),methods:{submitNewPassword:function(){var t=this;this.$store.dispatch("changePassword").then(function(){t.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},w=Object(a.a)(g,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Change your password")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),t.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[t._v("\n        Password changed successfully!\n      ")])],1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitNewPassword(e)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.changePassword.new_password,callback:function(e){t.$set(t.changePassword,"new_password",e)},expression:"changePassword.new_password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.changePassword.confirm_new_password,callback:function(e){t.$set(t.changePassword,"confirm_new_password",e)},expression:"changePassword.confirm_new_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Change password")])],1)],1)],1)},[],!1,null,null,null).exports,U=r("iINK"),C={methods:{percentFunc:function(t){return t+"%"}},components:{donut:U.DonutChart},props:{activity:{default:Array(),type:Array}},computed:{donutData:function(){var t=0,e=0,r=0,n=this.activity;n.forEach(function(n){n.is_collaborative?t+=1:n.is_focused?e+=1:n.is_refocusing?r+=1:console.log("Not categorized")});var s=[];return[{label:"Collaborative Time",value:(t/n.length*100).toFixed(2)},{label:"Independent Time",value:(e/n.length*100).toFixed(2)},{label:"Refocusing Time",value:(r/n.length*100).toFixed(2)}].forEach(function(t){0==t.value||isNaN(t.value)||s.push(t)}),s},graphColors:function(){var t={"Collaborative Time":'"#FF6384"',"Independent Time":'"#36A2EB"',"Refocusing Time":'"#FFFF11"'},e=[];return this.donutData.forEach(function(r){e.push(t[r.label])}),"["+e.join()+"]"}}},y=(r("RYMb"),{components:{pie:Object(a.a)(C,function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("h4",[this._v("Collaboration / Independent Time Score")]),this._v(" "),e("donut",{attrs:{id:"collaboration-pie",data:this.donutData,colors:this.graphColors,resize:"True",formatter:this.percentFunc}})],1)},[],!1,null,"531ea818",null).exports},computed:Object(c.b)({activityData:function(t){return t.activityData},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess}})}),E=Object(a.a)(y,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h1",[t._v("How you spend your time")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("div",[r("pie",{attrs:{activity:this.activityData}})],1)])],1)},[],!1,null,null,null).exports,k=r("BO1k"),S=r.n(k),F=r("fZjL"),x=r.n(F),P=r("woOf"),D=r.n(P),R=r("mtWM"),L=r.n(R);function j(){return L.a.get("/api/get_csrf")}var O=r("ppUw"),$=r.n(O),A=r("0xDb");n.default.use(c.a),n.default.use($.a);var T={email:null,password:null,csrf_token:null},N={username:null,email:null,password:null,confirm_password:null,csrf_token:null},q={new_password:null,confirm_new_password:null},I={users:[],userData:{},newUser:D()({},N),formErrors:null,loginUser:D()({},T),currentUser:null,CSRFToken:null,jwt:"",changePassword:D()({},q),changePasswordSuccess:!1,authCode:null,isLoggedIn:!1,activityData:[]},M={loadActivity:function(t,e){return(s={start_time:r,end_time:n},L.a.get("/api/activity-data",{params:s})).then(function(e){return t.commit("setActivityData",{time:e.data})});var r,n,s},loadUsers:function(t){return L.a.get("/api/users").then(function(e){return t.commit("setUsers",{users:e.data})})},loadUser:function(t,e){return L.a.get("/api/user_details").then(function(e){e.data||t.commit("setUserData",{userData:{error:!0}}),t.commit("setUserData",{userData:e.data})}).catch(function(t){console.log("Error loading user")})},loadCSRF:function(t){return j().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})})},registerNewUser:function(t){I.newUser.csrf_token=I.CSRFToken;var e;(e=I.newUser,L.a.post("/api/register",e)).then(function(e){return t.commit("clearNewUser",{}),t.commit("setErrors",{errors:null}),!0}).catch(function(e){j().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=H(e.response);return t.commit("setErrors",{errors:r}),!1})},userLogin:function(t){return I.loginUser.csrf_token=I.CSRFToken,(e=I.loginUser,L.a.post("/api/login",e)).then(function(e){return t.commit("setErrors",{errors:null}),t.commit("clearLoginUser",{}),t.commit("setCurrentUser",{currentUser:e.data})}).catch(function(e){j().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=H(e.response);return t.commit("setErrors",{errors:r})});var e},clearFormErrors:function(t){I.formErrors=null},checkLogin:function(t){return L.a.get("/api/check-login").then(function(e){return null==e.data?t.commit("clearCurrentUser",{}):t.commit("setCurrentUser",{currentUser:e.data})})},clearCredentials:function(t){return L.a.get("/api/logout").then(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e}).catch(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e})},changePassword:function(t){I.changePassword.csrf_token=I.CSRFToken;var e;(e=I.changePassword,I.currentUser,L.a.post("/api/change-password",e)).then(function(e){return j().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})}),t.commit("setErrors",{errors:null}),t.commit("setChangePassword",{changePasswordForm:D()({},q)}),t.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(e){j().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=H(e.response);return t.commit("setErrors",{errors:r}),t.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(t){t.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),t.commit("setChangePassword",{changePasswordForm:D()({},q)})}},Y={setUsers:function(t,e){t.users=e.users},setUserData:function(t,e){console.log(e.userData),t.userData=e.userData},setCSRF:function(t,e){t.CSRFToken=e.CSRFToken},setErrors:function(t,e){t.formErrors=e.errors},setNewUser:function(t,e){t.newUser=e.newUser},setJWT:function(t,e){t.jwt=e.jwt},setCurrentUser:function(t,e){t.currentUser=e.currentUser},saveCurrentUser:function(t,e){$cookies.set("currentUser",e.currentUser)},clearLoginUser:function(t,e){t.loginUser=D()({},T)},clearNewUser:function(t,e){t.newUser=D()({},N)},setChangePassword:function(t,e){t.changePassword=e.changePasswordForm},setChangePasswordStatus:function(t,e){t.changePasswordSuccess=e.changePasswordSuccess},clearCurrentUser:function(t,e){t.currentUser=null},setActivityData:function(t,e){t.activityData=e.time}},G={isLoggedIn:function(t){return null!=t.currentUser},isAuthenticated:function(t){return Object(A.a)(t.jwt)},currentUser:function(t){return t.currentUser},userData:function(t){return t.userData}};function H(t){var e,r=null;if(t.data.errors){var n=t.data.errors;r=[];var s=!0,a=!1,o=void 0;try{for(var i,c=S()((e=n,x()(e)));!(s=(i=c.next()).done);s=!0){var u=i.value,l=!0,d=!1,f=void 0;try{for(var m,v=S()(n[u]);!(l=(m=v.next()).done);l=!0){var p=m.value;r=r.concat(p)}}catch(t){d=!0,f=t}finally{try{!l&&v.return&&v.return()}finally{if(d)throw f}}}}catch(t){a=!0,o=t}finally{try{!s&&c.return&&c.return()}finally{if(a)throw o}}}return r}var J=new c.a.Store({state:I,actions:M,mutations:Y,getters:G});n.default.use(i.a);var Q=new i.a({routes:[{path:"/",name:"Home",component:l,beforeEnter:function(t,e,r){J.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:f,beforeEnter:function(t,e,r){var n=J.getters.isLoggedIn,s=J.getters.currentUser;n?s&&t.params.id===String(s.id)?J.dispatch("loadUser",s).then(function(){r()}):J.dispatch("loadUser",s).then(function(){r("/maestro/"+s.id)}):r("/login")}},{path:"/register-new-user",name:"Register",component:v,beforeEnter:function(t,e,r){J.getters.isLoggedIn||(J.dispatch("clearFormErrors"),r())}},{path:"/login",name:"Login",component:h,beforeEnter:function(t,e,r){(J.dispatch("clearFormErrors"),J.getters.isLoggedIn)?r("/maestro/"+J.getters.currentUser.id):r()}},{path:"/logout",name:"Logout",beforeEnter:function(t,e,r){return J.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:_,beforeEnter:function(t,e,r){J.dispatch("clearFormErrors");var n=J.getters.isLoggedIn,s=J.getters.currentUser;n?J.dispatch("loadUser",s).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:w,beforeEnter:function(t,e,r){J.dispatch("clearFormErrors"),W(r,J)}},{path:"/fulfilled-dashboard",name:"Fulfilled.ai - Focused Time",component:E,beforeEnter:function(t,e,r){var n=t.params.start_time,s=t.params.end_time;J.dispatch("clearFormErrors"),J.dispatch("loadActivity",n,s),W(r,J)}}]});function W(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",n=e.getters.isLoggedIn;e.getters.currentUser;return n?t():t(r)}Q.beforeEach(function(t,e,r){J.dispatch("checkLogin").then(function(){J.dispatch("loadCSRF").then(function(){r()})})});var Z=Q,B=r("Tqaz");n.default.config.productionTip=!1,n.default.use(B.a),new n.default({el:"#app",router:Z,store:J,components:{App:o},template:"<App/>"})},QOPB:function(t,e){},RYMb:function(t,e,r){"use strict";var n=r("3V6e");r.n(n).a},XwAu:function(t,e){},XwcA:function(t,e,r){t.exports=r.p+"static_files/img/logo_transparent.072b69b.png"},eAji:function(t,e,r){"use strict";var n=r("wlbq");r.n(n).a},fZSw:function(t,e,r){"use strict";var n=r("yHqF");r.n(n).a},j3OQ:function(t,e,r){"use strict";var n=r("sES5");r.n(n).a},lZ5c:function(t,e,r){"use strict";r("fZSw");var n=r("K1/g"),s=Object(n.a)({},function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"right-sidebar"}},[r("h3",[t._v("Quotes")]),t._v(" "),r("div",{staticClass:"sidebar-section"},[r("p",{staticClass:"sidebar"},[t._v('"Less mental clutter means more mental resources available for deep thinking."')]),t._v(" "),r("h6",[t._v("-Cal Newport")])]),t._v(" "),r("h3",[t._v("Concepts")]),t._v(" "),r("div",[r("p",{staticClass:"sidebar"},[t._v('"Attention residue is when thoughts about a task persist and intrude while performing another task"')]),t._v(" "),r("h6",[t._v("-Sophie Leroy")])])])}],!1,null,null,null);e.a=s.exports},sES5:function(t,e){},teIl:function(t,e,r){"use strict";var n=[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container"},[e("div",{staticClass:"row"},[e("img",{staticClass:"logo",attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"70",height:"70"}})])])}],s=r("NYxO"),a=(r("0xDb"),{computed:Object(s.b)({isAuthenticated:function(t){return console.log(t),!!t.currentUser},currentUser:function(t){return t.currentUser}})}),o=(r("yfgR"),r("K1/g")),i=Object(o.a)(a,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-navbar",{attrs:{toggleable:"lg"}},[r("div",[r("b-navbar-brand",{attrs:{to:"/"}})],1),t._v(" "),r("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),r("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[r("b-navbar-nav",{staticClass:"ml-auto"},[t.isAuthenticated?[r("b-nav-item-dropdown",{attrs:{text:t.currentUser.email,right:""}},[r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Dashboard")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/focus-plan"}},[t._v("Focus Plan")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/settings"}},[t._v("Settings")]),t._v(" "),r("b-dropdown-item",{attrs:{to:"/logout"}},[t._v("Logout")])],1)]:[r("b-nav-item",{attrs:{to:"/login"}},[t._v("Login")]),t._v(" "),r("b-nav-item",{attrs:{to:"/register-new-user"}},[t._v("Register")])]],2)],1)],1),t._v(" "),t._m(0)],1)},n,!1,null,null,null);e.a=i.exports},wlbq:function(t,e){},x8S4:function(t,e,r){"use strict";(function(t){var n=r("teIl"),s=r("lZ5c"),a=r("Jmt5"),o=(r.n(a),r("9M+g")),i=(r.n(o),r("0UmN")),c=r.n(i),u=r("NYxO");t.Raphael=c.a,e.a={name:"App",components:{"app-header":n.a,"right-sidebar":s.a},computed:Object(u.b)({currentUser:function(t){return t.currentUser},isAuthenticated:function(t){return t.currentUser?(console.log(!0),!0):(console.log(!1),!1)}})}}).call(e,r("DuR2"))},yHqF:function(t,e){},yfgR:function(t,e,r){"use strict";var n=r("QOPB");r.n(n).a}},["NHnr"]);
//# sourceMappingURL=app.7ff34b1f59f7f7329475.js.map