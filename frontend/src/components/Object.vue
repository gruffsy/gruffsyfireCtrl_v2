<template>
  <v-card>
    <v-container grid-list-xs>
      
      <form>
        <v-row>
          <v-col cols="12" md="4">
            <!--TODO Hente Extinguishants fra Model-->
            <v-select
              :disabled="status == false"
              v-model="name"
              :error-messages="nameErrors"
              label="Extinguishant TODO: Må hente Extinguishant Model"
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
            ></v-select>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              v-model="email"
              :error-messages="emailErrors"
              label="Etasje"
              required
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <!--TODO Hente Kunder fra Customers-->
            <v-select
              :disabled="status == false"
              v-model="select"
              :items="items"
              :error-messages="selectErrors"
              label="Kundenavn (TODO: Må hentes fra kunde)"
              required
              @change="$v.select.$touch()"
              @blur="$v.select.$touch()"
            ></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              v-model="name"
              :error-messages="nameErrors"
              :counter="10"
              label="Lokasjon"
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              :disabled="status == false"
              v-model="email"
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
              v-model="select"
              :items="items"
              :error-messages="selectErrors"
              label="Produksjonsår"
              type="number"
              required
              @change="$v.select.$touch()"
              @blur="$v.select.$touch()"
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
                  placeholder="Forrige 5-/10-årskontroll"
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
                  placeholder="Neste 5-/10-årskontroll"
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
                  placeholder="Forrige 1-årskontroll"
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
          v-model="deleted"
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
        {{ status }}
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

  data: () => ({
    status: false,
    name: "",
    email: "",
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
    fromDateMenu: false,
    fromDateVal: null,
    minDate: "2020-01-05",
    maxDate: "2019-08-30"
  }),

  computed: {
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
    }
  }
};
</script>