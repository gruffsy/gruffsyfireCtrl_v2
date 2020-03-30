import Vue from "vue";
import VueRouter from "vue-router";
import Customers from "../pages/Customers";
import Auth from "../components/Auth";
import CustomerObjects from "../pages/CustomerObjects"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "customers",
    component: Customers
  },
  {
    path: "/login",
    name: "Auth",
    component: Auth
  },
  {
    path: "/customer-objects/:id",
    name: "CustomerObjects",
    component: CustomerObjects
  },
];
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
