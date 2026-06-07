<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBarComponent.vue'
</script>

<template>
  <NavBar />

  <main>
    <RouterView />
  </main>

  <footer class="bg-light text-center py-4 mt-5 border-top">
    <div class="container">
      <p class="mb-0 text-muted">© 2026 Moja Aplikacja. Wszelkie prawa zastrzeżone.</p>
    </div>
  </footer>
</template>

<style>
body {
  background-color: #faf8f9; 
}

a {
  color: #212529;
  text-decoration: none;
}

a:hover {
  color: #495057;
  text-decoration: underline;
}

.text-primary {
  color: #212529 !important; 
}
</style>