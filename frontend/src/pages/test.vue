<template>
  <div>
      <Navbar />
    <h1>Hello customerw</h1>
    <h2>{{customers}}</h2>
  <h1>Hello objects</h1>
    <h2>{{objects}}</h2>
  </div>
</template>

<script>
import Navbar from "../components/Navbar"


export default {
  name: "test",
  components: {
      Navbar,
  },
  data() {
    return {
      customers: [],
      objects: []
    };
  },
  methods: {
    retrieveCustomers() {
      this.$dataservice.getAllCustomers()
        .then(response => {
          this.customers = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveObjects() {
        this.$dataservice.getAllObjects()
        .then(response => {
            this.objects = response.data;
            console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        })
    }
  },
  mounted() {
    this.retrieveCustomers();
    this.retrieveObjects();
  }
};
</script>