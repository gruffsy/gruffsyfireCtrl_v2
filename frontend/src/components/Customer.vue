<template>
  <v-layout align-center justify-center>
  <v-card color="primary" dark>
    <div class="overline ma-2">Aktiv kunde</div>
    <v-card-title class="headline mb-1" primary-title> 
      <v-icon x-large class="px-1">mdi-home</v-icon>
      {{customer.kunde}}
      
      <v-spacer></v-spacer>
      <v-menu top>
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

    <v-card-subtitle :hidden="hidden">
      Trippletex: {{customer.tripletex}}
      <br />
      Adresse: {{customer.badresse}},
      <br />
      Postnr./-sted: {{customer.bpostnr}} {{customer.bpoststed}}
      <br />
      Kontaktperson: {{customer.kontaktperson}}
      <br />
      tlf: {{customer.tlf1}}
      <span v-if="customer.tlf2">/ {{customer.tlf2}}</span>
    </v-card-subtitle>
  </v-card>
  </v-layout>
</template>

<script>
export default {
  name: "Customer",
  data() {
    return {
      hidden: false,
      customer: [],
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
    };
  },
  props: ["kid", "strFilter", "arrow"],
  methods: {
    retrieveCustomer(id) {
      this.$dataservice
        .getCustomer(id)
        .then(response => {
          this.customer = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  created() {
    this.retrieveCustomer(this.kid);
  }
};
</script>

