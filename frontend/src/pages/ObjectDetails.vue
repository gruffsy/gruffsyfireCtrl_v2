<template>
  <div>
    <Navbar />
    <v-container grid-list-xs>
      <Customer :kid="kid" />
      <PickedObject class="my-1" :kid="kid" :objid="objid" :object="object" />

      <v-row justify="center">
        <v-btn color="primary" class="ma-2" dark @click="dialog = true">Objektdetaljer</v-btn>
        <v-btn color="primary" class="ma-2" dark @click="dialog2 = true">Avvikskontroll</v-btn>
        <v-btn color="error" class="ma-2" dark @click="dialog3 = true">Slett objekt</v-btn>
        <v-menu bottom offset-y>
          <template v-slot:activator="{ on }">
            <v-btn class="ma-2" v-on="on">A Menu</v-btn>
          </template>
          <v-list>
            <v-list-item v-for="(item, i) in items" :key="i" @click="() => {}">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
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

        <v-dialog v-model="dialog2" max-width="500px">
          <v-card>
            <v-card-title>Dialog 2</v-card-title>
            <v-card-subtitle>
              <v-btn color="primary" dark @click="dialog3 = !dialog3">Open Dialog 3</v-btn>
              <v-select :items="select" label="A Select List" item-value="text"></v-select>
            </v-card-subtitle>
            <v-card-actions>
              <v-btn color="primary" text @click="dialog2 = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialog3" max-width="500px">
          <v-card>
            <v-card-title>
              <span>Dialog 3</span>
              <v-spacer></v-spacer>
              <v-menu bottom left>
                <template v-slot:activator="{ on }">
                  <v-btn icon v-on="on">
                    <v-icon>mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item v-for="(item, i) in items" :key="i" @click="() => {}">
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-card-title>
            <v-card-actions>
              <v-btn color="primary" text @click="dialog3 = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Object from "../components/Object";
import Customer from "../components/Customer";
import PickedObject from "../components/PickedObject";

export default {
  name: "ObjectDetails",
  components: {
    Navbar,
    Object,
    Customer,
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
      dialog2: false,
      dialog3: false,
      notifications: false,
      sound: true,
      widgets: false,
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
