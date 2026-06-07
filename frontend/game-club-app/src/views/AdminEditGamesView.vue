<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();
</script>

<template>
    <div class="container mt-5">
        <h2>Edycja Gier</h2>
        <p>Tu znajdzie się panel zarządzania grami.</p>
        <button class="btn btn-secondary mt-3" @click="router.push('/admin/main')">Wróć do panelu</button>
    </div>
</template>
