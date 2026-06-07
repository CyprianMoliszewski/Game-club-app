<script setup lang="ts">
interface News {
  news_id: number;
  news_title: string;
  news_description: string;
  news_photo: string;
  news_date: string;
  is_active: boolean;
}

defineProps<{
  news: News
}>();

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('pl-PL', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};
</script>

<template>
  <div class="card h-100 shadow-sm">
    <img 
      :src="news.news_photo || 'https://via.placeholder.com/300x150?text=Brak+Zdj%C4%99cia'" 
      class="card-img-top" 
      alt="Zdjęcie newsa"
      style="object-fit: cover; height: 200px;"
    >
    <div class="card-body d-flex flex-column">
      <h5 class="card-title">{{ news.news_title }}</h5>
      <p class="card-text text-muted small">{{ formatDate(news.news_date) }}</p>
      
      <p class="card-text flex-grow-1">
        {{ news.news_description.substring(0, 100) }}...
      </p>
      
      <router-link 
        :to="{ name: 'news-detail', params: { id: news.news_id } }" 
        class="btn btn-outline-dark mt-auto">
        Czytaj więcej
      </router-link>
    </div>
  </div>
</template>