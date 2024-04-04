import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReservacionView from '@/views/ReservacionView.vue'
import LoginView from '@/views/LoginView.vue'
import RegistroView from '@/views/RegistroView.vue'
import GaleriaView from '@/views/GaleriaView.vue'
import ViajesProgramadosView from '@/views/ViajesProgramadosView.vue'
import EditarReservacionView from '@/views/EditarReservacionView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path:'/reservaciones',
      name: 'reservaciones',
      component:ReservacionView
    },
    {
      path:'/login',
      name:'login',
      component:LoginView
    },
    {
      path:'',
      name:'default',
      component:LoginView
    },
    {
      path:'/registro',
      name:'registro',
      component:RegistroView
    },
    {
      path:'/galeria',
      name:'galeria',
      component: GaleriaView
    },
    {
      path:'/viajes',
      name:'viajes programados',
      component:ViajesProgramadosView
    },
    {
      path: '/editarReservacion/:id',
      name:'editarReservacion',
      component:EditarReservacionView,
      props:true
    }
  ]
})

export default router
