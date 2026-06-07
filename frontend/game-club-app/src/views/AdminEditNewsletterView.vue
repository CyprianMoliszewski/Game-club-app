<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const peopleList = ref<any[]>([]);

const fetchPeople = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/newsletter');
    if (res.ok) {
      peopleList.value = await res.json();
    }
  } catch (err) {
    console.error("Błąd pobierania bazy maili:", err);
  }
};

const deletePerson = async (id: number) => {
  if (!confirm('Czy na pewno chcesz trwale usunąć ten adres e-mail z bazy?')) return;

  try {
    const res = await fetch(`http://127.0.0.1:8000/api/newsletter/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });

    if (res.ok) {
      fetchPeople();
    } else {
      alert("Błąd podczas usuwania. Sprawdź konsolę backendu.");
    }
  } catch (err) {
    console.error("Błąd sieci:", err);
  }
};

onMounted(fetchPeople);
</script>
<template>
  <div class="container mt-4 mb-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2>Lista Subskrybentów Newslettera</h2>
      <button class="btn btn-secondary" @click="router.push('/admin/main')">Wróć do panelu</button>
    </div>

    <div class="card shadow-sm p-4">
      <div class="table-responsive">
        <table class="table table-bordered table-hover align-middle mb-0">
          <thead class="table-light">
            <tr>
              <th style="width: 80px;">ID</th>
              <th>Adres E-mail</th>
              <th style="width: 100px;">Akcje</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="person in peopleList" :key="person.id">
              <td>{{ person.id }}</td>
              <td><strong>{{ person.email }}</strong></td>
              <td>
                <button class="btn btn-sm btn-danger w-100" @click="deletePerson(person.id)">Usuń</button>
              </td>
            </tr>
            <tr v-if="peopleList.length === 0">
              <td colspan="3" class="text-center text-muted p-4">Brak zapisanych adresów e-mail.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


