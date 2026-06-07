<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const goTo = (path: string) => {
    router.push(path);
};

const handleLogout = () => {
    authStore.logout();
    router.push('/login');
};
</script>

<template>
    <div class="container mt-5">
        <h2>Panel administracyjny</h2>
        <p>Zalogowano z uprawnieniami: <span class="badge bg-info text-dark fs-6">{{ authStore.userRole || 'Brak danych' }}</span></p>
        
        <div class="row mt-4">
            <div class="col-md-4 mb-3">
                <div class="card h-100">
                    <div class="card-body text-center d-flex flex-column">
                        <h5 class="card-title">Edycja wpisów</h5>
                        <p class="card-text flex-grow-1">Zarządzaj wpisami i aktualnościami na stronie głównej.</p>
                        <button class="btn btn-primary mt-auto" :disabled="!authStore.hasAccess(['mod', 'pr_manager'])" @click="goTo('/admin/news')">
                            {{ authStore.hasAccess(['mod', 'pr_manager']) ? 'Przejdź' : 'Brak uprawnień' }}
                        </button>
                    </div>
                </div>
            </div>

            <div class="col-md-4 mb-3">
                <div class="card h-100">
                    <div class="card-body text-center d-flex flex-column">
                        <h5 class="card-title">Edycja gier</h5>
                        <p class="card-text flex-grow-1">Zarządzaj listą gier.</p>
                        <button class="btn btn-primary mt-auto" :disabled="!authStore.hasAccess(['mod', 'worker'])" @click="goTo('/admin/games')">
                            {{ authStore.hasAccess(['mod', 'worker']) ? 'Przejdź' : 'Brak uprawnień' }}
                        </button>
                    </div>
                </div>
            </div>

            <div class="col-md-4 mb-3">
                <div class="card h-100">
                    <div class="card-body text-center d-flex flex-column">
                        <h5 class="card-title">Newsletter</h5>
                        <p class="card-text flex-grow-1">Zarządzaj listą subskrybentów.</p>
                        <button class="btn btn-primary mt-auto" :disabled="!authStore.hasAccess([])" @click="goTo('/admin/newsletter')">
                            {{ authStore.hasAccess([]) ? 'Przejdź' : 'Brak uprawnień' }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-4">
            <button class="btn btn-danger" @click="handleLogout">Wyloguj się</button>
        </div>
    </div>
</template>

<style scoped>
.card {
    transition: transform 0.2s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
</style>
