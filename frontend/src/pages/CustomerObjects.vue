<template>
  <div>
    <Navbar />
    <v-container>
      <Customer :kid="kid" :arrow="arrow" />
      <PrevObject class="my-1" />

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
import Customer from "../components/Customer";
import ObjectTable from "../components/ObjectTable";
import PrevObject from "../components/PrevObject";
export default {
  name: "CustomerObjects",
  components: {
    Navbar,
    Customer,
    ObjectTable,
    PrevObject
  },
  data() {
    return {
      hidden: "table",
      slider: 200,
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
      etgs: null,
      lokasjons: null,
      plasserings: null,
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
    //console.log(this.filterIkkeKontrollerte);
    //console.log("kid what");
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
        (this.retrieveObjects(kid, filter),
        this.retrieveEtgs(kid, filter),
        this.retrieveLokasjons(kid, filter),
        this.retrievePlasserings(kid, filter))
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
<style scoped>
@media print {
    body * {
        visibility: hidden;
        font-size: 20px !important;
    }

    #print, #print * {
        visibility: visible;
        border-bottom: none;
    }

    #title {
        visibility: hidden;
    }

    #print {
        padding: 20px;
        position: fixed;
        height: 100%;
        left: 0;
        top: 0;
    }
}
</style>