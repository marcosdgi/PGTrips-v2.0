import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'animate.css'
import {Dropdown} from 'bootstrap'

const app = createApp(App)
app.use(router)
app.mount('#app')

document.querySelectorAll('.dropdown-toggle').forEach(dropdown => {
    new Dropdown(dropdown)
})

