<script setup>
import router from '@/router/index.js'
import {onMounted, ref} from "vue";
import axios from "axios";

function volverLogin() {
  return router.push('/login')
}

const theme = localStorage.getItem('theme')
const usuario = ref({

  username:'',
  apellidos:'',
  password:'',
  password2:'',
  correo:'',

})
const errores = [
  'Su contraseña no coincide',
  'Su correo debe tener el formato correcto, Reviselo',
  'Este campo es obligatorio',
]
const hayErrores = ref(false)
const validarInfo = () => {
  if (usuario.value.password === usuario.value.password) {
    hayErrores.value = false
    return usuario.value
  } else {
    hayErrores.value = true
  }
}
const insertarUsuario = async () => {
  try {
    validarInfo()
    if (hayErrores.value === false) {
      const response = await axios.post('http://localhost:8000/auth/register/', usuario.value)
      console.log(usuario.value)
    } else {
      console.log("Existen errores")
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
</script>

<template>
  <div class="contenedor container-fluid w-25 h-50  justify-content-center d-grid gap-5 ">
    <h1 class="display-5">
      Registrese en nuestro sistema
    </h1>
    <div>
      <form @submit.prevent="insertarUsuario">
        <div class="form-floating">
          <input id="inputNombre" type="text" class="form-control" v-model="usuario.username">
          <label for="inputNombre" class="label">Nombre de Usuario *</label>
          <p class="text-danger" v-if=" usuario.username.length===0 ">{{ errores[2] }}</p>
        </div>
        <div class="form-floating">
          <input id="inputApellido" type="text" class="form-control" v-model="usuario.apellidos">
          <label for="inputApellido" class="label">Apellidos</label>
        </div>
        <div class="form-floating">
          <input id="inputMail" type="email" class="form-control" v-model="usuario.correo">
          <label for="inputMail" class="label">Correo Electrónico *</label>
          <p class="text-danger" v-if="hayErrores">{{ errores[1] }}</p>
          <p class="text-danger" v-if="usuario.correo.length===0">{{ errores[2] }}</p>

        </div>
        <div class="form-floating">
          <input id="inputPass" type="password" class="form-control" v-model="usuario.password">
          <label for="inputPass" class="label" ontoggle="show()">Contraseña</label>
          <p class="text-danger" v-if="usuario.password.length===0">{{ errores[2] }}</p>

        </div>
        <div class="form-floating">
          <input id="inputConfirmPass" type="password" class="form-control" v-model="usuario.password2">
          <label for="inputConfirmPass" class="label" ontoggle="show()">Confirmar Contraseña *</label>
          <p class="text-danger" v-if="hayErrores">{{ errores[0] }}</p>
          <p class="text-danger" v-if="usuario.password2.length===0">{{ errores[2] }}</p>

        </div>
        <input type="submit" class="btnlogin btn btn-primary justify-content-center" value="Aceptar">
        <button class="btnlogin btn btn-primary  justify-content-center" @click="volverLogin">Cancelar</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
input {
  margin-top: 5%;
}

.contenedor {
  margin-top: 5%;
  align-content: center;
  background-color: rgba(0, 139, 139, 0.47);
  padding: 2%;
  border-radius: 10px;
  box-shadow: 10px 10px 10px black;

}

.btnlogin {
  margin-top: 10%;
  margin-right: 10%;

}
</style>