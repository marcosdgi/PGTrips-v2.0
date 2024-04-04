<script setup>
import router from '@/router/index.js'
import axios from 'axios'
import {onMounted, ref} from 'vue'

function volver() {
  return router.push('/viajes')
}
const reservacion = ref({
  'origen':'',
  'destino':'',
  'fecha':'',
  'hora':''
})
// const route = useRouter()
const id = Number(router.currentRoute.value.params.id)

const actualizarReservacion = async (id) =>{
  try{

    const data = await axios.put(`http://localhost:8000/reservaciones/${id}`,reservacion.value)
    console.log(data)
    return router.push('/viajes')
  }catch (error){
    console.error(error)
  }
}

const theme = localStorage.getItem('theme')

onMounted(
  ()=>{
    document.documentElement.setAttribute('data-bs-theme', theme)
    console.log(theme)
  }
)
</script>

<template>
  <div class="container-fluid d-flex justify-content-center w-50">
    <div class="justify-content-center ">
      <h1 class="display-4 form-floating mb-4">Edite su Reservacion </h1>
      <form @submit.prevent="actualizarReservacion(id)">
        <div class="container d-flex flex-column align-items-center">
          <div class="form-floating mb-3 w-50">
            <input type="text" class="form-control" id="floatingOrigen" v-model="reservacion.origen" placeholder="Origen">
            <label for="floatingInput">Origen</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="text" class="form-control" id="floatingDestino" placeholder="Destino" v-model="reservacion.destino">
            <label for="floatingDestino">Destino</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="Date" class="form-control" id="floatingFecha" placeholder="Fecha" v-model="reservacion.fecha">
            <label for="floatingFecha">Fecha</label>
          </div>
          <div class="form-floating mb-3 w-50">
            <input type="time" class="form-control" id="floatingHora" placeholder="Hora" v-model="reservacion.hora">
            <label for="floatingHora">Hora</label>
          </div>
        </div>
        <div class="container d-flex justify-content-center gap-5">
          <input type="submit" value="Actualizar" class="btn btn-primary">
          <button class="btn btn-danger" @click="volver">Cancelar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.container-fluid {
  margin-top: 5%;
  background-color: rgba(0, 139, 139, 0.33);
  padding: 2%;
  border-radius: 10px;
  box-shadow: 8px 8px 25px black;
}
.container{
  margin-top: 2%;
}

</style>