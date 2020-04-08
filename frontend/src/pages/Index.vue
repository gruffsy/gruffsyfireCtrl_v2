<template>
  <div>
    <Navbar />

    <v-container>
      
      
      <br />
      
      <PrevCustomers v-if="isActive == 'prev'"/>
      <br>
      <v-tabs>
        <v-tab @click="isActive = 'prev'">Siste kunde</v-tab>
        <v-tab @click="isActive = 'search'">Søk kunder</v-tab>
        <v-tab @click="isActive = 'month'">Kontrollmåned</v-tab>
      </v-tabs>
      <br />
      <Search v-if="isActive == 'search'" />

      <Month v-if="isActive == 'month'" />

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
import Search from "../components/Search";
import Month from "../components/Month";
import PrevCustomers from "../components/PrevCustomers";

export default {
  name: "Index",
  components: {
    Navbar,
    Search,
    Month,
    PrevCustomers,
    
  },
  data() {
    return {
      isActive: "prev"
    };
  },
  created() {},

  methods: {},
  computed: {}
};
</script>
