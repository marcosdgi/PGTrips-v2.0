<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '@/router/index.js'

const reservacion = ref({
  'origen': '',
  'destino': '',
  'fecha': '',
  'hora': '',
  'a_nombre_de': Number(localStorage.getItem('user_id'))
})
const realizarReservacion = async () => {
  try {
    const username = localStorage.getItem('username')
    const password = localStorage.getItem('password')
    const id = Number(localStorage.getItem('user_id'))
    if (username && password) {
      const token = btoa(`${username}:${password}`)
      axios.defaults.headers.common['Authorization'] = `Basic ${token}}`
    } else {
      router.push('login/')
    }
    const data = await axios.post(`http://localhost:8000/reservaciones/`, reservacion.value)
    return router.push('/viajes')
  } catch (error) {
    console.error(error)
  }
}
const theme = localStorage.getItem('theme')
onMounted(
  ()=>{
    document.documentElement.setAttribute('data-bs-theme', theme)
  }
)
</script>

<template>
  <article>
    <div id="FormularioReservacion" class="container d-flex justify-content-center w-50 text-sm-center">
      <form @submit.prevent="realizarReservacion">
        <h1 class=" display-4 form-floating mb-4">Agende su viaje, A qué estás esperando?!</h1>
        <div class="d-flex justify-content-center align-items-center flex-column">
          <div class="form-floating mb-3 w-50">
            <input type="text" class="form-control" id="floatingorigen" placeholder="Origen"
                   v-model="reservacion.origen">
            <label for="floatingorigen">Origen</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="text" class="form-control" id="floatingdestino" placeholder="Destino"
                   v-model="reservacion.destino">
            <label for="floatingdestino">Destino</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="date" class="form-control" id="floatingfecha" placeholder="Fecha" v-model="reservacion.fecha">
            <label for="floatingfecha">Fecha</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="time" class="form-control" id="floatinghora" placeholder="Hora" v-model="reservacion.hora">
            <label for="floatinghora">Hora</label>
          </div>

          <div class="form-floating d-flex justify-content-center align-items-center">
            <input type="submit" class="btn btn-primary" value="Reservar">
          </div>
        </div>
      </form>
    </div>
  </article>
</template>

<style scoped>
#FormularioReservacion {
  background-color: rgba(4, 35, 54, 0.45);
  margin-top: 3%;
  padding-top: 3%;
  padding-bottom: 3%;
  border-bottom-right-radius: 3%;
  border-bottom-left-radius: 3%;
  box-shadow: 6px 6px 25px black;

}

#submitReservacion {
  margin-top: 10%;
  margin-bottom: 10%;
}

#tituloReservacion {
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  margin-top: 2%;
  padding: 2% 0;
}
</style>