<template>
 <v-lazy
  :min-height="200"
  :options="{'threshold':0.5}"
  transition="fade-transition">
    <v-container class="animate__animated animate__bounceInDown" style=" border-radius: 30px; margin-top: 10%;">
    <h2 class="primerP" style="font-size: 350%;">
      Quienes Somos?
    </h2>
        <div><p style="font-size: 200%;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, eius iste laboriosam libero
        necessitatibus pariatur quam saepe sapiente ullam? Autem, error iste itaque magnam quisquam sapiente sed soluta
        unde vel!</p></div>
  </v-container>
 </v-lazy>

</template>
<script>
</script>
<style >
v-container {
  display: flex;
  justify-content: center;
  padding: 0 9rem;
  position: fixed;
  border-radius:5px;
}

.primerP {
  text-align: center;
}
</style>
