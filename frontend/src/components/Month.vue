<template>
  <v-expansion-panels focusable>
    <v-expansion-panel v-for="month in months" :key="month.id">
      <v-expansion-panel-header>{{ month.navn }}</v-expansion-panel-header>
      <v-expansion-panel-content>
        <!-- eslint-disable -->
        <v-list-item
          dense
          prepend-icon="mdi-house"
          three-line
          v-for="customer in customers"
          :key="customer.id"
          v-if="customer.month == month.id"
        >
          <!-- eslint-enable -->
          <v-list-item-content>
            <Customer :kid="customer.id" />
          </v-list-item-content>
        </v-list-item>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Customer from "../components/Customer";
export default {
  name: "Month",
  components: {
    Customer
  },
  data() {
    return {
      months: [],
      customers: []
    };
  },
  created() {
    this.retrieveMonths();
    this.retrieveCustomers();
  },
  methods: {
    retrieveMonths() {
      this.$dataservice
        .getAllMonths()
        .then(response => {
          this.months = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveCustomers() {
      this.$dataservice
        .getAllCustomers()
        .then(response => {
          this.customers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  computed: {}
};
</script>
