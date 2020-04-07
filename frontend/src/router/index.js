import Vue from "vue";
import VueRouter from "vue-router";
import Customers from "../pages/Customers";
import Auth from "../components/Auth";


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
    path: "/customer-objects/",
    name: "CustomerObjects",
    component: () => 
      import("../pages/CustomerObjects"),
    props: route => ({ kid: route.query.kid, 
      objid: route.query.objid }) // kid = kundeid, objid = objectid
  },
  {
    path: "/object-details/",
    name: "ObjectDetails",
    component: () => 
      import("../pages/ObjectDetails"),
    props: route => ({ kid: route.query.kid, 
      objid: route.query.objid }) // kid = kundeid, objid = objectid
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
    props: route => ({ customer: route.query.customerId, 
    query: route.query.q })
  }
];
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
