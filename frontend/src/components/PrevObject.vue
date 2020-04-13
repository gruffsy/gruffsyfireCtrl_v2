<template>
  <v-card outlined color="primary" dark>
    <div class="overline ma-2">Siste objekt</div>
    <v-card-title>
      <v-icon x-large class="px-1">mdi-fire-extinguisher</v-icon>
      {{object.fabrikat}} {{object.type}} {{object.lengde}} {{object.slukkemiddel}}
      <v-btn dark icon @click="hidden=!hidden">
        <v-icon v-if="hidden">mdi-menu-down</v-icon>
        <v-icon v-if="!hidden">mdi-menu-up</v-icon>
      </v-btn>
      <router-link
        :to="{
            path: '/object-details/',
            query: { kid: object.customer, objid: object.id }
          }"
      >
        <v-btn dark icon depressed>
          <v-icon>mdi-menu-right</v-icon>
        </v-btn>
      </router-link>
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
      <v-icon class="pl-4">mdi-home</v-icon> <br/>
      Plassering: {{object.etg}}. etg => {{object.lokasjon}} => {{object.plassering}}
 
      <v-icon class="pl-4">mdi-calendar</v-icon> <br/>
      Forrige 1-årskontroll: {{object.sistekontroll}} <br/>
      Forrige 5/10-årskontroll: {{object.sisteservice}} <br/>
      Neste 1-årskontroll: {{object.nestekontroll}} <br/>
      Neste 5/10-årskontroll: {{object.nesteservice}} <br/>
    </v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: "PrevObject",
  data() {
    return {
      hidden: true,
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
