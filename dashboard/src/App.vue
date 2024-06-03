<template>
  <v-app>
    <v-layout class="rounded rounded-md">
      <MainSidebar />

      <v-main class="d-flex align-center justify-center">
        <router-view />
      </v-main>
    </v-layout>
  </v-app>
</template>

<script lang="ts">
import MainSidebar from "./components/MainSidebar.vue";

export default {
  components: {
    MainSidebar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
