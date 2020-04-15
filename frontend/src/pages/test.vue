<template>
  <div>
    <Navbar />
    {{month}}
    <br />
    {{message}}
    <VBtn color="success" @click="updateO()">text</VBtn>
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
      month: [],
      message: null
    };
  },

  methods: {
    updateO() {
      this.$dataservice
        .updateMonth(1, { navn: "Janu" })
        .then(response => {
          console.log(response.data);
          this.message = "The tutorial was updated successfully!";
        })
        .catch(e => {
          console.log(e);
          this.message = "noe gokk forferdelg galt!";
        });
    },
    retrieveMonth(id) {
      this.$dataservice
        .getMonth(id)
        .then(response => {
          this.month = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveMonth(1);
  }
};
</script>