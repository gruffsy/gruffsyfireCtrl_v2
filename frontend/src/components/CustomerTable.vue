<template>
  <div>
    <div id="app-instasearch">
      <v-card>
        <v-container fluid>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Søk"
            single-line
            hide-details
          ></v-text-field>
        </v-container>
        <v-data-table
          :headers="headers"
          :items="customers"
          item-key="id"
          class="cursor-pointer elevation-3"
          @click:row="selectItem"
          disable-pagination="true"
          hide-default-footer="true"
          :search="search"
          :dense="dense"
        >
          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">More info about {{ item.name }}</td>
          </template>
        </v-data-table>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomerTable",
  components: {},
  props: ["customers"],
  data() {
    return {
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

  mounted() {},
  methods: {
    selectItem(item) {
      console.log("Item selected: " + item.id);
      // with query, resulting in /register?plan=private
      this.$router.push({
        path: "../customer-objects/",
        query: { kid: item.id }
      });
    }
  }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
