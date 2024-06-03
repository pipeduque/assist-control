<template>
  <v-navigation-drawer :width="361">
    <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
    <v-divider></v-divider>
    <v-list-item link title="List Item 1">
      <router-link to="/">Home</router-link>
    </v-list-item>
    <v-list-item link title="List Item 2">
      <router-link to="/about">About</router-link>
    </v-list-item>
  </v-navigation-drawer>
</template>

<script lang="ts">
export default {
  name: "MainSidebar",
  methods: {},
};
</script>

<style></style>
