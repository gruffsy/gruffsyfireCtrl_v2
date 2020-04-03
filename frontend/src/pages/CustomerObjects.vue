<template>
  <div>
    <Navbar />
    {{ etgs }}
    <v-container>
      <br />
      <v-btn @click="getCustomer">ID:{{ id }}</v-btn>
      <h2>Kunde: {{ customer.kunde }}</h2>
      <h3>Månedsnummer: {{ monthId }}</h3>
      
      <ul>
        <li v-for="etg in etgs" :key="etg.id">Etasje:{{ etg.etg }} 
        <ul><!-- eslint-disable -->
          <li v-if="obj.etg == etg.etg" v-for="obj in objects" :key="obj.id">{{ obj.lokasjon }}</li>
         <!-- eslint-enable -->
        </ul></li>
      </ul>
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
      objects: null,
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
    },
    hideIt() {
      this.isHidden = true;
    }
  },
  computed: {}
};
</script>
