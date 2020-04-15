<template>
  <div>
    <Navbar />

    <v-container>
      <PrevCustomers v-if="isActive == 'prev'" />

      <PrevObject class="my-1" v-if="isActive == 'prev'" />
      <v-tabs>
        <v-tab @click="isActive = 'prev'">Siste kunde</v-tab>
        <v-tab @click="isActive = 'search'">Søk kunder</v-tab>
        <v-tab @click="isActive = 'month'">Kontrollmåned</v-tab>
      </v-tabs>
<CustomerTable />
      <Search :hide="hidden" v-if="isActive == 'search'" />

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
import PrevObject from "../components/PrevObject";
import CustomerTable from "../components/CustomerTable"
export default {
  name: "Index",
  components: {
    Navbar,
    Search,
    Month,
    PrevCustomers,
    PrevObject,
    CustomerTable
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
<style>
.routerLink {
  text-decoration: none;
  color: white;
}
</style>
