import { useAuthStore } from '@/stores/authStore'
import AdminEditGamesView from '@/views/AdminEditGamesView.vue'
import AdminEditNewsletterView from '@/views/AdminEditNewsletterView.vue'
import AdminEditNewsView from '@/views/AdminEditNewsView.vue'
import AdminLoginView from '@/views/AdminLoginView.vue'
import AdminPageView from '@/views/AdminPageView.vue'


import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: AdminLoginView
    },
    {
      path: '/admin/main',
      name: 'AdminDashboard',
      component: AdminPageView,
      meta: { requiresAuth: true, allowedRoles: ['mod', 'worker', 'pr_manager'] }
    },
    {
      path: '/admin/news',
      name: 'AdminEditNews',
      component: AdminEditNewsView,
      meta: { requiresAuth: true, allowedRoles: ['mod', 'pr_manager'] }
    },
    {
      path: '/admin/games',
      name: 'AdminEditGames',
      component: AdminEditGamesView,
      meta: { requiresAuth: true, allowedRoles: ['mod', 'worker'] }
    },
    {
      path: '/admin/newsletter',
      name: 'AdminEditNewsletter',
      component: AdminEditNewsletterView,
      meta: { requiresAuth: true, allowedRoles: [] }
    }





  ],
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      return next('/login');
    }
    
    if (to.meta.allowedRoles) {
      const allowedRoles = to.meta.allowedRoles as string[];
      if (!authStore.hasAccess(allowedRoles)) {
        alert("Brak uprawnień do tej podstrony!");
        return next('/admin/main');
      }
    }
  }
  next();
})


export default router
