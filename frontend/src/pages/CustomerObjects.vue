<template>
  <div>
    <Navbar />
    <v-container>
      <br />
      <v-card outlined link route to color="primary" dark>
        <v-list-item three-line dark>
          <v-list-item-content v-for="customer in objects.slice(0, 1)" :key="customer.id">
            <div class="overline mb-4">Siste kunde:</div>
            <v-list-item-title class="headline mb-1">{{customer.kundenavn}} - {{customer.customer}}</v-list-item-title>
            <v-card outlined color="primary" dark router
          :to="{
            path: `/object-details/`,
             query: { customerId: customer.customer,
                      objektid: customer.id }
             }">
            <v-list-item-subtitle>Siste objekt:</v-list-item-subtitle>
            <v-list-item-subtitle>{{customer.fabrikat}} {{customer.type}} {{customer.slukkemiddel}} {{customer.lengde}} - {{customer.id}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{customer.etg}}. etg -> {{customer.lokasjon}} -> {{customer.plassering}}</v-list-item-subtitle>
            </v-card>
          </v-list-item-content>
        </v-list-item>
      </v-card>
      <v-expansion-panels>
        <v-expansion-panel v-for="etg in etgs" :key="etg.id">
          <v-expansion-panel-header>{{etg.etg}}. etg</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list><!-- eslint-disable -->
              <v-list-group v-if="lok.etg == etg.etg" v-for="lok in lokasjons" :key="lok.id">
                <template v-slot:activator>
                  <v-list-item-title>{{lok.lokasjon}}</v-list-item-title>
                </template><!-- eslint-enable -->
<!-- eslint-disable -->
                <v-list-group
                  no-action
                  sub-group
                  v-if="plassering.lokasjon == lok.lokasjon"
                  v-for="plassering in plasserings"
                  :key="plassering.id"
                ><!-- eslint-enable -->
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
            path: `/object-details/${obj.id}`,
            query: { customerId: obj.customer }
          }"
                  >
                    <v-list-item-content><!-- eslint-enable -->
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
import axios from "axios";
export default {
  name: "CustomerObjects",
  components: {
    Navbar
  },
  data() {
    return {
      customer: null,
      etgs: null,
      lokasjons: null,
      plasserings: null,
      objects: [],
      axiosConfig: {
        headers: {
          Authorization: "Token " + this.$token.getToken()
        }
      }
    };
  },
  beforeCreate() {
    this.id = parseInt(this.$route.params.id);
    this.monthId = parseInt(this.$route.query.monthId);
  },
  created() {
    this.getCustomer();
    this.getObjects();
    this.getEtgs();
  },
  methods: {
    getCustomer() {
      axios
        .get("../api/customers/" + this.id + "/", this.axiosConfig)
        .then(res => {
          this.customer = res.data;
        });
    },
    getObjects() {
      axios
        .get("../api/customers/" + this.id + "/objects/", this.axiosConfig)
        .then(res => {
          this.objects = res.data;
        });
    },
    getEtgs() {
      axios
        .get("../api/customers/" + this.id + "/etgs/", this.axiosConfig)
        .then(res => {
          this.etgs = res.data;
        });
      axios
        .get("../api/customers/" + this.id + "/lokasjons/", this.axiosConfig)
        .then(res => {
          this.lokasjons = res.data;
        });
      axios
        .get("../api/customers/" + this.id + "/plasserings/", this.axiosConfig)
        .then(res => {
          this.plasserings = res.data;
        });
    },
    hideIt() {
      this.isHidden = true;
    }
  },
  computed: {}
};
</script>
