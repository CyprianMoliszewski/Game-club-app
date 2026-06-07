<script setup lang="ts">
import { useAuthStore } from '@/stores/authStore';
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const authStore = useAuthStore();

const message = ref('');

interface FormData {
    username: string
    password: string
}

const formData: FormData = reactive({ username: "", password: "" })

const login = async function () {
    message.value = '';
    try {
        const response = await fetch('http://127.0.0.1:8000/api/admin/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: formData.username,
                password: formData.password
            })
        });
        if (response.ok) {
            const data = await response.json();
            authStore.login(data.access_token);
            router.push('/admin/main'); 
        } else {
            message.value = "Błędny login lub hasło!";
        }
    } catch (error) {
        console.error("Błąd logowania:", error);
        message.value = "Wystąpił błąd połączenia z serwerem.";
    }
}
</script>

<template>
    <div class="container mt-5">
        <div v-if="message" class="alert alert-danger alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" @click="message = ''" aria-label="Close"></button>
        </div>
        <form>
            <div class="m-3">
                <label for="input_login" class="form-label">Login</label>
                <input v-model="formData.username" id="input_login" type="text" class="form-control m-3" />
                <label for="input_password" class="form-label">Hasło</label>
                <input v-model="formData.password" id="input_password" type="password" class="form-control m-3" />
            </div>
            <div class="float-end">
                <button @click.prevent="login" class="btn btn-primary">Prześlij</button>
            </div>
        </form>
    </div>
</template>

<style></style>