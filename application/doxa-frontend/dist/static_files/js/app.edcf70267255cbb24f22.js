webpackJsonp([1],{"0xDb":function(t,e,r){"use strict";e.a=function(t){if(!t||t.split(".").length<3)return!1;var e=JSON.parse(atob(t.split(".")[1])),r=new Date(1e3*e.exp);return new Date<r}},"2w/H":function(t,e,r){"use strict";var a=r("yavf");r.n(a).a},"6mK1":function(t,e,r){"use strict";var a=r("ifoh");r.n(a).a},"9M+g":function(t,e){},Bmzg:function(t,e,r){t.exports=r.p+"static_files/img/cal.af27f87.png"},CSik:function(t,e,r){"use strict";var a=r("XwAu");r.n(a).a},Jmt5:function(t,e){},KIop:function(t,e){},M3wb:function(t,e,r){t.exports=r.p+"static_files/img/tips.9c8e92d.png"},NHnr:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=r("7+uW"),n=r("x8S4").a,s=(r("CSik"),r("K1/g")),o=Object(s.a)(n,function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("div",{staticClass:"container"},[e("app-header")],1),this._v(" "),e("div",{staticClass:"container"},[this.isAuthenticated?e("div",{staticClass:"row"},[e("div",{staticClass:"col-md-10"},[e("router-view")],1),this._v(" "),e("div",{staticClass:"col-md-2"},[e("right-sidebar")],1)]):e("div",[e("router-view")],1)])])},[],!1,null,null,null).exports,i=r("/ocq"),c=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("section",{staticClass:"hero is-primary"},[a("div",{staticClass:"container"},[a("div",{staticClass:"row hero-section"},[a("div",[a("h1",[t._v("Find focus at work with Fulfilled.")]),t._v(" "),a("h4",[t._v("Developers use Fulfilled to focus on their craft, collaborate smarter, and disconnect after work.")]),t._v(" "),a("button",{staticClass:"btn btn-dark",attrs:{onclick:"window.location.href = 'https://fulfilled.ai/#/register-new-user';"}},[t._v("Try it free")])])]),t._v(" "),a("div",{staticClass:"row hero-section"},[a("div",{staticClass:"col-md-6 my-auto"},[a("h3",[t._v("Book time to work deeply everyday")])]),t._v(" "),a("div",{staticClass:"col-md-6"},[a("img",{staticClass:"trends",attrs:{src:r("Bmzg"),alt:"Fulfilled.ai"}})])]),t._v(" "),a("div",{staticClass:"row hero-section"},[a("div",{staticClass:"col-md-6 order-sm-12 my-auto"},[a("h3",[t._v("Reflect on your work patterns")])]),t._v(" "),a("div",{staticClass:"col-md-6 order-sm-1"},[a("img",{staticClass:"trends",attrs:{src:r("nm9u"),alt:"Fulfilled.ai"}})])]),t._v(" "),a("div",{staticClass:"row hero-section"},[a("div",{staticClass:"col-md-6 my-auto"},[a("h3",[t._v("Get tips to focus better and disconnect after work")])]),t._v(" "),a("div",{staticClass:"col-md-6"},[a("img",{staticClass:"trends",attrs:{src:r("M3wb"),alt:"Fulfilled.ai"}})])])])])])}],u=r("NYxO"),l={data:function(){return{}},computed:Object(u.b)({users:function(t){return t.users}})},v=(r("6mK1"),Object(s.a)(l,function(){this.$createElement;this._self._c;return this._m(0)},c,!1,null,"0cbe357c",null).exports),d={computed:Object(u.b)({maestro:function(t){return t.userData},currentUser:function(t){return t.currentUser}})},f=(r("eAji"),Object(s.a)(d,function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("h1",[t._v("h1 Welcome, Maestros.")]),t._v(" "),r("h2",[t._v("Let's connect your apps.")]),t._v(" "),r("h3",[t._v("h3 Use this for most section headers.")]),t._v(" "),r("h4",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("h5",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("p",[t._v("h1 Let's connect your apps.")]),t._v(" "),r("a",[t._v("h1 Let's connect your apps.")])])}],!1,null,"fc54b8da",null).exports),m={computed:Object(u.b)({newUser:function(t){return t.newUser},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;this.$store.dispatch("registerNewUser").then(function(){t.formErrors||t.$router.push({name:"Login"})})}}},_=Object(s.a)(m,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Register for Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Username","label-for":"input-1",description:"Just the username you use in Fulfilled.ai"}},[r("b-form-input",{attrs:{placeholder:"Feridan_UW_Hamdallahpur",required:"",id:"input-1",type:"text"},model:{value:t.newUser.username,callback:function(e){t.$set(t.newUser,"username",e)},expression:"newUser.username"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Email Address","label-for":"input-email-register",description:"Your work email address."}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-email-register",type:"email"},model:{value:t.newUser.email,callback:function(e){t.$set(t.newUser,"email",e)},expression:"newUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-3",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.newUser.password,callback:function(e){t.$set(t.newUser,"password",e)},expression:"newUser.password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm password","label-for":"input-4",description:"Must be the same as your password above"}},[r("b-form-input",{attrs:{required:"",id:"input-4",type:"password"},model:{value:t.newUser.confirm_password,callback:function(e){t.$set(t.newUser,"confirm_password",e)},expression:"newUser.confirm_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Register")])],1)],1)],1)},[],!1,null,null,null).exports,p={computed:Object(u.b)({loginUser:function(t){return t.loginUser},isLoggedIn:function(t){return t.isLoggedIn},formErrors:function(t){return t.formErrors}}),methods:{submitUser:function(){var t=this;return this.$store.dispatch("userLogin").then(function(){if(!t.formErrors)return t.$router.push({name:"Dashboard"},function(){})})}}},h=Object(s.a)(p,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Log in to Fulfilled.ai")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitUser(e)}}},[r("b-form-group",{attrs:{label:"Email","label-for":"input-1"}},[r("b-form-input",{attrs:{placeholder:"maestro@fulfilled.ai",required:"",id:"input-1",type:"text"},model:{value:t.loginUser.email,callback:function(e){t.$set(t.loginUser,"email",e)},expression:"loginUser.email"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Password","label-for":"input-2"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.loginUser.password,callback:function(e){t.$set(t.loginUser,"password",e)},expression:"loginUser.password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Login")])],1)],1)],1)},[],!1,null,null,null).exports,b=r("B2B0"),g=r.n(b),w={data:function(){return{workdayStart:{type:Object,default:function(){return{HH:"9",mm:"30"}}},workdayEnd:{type:Object,default:function(){return{HH:"5",mm:"30"}}}}},computed:Object(u.b)({userData:function(t){return t.userData}}),components:{VueTimepicker:g.a}},y=(r("yBiD"),Object(s.a)(w,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("b-row",{staticClass:"text-center"},[r("b-col",{attrs:{cols:"1"}}),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h1",[t._v("Settings")])]),t._v(" "),r("b-col",{attrs:{cols:"1"}})],1),t._v(" "),r("b-row",[r("br")]),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col",{attrs:{cols:"1"}}),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Update your details")])]),t._v(" "),r("b-col",{attrs:{cols:"1"}})],1),t._v(" "),r("b-form",{on:{submit:function(t){}}},[r("b-form-group",{attrs:{label:"Workday Start","label-for":"input-2",description:"Usual time that your workday starts (e.g. 9:30am)",row:""}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}},[r("option",{attrs:{disabled:"",value:""}},[t._v("Please select one")]),t._v(" "),r("option",[t._v("6:00 am")]),t._v(" "),r("option",[t._v("6:30 am")]),t._v(" "),r("option",[t._v("7:00 am")]),t._v(" "),r("option",[t._v("7:30 am")]),t._v(" "),r("option",[t._v("8:00 am")]),t._v(" "),r("option",[t._v("8:30 am")]),t._v(" "),r("option",[t._v("9:00 am")]),t._v(" "),r("option",[t._v("9:30 am")]),t._v(" "),r("option",[t._v("10:00 am")]),t._v(" "),r("option",[t._v("10:30 am")]),t._v(" "),r("option",[t._v("11:00 am")]),t._v(" "),r("option",[t._v("11:30 am")]),t._v(" "),r("option",[t._v("12:00 pm")]),t._v(" "),r("option",[t._v("12:30 pm")]),t._v(" "),r("option",[t._v("1:00 pm")]),t._v(" "),r("option",[t._v("1:30 pm")]),t._v(" "),r("option",[t._v("2:00 pm")]),t._v(" "),r("option",[t._v("2:30 pm")])])],1),t._v(" "),r("b-form-group",{attrs:{label:"Workday End","label-for":"input-3",description:"Usual time that your workday ends. (e.g. 5:30pm)",row:""}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}},[r("option",{attrs:{disabled:"",value:""}},[t._v("Please select one")]),t._v(" "),r("option",[t._v("3:00 pm")]),t._v(" "),r("option",[t._v("3:30 pm")]),t._v(" "),r("option",[t._v("4:00 pm")]),t._v(" "),r("option",[t._v("4:30 pm")]),t._v(" "),r("option",[t._v("5:00 pm")]),t._v(" "),r("option",[t._v("5:30 pm")]),t._v(" "),r("option",[t._v("6:00 pm")]),t._v(" "),r("option",[t._v("6:30 pm")]),t._v(" "),r("option",[t._v("7:00 pm")]),t._v(" "),r("option",[t._v("7:30 pm")]),t._v(" "),r("option",[t._v("8:00 pm")]),t._v(" "),r("option",[t._v("8:30 pm")]),t._v(" "),r("option",[t._v("9:00 pm")]),t._v(" "),r("option",[t._v("9:30 pm")]),t._v(" "),r("option",[t._v("10:00 pm")]),t._v(" "),r("option",[t._v("10:30 pm")]),t._v(" "),r("option",[t._v("11:00 pm")])])],1),t._v(" "),r("b-form-group",{attrs:{label:"Focus Time Length","label-for":"input-3",description:"How long you want to focus daily (e.g. 120 mins)",row:""}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}},[r("option",{attrs:{disabled:"",value:""}},[t._v("Please select one")]),t._v(" "),r("option",[t._v("30 min")]),t._v(" "),r("option",[t._v("60 min")]),t._v(" "),r("option",[t._v("90 min")]),t._v(" "),r("option",[t._v("120 min")]),t._v(" "),r("option",[t._v("180 min")])])],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")])],1),t._v(" "),r("b-row",[r("br")]),t._v(" "),r("b-row",[r("br")]),t._v(" "),r("b-row",{staticClass:"text-center"},[r("b-col",{attrs:{cols:"1"}}),t._v(" "),r("b-col",{attrs:{cols:"10"}},[r("h4",[t._v("Your integrations")])]),t._v(" "),r("p",[t._v("We use your Slack and Calendar events to book time to focus in the upcoming period, offer personal suggestions and display aggregated historical data spent in collaboration and focus. Github history is used to estimate of your contribution for a given period. Your data is never shared with others and available exclusively to you (for now...)")]),t._v(" "),r("b-col",{attrs:{cols:"1"}})],1),t._v(" "),r("b-row",[r("br")]),t._v(" "),t.userData.slack_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Slack has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/slack-install"}},[t._v("Reintegrate Slack")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n          You still need to integrate Slack\n        ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/slack-install"}},[t._v("Integrate Slack")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.google_calendar_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Google Calendar has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/build_google_calendar_auth_request"}},[t._v("Reintegrate Google Calendar")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n          You still need to integrate Google Calendar\n        ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/build_google_calendar_auth_request"}},[t._v("Integrate Google Calendar")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("hr",{staticClass:"my-4"}),t._v(" "),t.userData.github_user_id?r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("Github has been integrated")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-secondary",href:"/github-auth"}},[t._v("Reintegrate Github")])],1),t._v(" "),r("b-col")],1):r("b-row",[r("b-col"),t._v(" "),r("b-col",{staticClass:"text-center",attrs:{cols:"4"}},[t._v("\n          You still need to integrate Github\n        ")]),t._v(" "),r("b-col",{attrs:{cols:"4"}},[r("b-button",{attrs:{variant:"outline-primary",href:"/github-auth"}},[t._v("Integrate Github")])],1),t._v(" "),r("b-col")],1),t._v(" "),r("b-row",[r("br")]),t._v(" "),r("b-row",[r("br")])],1),t._v(" "),r("b-form-group",{attrs:{label:""}},[r("b-button",{attrs:{variant:"outline-info",to:"change-password"}},[t._v("Change your password")])],1)],1)},[],!1,null,"8e483392",null).exports),C={data:function(){return{}},computed:Object(u.b)({changePassword:function(t){return t.changePassword},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess}}),methods:{submitNewPassword:function(){var t=this;this.$store.dispatch("changePassword").then(function(){t.formErrors})}},beforeMount:function(){this.$store.dispatch("clearPasswordForm")}},D=Object(s.a)(C,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("h2",[t._v("Change your password")]),t._v(" "),t.formErrors?r("div",{staticClass:"error-messages"},t._l(t.formErrors,function(e){return r("b-alert",{key:e,attrs:{show:"",variant:"warning"}},[t._v("\n        "+t._s(e)+"\n      ")])}),1):t._e(),t._v(" "),t.changePasswordSuccess?r("div",{staticClass:"error-messages"},[r("b-alert",{attrs:{show:"",variant:"success"}},[t._v("\n        Password changed successfully!\n      ")])],1):t._e(),t._v(" "),r("b-form",{on:{submit:function(e){return e.preventDefault(),t.submitNewPassword(e)}}},[r("b-form-group",{attrs:{label:"New password","label-for":"input-2",description:"Minimum of 1 character"}},[r("b-form-input",{attrs:{required:"",id:"input-2",type:"password"},model:{value:t.changePassword.new_password,callback:function(e){t.$set(t.changePassword,"new_password",e)},expression:"changePassword.new_password"}})],1),t._v(" "),r("b-form-group",{attrs:{label:"Confirm new password","label-for":"input-3",description:"Must match new password"}},[r("b-form-input",{attrs:{required:"",id:"input-3",type:"password"},model:{value:t.changePassword.confirm_new_password,callback:function(e){t.$set(t.changePassword,"confirm_new_password",e)},expression:"changePassword.confirm_new_password"}})],1),t._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Change password")])],1)],1)],1)},[],!1,null,null,null).exports,k=r("iINK"),U={methods:{percentFunc:function(t){return t+" hrs"}},components:{donut:k.DonutChart},props:{activity:{default:Array(),type:Array},number:{default:1,type:Number},isReady:{default:!1,type:Boolean}},computed:{donutData:function(){var t=0,e=0,r=0;this.activity.forEach(function(a){var n=new Date(a.datetime_utc),s=new Date;a.is_workday_time&&n<s&&(1,1==a.is_collaborative_time?t+=1:1==a.is_refocus_time?(console.log(a.datetime_utc),r+=1):1==a.is_focus_time?e+=1:console.log("Not categorized"))});var a=[];return[{label:"Collaborative Time",value:(5*t/60).toFixed(1)},{label:"Focused Time",value:(5*e/60).toFixed(1)},{label:"Refocusing Time",value:(5*r/60).toFixed(1)}].forEach(function(t){0==t.value||isNaN(t.value)||a.push(t)}),a},graphColors:function(){var t={"Collaborative Time":'"#294d64"',"Focused Time":'"#69B8EA"',"Refocusing Time":'"#3b7194"'},e=[];return this.donutData.forEach(function(r){e.push(t[r.label])}),"["+e.join()+"]"},name:function(){return"collaboration-pie"+this.number},noData:function(){return this.activity.length>0&0==this.donutData.length},collabMessage:function(){if(this.isReady){var t=parseFloat(this.donutData.filter(function(t){return"Collaborative Time"==t.label})[0].value);return t<14.5?"Nice work! Last week you had "+t+" collaborative hours, less than your all time average of 14.5 hours.":"Last week you had "+t+" collaborative hours, more than your all time average of 14.5 hours."}return""}}},E=(r("2w/H"),Object(s.a)(U,function(){var t=this,e=t.$createElement,r=t._self._c||e;return this.isReady?r("div",{staticClass:"container text-center"},[r("h5",[t._v("Collaboration / Independent Time Balance")]),t._v(" "),r("div",[t._v("\n    "+t._s(this.collabMessage)+"\n  ")]),t._v(" "),r("donut",{attrs:{id:t.name,data:t.donutData,colors:t.graphColors,resize:"True",formatter:this.percentFunc}})],1):r("div",{staticClass:"container text-center"},[r("h5",{staticClass:"text-center"},[t._v("Collaboration / Independent Time Balance")]),t._v(" "),r("br"),t._v(" "),r("br"),t._v(" "),r("b",{staticClass:"text-center"},[t._v("Loading...")])])},[],!1,null,"422c3186",null).exports),x=r("fZjL"),S=r.n(x),F=r("lHA8"),R=r.n(F),P={props:{activity:{default:Array(),type:Array},isReady:{default:!1,type:Boolean}},computed:{collaborativeDayCounts:function(){var t=0,e=this.activity.filter(function(t){return!t.work}),r=new R.a(e.map(function(t){return new Date(t.datetime_utc).getUTCDate()})),a={},n=(new Date).getDate();r.forEach(function(t){t<=n&&(a[t]=0)}),e.forEach(function(t){if(t.is_collaborative_time){var e=new Date(t.datetime_utc).getUTCDate();e in a&&(a[e]+=1)}});t=0;var s=S()(a).length;return S()(a).forEach(function(e){0==a[e]&&(t+=1)}),{totalDays:s-1,disconnectedDays:t}}}},A=(r("gJ3f"),{components:{pie:E,disconnect:Object(s.a)(P,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"text-center"},[r("h5",[t._v("Disconnected After-Hours")]),t._v(" "),t._m(0),t._v(" "),r("br"),t._v(" "),r("br"),t._v(" "),this.isReady?r("div",{staticClass:"text-center"},[r("h2",[t._v("You disconnected from work after-hours")]),t._v(" "),r("h2",{staticClass:"disconnected-days"},[t._v(t._s(t.collaborativeDayCounts.disconnectedDays)+" / "+t._s(t.collaborativeDayCounts.totalDays))]),t._v(" "),r("h2",[t._v("days last week.")])]):r("div",{staticClass:"row text-center"},[r("b",{staticClass:"text-center"},[t._v("Loading...")])])])},[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[this._v("\n    All-time average "),e("b",[this._v("2.7")]),this._v(" days per week.\n  ")])}],!1,null,"3b47b4b0",null).exports},props:{shouldNudge:{type:Object,default:function(){return{"dnd-now":!0,"dnd-after-hours":!0,"open-calendar":!0}}}},methods:{requestNudge:function(t){this.$store.dispatch("requestNudge",{nudgeType:t}),this.shouldNudge[t]=!1}},computed:Object(u.b)({userName:function(t){return t.currentUser.username},activityData:function(t){return t.activityData},activityDataIsReady:function(t){return t.activityData.length>0},lastWeekActivityData:function(t){return t.lastWeekActivityData},lastWeekActivityDataIsReady:function(t){return t.lastWeekActivityData.length>0},totalWorkHours:function(t){return this.activityDataIsReady?this.activityData.filter(function(t){return 1==t.is_workday_time}).length/12:"-"},remainingFocusHours:function(t){var e=t.activityData,r=new Date;return(e.filter(function(t){return new Date(t.datetime_utc)>r&&t.is_workday_time&&!t.is_collaborative_time&&!t.is_refocus_time}).length*(1/12)).toFixed(0)},formErrors:function(t){return t.formErrors},changePasswordSuccess:function(t){return t.changePasswordSuccess},dateRange:function(t){if(0==t.activityData.length)return{};var e=new Date(t.activityData[0].datetime_utc);return{startDate:e=7==e.getDate()&&2==e.getMonth()&&2020==e.getUTCFullYear()?new Date(e.setDate(8)).toDateString():e.toDateString(),endDate:new Date(t.activityData[t.activityData.length-1].datetime_utc).toDateString()}},lastWeekDateRange:function(t){if(0==t.lastWeekActivityData.length)return{};var e=new Date(t.lastWeekActivityData[0].datetime_utc);return 29==e.getDate()&&1==e.getMonth()&&2020==e.getUTCFullYear()&&(e=new Date(new Date(e.setDate(1)).setMonth(2))),{startDate:e=e.toDateString(),endDate:new Date(t.lastWeekActivityData[t.lastWeekActivityData.length-1].datetime_utc).toDateString()}},timeOfDay:function(){var t=(new Date).getHours();return t<12&&t>0?"Morning":t>12&&t<18?"Afternoon":"Evening"}})}),N=(r("uj2o"),Object(s.a)(A,function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",[r("div",{staticClass:"row greeting"},[r("div",[r("h5",[t._v("Good "+t._s(this.timeOfDay)+", "),r("b",[t._v(t._s(this.userName))]),t._v(".")])])]),t._v(" "),r("div",{staticClass:"row current-week"},[r("div",[r("h3",{staticClass:"subber"},[this.activityDataIsReady?r("b",[t._v(t._s(this.remainingFocusHours)+"/"+t._s(this.totalWorkHours))]):r("b",{staticClass:"text-center"},[t._v("-/"+t._s(this.totalWorkHours))]),t._v("\n          hours remain to focus this week.\n        ")]),t._v(" "),r("p",[t._v("Current week from \n          "),this.activityDataIsReady?r("b",[t._v(t._s(this.dateRange.startDate))]):r("b",[t._v("-")]),t._v("\n          to\n          "),this.activityDataIsReady?r("b",[t._v(t._s(this.dateRange.endDate))]):r("b",[t._v("-")])]),t._v(" "),r("p",[t._v("Next focus session is "),r("b",[t._v("tomorrow at 9:30am")]),t._v(".")])])]),t._v(" "),r("div",{staticClass:"row suggestions"},[t.shouldNudge["dnd-now"]?r("span",[r("h5",{staticClass:"alert alert-warning"},[t._v("Spend less time on Slack today. "),r("a",{on:{click:function(e){return t.requestNudge("dnd-now")}}},[t._v("Set Do Not Disturb Now")])])]):r("span",[r("h5",{staticClass:"alert alert-success"},[t._v("DONE. Fulfilled has set Slack to "),r("em",[t._v("Do Not Disturb")]),t._v(" so you can focus without distraction.")])]),t._v(" "),t.shouldNudge["open-calendar"]?r("span",[r("h5",{staticClass:"alert alert-warning"},[t._v("Need to attend all meetings this week? "),r("a",{attrs:{href:"https://calendar.google.com",target:"_blank"},on:{click:function(e){return t.requestNudge("open-calendar")}}},[t._v("Open Calendar")]),t._v(".")])]):r("span",[r("h5",{staticClass:"alert alert-success"},[t._v("Cool. If you need "),r("b",[r("em",[t._v("Fulfilled")])]),t._v(' to also schedule time for you, go to Settings and click "Schedule Time".')])]),t._v(" "),t.shouldNudge["dnd-after-hours"]?r("span",[r("h5",{staticClass:"alert alert-warning"},[t._v("Have you disconnected after work this week? "),r("a",{on:{click:function(e){return t.requestNudge("dnd-after-hours")}}},[t._v("Set Do Not Disturb after hours")])])]):r("span",[r("h5",{staticClass:"alert alert-success"},[t._v("DONE. Fulfilled will set Slack to "),r("em",[t._v("Do Not Disturb")]),t._v(" when your workday ends so you can disconnect from it.")])])]),t._v(" "),r("div",{staticClass:"row previous-week"},[r("div",[r("h3",{staticClass:"subber"},[t._v("Previous week trends")]),t._v(" "),r("p",[t._v("Previous week from \n          "),this.lastWeekActivityDataIsReady?r("b",[t._v(t._s(this.lastWeekDateRange.startDate))]):r("b",[t._v("-")]),t._v("\n          to\n          "),this.lastWeekActivityDataIsReady?r("b",[t._v(t._s(this.lastWeekDateRange.endDate))]):r("b",[t._v("-")])])])]),t._v(" "),r("br"),t._v(" "),r("div",{staticClass:"row"},[r("div",{staticClass:"col-md-6"},[r("pie",{attrs:{activity:this.lastWeekActivityData,number:1,isReady:this.lastWeekActivityDataIsReady}})],1),t._v(" "),r("div",{staticClass:"col-md-6"},[r("disconnect",{attrs:{activity:this.lastWeekActivityData,isReady:this.lastWeekActivityDataIsReady}})],1)]),t._v(" "),r("b-row",[r("br")])],1)],1)},[],!1,null,null,null).exports),O=r("BO1k"),L=r.n(O),j=r("woOf"),T=r.n(j),W=r("mtWM"),$=r.n(W);function I(){return $.a.get("/api/get_csrf")}function q(t){var e=t.weekOffset;return $.a.get("/api/activity-data?week-offset="+e)}var H=r("ppUw"),M=r.n(H),B=r("0xDb");a.default.use(u.a),a.default.use(M.a);var Y={email:null,password:null,csrf_token:null},G={username:null,email:null,password:null,confirm_password:null,csrf_token:null},J={new_password:null,confirm_new_password:null},K={users:[],userData:{},newUser:T()({},G),formErrors:null,loginUser:T()({},Y),currentUser:null,CSRFToken:null,jwt:"",changePassword:T()({},J),changePasswordSuccess:!1,authCode:null,isLoggedIn:!1,activityData:[],lastWeekActivityData:[]},z={loadActivity:function(t,e){return q({}).then(function(e){return t.commit("setActivityData",{time:e.data})})},loadPastActivity:function(t){return q({weekOffset:-1}).then(function(e){return t.commit("setLastWeekActivityData",{time:e.data})})},loadUsers:function(t){return $.a.get("/api/users").then(function(e){return t.commit("setUsers",{users:e.data})})},loadUser:function(t,e){return $.a.get("/api/user_details").then(function(e){e.data||t.commit("setUserData",{userData:{error:!0}}),t.commit("setUserData",{userData:e.data})}).catch(function(t){console.log("Error loading user")})},loadCSRF:function(t){return I().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})})},registerNewUser:function(t){K.newUser.csrf_token=K.CSRFToken;var e;(e=K.newUser,$.a.post("/api/register",e)).then(function(e){return t.commit("clearNewUser",{}),t.commit("setErrors",{errors:null}),!0}).catch(function(e){I().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);return t.commit("setErrors",{errors:r}),!1})},userLogin:function(t){return K.loginUser.csrf_token=K.CSRFToken,(e=K.loginUser,$.a.post("/api/login",e)).then(function(e){return t.commit("setErrors",{errors:null}),t.commit("clearLoginUser",{}),t.commit("setCurrentUser",{currentUser:e.data})}).catch(function(e){I().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);return t.commit("setErrors",{errors:r})});var e},clearFormErrors:function(t){K.formErrors=null},checkLogin:function(t){return $.a.get("/api/check-login").then(function(e){return null==e.data?t.commit("clearCurrentUser",{}):t.commit("setCurrentUser",{currentUser:e.data})})},clearCredentials:function(t){return $.a.get("/api/logout").then(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e}).catch(function(e){return t.commit("clearCurrentUser",{}),t.commit("clearLoginUser",{}),e})},changePassword:function(t){K.changePassword.csrf_token=K.CSRFToken;var e;(e=K.changePassword,K.currentUser,$.a.post("/api/change-password",e)).then(function(e){return I().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})}),t.commit("setErrors",{errors:null}),t.commit("setChangePassword",{changePasswordForm:T()({},J)}),t.commit("setChangePasswordStatus",{changePasswordSuccess:!0}),!0}).catch(function(e){I().then(function(e){return t.commit("setCSRF",{CSRFToken:e.data.csrf_token})});var r=Q(e.response);return t.commit("setErrors",{errors:r}),t.dispatch("clearPasswordForm"),!1})},clearPasswordForm:function(t){t.commit("setChangePasswordStatus",{changePasswordSuccess:!1}),t.commit("setChangePassword",{changePasswordForm:T()({},J)})},requestNudge:function(t,e){console.log(e),function(t){var e=t.nudgeType;$.a.get("/api/activate-nudge?nudge_type="+e)}(e)}},Z={setUsers:function(t,e){t.users=e.users},setUserData:function(t,e){console.log(e.userData),t.userData=e.userData},setCSRF:function(t,e){t.CSRFToken=e.CSRFToken},setErrors:function(t,e){t.formErrors=e.errors},setNewUser:function(t,e){t.newUser=e.newUser},setJWT:function(t,e){t.jwt=e.jwt},setCurrentUser:function(t,e){t.currentUser=e.currentUser},saveCurrentUser:function(t,e){$cookies.set("currentUser",e.currentUser)},clearLoginUser:function(t,e){t.loginUser=T()({},Y)},clearNewUser:function(t,e){t.newUser=T()({},G)},setChangePassword:function(t,e){t.changePassword=e.changePasswordForm},setChangePasswordStatus:function(t,e){t.changePasswordSuccess=e.changePasswordSuccess},clearCurrentUser:function(t,e){t.currentUser=null},setActivityData:function(t,e){t.activityData=e.time},setLastWeekActivityData:function(t,e){t.lastWeekActivityData=e.time}},X={isLoggedIn:function(t){return null!=t.currentUser},isAuthenticated:function(t){return Object(B.a)(t.jwt)},currentUser:function(t){return t.currentUser},userData:function(t){return t.userData}};function Q(t){var e,r=null;if(t.data.errors){var a=t.data.errors;r=[];var n=!0,s=!1,o=void 0;try{for(var i,c=L()((e=a,S()(e)));!(n=(i=c.next()).done);n=!0){var u=i.value,l=!0,v=!1,d=void 0;try{for(var f,m=L()(a[u]);!(l=(f=m.next()).done);l=!0){var _=f.value;r=r.concat(_)}}catch(t){v=!0,d=t}finally{try{!l&&m.return&&m.return()}finally{if(v)throw d}}}}catch(t){s=!0,o=t}finally{try{!n&&c.return&&c.return()}finally{if(s)throw o}}}return r}var V=new u.a.Store({state:K,actions:z,mutations:Z,getters:X});a.default.use(i.a);var tt=new i.a({routes:[{path:"/",name:"Home",component:v,beforeEnter:function(t,e,r){V.dispatch("loadUsers").then(function(){r()})}},{path:"/maestro/:id",name:"Maestro",component:f,beforeEnter:function(t,e,r){r("/fulfilled-dashboard")}},{path:"/register-new-user",name:"Register",component:_,beforeEnter:function(t,e,r){V.getters.isLoggedIn||(V.dispatch("clearFormErrors"),r())}},{path:"/login",name:"Login",component:h,beforeEnter:function(t,e,r){if(V.dispatch("clearFormErrors"),V.getters.isLoggedIn){V.getters.currentUser;r("/fulfilled-dashboard")}else r()}},{path:"/logout",name:"Logout",beforeEnter:function(t,e,r){return V.dispatch("clearCredentials").then(function(){r("/login")})}},{path:"/settings",name:"Settings",component:y,beforeEnter:function(t,e,r){V.dispatch("clearFormErrors");var a=V.getters.isLoggedIn,n=V.getters.currentUser;a?V.dispatch("loadUser",n).then(function(){r()}):r("/login")}},{path:"/change-password",name:"Change password",component:D,beforeEnter:function(t,e,r){V.dispatch("clearFormErrors"),et(r,V)}},{path:"/fulfilled-dashboard",name:"Dashboard",component:N,beforeEnter:function(t,e,r){var a=t.params.start_time,n=t.params.end_time;V.dispatch("clearFormErrors"),V.dispatch("loadActivity",a,n),V.dispatch("loadPastActivity",a,n),et(r,V)}}]});function et(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"/login",a=e.getters.isLoggedIn;e.getters.currentUser;return a?t():t(r)}tt.beforeEach(function(t,e,r){V.dispatch("checkLogin").then(function(){V.dispatch("loadCSRF").then(function(){r()})})});var rt=tt,at=r("Tqaz");a.default.config.productionTip=!1,a.default.use(at.a),new a.default({el:"#app",router:rt,store:V,components:{App:o},template:"<App/>"})},QOPB:function(t,e){},XwAu:function(t,e){},XwcA:function(t,e,r){t.exports=r.p+"static_files/img/logo_transparent.072b69b.png"},eAji:function(t,e,r){"use strict";var a=r("wlbq");r.n(a).a},fZSw:function(t,e,r){"use strict";var a=r("yHqF");r.n(a).a},gJ3f:function(t,e,r){"use strict";var a=r("xWmm");r.n(a).a},iDhR:function(t,e){},ifoh:function(t,e){},lZ5c:function(t,e,r){"use strict";r("fZSw");var a=r("K1/g"),n=Object(a.a)({},function(){this.$createElement;this._self._c;return this._m(0)},[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"right-sidebar"}},[r("h3",[t._v("Quotes")]),t._v(" "),r("div",{staticClass:"sidebar-section"},[r("p",{staticClass:"sidebar"},[t._v('"Less mental clutter means more mental resources available for deep thinking."')]),t._v(" "),r("h6",[t._v("-Cal Newport")])]),t._v(" "),r("h3",[t._v("Concepts")]),t._v(" "),r("div",[r("p",{staticClass:"sidebar"},[t._v('"Attention residue is when thoughts about a task persist and intrude while performing another task"')]),t._v(" "),r("h6",[t._v("-Sophie Leroy")])])])}],!1,null,null,null);e.a=n.exports},nm9u:function(t,e,r){t.exports=r.p+"static_files/img/trends.c70a865.png"},teIl:function(t,e,r){"use strict";var a=r("NYxO"),n=(r("0xDb"),{computed:Object(a.b)({isAuthenticated:function(t){return!!t.currentUser},currentUser:function(t){return t.currentUser}})}),s=(r("yfgR"),r("K1/g")),o=Object(s.a)(n,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("b-navbar",{attrs:{toggleable:"lg"}},[a("div",{staticClass:"logo"},[a("b-navbar-brand",{attrs:{to:"/"}},[a("img",{staticClass:"logo",attrs:{src:r("XwcA"),alt:"Fulfilled.ai",width:"70",height:"70"}})])],1),t._v(" "),a("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),a("b-collapse",{staticClass:"mr-auto",attrs:{id:"nav-collapse","is-nav":""}},[a("b-navbar-nav",{staticClass:"ml-auto center"},[t.isAuthenticated?[a("b-nav-item",{attrs:{to:"/fulfilled-dashboard"}},[t._v("Dashboard")]),t._v(" "),a("b-nav-item",{attrs:{to:"/settings"}},[t._v("Settings")]),t._v(" "),a("b-nav-item",{attrs:{to:"/Logout"}},[t._v("Logout")])]:[a("b-nav-item",{attrs:{to:"/login"}},[t._v("Login")]),t._v(" "),a("b-nav-item",{attrs:{to:"/register-new-user"}},[t._v("Register")])]],2)],1)],1)},[],!1,null,null,null);e.a=o.exports},uj2o:function(t,e,r){"use strict";var a=r("yV3i");r.n(a).a},wlbq:function(t,e){},x8S4:function(t,e,r){"use strict";(function(t){var a=r("teIl"),n=r("lZ5c"),s=r("Jmt5"),o=(r.n(s),r("9M+g")),i=(r.n(o),r("iDhR")),c=(r.n(i),r("0UmN")),u=r.n(c),l=r("NYxO");t.Raphael=u.a,e.a={name:"App",components:{"app-header":a.a,"right-sidebar":n.a},computed:Object(l.b)({currentUser:function(t){return t.currentUser},isAuthenticated:function(t){return t.currentUser?(console.log(!0),!0):(console.log(!1),!1)}})}}).call(e,r("DuR2"))},xWmm:function(t,e){},yBiD:function(t,e,r){"use strict";var a=r("KIop");r.n(a).a},yHqF:function(t,e){},yV3i:function(t,e){},yavf:function(t,e){},yfgR:function(t,e,r){"use strict";var a=r("QOPB");r.n(a).a}},["NHnr"]);
//# sourceMappingURL=app.edcf70267255cbb24f22.js.map