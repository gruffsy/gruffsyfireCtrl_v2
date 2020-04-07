<template>
  <div>
    <Navbar />
    <v-container grid-list-xs>
      <br />
      <v-card
        outlined
        link
        router
        :to="{
            path: '/customer-objects/',
            query: { kid: customer.id }
          }"
        color="primary"
        dark
      >
        <v-card-title class="headline mb-1" primary-title>
          <v-icon>mdi-home-city</v-icon>
          {{customer.kunde}}
        </v-card-title>

        <v-card-subtitle>
          {{ customer.badresse }},
          <br />
          {{ customer.bpostnr }} {{customer.bpoststed}}
          <br />
          Kontaktperson: {{ customer.kontaktperson }}
          <br />
          tlf: {{ customer.tlf1 }}
          <span v-if="customer.tlf2">/ {{customer.tlf2}}</span>
        </v-card-subtitle>
      </v-card>
      <br />
      <v-spacer></v-spacer>
      
      <Object />

      
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
            <v-card-subtitle>
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

export default {
  name: "ObjectDetails",
  components: {
    Navbar,
    Object
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
      customer: [],
      
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
