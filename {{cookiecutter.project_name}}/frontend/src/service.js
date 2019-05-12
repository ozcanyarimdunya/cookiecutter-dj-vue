import axios from "axios";
import store from './store';
import router from './router';

export const apiUrl = {
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://127.0.0.1:8000',
  admin: '/admin/',
  getToken: '/get-token/',
  refreshToken: '/refresh-token/',
};


export const session = axios.create({
  baseURL: apiUrl.baseURL,
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
});

session.interceptors.response.use(response => response, error => {
  const {status} = error.response;
  if (status === 401) {/*Unauthorized*/
    store.dispatch('auth/logout')
      .then(() => {
        router.push({name: 'login'})
      });
  }
  return Promise.reject(error);
});

export default {
  login(username, password) {
    return session.post(apiUrl.getToken, {username, password});
  },
  logout() {
    return new Promise((resolve, reject) => resolve());
  },
};
