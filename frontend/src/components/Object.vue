<template>
  <v-card>
    <v-container fluid>
      TODO: Gi nytt navn til besteforeldre-barn metoder
      <p>I am the grand-child: <v-btn color="success" @click="emitToggleEvent">Toggle the value</v-btn></p>
      <form>
        <v-row>
          <!-- Etasje -->
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              label="Etasje"
              v-model="object.etg"
              type="number"
              prepend-icon="mdi-home-floor-1"
            ></v-text-field>
          </v-col>

          <!-- Lokasjon -->
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              label="Lokasjon"
              v-model="object.lokasjon"
              prepend-icon="mdi-home-import-outline"
            ></v-text-field>
          </v-col>

          <!-- Plassering -->
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              label="Plassering"
              prepend-icon="mdi-home-search-outline"
              v-model="object.plassering"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <!-- Slokkervalg -->
          <v-col cols="12" sm="6" md="4">
            <v-select
              :items="extinguishantItems"
              label="Slokker"
              prepend-icon="mdi-fire-extinguisher"
              v-model="object.extinguishant"
              item-text="fabrikat"
              item-value="id"
            >
              <template
                slot="selection"
                slot-scope="data"
              >{{ data.item.fabrikat }} - {{ data.item.type }}</template>
              <template slot="item" slot-scope="data">
                <template>
                  <v-list-item-content>
                    <v-list-item-title v-html="data.item.fabrikat"></v-list-item-title>
                    <v-list-item-subtitle v-html="data.item.type"></v-list-item-subtitle>
                  </v-list-item-content>
                </template>
              </template>
            </v-select>
          </v-col>

          <!-- Produksjonsår -->
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              label="Produksjonsår"
              v-model="object.prodyear"
              prepend-icon="mdi-update"
              type="text"
            ></v-text-field>
          </v-col>

          <!-- Test monthpicker -->
        </v-row>

        <v-row>
          <!-- Siste Service -->
          <v-col cols="12" sm="6" md="4">
            <v-menu
              v-model="prevServiceDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="object.sisteservice"
                  label="Forrige 5/10-årskontroll"
                  prepend-icon="mdi-calendar"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="object.sisteservice"
                @input="prevServiceDateMenu = false"
              ></v-date-picker>
            </v-menu>
          </v-col>

          <!-- Neste Service -->
          <v-col cols="12" sm="6" md="4">
            <v-menu
              v-model="nextServiceDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="object.nesteservice"
                  label="Neste 5/10-årskontroll"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="object.nesteservice"
                @input="nextServiceDateMenu = false"
              ></v-date-picker>
            </v-menu>
          </v-col>

          <!-- Siste kontroll -->
          <v-col cols="12" sm="6" md="4">
            <v-menu
              v-model="prevKontrollDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="object.sistekontroll"
                  label="Forrige 1-årskontroll"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="object.sistekontroll"
                @input="prevKontrollDateMenu = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
        {{ objectInput }}
        <v-btn class="mr-4" @click="updateObject()">Oppdater</v-btn>
        <br />
        {{ message }}
      </form>
    </v-container>
  </v-card>
</template>

<script>
export default {
  props: ["object"],
  data() {
    return {
      extinguishantItems: [],
      message: null,
      checkbox: false,
      prevServiceDateMenu: false,
      prevKontrollDateMenu: false,
      nextServiceDateMenu: false
    };
  },
  
  computed: {
    fromDateDisp() {
      return this.fromDateVal;
      // format/do something with date
    },
    
  },
  created() {
    this.retrieveExtinguishants()
  },
  methods: {
    emitToggleEvent() { this.$emit('toggle-value') },
    submit() {
      this.$v.$touch();
    },
    aktiver() {
      this.status = !this.status;
    },
    updateObject() {
      this.$dataservice
        .updateObject(this.object.id, this.object)
        .then(response => {
          console.log(response.data);
          this.message = "Objektet ble oppdatert!";
          this.emitToggleEvent(); 
          this.dialog = false;
        })
        .catch(e => {
          console.log(e);
          this.message = "Noe gikk forferdelig galt!";
        });
    },
    retrieveExtinguishants() {
      this.$dataservice
        .getAllExtinguishants()
        .then(response => {
          this.extinguishantItems = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  }
};
</script>
