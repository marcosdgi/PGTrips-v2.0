<script setup>
import MiHeader from '@/components/MiHeader.vue'
import Footer from '@/components/Footer.vue'
import Texto2 from '@/components/Texto2.vue'
import Texto1 from '@/components/Texto1.vue'
import {onMounted} from "vue";

const theme = localStorage.getItem('theme')

onMounted(
    () => {
      document.documentElement.setAttribute('data-bs-theme', theme)
      console.log(theme)
    }
)
</script>

<template>

  <MiHeader/>
  <Texto1/>
  <Texto2/>

  <Footer/>
</template>

