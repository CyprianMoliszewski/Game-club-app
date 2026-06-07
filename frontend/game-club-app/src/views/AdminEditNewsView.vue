<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const editingId = ref<number | null>(null);
const imageFile = ref<File | null>(null);
const form = ref({ title: '', description: '', date: '' });
const newsList = ref<any[]>([]);

const fetchNews = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/news');
    if (res.ok) {
      newsList.value = await res.json();
    }
  } catch (err) {
    console.error("Błąd pobierania bazy wpisów:", err);
  }
};

const onFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    const file = target.files[0];
    if (!file) return;
    
    if (file.type !== 'image/png') {
        alert('Dozwolone są tylko pliki .png!');
        target.value = '';
        imageFile.value = null;
        return;
    }
    
    if (file.size > 5 * 1024 * 1024) {
        alert('Zdjęcie jest za duże! Maksymalny rozmiar to 5MB.');
        target.value = ''; 
        imageFile.value = null;
        return;
    }
    
    imageFile.value = file;
  }
};

const submitForm = async () => {
  if (!form.value.title.trim()) return alert("Tytuł nie może być pusty!");
  if (form.value.title.length > 100) return alert("Tytuł max 100 znaków!");
  if (!form.value.description.trim()) return alert("Opis nie może być pusty!");

  const formData = new FormData();
  formData.append('title', form.value.title);
  formData.append('description', form.value.description);
  formData.append('date', form.value.date);
  if (imageFile.value) {
    formData.append('image', imageFile.value);
  }

  const url = editingId.value 
    ? `http://127.0.0.1:8000/api/news/${editingId.value}`
    : `http://127.0.0.1:8000/api/news`;
  const method = editingId.value ? 'PUT' : 'POST';

  try {
    const res = await fetch(url, {
      method: method,
      headers: { 'Authorization': `Bearer ${authStore.token}` },
      body: formData
    });

    if (res.ok) {
      alert(editingId.value ? 'Zaktualizowano wpis!' : 'Dodano nowy wpis!');
      cancelEdit();
      fetchNews();
    } else {
      alert('Błąd serwera przy zapisie.');
    }
  } catch (err) {
    console.error("Błąd sieci:", err);
  }
};

const deleteNews = async (id: number) => {
  if (!confirm('Czy na pewno chcesz usunąć ten wpis?')) return;

  try {
    const res = await fetch(`http://127.0.0.1:8000/api/news/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });

    if (res.ok) {
      if (editingId.value === id) cancelEdit(); 
      fetchNews();
    } else {
      alert("Błąd podczas usuwania.");
    }
  } catch (err) {
    console.error("Błąd sieci:", err);
  }
};

const editNews = (news: any) => {
  editingId.value = news.id;
  form.value = { title: news.title, description: news.description, date: news.date };
  imageFile.value = null;
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const cancelEdit = () => {
  editingId.value = null;
  imageFile.value = null;
  form.value = { title: '', description: '', date: '' };
};

onMounted(fetchNews);
</script>


<template>
  <div class="container mt-4 mb-5">
    <button class="btn btn-secondary mb-4" @click="router.push('/admin/main')">Wróć do głównego panelu</button>

    <!-- FORMULARZ -->
    <form @submit.prevent="submitForm" class="card p-4 mb-5 shadow-sm">
      <h4 class="mb-3">{{ editingId ? 'Edytuj wpis ID: ' + editingId : 'Dodaj nowy wpis' }}</h4>
      
      <div class="mb-3">
        <label class="form-label">Tytuł</label>
        <input v-model="form.title" type="text" class="form-control" maxlength="100" placeholder="Tytuł (max 100 znaków)" required />
      </div>
      
      <div class="mb-3">
        <label class="form-label">Opis</label>
        <textarea v-model="form.description" class="form-control" rows="4" placeholder="Opis wpisu..." required></textarea>
      </div>

      <div class="mb-3">
        <label class="form-label">Data</label>
        <input v-model="form.date" type="date" class="form-control" required />
      </div>

      <div class="mb-3">
        <label class="form-label">Zdjęcie (Tylko PNG, max 5MB)</label>
        <input type="file" @change="onFileChange" class="form-control" accept="image/png" :required="!editingId" />
        <small v-if="editingId" class="text-muted">Pozostaw puste, jeśli nie zmieniasz zdjęcia.</small>
      </div>

      <div class="d-flex gap-2">
        <button type="submit" class="btn" :class="editingId ? 'btn-warning' : 'btn-success'">
          {{ editingId ? 'Zapisz zmiany' : 'Dodaj wpis' }}
        </button>
        <button v-if="editingId" type="button" class="btn btn-outline-secondary" @click="cancelEdit">
          Anuluj edycję
        </button>
      </div>
    </form>

    <!-- LISTA WPISÓW -->
    <h4>Aktualne wpisy</h4>
    <div class="table-responsive">
      <table class="table table-bordered table-hover align-middle">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>Tytuł</th>
            <th>Data</th>
            <th style="width: 150px;">Akcje</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="news in newsList" :key="news.id">
            <td>{{ news.id }}</td>
            <td><strong>{{ news.title }}</strong></td>
            <td>{{ news.date }}</td>
            <td>
              <button class="btn btn-sm btn-primary me-2" @click="editNews(news)">Edytuj</button>
              <button class="btn btn-sm btn-danger" @click="deleteNews(news.id)">Usuń</button>
            </td>
          </tr>
          <tr v-if="newsList.length === 0">
            <td colspan="4" class="text-center text-muted p-4">Brak wpisów w bazie.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

