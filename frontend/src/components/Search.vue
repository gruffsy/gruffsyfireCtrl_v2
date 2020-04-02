<template>
  <div>
    <div id="app-instasearch">
      <v-card>
        <v-card-text>
          <v-text-field
            label="Søk etter kunde"
            v-model="kundeNameSearchString"
          ></v-text-field>
        </v-card-text>
        <v-list-item
          link
          three-line
          router
          :to="{
            path: `/customer-objects/${customer.id}`,
            query: { monthId:customer.month }
          }"
          v-for="customer in filteredCustomerFeed"
          v-bind:key="customer.id"
        >
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
        </v-list-item></v-card
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Customers",
  components: {},
  data() {
    return {
      kundeNameSearchString: "",
      customerFeed: null,
      axiosConfig: {
        headers: {
          Authorization: "Token " + this.$token.getToken()
        }
      }
    };
  },

  mounted() {
    axios
      .get("api/customers/", this.axiosConfig)
      .then(response => {
        this.customerFeed = response.data;
      })
      .catch(error => console.log(error));
  },

  computed: {
    filteredCustomerFeed: function() {
      var customers = this.customerFeed;
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
<style>
.photo {
  list-style: none;
  display: grid;
  grid-template-columns: 200px auto;
  margin-top: 20px;
  align-items: center;
  background-color: #e9edf0;
  padding: 30px 50px;
  border-radius: 5px;
  border: 1px solid #e3e3e3;
}

.author {
  font-size: 25px;
  margin-left: 20px;
  color: #75818e;
}

.photo img {
  border-radius: 5px;
  width: 200px;
}
.input-container {
  border-radius: 5px;
  background: #677482;
  padding: 10px;
}

.input-container input {
  border: none;
  background: transparent;
  color: white;
  padding: 6px 15px;
  font-size: 18px;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #a6b0ba;
  opacity: 1; /* Firefox */
}
</style>
