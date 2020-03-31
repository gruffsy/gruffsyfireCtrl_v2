<template>
  <div>
    <Navbar />

    <v-container>
      <br />
      <v-btn @click="getCustomer">ID:{{ id }}</v-btn>
      <h2>Kunde: {{ customer.kunde }}</h2>
      <h3>Månedsnummer: {{ monthId }} </h3>
      <v-expansion-panels focusable>
        <v-expansion-panel v-if="customer.length < 0" v-for="obj in customer" :key="obj.id">
          <v-expansion-panel-header>{{ obj.kunde }}. Etage</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list>
              <v-list-group>
                <template v-slot:activator>
                  <v-list-item-title>Lokasjon</v-list-item-title>
                </template>
                <v-list-group no-action sub-group>
                  <template v-slot:activator>
                    <v-list-item-content>
                      <v-list-item-title>Plassering</v-list-item-title>
                    </v-list-item-content>
                  </template>
                  <v-list-item link three-line router to="/object-details">
                    <v-list-item-content>
                      <v-list-item-icon>
                        <v-icon>mdi-fire-extinguisher</v-icon>
                      </v-list-item-icon>
                      <v-list-item-title>Objekt</v-list-item-title>
                      <v-list-item-subtitle>hei på deg</v-list-item-subtitle>
                      <v-list-item-subtitle>hei på deg</v-list-item-subtitle>
                      <v-list-item-subtitle>hei på deg</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-group>
              </v-list-group>
            </v-list>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      <br />
      <br />
      <br />
      <br />
      <br />
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
      isHidden: false,
      customer: [],
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
  },
  methods: {
    getCustomer() {
      axios.get("../api/customers/" + this.id + "/", this.axiosConfig)
      .then(res => {
        this.customer = res.data;
      });
    },
    hideIt() {
      this.isHidden = true;
    }
  },
  computed: {}
};
</script>