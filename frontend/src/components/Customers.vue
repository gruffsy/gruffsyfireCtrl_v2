<template>
    <div>
        Customer page
    </div>
</template>

<script>
import router from "../router/index";
export default {
  name: "Movies",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
        this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      }
    }
  }
};
</script>