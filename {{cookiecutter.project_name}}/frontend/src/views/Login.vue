<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>{{cookiecutter.project_name}} | Login</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-tooltip bottom>
              <v-btn icon large slot="activator">
                <v-icon large>info</v-icon>
              </v-btn>
              <span>Enter your credentials.</span>
            </v-tooltip>
          </v-toolbar>
          <v-form v-model="valid" ref="form">
            <v-card-text>
              <v-text-field
                v-model="model.username"
                :rules="rules.usernameRules"
                prepend-icon="person"
                label="Username"
                type="text"
                required
              ></v-text-field>
              <v-text-field
                v-model="model.password"
                :rules="rules.passwordRules"
                prepend-icon="lock"
                label="Password"
                type="password"
                required
              ></v-text-field>
            </v-card-text>
            <v-card-actions class="mx-2">
              <span class="group pa-2 error--text" v-if="error">
                Invalid credentials!
              </span>
              <v-spacer></v-spacer>
              <v-btn color="primary" :disabled="!valid" :loading="authenticating" @click="submit">Login</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {mapActions, mapState} from "vuex";

  export default {
    name: 'Login',
    data() {
      return {
        valid: false,
        model: {
          username: '',
          password: ''
        },
        rules: {
          usernameRules: [
            v => !!v || 'Username is required',
          ],
          passwordRules: [
            v => !!v || 'Password is required',
          ]
        },
      }
    },
    methods: {
      ...mapActions('auth', ['login']),

      submit() {
        if (this.$refs.form.validate()) {
          const {username, password} = this.model;
          this.login({username, password})
            .then(() => {
              if (!this.error) {
                this.$router.push({name: 'home'})
              }
            });
        }
      },
    },
    computed: {
      ...mapState('auth', ['authenticating', 'error', 'token']),
    },
  }
</script>
<style>
</style>
