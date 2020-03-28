<template>
<v-container v-if="loading">
    <div class="text-xs-center">
      <v-progress-circular
        indeterminate
        :size="150"
        :width="8"
        color="green">
      </v-progress-circular>
    </div>
  </v-container>
<v-container v-else grid-list-xl>
    <v-layout wrap>
      <v-flex xs4
        v-for="(item, index) in subscriptions"
        :key="index"
        mb-2>
        <v-card>
          <v-img
            :src="item.name"
            aspect-ratio="1"
          ></v-img>
<v-card-title primary-title>
            <div>
              <h2>{{item.description}}</h2>
              <div>Year: {{item.name}}</div>
              <div>Type: {{item.currency}}</div>
              
            </div>
          </v-card-title>
<v-card-actions class="justify-center">
            <v-btn flat
              color="green"
              @click="singleMovie(item.name)"
              >View</v-btn>
          </v-card-actions>
</v-card>
      </v-flex>
  </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: "Index",

  data() {
    return {
      subscriptions: []
    };
  },
  methods: {
    all: function() {
      axios
      .get("http://127.0.0.1:8000/api/subscriptions/")
      .then(response => {
        this.subscriptions = response.data;
      });
    }
  },
  created() {
    this.all();
  }
};
</script>