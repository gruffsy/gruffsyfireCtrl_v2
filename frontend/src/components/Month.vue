<template>
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
          :to="{
            path: `/customer-objects/${customer.id}`,
            query: { monthId: month.id }
          }"
          v-for="customer in customers"
          :key="customer.id"
          v-if="customer.month == month.url"
        >
          <!-- eslint-enable -->
          <v-list-item-content>
            

            
            <v-list-item-title x-large><v-list-item-icon>
              <v-icon x-large>mdi-home-city</v-icon>
            </v-list-item-icon>{{ customer.kunde }}</v-list-item-title>
            <v-list-item-subtitle>
              {{ customer.badresse }}, {{ customer.bpostnr }}&nbsp;{{
                customer.bpoststed
              }}
            </v-list-item-subtitle>
            <v-list-item-subtitle
              >Kontaktperson: {{ customer.kontaktperson }}</v-list-item-subtitle
            >
            <v-list-item-subtitle>{{ customer.tlf1 }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ customer.tlf2 }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import axios from "axios";

export default {
  name: "Month",
  components: {},
  data() {
    return {
      months: [],
      month_detail: [],

      customers: [],
      axiosConfig: {
        headers: {
          Authorization: "Token " + this.$token.getToken()
        }
      }
    };
  },
  created() {
    this.allMonths();
    this.allCustomers();
  },

  methods: {
    allMonths() {
      axios.get("api/months/", this.axiosConfig).then(response => {
        this.months = response.data;
      });
    },
    monthDetail(id) {
      axios.get("api/months/" + id + "/", this.axiosConfig).then(response => {
        this.month_detail = response.data;
      });
    },
    allCustomers() {
      axios.get("api/customers/", this.axiosConfig).then(response => {
        this.customers = response.data;
      });
    }
  },
  computed: {}
};
</script>
