import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://94.228.114.254:8000';

const app = createApp(App)

app.config.globalProperties.$axios = axios

app.use(router)
app.mount('#app')
