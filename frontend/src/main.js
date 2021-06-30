import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import infiniteScroll from 'vue-infinite-scroll';
import router from './router';
import store from './store';
import Carousel3d from 'vue-carousel-3d';
import VueScrollReveal from 'vue-scroll-reveal';
import VueAnime from 'vue-animejs';

Vue.config.productionTip = false;
Vue.use(infiniteScroll);
Vue.use(Carousel3d);
Vue.use(VueAnime)
Vue.use(VueScrollReveal, {
  class: 'v-scroll-reveal', // A CSS class applied to elements with the v-scroll-reveal directive; useful for animation overrides.
  duration: 1000,
  scale: 1,
  distance: '10px',
  mobile: false
});

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App)
}).$mount('#app');
