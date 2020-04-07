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
            path: '/customer-objects/',
            query: { kid: customer.id }
          }"
          v-for="customer in customers"
          :key="customer.id"
          v-if="customer.month == month.id"
        >
          <!-- eslint-enable -->
          <v-list-item-content>
            <v-list-item-title x-large>
              <v-list-item-icon>
                <v-icon x-large>mdi-home-city</v-icon>
              </v-list-item-icon>
              {{ customer.kunde }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ customer.badresse }}, {{ customer.bpostnr }}&nbsp;{{
              customer.bpoststed
              }}
            </v-list-item-subtitle>
            <v-list-item-subtitle>Kontaktperson: {{ customer.kontaktperson }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ customer.tlf1 }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ customer.tlf2 }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
export default {
  name: "Month",
  components: {},
  data() {
    return {
      months: [],
      customers: []
    };
  },
  created() {
    this.retrieveMonths();
    this.retrieveCustomers()
    
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
      this.$dataservice.getAllCustomers()
        .then(response => {
          this.customers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  computed: {}
};
</script>
