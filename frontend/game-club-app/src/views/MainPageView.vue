<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import NewsList from '../components/NewsListComponent.vue';

interface News {
  news_id: number;
  news_title: string;
  news_description: string;
  news_photo: string;
  news_date: string;
  is_active: boolean;
}

const allNews = ref<News[]>([]);

const fetchNews = async () => {  
  allNews.value = [
    {
      news_id: 1,
      news_title: 'Wielki Turniej Zimowy',
      news_description: 'Zapisy na nasz coroczny turniej już wystartowały.',
      news_photo: '', 
      news_date: '2026-12-15T18:00:00', 
      is_active: true
    },
    {
      news_id: 2,
      news_title: 'Aktualizacja serwerów',
      news_description: 'W najbliższy weekend serwery będą wyłączone.',
      news_photo: '',
      news_date: '2026-06-10T22:00:00', 
      is_active: true
    },
    {
      news_id: 3,
      news_title: 'Wyniki ligi wiosennej',
      news_description: 'Znamy już zwycięzców naszej wiosennej edycji rozgrywek!',
      news_photo: '',
      news_date: '2026-05-20T14:30:00', 
      is_active: true
    },
    {
      news_id: 4,
      news_title: 'Wyniki ligi wiosennej',
      news_description: 'Znamy już zwycięzców naszej wiosennej edycji rozgrywek!',
      news_photo: '',
      news_date: '2027-05-20T14:30:00', 
      is_active: true
    }
  ];
};

onMounted(() => {
  fetchNews();
});

const futureNews = computed(() => {
  const now = new Date();
  return allNews.value
    .filter(news => new Date(news.news_date) > now && news.is_active)
    .sort((a, b) => new Date(a.news_date).getTime() - new Date(b.news_date).getTime());
});

const pastNews = computed(() => {
  const now = new Date();
  return allNews.value
    .filter(news => new Date(news.news_date) <= now && news.is_active)
    .sort((a, b) => new Date(b.news_date).getTime() - new Date(a.news_date).getTime());
});
</script>

<template>
  <div>
    <div class="hero-welcomer text-white mb-5">
      <div class="container h-100 d-flex align-items-center">
        <div class="row w-100 justify-content-center">
          <div class="col-lg-10 text-center">
            <h1 class="display-3 fw-bold mb-4">Witaj w naszej społeczności!</h1>
            <p class="lead mb-0 text-light opacity-85"> 
              Dołącz do naszej grupy, aby grać w planszówki 
              w przyjaznej atmosferze na Wydziale EkSoc!
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-12 mb-4">
          <NewsList 
            title="Nadchodzące wydarzenia" 
            :newsList="futureNews" 
            layout="scroll" 
          />
        </div>
        
        <div class="col-12">
          <NewsList 
            title="Przeszłe wydarzenia" 
            :newsList="pastNews" 
            layout="carousel" 
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-welcomer {
  background-color: rgba(0, 0, 0, 0.75); 
  padding-top: 100px;
  padding-bottom: 100px;
  width: 100%;  
  margin-top: 0 !important; 
}

.hero-welcomer h1 {
  text-shadow: 1px 1px 3px rgba(0,0,0,0.5); 
}
</style>