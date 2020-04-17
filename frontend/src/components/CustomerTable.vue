<template>
  <div>
    <div id="app-instasearch">
      <v-card>
        <v-container fluid>
          
          
          <v-chip class="ma-1" color="error" @click="getString">Ikke kontrollert på {{slider}} dager</v-chip>
          {{strFilter}} {{resultCount}}
          <v-slider
          v-model="slider"
          step="10"
          :thumb-size="18"
          thumb-label
          max="740"
          min="0"
          @change="getString"
        ></v-slider>
          
          
          
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
  data() {
    return {
      search: "",
      selectedItem: null,
      dense: false,
      strFilter: "",
      kontrollerteKunder: "objekter__sistekontroll__lte=",
      slider: 150,
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
      ],

      kundeNameSearchString: "",
      customers: []
    };
  },

  mounted() {
    
    this.getString();
  },
  methods: {
      getString() {
         var dt = new Date();
         dt.setDate( dt.getDate() - this.slider );
         this.strFilter = this.kontrollerteKunder + dt.toISOString().substring(0, 10);
         this.retrieveCustomers(this.strFilter);
      },
    selectItem(item) {
      console.log("Item selected: " + item.id);
      // with query, resulting in /register?plan=private
      this.$router.push({
        path: "../customer-objects/",
        query: { kid: item.id }
      });
    },
    retrieveCustomers(strFilter) {
      this.$dataservice
        .getAllCustomers(strFilter)
        .then(response => {
          this.customers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  computed: {
    resultCount() {
      return this.customers && this.customers.length + " stk ";
    }
  }
  
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
