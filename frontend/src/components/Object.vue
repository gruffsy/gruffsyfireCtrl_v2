<template>
  <v-card>
    <v-container fluid>
      <form>
        <v-row>
          <!-- Etasje -->
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              label="Etasje"
              v-model="object.etg"
              type="number"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Lokasjon -->
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              label="Lokasjon"
              v-model="object.lokasjon"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Plassering -->
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              label="Plassering"
              v-model="object.plassering"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <!-- Slokkervalg -->
          <v-col cols="12" md="4">
            <v-select
              :disabled="status == false"
              :items="extinguishantItems"
              label="Slokker"
              v-model="extInput.extinguishant"
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
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              label="Produksjonsår"
              v-model="object.prodyear"
              type="text"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Test monthpicker -->

          <v-spacer></v-spacer>
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
                  v-model="prevServiceInput.sisteservice"
                  label="Forrige 5/10-årskontroll"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="prevServiceInput.sisteservice"
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
                  v-model="nextServiceInput.nesteservice"
                  label="Neste 5/10-årskontroll"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="nextServiceInput.nesteservice"
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
                  v-model="prevKontrollInput.sistekontroll"
                  label="Forrige 1-årskontroll"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="no-nb"
                no-title
                v-model="prevKontrollInput.sistekontroll"
                @input="prevKontrollDateMenu = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>

        {{prevServiceInput}} date {{date}}
        <v-checkbox
          :disabled="status==false"
          label="Fjernes?"
          @change="$v.checkbox.$touch()"
          @blur="$v.checkbox.$touch()"
        ></v-checkbox>
        <v-checkbox
          v-model="checkbox"
          label="Redigere?"
          @change="aktiver()"
          @blur="$v.checkbox.$touch()"
        ></v-checkbox>
        <v-btn :hidden="status == false" class="mr-4" @click="submit">Oppdater</v-btn>
        <v-btn :hidden="status == false" @click="clear">Avbryt</v-btn>
      </form>
    </v-container>
  </v-card>
</template>

<script>
export default {
  props: ["kid", "objid"],
  data() {
    return {
      date: new Date().toISOString().substr(0, 7),
      menu2: false,
      etg: "1.etasje",
      status: true,
      extinguishantItems: [],
      object: null,
      extinguishantNumber: null,
      extInput: {
        extinguishant: null
      },
      prevServiceInput: {
        sisteservice: new Date().toISOString().substr(0, 7)
      },
      nextServiceInput: {
        nesteservice: new Date().toISOString().substr(0, 7)
      },
      prevKontrollInput: {
        sistekontroll: new Date().toISOString().substr(0, 7)
      },
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
    }
  },
  mounted() {
    this.retrieveExtinguishants();
    this.retrieveObject(this.objid);
  },
  methods: {
    submit() {
      this.$v.$touch();
    },
    aktiver() {
      this.status = !this.status;
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
    },
    retrieveObject(id) {
      this.$dataservice.getObject(id).then(resp => {
        this.object = resp.data;
        this.extInput.extinguishant = resp.data.extinguishant;
        this.prevServiceInput.sisteservice = resp.data.sisteservice;
        this.prevKontrollInput.sistekontroll = resp.data.sistekontroll;
        this.nextServiceInput.nesteservice = resp.data.nesteservice;
      });
    }
  }
};
</script>