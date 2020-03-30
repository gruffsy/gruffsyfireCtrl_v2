<template>
<div>
  <Navbar />
  <v-container>
    <v-card outlined link route to class="primary" dark>
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">Siste kunde</div>
          <v-list-item-title class="headline mb-1">Siste aktive kunde</v-list-item-title>
          <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar tile size="80" color="grey">mdi-account</v-list-item-avatar>
      </v-list-item>

      <v-card-actions></v-card-actions>
    </v-card>

    <br />
    <v-expansion-panels focusable>
      <v-expansion-panel v-for="month in months" :key="month.id">
        <v-expansion-panel-header>{{ month.navn }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <!-- eslint-disable -->
          <v-list-item
            dense
            link
            prepend-icon="mdi-house"
            three-line
            router
            :to="`/api/customers/${kunde.id}/`"
            v-for="kunde in customers"
            :key="kunde.id"
            v-if="kunde.month === month.id"
          >
            <!-- eslint-enable -->
            <v-list-item-content>
              <v-list-item-icon>
                <v-icon>mdi-home-city</v-icon>
              </v-list-item-icon>
              <v-list-item-title>{{ kunde.kunde }}</v-list-item-title>
              <v-list-item-subtitle>
                {{ kunde.badresse }}, {{ kunde.bpoststed }}&nbsp;{{
                kunde.bpoststed
                }}
              </v-list-item-subtitle>
              <v-list-item-subtitle>Kontaktperson: {{ kunde.kontaktperson }}</v-list-item-subtitle>
              <v-list-item-subtitle>{{ kunde.tlf1 }}</v-list-item-subtitle>
              <v-list-item-subtitle>{{ kunde.tlf2 }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <br />
    <br />
    <br />
    <br />
    <br />
  </v-container>
  </div>
</template>

<script>
import router from "../router/index";
import axios from "axios";
import { TokenService } from "../storage/service";
import Navbar from "../components/Navbar";
export default {
  name: "Customers",
  components: {
    Navbar,
  },
  data() {
    return {
      months: [],
      month_detail: [],
      customers: []
    };
  },
  created() {
    this.token = TokenService.getToken();
    this.allMonths();
    this.allCustomers();
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
      });
    },
    allCustomers() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios.get("api/customers/", axiosConfig).then(response => {
        this.customers = response.data;
      });
    }
  },
  computed: {}
};
</script>