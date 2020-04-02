<template>
  <v-card outlined link route to color="primary" dark>
    <v-list-item three-line dark>
      <v-list-item-content>
        <div class="overline mb-4">Siste kunde</div>
        <v-list-item-title class="headline mb-1"
          >Navn på siste aktive kunde</v-list-item-title
        >
        <v-list-item-subtitle
          >Info om siste kunde evt. siste objekt</v-list-item-subtitle
        >
      </v-list-item-content>

      <v-list-item-avatar tile size="80" color="grey"
        >mdi-account</v-list-item-avatar
      >
    </v-list-item>

    <v-card-actions></v-card-actions>
  </v-card>
</template>
