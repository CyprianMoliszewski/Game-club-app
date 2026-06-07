<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

interface News {
  news_id: number;
  news_title: string;
  news_description: string;
  news_photo: string;
  news_date: string;
  is_active: boolean;
}

const route = useRoute();
const router = useRouter();
const newsItem = ref<News | null>(null);
const isLoading = ref<boolean>(true);

const fetchNewsDetails = async () => {
  const currentId = route.params.id as string;

  const mockTitles: Record<string, string> = {
    '1': 'Wielki Turniej Zimowy',
    '2': 'Aktualizacja serwerów',
    '3': 'Wyniki ligi wiosennej',
    '4': 'Wyniki ligi wiosennej (edycja letnia)'
  };

  setTimeout(() => {
    newsItem.value = {
      news_id: Number(currentId),
      news_title: mockTitles[currentId] || `Nieznany artykuł (ID: ${currentId})`,
      news_description: 'To jest pełna treść artykułu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id cursus urna, at commodo sem. Nulla bibendum eget purus at pretium. Mauris vehicula euismod rutrum. Nunc tempor tellus non tellus scelerisque dignissim. Fusce eget consequat ex. Sed dignissim justo eget sodales sollicitudin. Proin mattis, mi non laoreet sagittis, ipsum magna pretium ante, nec pellentesque orci est vitae mauris.',
      news_photo: `https://via.placeholder.com/1200x500?text=Zdjecie+Artykulu+${currentId}`,
      news_date: '2026-06-10T22:00:00',
      is_active: true
    };
    
    isLoading.value = false;
  }, 400); 
};

onMounted(() => {
  fetchNewsDetails();
});

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('pl-PL', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

const goBack = () => {
  router.back();
};
</script>

<template>
  <div class="container mt-5">
    
    <div v-if="isLoading" class="text-center my-5 py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Ładowanie...</span>
      </div>
    </div>

    <div v-else-if="!newsItem" class="alert alert-danger text-center my-5">
      <h4 class="alert-heading">Błąd 404</h4>
      <p>Nie znaleziono takiego artykułu w bazie danych.</p>
      <button @click="goBack" class="btn btn-outline-secondary mt-3">Wróć</button>
    </div>

    <div v-else class="row justify-content-center">
      <div class="col-lg-9">
        
        <button @click="goBack" class="btn btn-sm btn-light border mb-4 shadow-sm">
          &larr; Wróć do listy
        </button>

        <h1 class="fw-bold mb-3 display-5">{{ newsItem.news_title }}</h1>
        <p class="text-muted mb-4 fs-6">
          <strong>Opublikowano:</strong> {{ formatDate(newsItem.news_date) }}
        </p>

        <img 
          :src="newsItem.news_photo" 
          :alt="newsItem.news_title"
          class="img-fluid rounded shadow-sm w-100 mb-5"
          style="max-height: 450px; object-fit: cover;"
        >

        <div class="content fs-5 text-body" style="line-height: 1.8; text-align: justify;">
          {{ newsItem.news_description }}
        </div>
        
      </div>
    </div>

  </div>
</template>