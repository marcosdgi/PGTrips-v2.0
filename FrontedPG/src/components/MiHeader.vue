<template>
<div class="jumbotron animate__animated animate__pulse">
  <div class="container-fluid">
    <div class="contenedorPrincipal d-flex flex-column gap-5 w-75">
    <h1 class="display-3">¡Bienvenido a PGTrips!</h1>

  </div>
  </div>
</div>

</template>

<style scoped>
.jumbotron{

  background-image: url("/header6.jpeg");
  background-size: cover ;
  background-repeat: no-repeat;
  background-position: 0  -450px ;
  padding: 20%;
  overflow: hidden;
  border-radius: 0 0 0 30%;
}
.contenedorPrincipal{
  background-color: rgba(0, 128, 128, 0.79);
  border-radius: 10px;
  text-align: center;
  position: relative;
}
#sub-container{
  background-color: rgba(0, 0, 0, 0.35);
  border-radius: 5px ;
  padding: 3%;
  margin: 0 5%;
}
.jumbotron::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Ajusta el último valor para cambiar la opacidad */
}
</style>
<script setup>

</script>