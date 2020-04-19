<template>
  <v-dialog
    v-model="dialog"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card>
      <v-app-bar class="primary darken-2" dark app height="84" hide-on-scroll>
        <v-btn icon dark @click="dialog = false">
          <v-icon x-large>mdi-close</v-icon>
        </v-btn>
      </v-app-bar>
      <PickedObject class="my-1" :kid="kid" :objid="objid" :object="object" />
      <v-card-subtitle>
        <v-btn color="primary" dark class="ma-2" @click="dialog2 = !dialog2">Open Dialog 2</v-btn>
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn class="ma-2" v-on="on">Tool Tip Activator</v-btn>
          </template>
          Tool Tip
        </v-tooltip>

        <v-divider></v-divider>
        <Object :kid="kid" :objid="objid" :object="object" />
      </v-card-subtitle>

      <div style="flex: 1 1 auto;"></div>
    </v-card>
  </v-dialog>
</template>
<script>
import Object from "../components/Object";
import PickedObject from "../components/PickedObject";

export default {
  name: "ObjectDetails",
  components: {
    Object,
    PickedObject
  },
  props: ["objid", "kid"],
  data() {
    return {
      items: [
        {
          title: "Click Me"
        },
        {
          title: "Click Me"
        },
        {
          title: "Click Me"
        },
        {
          title: "Click Me 2"
        }
      ],
      select: [
        { text: "State 1" },
        { text: "State 2" },
        { text: "State 3" },
        { text: "State 4" },
        { text: "State 5" },
        { text: "State 6" },
        { text: "State 7" }
      ],
      dialog: false,

      object: [],
      customer: []
    };
  },
  created() {
    this.retrieveObject(this.objid);
    this.retrieveCustomer(this.kid);
  },
  methods: {
    retrieveObject(id) {
      this.$dataservice
        .getObject(id)
        .then(response => {
          this.object = response.data;
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
  computed: {}
};
</script>