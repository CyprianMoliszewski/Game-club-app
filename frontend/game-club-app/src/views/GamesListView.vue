<script setup lang="ts">
import { ref, onMounted } from 'vue';
import GameItem from '../components/GameItemComponent.vue';

interface Game {
  game_id: number;
  game_name: string;
  game_photo: string;
  game_description: string;
}

const gamesList = ref<Game[]>([]);

const fetchGames = async () => {
  gamesList.value = [
    {
      game_id: 1,
      game_name: 'Catan (Osadnicy z Catanu)',
      game_photo: 'https://via.placeholder.com/400x250?text=Catan',
      game_description: 'Klasyczna gra ekonomiczna. Zbieraj surowce, buduj drogi oraz osady i handluj z innymi graczami, aby przejąć kontrolę nad wyspą.'
    },
    {
      game_id: 2,
      game_name: 'Wsiąść do Pociągu: Europa',
      game_photo: 'https://via.placeholder.com/400x250?text=Wsi%C4%85%C5%9B%C4%87+do+Poci%C4%85gu',
      game_description: 'Zbieraj karty kolorowych wagonów i buduj trasy kolejowe łączące największe metropolie Europy w tej kultowej grze rodzinnej.'
    },
    {
      game_id: 3,
      game_name: 'Carcassonne',
      game_photo: 'https://via.placeholder.com/400x250?text=Carcassonne',
      game_description: 'Gra polegająca na dokładaniu kafelków. Wspólnie z rywalami twórz mapę średniowiecznej Francji, rozbudowując miasta, drogi i klasztory.'
    },
    {
      game_id: 4,
      game_name: 'Scythe',
      game_photo: 'https://via.placeholder.com/400x250?text=Scythe',
      game_description: 'Rozbudowana gra strategiczna osadzona w alternatywnej rzeczywistości lat 20. XX wieku. Zarządzaj frakcją, wydobywaj surowce i wysyłaj do walki potężne mechy.'
    }
  ];
};

onMounted(() => {
  fetchGames();
});
</script>

<template>
  <div class="container mt-5">
    <div class="mb-5 text-center">
      <h1 class="fw-bold">Dostępne gry</h1>
      <p class="text-muted">Lista tytułów obecnych na stanie.</p>
    </div>

    <div v-if="gamesList.length === 0" class="alert alert-info text-center">
      Obecnie nie mamy żadnych dodanych gier.
    </div>

    <div v-else class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      <div class="col" v-for="game in gamesList" :key="game.game_id">
        <GameItem :game="game" />
      </div>
    </div>
  </div>
</template>