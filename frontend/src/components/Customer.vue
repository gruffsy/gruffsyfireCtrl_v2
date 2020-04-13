<template>
  <v-card
    outlined
    link
    router
    :to="{
            path: '/customer-objects/',
            query: {kid: customer.id}
          }"
    color="primary"
    dark
  >
 
    <v-card-title class="headline mb-1" primary-title>
       <v-icon x-large class="pa-2">mdi-home-city</v-icon>
      {{customer.kunde}}
    </v-card-title>

    <v-card-subtitle hidden=true>
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
      customer: [],
      
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

