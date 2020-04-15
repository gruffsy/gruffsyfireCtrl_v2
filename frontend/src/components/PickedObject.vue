<template>
  <v-card outlined color="secondary lighten-1" dark>
    <div class="overline ma-2">Siste aktive objekt</div>
    <v-card-title>
      <v-icon x-large class="px-1">mdi-fire-extinguisher</v-icon>
      {{object.fabrikat}} {{object.type}} {{object.lengde}} {{object.slukkemiddel}}
      <v-btn dark icon @click="hidden=!hidden">
        <v-icon v-if="hidden">mdi-menu-down</v-icon>
        <v-icon v-if="!hidden">mdi-menu-up</v-icon>
      </v-btn>

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

    <v-card-subtitle class="mt-2" :hidden="hidden">
      <strong>Plassering: {{object.etg}}. etg => {{object.lokasjon}} => {{object.plassering}}</strong>
      <br />
    </v-card-subtitle>
    <v-card-subtitle :hidden="hidden">
      Forrige 1-årskontroll: {{object.sistekontroll}}
      <br />
      Forrige 5/10-årskontroll: {{object.sisteservice}}
      <br />
      Neste 1-årskontroll: {{object.nestekontroll}}
      <br />
      Neste 5/10-årskontroll: {{object.nesteservice}}
      <br />
    </v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: "PickedObject",
  data() {
    return {
      hidden: false
    };
  },
  props: ["objid", "kid", "object"],
  methods: {},

  mounted() {}
};
</script>
