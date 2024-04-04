<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="/logo2.png" width="45px">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="home">Home</a>
            <transition/>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="reservaciones">Reservaciones
              <transition/>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Ayuda</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/viajes">Mis Viajes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/galeria">Galeria</a>
          </li>


        </ul>
        <!--      BOTON DESPLEGABLE-->
        <div class="dropdown position-absolute end-0 top-0" style="margin-top: 1.2%">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                  aria-expanded="false">
            <img src="/avatar.png" width="20rem">
            {{ usuario }}
          </button>
          <ul class="dropdown-menu animate__animated animate__bounceIn">
            <li><a class="dropdown-item" href="#" @click="toggleTheme">Tema</a></li>

            <li v-if="usuario!=null">
              <button class="dropdown-item" @click="cerrarSesion" href="#">Cerrar Sesión</button>
            </li>
            <li v-if="usuario==null">
              <button class="dropdown-item" @click="iniciarSesion">Iniciar Sesión</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>
<script setup>
import {ref} from 'vue'
import router from "@/router/index.js";
import axios from "axios";


const usuario = localStorage.getItem('username')
const iniciarSesion = () => {
  return router.push('/login')
}
const cerrarSesion = () => {
  localStorage.removeItem('username')
  if (usuario == null) {
    router.push('/login')
  }
}



const toggleTheme = () => {
  const theme = ref(localStorage.getItem('theme'))

  if (!theme.value) {
    localStorage.setItem('theme', 'light')
  }

  if (theme.value === 'light') {
    theme.value = 'dark'
    localStorage.setItem('theme', theme.value)
  } else {
    theme.value = 'light'
    localStorage.setItem('theme', theme.value)
  }

  document.documentElement.setAttribute('data-bs-theme', theme.value)
}

</script>
<style>
.navbar {
  background-color: rgba(161, 217, 217, 0.76);
}

:root {
  --color-background: #fff;
  --color-text: #000;
}

[data-bs-theme="dark"] {
  --color-background: rgba(0, 0, 0, 0.13);
  --color-text: #fff;
}

body {
  background-color: var(--color-background);
  color: var(--color-text);
  transition: background-color 0.5s, color 0.7s;
}
</style>