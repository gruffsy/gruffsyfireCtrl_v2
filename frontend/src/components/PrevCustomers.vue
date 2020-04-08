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

    <v-card-subtitle>
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
  name: "PrevCustomers",
  data() {
    return {
      customer: [],
      kid: 344
    };
  },
  methods: {
    async retrievePrevCustomers() {
      let kid;
      this.$dataservice.getPrevCustomers().then(response => {
        kid = response.data[0].customer;
        this.$dataservice.getCustomer(kid).then(response => {
          this.customer = response.data;
          this.kid = kid;
        })
      })
    }
  },

  async mounted() {
    await this.retrievePrevCustomers();
    
    
  }
};
</script>
