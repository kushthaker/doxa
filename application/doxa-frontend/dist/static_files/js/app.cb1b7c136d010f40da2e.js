webpackJsonp([1],{NHnr:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0});var s=t("7+uW"),n={render:function(){var e=this.$createElement,r=this._self._c||e;return r("div",{attrs:{id:"app"}},[r("router-view")],1)},staticRenderFns:[]};var o=t("VU/8")({name:"App"},n,!1,function(e){t("gsu9")},null,null).exports,a=t("/ocq"),i=t("NYxO"),u={data:function(){return{}},computed:Object(i.b)({users:function(e){return e.users}}),beforeMount:function(){this.$store.dispatch("loadUsers")}},l={render:function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",[e._m(0),e._v(" "),t("section",{staticClass:"section"},[t("div",{staticClass:"container"},e._l(e.users,function(r){return t("div",{key:r.id,staticClass:"card"},[t("div",{staticClass:"card-content"},[r?t("div",[t("p",{staticClass:"title"},[e._v("Name: "+e._s(r.username)+"; Email: "+e._s(r.email))]),e._v(" "),t("p",{staticClass:"detail"},[e._v("See this "),t("router-link",{attrs:{to:"maestro/"+r.id}},[e._v("maestro")])],1)]):e._e()])])}),0)])])},staticRenderFns:[function(){var e=this.$createElement,r=this._self._c||e;return r("section",{staticClass:"hero is-primary"},[r("div",{staticClass:"hero-body"},[r("div",{staticClass:"container has-text-centered"},[r("h2",{staticClass:"title"},[this._v("List of users")])])])])}]};var c=t("VU/8")(u,l,!1,function(e){t("h++/")},"data-v-52794a2f",null).exports,m={computed:Object(i.b)({maestro:function(e){return e.userData}}),beforeMount:function(){var e=parseInt(this.$route.params.id);this.$store.dispatch("loadUser",e)}},d={render:function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",[e.maestro?t("div",[t("h3",[e._v("The maestro is "),t("em",[e._v(e._s(e.maestro.username))])]),e._v(" "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.username,expression:"maestro.username"}],attrs:{placeholder:"e.g. Callum John Killian Mitchell"},domProps:{value:e.maestro.username},on:{input:function(r){r.target.composing||e.$set(e.maestro,"username",r.target.value)}}}),e._v(" "),t("p",[e._v("The maestro's email is "),t("strong",[e._v(e._s(e.maestro.email))])]),e._v(" "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.maestro.email,expression:"maestro.email"}],attrs:{placeholder:"e.g. maestro@fulfilled.maestro"},domProps:{value:e.maestro.email},on:{input:function(r){r.target.composing||e.$set(e.maestro,"email",r.target.value)}}})]):t("div",[e._v("\n    No user found.\n  ")])])},staticRenderFns:[]};var p=t("VU/8")(m,d,!1,function(e){t("oUWl")},"data-v-2bb9ef09",null).exports,f={computed:Object(i.b)({newUser:function(e){return e.newUser},formErrors:function(e){return e.formErrors}}),methods:{submitUser:function(){var e=this;this.$store.dispatch("registerNewUser").then(function(){e.formErrors||e.$router.push({name:"Home"})})}},beforeMount:function(){this.$store.dispatch("loadCSRF")}},v={render:function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",[e.formErrors?t("ul",{staticClass:"error-messages"},e._l(e.formErrors,function(r){return t("li",[e._v("\n      "+e._s(r)+"\n    ")])}),0):e._e(),e._v(" "),t("form",{on:{submit:function(r){return r.preventDefault(),e.submitUser(r)}}},[t("p",[e._v("Username: "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.newUser.username,expression:"newUser.username"}],attrs:{placeholder:"realdonaldtrump"},domProps:{value:e.newUser.username},on:{input:function(r){r.target.composing||e.$set(e.newUser,"username",r.target.value)}}})]),e._v(" "),t("p",[e._v("Email address: "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.newUser.email,expression:"newUser.email"}],attrs:{placeholder:"maestro@fulfilled.ai"},domProps:{value:e.newUser.email},on:{input:function(r){r.target.composing||e.$set(e.newUser,"email",r.target.value)}}})]),e._v(" "),t("p",[e._v("Password: "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.newUser.password,expression:"newUser.password"}],attrs:{required:"",type:"password"},domProps:{value:e.newUser.password},on:{input:function(r){r.target.composing||e.$set(e.newUser,"password",r.target.value)}}})]),e._v(" "),t("p",[e._v("Confirm password: "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.newUser.confirm_password,expression:"newUser.confirm_password"}],attrs:{required:"",type:"password"},domProps:{value:e.newUser.confirm_password},on:{input:function(r){r.target.composing||e.$set(e.newUser,"confirm_password",r.target.value)}}})]),e._v(" "),t("button",[e._v("Register")])])])},staticRenderFns:[]},h=t("VU/8")(f,v,!1,null,null,null).exports,U={computed:Object(i.b)({loginUser:function(e){return e.loginUser},currentUser:function(e){return e.currentUser}}),methods:{submitUser:function(){var e=this;this.$store.dispatch("userLogin").then(function(){e.formErrors||e.$router.push({name:"Home"})})}},beforeMount:function(){this.$store.dispatch("loadCSRF"),this.$store.dispatch("loadCookie"),null===this.currentUser&&this.$store.dispatch("setCurrentUser")}},w={render:function(){var e=this,r=e.$createElement,t=e._self._c||r;return t("div",[t("form",{on:{submit:function(r){return r.preventDefault(),e.submitUser(r)}}},[t("input",{directives:[{name:"model",rawName:"v-model",value:e.loginUser.email,expression:"loginUser.email"}],attrs:{placeholder:"Your email address",required:""},domProps:{value:e.loginUser.email},on:{input:function(r){r.target.composing||e.$set(e.loginUser,"email",r.target.value)}}}),e._v(" "),t("input",{directives:[{name:"model",rawName:"v-model",value:e.loginUser.password,expression:"loginUser.password"}],attrs:{placeholder:"Password",required:"",type:"password"},domProps:{value:e.loginUser.password},on:{input:function(r){r.target.composing||e.$set(e.loginUser,"password",r.target.value)}}}),e._v(" "),t("button",[e._v("Login")])])])},staticRenderFns:[]},_=t("VU/8")(U,w,!1,null,null,null).exports;s.a.use(a.a);var g=new a.a({routes:[{path:"/",name:"Home",component:c},{path:"/maestro/:id",name:"Maestro",component:p},{path:"/register-new-user",name:"Register",component:h},{path:"/login",name:"Login",component:_}]}),C=t("fZjL"),$=t.n(C),b=t("BO1k"),k=t.n(b),R=t("mtWM"),E=t.n(R);function F(){return E.a.get("/api/get_csrf")}var x=t("ppUw"),N=t.n(x);s.a.use(i.a),s.a.use(N.a);var y={users:[],userData:null,newUser:{username:null,email:null,password:null,confirm_password:null,csrf_token:null},formErrors:null,loginUser:{email:null,password:null,csrf_token:null},currentUser:null,CSRFToken:null,session:null},S={loadUsers:function(e){return E.a.get("/api/users").then(function(r){return e.commit("setUsers",{users:r.data})})},loadUser:function(e,r){return(t=r,E.a.get("/api/users/"+t).then(function(e){return e}).catch(function(e){if(404==e.response.status)return{data:null}})).then(function(r){e.commit("setUserData",{userData:r.data})});var t},loadCookie:function(e){console.log($cookies.keys())},loadCSRF:function(e){return F().then(function(r){return e.commit("setCSRF",{CSRFToken:r.data.csrf_token})})},registerNewUser:function(e){var r;return y.newUser.csrf_token=y.CSRFToken,(r=y.newUser,E.a.post("/register",r)).then(function(r){var t,s=null,n=r.data;if(n.errors){s=[];var o=!0,a=!1,i=void 0;try{for(var u,l=k()((t=n.errors,$()(t)));!(o=(u=l.next()).done);o=!0){var c=u.value,m=!0,d=!1,p=void 0;try{for(var f,v=k()(n.errors[c]);!(m=(f=v.next()).done);m=!0){var h=f.value;s=s.concat(h)}}catch(e){d=!0,p=e}finally{try{!m&&v.return&&v.return()}finally{if(d)throw p}}}}catch(e){a=!0,i=e}finally{try{!o&&l.return&&l.return()}finally{if(a)throw i}}}F().then(function(r){return e.commit("setCSRF",{CSRFToken:r.data.csrf_token})}),e.commit("setErrors",{errors:s}),e.commit("setNewUser",{newUser:n})})},setCurrentUser:function(e){},userLogin:function(e){var r;return y.loginUser.csrf_token=y.CSRFToken,(r=y.loginUser,E.a.post("/login",r,{withCredentials:!0})).then(function(e){console.log(e)})}};var P=new i.a.Store({state:y,actions:S,mutations:{setUsers:function(e,r){e.users=r.users},setUserData:function(e,r){e.userData=r.userData},setCSRF:function(e,r){e.CSRFToken=r.CSRFToken},setErrors:function(e,r){e.formErrors=r.errors},setNewUser:function(e,r){e.newUser=r.newUser}},getters:{}});s.a.config.productionTip=!1,new s.a({el:"#app",router:g,store:P,components:{App:o},template:"<App/>"})},gsu9:function(e,r){},"h++/":function(e,r){},oUWl:function(e,r){}},["NHnr"]);
//# sourceMappingURL=app.cb1b7c136d010f40da2e.js.map