<script setup>
import {onMounted} from "vue";

const prop = defineProps(
  {
    showModal: Boolean
  }, {
    confirmacion: Boolean
  }, {
    abrir: Boolean
  },

)

const emision = defineEmits(['abrir', 'cerrar', 'confirmacion'])

const cerrar = () => {
  emision('cerrar')
}
const confirmar = () => {
  emision('confirmacion')
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
  <div v-if="showModal" class="modal animate__animated animate__bounceIn">
    <div class="modal-content">
      <span @click="cerrar" class="close">&times;</span>
      <h1 class="display-4 text-danger text-center">¿Esta seguro que desea cancelar su viaje ?</h1>
      <div class="d-flex justify-content-center gap-3 m-5 ">
        <button @click="cerrar" class="btn btn-primary w-25">
          No mucho
        </button>
        <button class="btn btn-danger w-25" @click="confirmar">
          Sí, Lo estoy</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  display: flex;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(255, 255, 255, 0);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover
 {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>