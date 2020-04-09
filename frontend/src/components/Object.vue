<template>
  <v-card>
    <v-container fluid>
      <form>
        <v-row>
          <v-col cols="12" md="4">
            <!--TODO Hente Extinguishants fra Model-->
            <v-select
              :disabled="status == false"
              :items="extinguishantItems"
              :label="extinguishantSelect"
              v-model="extInput.extinguishant"
              return-object
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
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              :error-messages="emailErrors"
              label="Etasje"
              v-model="object.etg"
              required
              type="number"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <!--TODO Hente Kunder fra Customers-->
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              :error-messages="nameErrors"
              label="Lokasjon"
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              :error-messages="emailErrors"
              label="Plassering"
              required
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              :error-messages="emailErrors"
              label="Produksjonsår"
              v-model="object.prodyear"
              required
              type="number"
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-menu
              v-model="fromDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  label="Forrige 5-/10-årskontroll"
                  v-model="object.sisteservice"
                  :disabled="status == false"
                  readonly
                  :value="fromDateDisp"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="en-in"
                v-model="fromDateVal"
                no-title
                @input="fromDateMenu = false"
                :min="minDate"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols="12" md="4">
            <v-menu
              v-model="fromDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  label="Neste 5-/10-årskontroll"
                  v-model="object.nesteservice"
                  :disabled="status == false"
                  readonly
                  :value="fromDateDisp"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="en-in"
                v-model="fromDateVal"
                no-title
                @input="fromDateMenu = false"
                :min="minDate"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols="12" md="4">
            <v-menu
              v-model="fromDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  label="Forrige 1-årskontroll"
                  v-model="object.sistekontroll"
                  :disabled="status == false"
                  readonly
                  :value="fromDateDisp"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                locale="en-in"
                v-model="fromDateVal"
                no-title
                @input="fromDateMenu = false"
                :min="minDate"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>

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
        {{ test }} - {{extInput}} - {{object}}
        <v-btn :hidden="status == false" class="mr-4" @click="submit">submit</v-btn>
        <v-btn :hidden="status == false" @click="clear">clear</v-btn>
      </form>
    </v-container>
  </v-card>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email },
    select: { required },

    checkbox: {
      checked(val) {
        return val;
      }
    }
  },
  props: ["kid", "objid"],
  data() {
    
    return {
      etg: "1.etasje",
      status: true,
      dbSelect: "",
      items: ["Item 1", "Item 2", "Item 3", "Item 4"],
      extinguishantItems: [],
      object: null,
      extinguishantNumber: null,
      checkbox: false,
      fromDateMenu: false,
      fromDateVal: null,
      minDate: "2020-01-05",
      maxDate: "2019-08-30"
    };
  },

  computed: {
    extInput() {
      return {extinguishant: this.extinguishantNumber}
    },
    fromDateDisp() {
      return this.fromDateVal;
      // format/do something with date
    },
    checkboxErrors() {
      const errors = [];
      if (!this.$v.checkbox.$dirty) return errors;
      !this.$v.checkbox.checked && errors.push("You must agree to continue!");
      return errors;
    },
    selectErrors() {
      const errors = [];
      if (!this.$v.select.$dirty) return errors;
      !this.$v.select.required && errors.push("Item is required");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.maxLength &&
        errors.push("Name must be at most 10 characters long");
      !this.$v.name.required && errors.push("Name is required.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
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

    clear() {
      this.$v.$reset();
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = false;
    },
    retrieveExtinguishants() {
      this.$dataservice
        .getAllExtinguishants()
        .then(response => {
          this.extinguishantItems = response.data;
          console.log(this.extinguishantItems);
        })
        .catch(e => {
          console.log(e);
        });
    },
    retrieveObject(id) {
      this.$dataservice.getObject(id).then(resp => {
        this.object = resp.data;
        this.extinguishantNumber = resp.data.extinguishant;
      });
    }
  }
};
</script>