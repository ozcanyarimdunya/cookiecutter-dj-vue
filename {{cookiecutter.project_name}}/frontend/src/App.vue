<template>
  <v-app>
    <nav-bar v-if="isAuthenticated"></nav-bar>
    <v-content>
        <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
  import {mapGetters} from "vuex";
  import NavBar from "@/components/NavBar";

  export default {
    name: 'App',
    components: {
      NavBar
    },
    data() {
      return {}
    },
    computed: {
      ...mapGetters('auth', ['isAuthenticated']),

    },
  }
</script>
