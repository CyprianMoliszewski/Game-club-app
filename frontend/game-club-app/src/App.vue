<script setup>
import { ref, onMounted } from 'vue'

const odpowiedz = ref('czekam na odpowiedz z backendu...')

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/test')
    const data = await response.json()

    odpowiedz.value = data.message
  } catch (error) {
    odpowiedz.value = 'blad polaczenia z backendem'
    console.error(error)
  }
})
</script>

<template>
  <div class="container mt-5">
    <h1 class="mb-4">Test endpointu</h1>
    <p>{{ odpowiedz }}</p>
  </div>
</template>

<style>

</style>