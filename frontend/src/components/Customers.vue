<template>
  <v-container grid-list-xs>
    <h1>Måneder</h1>
    <ol>
      <li v-for="(month, index) in months" :key="index">
        <v-btn color="success" @click="monthDetail(month.id)">Månedsnavn: {{ month.navn }}</v-btn>
      </li>
    </ol>
    <v-btn color="success" @click="logout">logout</v-btn>

    <v-btn v-if="month_detail.navn" color="warning" @click="back">tilbake</v-btn>
    singel måned valgt: {{ month_detail.navn}}
    <ul>
      <li v-for="(customer, index) in customers" :key="index">
        <div v-if="month_detail.id === customer.month">{{ customer.kunde }}</div></li>
    </ul>
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
      months: {},
      month_detail: {},
      customers: {}
    };
  },
  created() {
    this.token = TokenService.getToken();
    this.allMonths();
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    back() {
      this.allMonths();
      this.month_detail = {};
    },
    checkLoggedIn() {
      //console.log(this.token)
      if (!this.token) {
        router.push("/login");
      }
    },
    logout() {
      localStorage.removeItem("user-token");
      this.$router.push("/login");
    },
    allMonths() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios.get("api/months/", axiosConfig).then(response => {
        this.months = response.data;
      });
    },
    monthDetail(id) {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios.get("api/months/" + id + "/", axiosConfig).then(response => {
        this.month_detail = response.data;
        this.months = {};
        this.filteredCustomers(id);
      });
    },
    filteredCustomers(id) {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios.get("api/customers/", axiosConfig).then(response => {
        this.customers = response.data.filter(customer =>
        customer.month === id);
        console.log(this.customers);
        
        
      });
    }
  },
  computed: {
    

  },
};
</script>