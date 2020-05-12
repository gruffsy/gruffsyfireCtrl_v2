<template>
  <v-card>
    <v-container>
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

    <ObjectDialog 
    :object="object" 
    v-on="$listeners"
    v-model="dialog"/>

  </v-card>
</template>
<script>
import ObjectDialog from "../components/ObjectDialog";
export default {
  props: ["objects", "kid"],
  components: {ObjectDialog},
  data() {
    return {
      object: [],
      objid: 123,
      dialog: false,
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
      ]
    };
  },
  methods: {
    retrieveObject(id) {
      this.$dataservice
        .getObject(id)
        .then(response => {
          this.object = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    objektnavn() {
      return this.object.fabrikat;
    },
    selectItem(item) {
      console.log("Item selected: " + item.id);

      /*this.$router.push({
        path: "../object-details/",
        query: { objid: item.id, kid: this.kid }
      });*/

      this.objid = item.id;
      this.retrieveObject(item.id);
      this.dialog = true;
    }
  }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>

