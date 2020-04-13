<template>
  <v-card
    outlined
    link
    router
    :to="{
            path: '/object-details/',
            query: { kid: object.customer, objid: object.id }
          }"
    color="primary"
    dark
  >
    <v-card-title dense>
      <v-icon x-large class="pa-2">mdi-fire-extinguisher</v-icon>
      {{object.fabrikat}} {{object.type}} {{object.lengde}} {{object.slukkemiddel}}
    </v-card-title>

    <v-card-subtitle hidden=true><v-icon class="pl-4">mdi-home</v-icon>
        Plassering: {{object.etg}}. etg => {{object.lokasjon}} => {{object.plassering}}</v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: "PrevObject",
  data() {
    return {
      object: []
    };
  },
  props: ["objid", "kid"],
  methods: {
    async retrievePrevObject() {
      this.$dataservice.getPrevCustomers().then(response => {
        this.object = response.data[0];
      });
    }
  },

  mounted() {
    this.retrievePrevObject();
  }
};
</script>
