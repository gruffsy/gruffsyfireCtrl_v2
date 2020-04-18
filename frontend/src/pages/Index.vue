<template>
  <div>
    <Navbar />

    <v-container>
      <PrevCustomers />

      <PrevObject class="my-1" />

      <v-card class="my-1 mb-2" flat dark :color="chipColor">
        <v-card-title>
          <div
            v-if="chipColor=='success' || chipColor=='warning'"
          >{{resultCount}} {{filterText}} {{slider}} dager</div>
          <div v-else>{{resultCount}} {{filterText}}</div>
          <v-spacer></v-spacer>
          <v-menu right>
            <template v-slot:activator="{ on }">
              <v-btn dark icon v-on="on">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item v-for="(item, index) in items" :key="index">
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-card-title>
      </v-card>
      <v-chip class="ma-1" color="success" @click="kontrollerte">Kontrollerte</v-chip>
      <v-chip class="ma-1" color="warning" @click="ikkeKontrollerte">Ikke kontrollert</v-chip>
      <v-chip class="ma-1" color="error" @click="kontrollerteAvvik">Avvik</v-chip>
      <v-chip class="ma-1" color="primary" @click="alleTilKontroll">Alle</v-chip>
      <v-chip class="ma-1" color="light">
        <v-icon small>mdi-plus</v-icon>Legg til ny kunde
      </v-chip>
      <div :hidden="sliderHidden">
        <v-slider
          v-model="slider"
          step="10"
          :thumb-size="18"
          thumb-label
          max="740"
          min="0"
          :hidden="sliderHidden"
          @change="getString(selectedFilter)"
        ></v-slider>
      </div><br>
      selectedFilter: {{selectedFilter}} <br>
      filterMonth: {{filterMonth}} <br>
      filterIkkeKontrollerte: {{filterIkkeKontrollerte}} <br>
      filterKontrollerte: {{filterKontrollerte}} <br>
      filterAlle: {{filterAlle}} <br>
      FIlterAvvik: {{FIlterAvvik}}<br>
      <CustomerTable
        :customers="customers"
        :months="months"
        class="my-2"
        @filterMonth="handleFilterMonth"
      />

      <br />
      <br />
      <br />
      <br />
      <br />
    </v-container>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import PrevCustomers from "../components/PrevCustomers";
import PrevObject from "../components/PrevObject";
import CustomerTable from "../components/CustomerTable";
export default {
  name: "Index",
  components: {
    Navbar,
    PrevCustomers,
    PrevObject,
    CustomerTable
  },
  data() {
    return {
      selectedFilter: this.filterIkkeKontrollerte,
      filterMonth: "",
      filterIkkeKontrollerte: this.filterMonth + "&objekter__sistekontroll__lte=",
      filterKontrollerte: this.filterMonth + "&objekter__sistekontroll__gte=",
      filterAlle: this.filterMonth + "&",
      FIlterAvvik: this.filterMonth + "&objekter__avvik=true",
      
      filterText: " er ikke kontrollert på over",
      chipColor: "warning",
      slider: 150,
      sliderHidden: false,
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
      customers: [],
      months: []
    };
  },
  mounted() {
    this.getString(this.filterIkkeKontrollerte);
    this.getMonths();
  },

  methods: {
    handleFilterMonth(event) {
      console.log("data after child handle: ", event); // get the data after child dealing
      this.filterMonth = "month__navn=" + event;
      this.sliderHidden = true;
      this.getString(this.filterMonth);
      console.log(this.filterMonth);
    },
    getMonths() {
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
    ikkeKontrollerte() {
      this.filterText = " er ikke kontrollert på over ";
      this.getString(this.filterIkkeKontrollerte);
      this.sliderHidden = false;
      this.chipColor = "warning";
    },
    kontrollerte() {
      this.filterText = " er kontrollert siste ";
      this.getString(this.filterKontrollerte);
      this.sliderHidden = false;
      this.chipColor = "success";
    },
    alleTilKontroll() {
      this.filterText = " totalt";
      this.sliderHidden = true;
      this.getString(this.filterAlle);
      this.chipColor = "primary";
      console.log(this.strFilter);
    },
    kontrollerteAvvik() {
      this.strFilter = this.FIlterAvvik;
      this.filterText = " er kontrollert med avvik";
      this.sliderHidden = true;
      this.getString(this.FIlterAvvik);
      this.chipColor = "error";
      console.log(this.strFilter);
    },
    getString(filter) {
      var dt = new Date();
      dt.setDate(dt.getDate() - this.slider);
      this.selectedFilter = filter;
      if (!this.sliderHidden)
        filter = filter + dt.toISOString().substring(0, 10);
      this.retrieveCustomers(filter);
    },
    retrieveCustomers(strFilter) {
      this.$dataservice
        .getAllCustomers(strFilter)
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
    resultCount() {
      return this.customers.length + " kunder ";
    },
    returnSlider() {
      return this.slider;
    },
    returnFilterMonth() {
      return this.filterMonth;
    }
  }
};
</script>
<style>
.routerLink {
  text-decoration: none;
  color: white;
}
</style>
