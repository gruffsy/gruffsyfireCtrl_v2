<template>
  <v-card outlined color="primary" dark>
    <v-card-title class="headline mb-1" primary-title>
      <v-icon x-large class="pa-2">mdi-home-city</v-icon>
      {{customer.kunde}}
      <v-btn dark icon @click="hidden=!hidden">
        <v-icon v-if="hidden">mdi-menu-down</v-icon>
        <v-icon v-if="!hidden">mdi-menu-up</v-icon>
      </v-btn>
      <router-link
          :to="{
            path: '/customer-objects/',
            query: {kid: customer.id}
          }"
        >
      <v-btn  class="ml-10" dark icon depressed>
        
        <v-icon x-large>mdi-menu-right</v-icon>
      </v-btn></router-link>
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
</template>

<script>
export default {
  name: "Customer",
  data() {
    return {
      hidden: true,
      customer: []
    };
  },
  props: ["kid", "strFilter"],
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
  mounted() {
    this.retrieveCustomer(this.kid);
  }
};
</script>

