<template>
<div>
    <router-link class="routerLink"
        :to="{
          path: '/customer-objects/',
          query: { kid: customer.id }
        }"
      >
    {{customer.kunde}}
    </router-link>
</div>
</template>
<script>
export default {
  name: "PrevSmallCustomer",
  data() {
    return {
      customer: [],
      kid: 344,
      hidden: true,
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ],
    };
  },
  methods: {
    async retrievePrevCustomers() {
      let kid;
      this.$dataservice.getPrevCustomers().then(response => {
        kid = response.data[0].customer;
        this.$dataservice.getCustomer(kid).then(response => {
          this.customer = response.data;
          this.kid = kid;
        });
      });
    }
  },

  async mounted() {
    await this.retrievePrevCustomers();
  }
};
</script>

<style scoped>
.routerLink {
  text-decoration: none;
  color: black;
}
</style>
