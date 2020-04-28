<template>
  <v-card>
    <v-container fluid>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="Søk" single-line hide-details></v-text-field>
    </v-container>
    <v-data-table
      :headers="headers"
      :items="objects"
      class="cursor-pointer elevation-3"
      @click:row="selectItem"
      disable-pagination
      hide-default-footer
      :search="search"
    ></v-data-table>
<ObjectDialog :objid="objid" :visibility="dialog=true" />
  </v-card>
</template>
<script>
import ObjectDialog from "../components/ObjectDialog"
export default {
  props: ["objects", "kid", "objid"],
  components: {
    ObjectDialog
  },
  data() {
    return {
      dialog: true,
      search: "",
      selectedItem: null,
      headers: [
        {
          text: "Objekttype",
          align: "start",
          sortable: false,
          value: "fabrikat"
        },
        { text: "Type", value: "type" },
        { text: "Slokketype", value: "slukkemiddel" },
        { text: "Etasje", value: "etg" },
        { text: "Lokasjon", value: "lokasjon" },
        { text: "Plassering", value: "plassering" },
        { text: "Forrige 1-årskontroll", value: "sistekontroll" },
        { text: "Neste 1-årskontroll", value: "nestekontroll" },
        { text: "Forrige 5/11-årskontroll", value: "sisteservice" },
        { text: "Neste 5/10-årskontroll", value: "nesteservice" },
        { text: "Avvik", value: "avvik" },
        { text: "ID", value: "id" }
      ],
      
    };
  },
  methods: {
    objektnavn() {
      return this.object.fabrikat;
    },
    selectItem(item) {
      //console.log("Item selected: " + item.id);
      // with query, resulting in /register?plan=private
      //this.$router.push({
        //path: "../object-details/",
        //query: { objid: item.id, kid: this.kid }
      this.dialog=true;
      this.objid=item.id;
      //});
    }
  }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>