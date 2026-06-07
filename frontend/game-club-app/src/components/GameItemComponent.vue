<script setup lang="ts">
interface Game {
  game_id: number;
  game_name: string;
  game_photo: string;
  game_description: string;
}

defineProps<{
  game: Game
}>();
</script>

<template>
  <div class="card h-100 shadow-sm border-0 bg-white">
    <img 
      :src="game.game_photo || 'https://via.placeholder.com/400x250?text=Brak+Zdj%C4%99cia'" 
      class="card-img-top" 
      :alt="game.game_name"
      style="object-fit: cover; height: 220px;"
    >
    <div class="card-body d-flex flex-column">
      <h4 class="card-title fw-bold">{{ game.game_name }}</h4>
      
      <p class="card-text text-muted flex-grow-1 mt-2">
        {{ game.game_description }}
      </p>
    </div>
  </div>
</template>