<script setup lang="ts">
import NewsItem from './NewsItemComponent.vue';

interface News {
  news_id: number;
  news_title: string;
  news_description: string;
  news_photo: string;
  news_date: string;
  is_active: boolean;
}

withDefaults(defineProps<{
  title: string;
  newsList: News[];
  layout?: 'scroll' | 'carousel';
}>(), {
  layout: 'scroll'
});
</script>

<template>
  <div class="mb-5">
    <h2 class="mb-4 border-bottom pb-2">{{ title }}</h2>
    
    <div v-if="newsList.length === 0" class="alert alert-info">
      Brak artykułów w tej sekcji.
    </div>

    <div 
      v-else-if="layout === 'scroll'" 
      class="row row-cols-1 row-cols-md-2 g-4" 
    >
      <div class="col" v-for="item in newsList" :key="item.news_id">
        <NewsItem :news="item" />
      </div>
    </div>

    <div 
      v-else-if="layout === 'carousel'" 
      class="d-flex flex-nowrap gap-3 pb-3 hide-scrollbar" 
      style="overflow-x: auto; scroll-snap-type: x mandatory;"
    >
      <div 
        v-for="item in newsList" 
        :key="item.news_id" 
        style="min-width: 300px; max-width: 300px; scroll-snap-align: start;"
      >
        <NewsItem :news="item" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.hide-scrollbar {
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>