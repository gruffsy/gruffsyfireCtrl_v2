<!-- TODO:
-->
<template>
  <nav>
    <v-app-bar class="primary darken-2" dark app height="84" hide-on-scroll>
      <router-link class="routerLink" :to="{
            path: '/',}">
        <v-icon x-large>{{ meny_icon }}</v-icon>
      </router-link>
      <router-link class="routerLink" :to="{
            path: '/',}">
        <v-toolbar-title dark>
          <span class="font-weight-light">fire</span>
          <span>Ctrl</span>
        </v-toolbar-title>
      </router-link>
      <v-spacer />
        <v-toolbar-title><SmallCustomer :kid="kid" v-if="kid"/></v-toolbar-title>
      <v-spacer />
      
      <v-btn v-if="token" @click="logout" text dark>
        <span>Logg ut</span>
        <v-icon right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>

   
  </nav>
</template>
<script>
import SmallCustomer from "./SmallCustomer"
export default {
  name: "Navbar",
  components: {SmallCustomer},
  data() {
    return {
      // token: localStorage.getItem("user-token") || null,
      drawer: false,
      meny_icon: "mdi-fire",
      items: [
        { title: "Kunder", icon: "mdi-view-dashboard", route: "/" },
        { title: "Objekter", icon: "mdi-image", route: "/customer-objects" },
        {
          title: "Objektdetaljer",
          icon: "mdi-help",
          route: "/object-details"
        },
        {
          title: "Legg til kunde",
          icon: "mdi-view-dashboard",
          route: "/create-customer/1"
        }
      ],
      right: null
    };
  },
  mounted() {
    this.checkLoggedIn();
  },
  created() {
    this.token = this.$token.getToken();
  },
  props: ['kid'],
  methods: {
    meny() {
      this.drawer = !this.drawer;
    },
    checkLoggedIn() {
      //console.log(this.token)
      if (!this.token) {
        this.$router.push("/login");
      }
    },
    logout() {
      localStorage.removeItem("user-token");
      this.$router.push("/login");
    }
  }
};
</script>
<style scoped>
.routerLink {
  text-decoration: none;
  color: white;
}
</style>