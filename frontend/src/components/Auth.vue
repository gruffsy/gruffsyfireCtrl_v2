<template>
  <v-container grid-list-md>
    <v-layout row wrap align-center justify-center fill-height>
      <v-flex xs12 sm8 lg4 md5>
        <v-card class="login-card">
          <v-card-title>
            <span class="headline">Logg inn - fireCtrl</span>
          </v-card-title>

          <v-spacer />

          <v-card-text>
            <v-layout row fill-height justify-center align-center v-if="loading">
              <v-progress-circular :size="50" color="primary" indeterminate />
            </v-layout>

            <v-form v-else ref="form" v-model="valid" lazy-validation>
              <v-container>
                <v-text-field
                  v-model="credentials.username"
                  :counter="70"
                  label="brukernavn"
                  :rules="rules.username"
                  maxlength="70"
                  required
                />

                <v-text-field
                  type="password"
                  v-model="credentials.password"
                  :counter="20"
                  label="passord"
                  :rules="rules.password"
                  maxlength="20"
                  required
                />
              </v-container>
              <v-btn class="pink white--text" :disabled="!valid" @click="login">Logg inn</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../router/index";
export default {
  name: "Auth",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    rules: {
      username: [
        v => !!v || "Et brukernavn er påkrevd",
        v => (v && v.length > 3) || "Et brukernavn må være minst 3 tegn",
        v =>
          /^[a-z0-9_]+$/.test(v) ||
          "Et brukernavn kan bare inneholde bokstaver og tall"
      ],
      password: [
        v => !!v || "Passord er påkrevd",
        v => (v && v.length > 6) || "Passordet må være på minst 6 tegn"
      ]
    }
  }),
  methods: {
    login() {
      // checking if the input is valid
      if (this.$refs.form.validate()) {
        this.loading = true;
        axios
          .post("http://localhost:8000/auth/", this.credentials)
          .then(res => {
            this.$session.start();
            this.$session.set("token", res.data.token);
            router.push("/");
          })
          .catch(e => {
            this.loading = false;
            console.log(e);
            swal({
              type: "warning",
              title: "Error",
              text: "Feil brukernavn eller passord",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
          });
      }
    }
  }
};
</script>