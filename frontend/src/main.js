import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueSession from "vue-session";
import { TokenService } from "./storage/service";
import http from "./http-common";
import DataService from "./services/DataService"

Vue.use(vuetify);
Vue.use(VueSession);

Vue.config.productionTip = false;
Vue.prototype.$token = TokenService;
Vue.prototype.$http = http;
Vue.prototype.$dataservice = DataService;

new Vue({
  router,
  store,
  vuetify,
  axios,
  VueSession,
  render: h => h(App)
}).$mount("#app");
