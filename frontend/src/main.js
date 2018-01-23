import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
// Vue.use(ElementUI)
Vue.use(ElementUI, { locale })

Vue.config.productionTip = true


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
