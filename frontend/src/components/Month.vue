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
            path: `/customer-objects/${kunde.id}`,
            query: { monthId: month.id }
          }"
          v-for="kunde in customers"
          :key="kunde.id"
          v-if="kunde.month == month.url"
        >
          <!-- eslint-enable -->
          <v-list-item-content>
            <v-list-item-icon>
              <v-icon>mdi-home-city</v-icon>
            </v-list-item-icon>
            <v-list-item-title style="font-size: 20px">{{
              kunde.kunde
            }}</v-list-item-title>
            <v-list-item-subtitle>
              {{ kunde.badresse }}, {{ kunde.bpostnr }}&nbsp;{{
                kunde.bpoststed
              }}
            </v-list-item-subtitle>
            <v-list-item-subtitle
              >Kontaktperson: {{ kunde.kontaktperson }}</v-list-item-subtitle
            >
            <v-list-item-subtitle>{{ kunde.tlf1 }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ kunde.tlf2 }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import axios from "axios";

export default {
  name: "Customers",
  components: {
    
  },
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
