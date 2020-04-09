<!-- TODO:    4. Få til oppdatering av object
     TODO:    5 gå igjennom å lage logikk for objid og kid
     TODO:    6 Lage sisteobjekt-kort
     TODO:    7 Lage ObjTr API
-->
<template>
  <nav>
    <v-app-bar class="primary darken-2" dark app height="84" hide-on-scroll>
      <v-icon @click="meny" x-large>{{ meny_icon }}</v-icon>
      <v-toolbar-title @click="meny" dark>
        <span class="font-weight-light">fire</span>
        <span>Ctrl</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="token" @click="logout" text dark>
        <span>Logg ut</span>
        <v-icon right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer class="primary darken-1" color="white--text" dark app v-model="drawer">
      <v-list-item>
        <v-list-item-content @click="meny">
          <v-list-item-title class="title">Meny</v-list-item-title>

          <v-list-item-subtitle>
            <v-icon size="20">{{ meny_icon }}</v-icon>fireCtrl
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list nav>
        <v-list-item v-for="item in items" :key="item.title" link router :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>
<script>
export default {
  name: "Navbar",
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
  created(){
    this.token = this.$token.getToken();
  },
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