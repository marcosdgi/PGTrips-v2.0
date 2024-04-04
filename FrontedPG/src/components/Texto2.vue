<script setup>

</script>

<template>
  <article id="articulo" class="container-fluid " >
  <div id="fondo">
    <div id="texto2" class="container-fluid  d-flex justify-content-center">
    <h1 class="display-4">
      ¿Qué ventajas tendrás al viajar con nosotros?
    </h1>
</div>
  <div id="ventajas" class="container d-table justify-content-center ">
    <p class="display-6">
      1- Podras viajar cómodamente y rápido
    </p >
    <p class="display-6">
      2- Bajo las condiciones que usted proponga
      </p>
    <p class="display-6">
      3- Gran confort y mucho más
    </p>
</div>
  </div>
</article>
</template>

<style scoped>
#texto2{
  width: 80%;
  margin-bottom: 4%;
  border-radius: 10px ;
}
#ventajas{
  border-radius: 10px;

}
#articulo{
  border-top-left-radius: 90%;
  background-color: rgba(161, 217, 217, 0.06);
  background-image: url("/pngwing.com.png");
  background-repeat: no-repeat;
  background-size: contain ;
  background-position: right  center;
}
#articulo ::before{
  content:"";
  position: absolute;
  opacity: 0.5;
  z-index: -1;
}

</style>