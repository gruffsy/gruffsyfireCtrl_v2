<template>
  <div>
    <router-link class="routerLink" :to="{
          path: '/'
        }">
      <v-btn class="ml-10" dark icon depressed>
        <v-icon x-large>mdi-menu-left</v-icon>
      </v-btn>
    </router-link>

    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <span class="link" @click.stop="dialog = true" v-on="on">
          <v-icon x-large class="px-1">mdi-home-city</v-icon>
          {{customer.kunde}}
        </span>
      </template>
      <span>{{customer.kunde}}</span>
    </v-tooltip>

    <v-dialog v-model="dialog">
      <Customer style="position: absolute; top: 65px; right: 0; left: 0;" :kid="kid" />
    </v-dialog>
  </div>
</template>

<script>
import Customer from "./Customer";
export default {
  name: "SmallCustomer",
  components: { Customer },
  data() {
    return {
      dialog: false,
      hidden: true,
      customer: [],
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ]
    };
  },
  props: ["kid", "strFilter", "arrow"],
  methods: {
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
    this.retrieveCustomer(this.kid);
  }
};
</script>

<style scoped>
span.link {
  cursor: pointer;
}

</style>