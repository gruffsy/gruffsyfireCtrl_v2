<template>
  <div>
    <div id="app-instasearch">
      <v-card>
        <v-card-text>
          <v-text-field label="Søk etter kunde" v-model="kundeNameSearchString"></v-text-field>
        </v-card-text>
        <v-list-item
          link
          three-line
          router
          :to="{
            path: '/customer-objects/',
            query: { kid: customer.id }
          }"
          v-for="customer in filteredCustomerFeed"
          v-bind:key="customer.id"
        >
          <v-list-item-content>
            
           <Customer :kid="customer.id"/>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>
import Customer from "../components/Customer"
export default {
  name: "Customers",
  components: {
    Customer
  },
  data() {
    return {
      kundeNameSearchString: "",
      customers: []
    };
  },

  mounted() {
    this.retrieveCustomers();
  },
  methods: {
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
  computed: {
    filteredCustomerFeed: function() {
      var customers = this.customers;
      var kundeNameSearchString = this.kundeNameSearchString;

      if (!kundeNameSearchString) {
        return customers;
      }

      kundeNameSearchString = kundeNameSearchString.trim().toLowerCase();

      customers = customers.filter(function(item) {
        if (item.kunde.toLowerCase().indexOf(kundeNameSearchString) !== -1) {
          return item;
        }
      });

      return customers;
    }
  }
};
</script>
<style scoped>
  color: red
</style>
