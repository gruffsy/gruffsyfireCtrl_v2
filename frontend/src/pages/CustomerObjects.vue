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
      <v-tabs>
        <v-tab @click="hideTable">Pr. etasje</v-tab>
        <v-tab @click="hideEtg">Tabell</v-tab>
      </v-tabs>
      <ObjectTable :hidden="hidden=='table'" :objects="objects" :kid="kid" :objid="objid" />
      <v-expansion-panels :hidden="hidden=='etg'">
        <v-expansion-panel v-for="etg in etgs" :key="etg.id">
          <v-expansion-panel-header>{{etg.etg}}. etg</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list>
              <!-- eslint-disable -->
              <v-list-group v-if="lok.etg == etg.etg" v-for="lok in lokasjons" :key="lok.id">
                <template v-slot:activator>
                  <v-list-item-title>{{lok.lokasjon}}</v-list-item-title>
                </template>
                <!-- eslint-enable -->
                <!-- eslint-disable -->
                <v-list-group
                  no-action
                  sub-group
                  v-if="(plassering.lokasjon == lok.lokasjon) & 
                  (plassering.etg == etg.etg)"
                  v-for="plassering in plasserings"
                  :key="plassering.id"
                >
                  <!-- eslint-enable -->
                  <template v-slot:activator>
                    <v-list-item-content>
                      <v-list-item-title>{{plassering.plassering}}</v-list-item-title>
                    </v-list-item-content>
                  </template>
                  <!-- eslint-disable -->
                  <v-list-item
                    v-if="(obj.etg == etg.etg) &
                          (obj.lokasjon == lok.lokasjon) &
                          (obj.plassering == plassering.plassering)"
                    v-for="obj in objects"
                    :key="obj.id"
                    link
                    :to="{
            path: '/object-details/',
            query: { kid: obj.customer, objid: obj.id }
          }"
                  >
                    <v-list-item-content>
                      <!-- eslint-enable -->
                      <v-list-item-title x-large>
                        <v-list-item-icon>
                          <v-icon x-large>mdi-fire-extinguisher</v-icon>
                        </v-list-item-icon>
                        {{obj.fabrikat}} {{obj.type}} {{obj.slukkemiddel}} {{obj.lengde}}
                      </v-list-item-title>
                      <v-list-item-subtitle>Objektnr. {{obj.id}}</v-list-item-subtitle>
                      <v-list-item-subtitle>Produksjonsår: {{obj.prodyear}}</v-list-item-subtitle>
                      <v-list-item-subtitle>Forrige 1-årskontroll: {{obj.sistekontroll}}</v-list-item-subtitle>
                      <v-list-item-subtitle>Forrige 5-/10-årskontroll: {{ obj.sisteservice }}</v-list-item-subtitle>
                      <v-list-item-subtitle>Neste 5-/10-årskontroll: {{ obj.nesteservice }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-group>
              </v-list-group>
            </v-list>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
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
    hideTable() {
      this.hidden = "table";
    },
    hideEtg() {
      this.hidden = "etg";
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
    retrieveEtgs(id, strFilter) {
      this.$dataservice
        .getEtgs(id, strFilter)
        .then(response => {
          this.etgs = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveLokasjons(id, strFilter) {
      this.$dataservice
        .getLokasjons(id, strFilter)
        .then(response => {
          this.lokasjons = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrievePlasserings(id, strFilter) {
      this.$dataservice
        .getPlasserings(id, strFilter)
        .then(response => {
          this.plasserings = response.data;
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
