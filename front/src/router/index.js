import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/verHojas',
    name: 'verHojas',
    component: () => import('../views/verHojas.vue')
  },
  {
    path: '/nueva',
    name: 'Nueva',
    component: () => import('../views/Nueva.vue')
  },
  {
    path: '/hoja/:id',
    name: 'Hoja',
    component: () => import('../views/Hoja.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
