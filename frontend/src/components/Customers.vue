<template>
  <v-container grid-list-xs>
    <h1>Måneder</h1>
    <ol>
      <li v-for="(month, index) in months" :key="index">Månedsnavn: {{ month.navn }}</li>
    </ol>
    <v-btn color="success" @click="logout">logout</v-btn>
  </v-container>
</template>

<script>
import router from "../router/index";
import axios from "axios";
import { TokenService } from "../storage/service";
export default {
  name: "Customers",
  data() {
    return {
      months: []
    };
  },
  created() {
    //let token;
    //console.log(token);
    this.token = TokenService.getToken();
    //console.log(this.token);
    this.all();
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      //console.log(this.token)
      if (!this.token) {
        router.push("/login");
      }
    },
    logout() {
      localStorage.removeItem("user-token");
      this.$router.push('/login');
    },
    all() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios.get("api/months/", axiosConfig).then(response => {
        this.months = response.data;
      });
    }
  }
};
</script>