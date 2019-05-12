<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-toolbar app dark color="primary">
    <v-toolbar-title class="headline" @click="goTo('home')">
      <v-btn dark flat>
        {{cookiecutter.project_name}}
        <span class="font-weight-light ml-1">
          <small>v0.1.0</small>
        </span>
      </v-btn>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="pl-5">
      <v-btn flat @click="goTo('home')">Home</v-btn>
      <v-btn flat @click="goTo('about')">About</v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-menu bottom left>
        <template v-slot:activator="{ on }">
          <v-btn dark flat v-on="on">
            <v-icon medium>account_circle</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-tile @click="goTo('profile')">
            <v-list-tile-title>
              <v-icon left>perm_identity</v-icon>
              Profile
            </v-list-tile-title>
          </v-list-tile>
          <v-list-tile @click="goTo('admin')">
            <v-list-tile-title>
              <v-icon left>gavel</v-icon>
              Admin
            </v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>
          <v-list-tile @click="goTo('logout')">
            <v-list-tile-title>
              <v-icon left>exit_to_app</v-icon>
              Logout
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
</template>
<script>
  export default {
    name: 'Navbar',
    data() {
      return {}
    },
    methods: {
      goTo(name) {
        this.$router.push({name})
      }
    },
  }
</script>
