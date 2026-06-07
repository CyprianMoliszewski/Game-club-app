<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <RouterLink class="navbar-brand" to="/">Moje Logo</RouterLink>
      
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Strona Główna</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/games">Gry</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/about">O nas</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/contact">Kontakt</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/login">Zaloguj</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.nav-link.router-link-active {
  font-weight: bold;
  color: #fff !important;
}
</style>