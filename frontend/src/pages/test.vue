<template>
  <div>
    <Navbar />
{{customers}}
  </div>
</template>

<script>
import Navbar from "../components/Navbar";

export default {
  name: "test",
  components: {
    Navbar
  },
  data() {
    return {
      customers: [],
      objects: [],
      customer: null
    };
  },
  props: ["kid"],
  methods: {
    retrieveCustomers() {
      this.$dataservice
        .getAllExtinguishants()
        .then(response => {
          this.customers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveObjects() {
      this.$dataservice
        .getAllObjects()
        .then(response => {
          this.objects = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveCustomer(id) {
      this.$dataservice
        .getCustomer(id)
        .then(response => {
          this.customer = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveCustomers();
    this.retrieveObjects();
    this.retrieveCustomer(this.kid);
  }
};
</script>