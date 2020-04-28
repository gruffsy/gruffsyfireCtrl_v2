<template>
  
    
  
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card>
      <v-toolbar class="primary darken-2" dark>
        <v-btn icon dark @click.stop="show=false">
          <v-icon x-large>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-container fluid>
     <PickedObject class="my-1" :object="object" />
      <v-card-subtitle>
        <v-btn color="primary" dark class="ma-2" @click="dialog2 = !dialog2">Open Dialog 2</v-btn>
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn class="ma-2" v-on="on">Tool Tip Activator</v-btn>
          </template>
          Tool Tip
        </v-tooltip>

object: {{object}}
        <v-divider></v-divider>
        <Object :object="object" />
      </v-card-subtitle>

      <div style="flex: 1 1 auto;"></div></v-container>
    </v-card>
  </v-dialog>
</template>
<script>
import Object from "../components/Object";
import PickedObject from "../components/PickedObject";

export default {
  name: "ObjectDialog",
  components: {
    Object,
    PickedObject
  },
  props: ["object", "value"],
 
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
   

     
     
    };
  },
  
  computed: {
    
    show: {
      get () {
        return this.value
      },
      set (value) {
         this.$emit('input', value)
      }
    }
  }
};
</script>