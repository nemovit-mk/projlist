import Vue from 'vue';
import Vuetify from 'vuetify';
import i18n from "./i18n";
import App from './App.vue';

// import ‘vuetify/dist/vuetify.min.css’

Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
    vuetify : new Vuetify(),
    i18n,
  render: h => h(App),
}).$mount('#app')
