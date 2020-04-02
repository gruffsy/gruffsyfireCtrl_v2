<template>
  <div>
    <Navbar />
    
    <v-container>
      <v-tabs>
    <v-tab @click="isActive = 'prev'">Siste kunder</v-tab>
    <v-tab @click="isActive = 'month'">Kontrollmåned</v-tab>
    <v-tab @click="isActive = 'search'">Søk kunder</v-tab>
  </v-tabs>
<br>
      <div id="prev_customer" v-if="isActive == 'prev'">
        
        <v-card outlined link route to class="primary" dark >
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">Siste kunde</div>
              <v-list-item-title class="headline mb-1"
                >Siste aktive kunde</v-list-item-title
              >
              <v-list-item-subtitle
                >Greyhound divisely hello coldly
                fonwderfully</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar tile size="80" color="grey"
              >mdi-account</v-list-item-avatar
            >
          </v-list-item>

          <v-card-actions></v-card-actions>
        </v-card>
      </div>
       
      <Search v-if="isActive == 'search'"/>
       
      <Month v-if="isActive == 'month'"/>

      <br />
      <br />
      <br />
      <br />
      <br />
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "../components/Navbar";
import Search from "../components/Search";
import Month from "../components/Month";
export default {
  name: "Customers",
  components: {
    Navbar,
    Search,
    Month,
  },
  data() {
    return {
      months: [],
      month_detail: [],
      isActive: 'prev',
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
