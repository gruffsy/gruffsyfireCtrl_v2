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
            <v-btn dark text>Save</v-btn>
          </v-toolbar-items>
        </v-toolbar>

        object: {{object}}
        <Object :object="object" />
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Object from "../components/Object";
export default {
  name: "test",
  components: {
    Object
  },
  props: ["object", "value"],
  data() {
    return {};
  },

  methods: {},
  mounted() {}
};
</script>