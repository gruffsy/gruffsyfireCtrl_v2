<template>
  <div>
    <v-card
      v-for="customer in prevCustomers"
      :key="customer.id"
      outlined
      color="primary"
      dark
      router
      :to="{
            path: '/customer-objects/',
            query: { kid: customer.customer }
          }"
    >
      <!--TODO: Gjøre om dette til EN component i som kan deles -->
      <v-list-item three-line dark>
        <v-list-item-content>
          <div class="overline mb-4">Siste kunde:</div>
          <v-list-item-title class="headline mb-1">{{customer.kundenavn}} - {{customer.customer}}</v-list-item-title>
          <v-card
            outlined
            color="primary"
            dark
            router
            :to="{
            path: '/customer-objects/',
            query: { kid: customer.id }
          }"
          >
            <v-list-item-subtitle>Siste objekt:</v-list-item-subtitle>
            <v-list-item-subtitle>{{customer.fabrikat}} {{customer.type}} {{customer.slukkemiddel}} {{customer.lengde}} - {{customer.id}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{customer.etg}}. etg -> {{customer.lokasjon}} -> {{customer.plassering}}</v-list-item-subtitle>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "PrevCustomers",

  data() {
    return {
      prevCustomers: null
    };
  },
  created() {
    this.retrievePrevCustomers();
  },
  methods: {
    retrievePrevCustomers() {
      this.$dataservice
        .getPrevCustomers()
        .then(response => {
          this.prevCustomers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  computed: {}
};
</script>
