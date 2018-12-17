import Vue from 'vue'
import Router from 'vue-router'

const HomePage = () => import('@/components/HomePage/index');
const Download = () => import('@/components/DownloadPage/index');
const Account = () => import('@/components/AccountPage/index');
const login = () => import('@/components/AccountPage/login');
const sign_in = () => import('@/components/AccountPage/sign_in');
const snapshot = () => import('@/components/VM/snapshot');

Vue.use(Router);

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
      path: '/Download',
      name: 'Download',
      component: Download,
    },
    {
      path: '/login',
      name: 'Login',
      component: login,
    },
        {
      path: '/snapshot',
      name: 'snapshot',
      component: snapshot,
    },
  ]
})
