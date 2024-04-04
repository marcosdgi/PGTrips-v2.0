<script setup>
import router from '@/router/index.js'
import axios from "axios";
import {onMounted, ref} from "vue";
function irRegistro(){
  return router.push('/registro')
}


const credenciales = ref(
    {
      'username':'',
      'password':''
    }
)
const autenticacion = async ()=>{
  let response
  try{
     response = await axios.post('http://localhost:8000/auth/login/',{
    'username':credenciales.value.username,
    'password':credenciales.value.password
})
    const token =  response.data
    localStorage.setItem('username', token['username'])
    localStorage.setItem('password', token['password'])
    localStorage.setItem('user_id', token['id'])


  if(response.status===200){
      await router.push('/home')
      return true
    }
  }catch (response){
    return false
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
<div class="contenedor container-fluid w-25   justify-content-center d-grid gap-5 ">
  <h1>
    Iniciar Sesión
  </h1>
  <div>
    <form @submit.prevent="autenticacion">
      <div class="form-floating justify-content-center">
        <input id="inputUser" type="text" class="form-control" v-model="credenciales.username">
      <label for="inputUser" class="label">Usuario</label>
      </div>
      <div class="form-floating">
        <input id="inputPass" type="password" class="form-control" v-model="credenciales.password">
      <label for="inputPass" class="label">Contraseña</label>
      </div>
      <input type="submit" class="btnlogin btn btn-primary justify-content-center" @click="iniciarSesion" value="Aceptar">

      <button class="btnlogin btn btn-primary justify-content-center" @click="irRegistro" >Registro</button>
    </form>
  </div>
</div>
</template>

<style scoped>
#inputPass{
  margin-top: 5%;
}
.contenedor{
    margin-top: 10%;
    align-content: center;
    background-color: rgba(0, 139, 139, 0.49);
    padding: 2%;
      border-radius: 10px;
  box-shadow: 10px 10px 10px black;
}
.btnlogin{
  margin-top: 10%;
  margin-right: 10%;

}
</style>