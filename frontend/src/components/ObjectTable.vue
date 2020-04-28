<template>
  <v-card>
    <v-container fluid>
      <v-btn color="accent" large @click="showScheduleForm=true"></v-btn>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="Søk" single-line hide-details></v-text-field>
    </v-container>
    objid {{returnObjid}} {{object}}
    <v-data-table
      :headers="headers"
      :items="objects"
      class="cursor-pointer elevation-3"
      @click:row="selectItem"
      disable-pagination
      hide-default-footer
      :search="search"
    ></v-data-table>
<ObjectDialog :object="object" :objid="returnObjid" v-model="showScheduleForm" />
  </v-card>
</template>
<script>
import ObjectDialog from "../components/ObjectDialog"
export default {
  props: ["objects", "kid"],
  components: {
    ObjectDialog
  },
  data() {
    return {
      showScheduleForm: false,
      dialog: true,
      search: "",
      selectedItem: null,
      objid: 3391,
      object: [],
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
     
      
      this.retrieveObject(item.id);
      this.showForm();
      
      //});
    },
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
    showForm(){
          this.showScheduleForm=true;
    }
  },
  computed:{
    
    
    
   }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>