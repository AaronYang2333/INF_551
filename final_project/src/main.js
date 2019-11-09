import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import firebase from 'firebase'

import './style/global.css'

Vue.use(ElementUI)

Vue.config.productionTip = false;

const firebaseConfig = {
  apiKey: "AIzaSyDXaJct946h6TGYPrpzsyBkG4BM6o0u7ic",
  authDomain: "ay2333.firebaseapp.com",
  databaseURL: "https://ay2333.firebaseio.com",
  projectId: "ay2333",
  storageBucket: "ay2333.appspot.com",
  messagingSenderId: "833765957318",
  appId: "1:833765957318:web:2a29e5626d380250dc01c7"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

new Vue({
  el: '#app',
  render: h => h(App)
})
