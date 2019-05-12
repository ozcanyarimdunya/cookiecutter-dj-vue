import Vue from 'vue'
import Router from 'vue-router'
import store from './store';

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login');
      } else {
        next();
      }
    });
};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next('/');
      } else {
        next();
      }
    });
};

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login'));
};

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  linkActiveClass: 'v-btn--active',
  saveScrollPosition: true,
  routes: [
    {
      path: '/',
      redirect: {name: 'home'}
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('./views/Home.vue'),
      beforeEnter: requireAuthenticated,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./views/About.vue'),
      beforeEnter: requireAuthenticated,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login'),
      beforeEnter: requireUnauthenticated,
    },
    {
      path: '/logout',
      name: 'logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '*',
      name: 'error',
      component: () => import('./views/Error'),
      beforeEnter: requireAuthenticated,
    },
  ]
})
