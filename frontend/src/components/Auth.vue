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
            <v-form ref="form" lazy-validation>
              <v-container>
                <v-text-field
                  v-model="username"
                  :counter="70"
                  label="brukernavn"
                  maxlength="70"
                  required
                />

                <v-text-field
                  type="password"
                  v-model="password"
                  :counter="20"
                  label="passord"
                  maxlength="20"
                  required
                />
              </v-container>
              <v-btn class="pink white--text" @click="login">Logg inn</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
//import router from "../router/index";
export default {
  name: "Auth",
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null
    };
  },
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/auth/", {
          username: this.username,
          password: this.password
        })
        .then(resp => {
          this.token = resp.data.token;
          console.log(this.token);
          localStorage.setItem("user-token", resp.data.token);
          this.$router.push('/');
        })
        .catch(err => {
          localStorage.removeItem("user-token");
          console.log(err);
        });
      //console.log(this.username);
      //console.log(this.password);
    }
  },
};
</script>