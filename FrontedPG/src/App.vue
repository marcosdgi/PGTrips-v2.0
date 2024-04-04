<script >
// import { RouterLink, RouterView } from 'vue-router'
// import Footer from '@/components/Footer.vue'

import {defineComponent, onMounted} from 'vue'
import NavBar from '@/components/NavBar.vue'

export default defineComponent({
  components: { NavBar }
})

const theme = localStorage.getItem('theme')

onMounted(
  ()=>{
    document.documentElement.setAttribute('data-bs-theme', theme)
    console.log(theme)
  }
)

</script>
<template>
<NavBar/>
   <RouterView/>
</template>

<style scoped >
.fade-enter-active, .fade-leave-active {
  transition: opacity 0s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
