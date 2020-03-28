<template>
    <v-container grid-list-xs>
        
        <h1>Måneder</h1>
        <ol>
            <li v-for="(month, index) in months"
            :key="index">Månedsnavn: {{ month.navn }}</li>
        </ol>
        <v-btn color="success" @click="logout">logout</v-btn>
    </v-container>
        
    
</template>

<script>
import router from "../router/index";
import axios from "axios";
export default {
  name: "Customers",
   data() {
    return {
      months: []
    };
  },
  created() {
    this.all();
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
        this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      }
    },
    logout() {
        this.$session.destroy();
        router.go("/login");
    },
    all() {
      axios
      .get("api/months/")
      .then(response => {
        this.months = response.data;
      });
    }
  }
};
</script>