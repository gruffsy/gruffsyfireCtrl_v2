<template>
  <div>
      <Navbar />
    <v-container grid-list-xs>
        <h1>KundeID: {{customerId}}</h1>
        <h2>Objekt ID: {{ id }}</h2>
    
    <v-row justify="center">
      <v-btn color="primary" class="ma-2" dark @click="dialog = true">Open Dialog 1</v-btn>
      <v-btn color="primary" class="ma-2" dark @click="dialog2 = true">Open Dialog 2</v-btn>
      <v-btn color="primary" class="ma-2" dark @click="dialog3 = true">Open Dialog 3</v-btn>
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
        <v-card tile>
          <v-toolbar flat dark color="primary">
            <v-btn icon dark @click="dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Settings</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="dialog = false">Save</v-btn>
            </v-toolbar-items>
            <v-menu bottom right offset-y>
              <template v-slot:activator="{ on }">
                <v-btn dark icon v-on="on">
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item v-for="(item, i) in items" :key="i" @click="() => {}">
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-toolbar>
          <v-card-text>
            <v-btn color="primary" dark class="ma-2" @click="dialog2 = !dialog2">Open Dialog 2</v-btn>
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-btn class="ma-2" v-on="on">Tool Tip Activator</v-btn>
              </template>
              Tool Tip
            </v-tooltip>
            <v-list three-line subheader>
              <v-subheader>User Controls</v-subheader>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Content filtering</v-list-item-title>
                  <v-list-item-subtitle>Set the content filtering level to restrict apps that can be downloaded</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Password</v-list-item-title>
                  <v-list-item-subtitle>Require password for purchase or use password to restrict purchase</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-list three-line subheader>
              <v-subheader>General</v-subheader>
              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="notifications"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Notifications</v-list-item-title>
                  <v-list-item-subtitle>Notify me about updates to apps or games that I downloaded</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="sound"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Sound</v-list-item-title>
                  <v-list-item-subtitle>Auto-update apps at any time. Data charges may apply</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="widgets"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Auto-add widgets</v-list-item-title>
                  <v-list-item-subtitle>Automatically add home screen widgets</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>

          <div style="flex: 1 1 auto;"></div>
        </v-card>
      </v-dialog>

      <v-dialog v-model="dialog2" max-width="500px">
        <v-card>
          <v-card-title>Dialog 2</v-card-title>
          <v-card-text>
            <v-btn color="primary" dark @click="dialog3 = !dialog3">Open Dialog 3</v-btn>
            <v-select :items="select" label="A Select List" item-value="text"></v-select>
          </v-card-text>
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
    </v-row> </v-container>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import axios from "axios";
export default {
  name: "ObjectDetails",
  components: {
    Navbar
  },
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
      customer: null,
      etgs: null,
      lokasjons: null,
      plasserings: null,
      objects: [],
      axiosConfig: {
        headers: {
          Authorization: "Token " + this.$token.getToken()
        }
      }
    };
  },
  beforeCreate() {
    this.id = parseInt(this.$route.params.id);
    this.customerId = parseInt(this.$route.query.customerId);
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
      axios
        .get("../api/customers/" + this.id + "/lokasjons/", this.axiosConfig)
        .then(res => {
          this.lokasjons = res.data;
        });
      axios
        .get("../api/customers/" + this.id + "/plasserings/", this.axiosConfig)
        .then(res => {
          this.plasserings = res.data;
        });
    },
    hideIt() {
      this.isHidden = true;
    }
  },
  computed: {}
};
</script>
