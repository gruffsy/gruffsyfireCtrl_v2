<template>
  <div>
    <div id="app-instasearch">
      <v-card>
        <v-container fluid>
        <v-row>
           
          <v-col>
            
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Søk"
            single-line
            hide-details
          ></v-text-field></v-col>
          <v-col>
          <v-select
            :items="months"
            v-model="key"
            item-key="id"
            item-text="navn"
            value="id"
            label="Filtrer på måned"
            @change="filterMonth"
          ></v-select></v-col>
          <v-col><br>
            <v-chip bottom small @click="resetMonth()">Nullstill måned</v-chip>
          </v-col></v-row>
        </v-container>
        <v-data-table
          :headers="headers"
          :items="customers"
          item-key="id"
          class="cursor-pointer elevation-3"
          @click:row="selectItem"
          disable-pagination
          hide-default-footer
          :search="search"
          :dense="dense"
        ></v-data-table>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomerTable",
  components: {},
  //props: ["customers", "months",],
  props: {
    customers: { type: Array },
    months: { type: Array }
  },
  data() {
    return {
      value: "I am the child.",
      key: "",
      search: "",
      selectedItem: null,
      dense: false,
      //strFilter: this.str.concat(this.isoDate),
      headers: [
        {
          text: "Kunde",
          align: "start",
          sortable: false,
          value: "kunde"
        },
        { text: "Kontrollmåned", value: "month_navn" },
        { text: "Adresse", value: "badresse" },
        { text: "Postnr", value: "bpostnr" },
        { text: "Poststed", value: "bpoststed" },
        { text: "Tripletex", value: "tripletex" },
        { text: "Kontaktperson", value: "kontaktperson" }
      ]
    };
  },

  mounted() {
    this.$emit("send-message", this.value);
  },
  methods: {
    selectItem(item) {
      console.log("Item selected: " + item.id);
      // with query, resulting in /register?plan=private
      this.$router.push({
        path: "../customer-objects/",
        query: { kid: item.id }
      });
    },
    resetMonth() {
      this.key = null;
      this.filterMonth();
    },
    filterMonth() {
      this.$emit("filterMonth", this.key);
    }
  }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
