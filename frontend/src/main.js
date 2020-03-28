import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueSession from "vue-session";

Vue.use(vuetify);
Vue.use(VueSession);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  axios,
  VueSession,
  render: h => h(App)
}).$mount("#app");
