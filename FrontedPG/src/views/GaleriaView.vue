<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";

const theme = localStorage.getItem('theme')
const cars = ref([])
const obtenerAutos = async () => {
  try {
    const username = localStorage.getItem('username')
    const password = localStorage.getItem('password')
    const id = Number(localStorage.getItem('user_id'))
    if (username && password) {
      const token = btoa(`${username}:${password}`)
      axios.defaults.headers.common['Authorization'] = `Basic ${token}}`
      const response = await axios.get('http://localhost:8000/galeria/autos/')
      cars.value = response.data
    }
  } catch (e) {
    console.error(e)
  }
}
onMounted(
    () => {
      document.documentElement.setAttribute('data-bs-theme', theme)
      console.log(theme)
    }
)
onMounted(
    () => {
      obtenerAutos()
    }
)
</script>

<template>
  <div class=" d-flex justify-content-center gap-3 text-center " style="margin-top: 1.5%; margin-bottom: 1%">

    <div class="d-flex justify-content-center flex-wrap gap-3 ">
      <div class="card d-flex" v-for="car in cars" :key="car.id">
        <img :src="'http://localhost:8000'+ car.Imagen" class="card-img-top" style="width: 20rem">
        <div class="card-body">
          <h5 class="card-title">{{ car.modelo }}</h5>
          <p class="card-text"> {{ car.placa }} </p>
          <p class="card-text"><small class="card-text">{{ car.km_recorridos }} km recorridos</small></p>
          <p class="card-text"><small class="text-body-secondary">En nuestro sistema desde {{
              car.fecha_annadido
            }}</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  transition: box-shadow .3s;
  margin-top: 5%;
}

.card:hover {
  box-shadow: 8px 8px 20px black;
}
</style>