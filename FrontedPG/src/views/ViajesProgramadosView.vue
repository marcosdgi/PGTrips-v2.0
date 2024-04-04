<script setup>

import { ref, onMounted } from 'vue'
import axios from 'axios'
import router from '@/router/index.js'
import Model from '@/components/Model.vue'

const reservaciones = ref([])

const obtenerReservaciones = async () => {
  try {
const username = localStorage.getItem('username')
    const password = localStorage.getItem('password')
    const id = Number(localStorage.getItem('user_id'))
    if (username && password) {
      const token = btoa(`${username}:${password}`)
      axios.defaults.headers.common['Authorization'] =`Basic ${token}}`
}else{
      router.push('login/')
    }
    const response = await axios.get('http://localhost:8000/reservaciones/')
    reservaciones.value = response.data

  } catch (error) {
    console.error(error)
  }
}
onMounted(() => {
  obtenerReservaciones()

})
const theme = localStorage.getItem('theme')

onMounted(
  ()=>{
    document.documentElement.setAttribute('data-bs-theme', theme)
    console.log(theme)
  }
)
const showModal = ref(false)

const cerrarModal = () => {
  showModal.value = false
}
const abrirModal = () => {
  showModal.value = true
}

function editarReservacion(id) {
  return router.push(`editarReservacion/${id}`)
}

//
const eliminarReservacion = async (id) => {
  try {
    const response = await axios.delete(`http://localhost:8000/reservaciones/${id}`)
    showModal.value=false
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}
const refresh = () =>{
  location.reload()
}
</script>

<template>
  <header class="d-flex justify-content-center gap-5 ">
    <input id="buscar" type="text" class="form-control d-flex text-bg-success" placeholder="Buscar...">
    <button @click="refresh" class="btn ">
      <img src="/refresh.png" width="30rem">

    </button>
  </header>
  <section class="container d-flex flex-wrap gap-3 animate__animated animate__pulse"
           style="margin-top: 5%">
    <div class="d-flex justify-content-center" v-for="reservacion in reservaciones" :key="reservacion.id">
      <div class="card " style="width: 18rem;">
        <div class="card-body text-bg-success">
          <h5 class="card-title">Reservacion {{ reservacion.id_reservacion }}</h5>

        </div>
        <ul class="list-group list-group-flush">
          <div class="p-2 ">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Origen: {{ reservacion.origen }}</li>
              <li class="list-group-item">Destino: {{ reservacion.destino }}</li>
              <li class="list-group-item">Fecha: {{ reservacion.fecha }}</li>
              <li class="list-group-item">Hora: {{ reservacion.hora }}</li>
            </ul>
          </div>
          <li class="list-group-item">
            <button id="btnEdit" class="btn " @click="editarReservacion(reservacion.id_reservacion)">
              <img class="animate__animated animate__bounce" style="--animate-duration: 1.4s;" src="/edit.png"
                   width="20rem">
              Editar
            </button>
            <button class="btn text-danger" @click="abrirModal"
            ><img
              class="animate__animated animate__bounce" style="--animate-duration: 1.4s;"
              src="/eliminar.jpg" width="20rem"> Eliminar
            </button>
            <Model :show-modal="showModal" @abrir="abrirModal" @cerrar="cerrarModal"
                   @confirmacion="eliminarReservacion(reservacion.id_reservacion)" />
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
#buscar {
  width: 10%;
}

.card {
  transition: box-shadow .3s;
}

.card:hover {
  box-shadow: 8px 8px 20px black;
}

section {
  margin-bottom: 5%;
}
</style>