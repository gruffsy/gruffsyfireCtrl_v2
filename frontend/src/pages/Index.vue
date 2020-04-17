<template>
  <div>
    <Navbar />

    <v-container>
      <PrevCustomers />

      <PrevObject class="my-1" />
 
     
        <v-card class="my-1 mb-2" flat dark :color="chipColor">
        <v-card-title>
          {{resultCount}} {{filterText}} test
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
       <CustomerTable class="my-2" />

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
      isActive: "prev",
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
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
