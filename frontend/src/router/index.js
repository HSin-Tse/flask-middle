import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  {path: '/', component: 'Home',meta: {title: 'click'}},
  {path: '/about', component: 'About',meta: {title: 'about'}},
  {path: '/page', component: 'Page',meta: {title: 'page'}},
  {path: '/h5click', component: 'H5click',meta: {title: 'H5click'}},
  {path: '/h5page', component: 'H5page',meta: {title: 'h5page'}},
  {path: '*', component: 'NotFound',meta: {title: '404'}}
];
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
});
Vue.use(Router);

const router=new Router({
  routes,
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  // console.log('global beforeEach');
  // console.log(to);
  document.title = to.meta.title
  next();
});
export default router
