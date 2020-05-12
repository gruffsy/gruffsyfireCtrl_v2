<template>
  <div>
    <v-dialog
      :value="value"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
      @input="$emit('input')"
    >
      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click.native="$emit('input')">
            <v-icon>mdi-close</v-icon>
          </v-btn>

          <v-toolbar-title>TESTMODAL DIALOG!!!!</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            
          </v-toolbar-items>
        </v-toolbar>
        
        <Object 
        :object="object"
        v-on="$listeners"
        />
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Object from "../components/Object";
export default {
  name: "ObjectDialog",
  components: {
    Object
  },
  props: ["object", "value"],
  data() {
    return {};
  },

  methods: {
    
  },
  mounted() {}
};
</script>