import { createRouter, createWebHistory } from 'vue-router'
import ListCards from '@/views/ListCards.vue'

const routes = [
  {
    path: '/',
    name: 'ListCards',
    component: ListCards
  },
  {
    path: '/camera/:id',
    name: 'DetailedCard',
    component: () => import('@/views/DetailedCard'),
    props: true,
  },
  {
    path: '/job-report/:id',
    name: 'JobReport',
    component: () => import('@/views/JobReport'),
    props: true,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
// path: `/camera/${itemData.id}`,

// path: `/job-report/${job.id}`,
