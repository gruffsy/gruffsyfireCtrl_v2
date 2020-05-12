<template>
  <div>
    <Navbar :kid="kid"/>
    <v-container>
      <v-card class="my-1 mb-2" flat dark :color="chipColor">
        <v-card-title>
          {{resultCount}} {{filterText}}
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
      </v-card>
      <v-chip class="ma-1" color="success" @click="kontrollerte">Kontrollerte</v-chip>
      <v-chip class="ma-1" color="warning" @click="ikkeKontrollerte">Gjenstår</v-chip>
      <v-chip class="ma-1" color="error" @click="kontrollerteAvvik">Avvik</v-chip>
      <v-chip class="ma-1" color="primary" @click="alleTilKontroll">Alle</v-chip>
      <v-chip class="ma-1" color="light">
        <v-icon small>mdi-plus</v-icon>Legg til nytt objekt
      </v-chip>
      <ObjectTable :objects="objects" :kid="kid" :objid="objid" @updateTable="updateTable" />
    </v-container>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import ObjectTable from "../components/ObjectTable";
export default {
  name: "CustomerObjects",
  components: {
    Navbar,
    ObjectTable,
  },
  data() {
    return {
      slider: 200,
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
      objects: [],
      strFilter: this.filterIkkeKontrollerte,
      filterIkkeKontrollerte: "sistekontroll__lte=",
      filterKontrollerte: "sistekontroll__gte=",
      filterAlle: "",
      filterAvvik: "avvik=true",
      filterText: " gjenstår å kontrollere",
      chipColor: "warning",
      arrow: "true",
      selectedFilter: ""
    };
  },
  props: ["objid", "kid"],
  mounted() {
    this.retrieveAll(this.kid, this.filterIkkeKontrollerte);
    
    },
  methods: {
    updateTable() {
      this.ikkeKontrollerte();
    },
    ikkeKontrollerte() {
      this.filterText = " gjenstår å kontrollere";
      this.chipColor = "warning";
      this.retrieveAll(this.kid, this.filterIkkeKontrollerte);
    },
    kontrollerte() {
      this.filterText = " er kontrollert";
      this.chipColor = "success";
      this.retrieveAll(this.kid, this.filterKontrollerte);
      console.log(this.chipColor);
    },
    alleTilKontroll() {
      this.filterText = " totalt";
      this.chipColor = "primary";
      this.retrieveAll(this.kid, this.filterAlle);
      console.log(this.strFilter);
    },
    kontrollerteAvvik() {
      this.filterText = " er kontrollert med avvik";
      this.chipColor = "error";
      this.retrieveAll(this.kid, this.filterAvvik);
      console.log(this.strFilter);
    },
    retrieveAll(kid, filter) {
      var dt = new Date();
      dt.setDate(dt.getDate() - this.slider);
      this.strFilter = filter;
      if (this.chipColor != "error") {
        filter = filter + dt.toISOString().substring(0, 10);
      }
      console.log(filter);
      [
        (this.retrieveObjects(kid, filter)
        )
      ];
    },
    retrieveObjects(id, strFilter) {
      this.$dataservice
        .getCustomerObjects(id, strFilter)
        .then(response => {
          this.objects = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    hideIt() {
      this.isHidden = true;
    }
  },
  computed: {
    resultCount() {
      return this.objects && this.objects.length + " stk ";
    }
  }
};
</script>
