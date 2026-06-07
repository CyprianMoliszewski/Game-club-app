<script setup lang="ts">
import { ref } from 'vue';

interface Owner {
  id: number;
  name: string;
  role: string;
  email: string;
  phone: string;
}

const owners = ref<Owner[]>([
  {
    id: 1,
    name: 'Cyprian Moliszewski',
    role: 'Współzałożyciel',
    email: 'cyprian@example.com',
    phone: '+48 111 222 333'
  },
  {
    id: 2,
    name: 'Anna Mieczyńska',
    role: 'Współzałożycielka',
    email: 'anna@example.com',
    phone: '+48 444 555 666'
  }
]);
</script>

<template>
  <div class="container mt-5">
    <div class="text-center mb-4">
      <h1 class="fw-bold">Kontakt</h1>
      <p class="text-muted lead">Masz pytania? Chcesz dołączyć do naszej społeczności? Skontaktuj się z nami!</p>
    </div>

    <div class="mb-4">
      <h3 class="fw-semibold mb-3 border-bottom pb-2">Organizatorzy</h3>
      <div class="row row-cols-1 row-cols-md-2 g-4">
        <div class="col" v-for="owner in owners" :key="owner.id">
          <div class="card shadow-sm border-0 bg-white h-100">
            <div class="card-body row align-items-center g-0 py-3 px-3">                         
              
              <div class="col-4">
                <h5 class="card-title fw-bold mb-1 text-dark" style="line-height: 1.2;">{{ owner.name }}</h5>
                <p class="text-muted small mb-0">{{ owner.role }}</p>
              </div>
              
              <div class="col ps-3 border-start">
                <div class="d-flex flex-column gap-1 small">
                  <span class="text-dark">
                    <strong>Email:</strong> <a :href="'mailto:' + owner.email" class="text-dark text-decoration-none">{{ owner.email }}</a>
                  </span>
                  <span class="text-dark">
                    <strong>Telefon:</strong> <a :href="'tel:' + owner.phone" class="text-dark text-decoration-none">{{ owner.phone }}</a>
                  </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5 pt-3">
      <div class="col-12">
        <h3 class="fw-semibold mb-3 border-bottom pb-2">Miejsce spotkań</h3>
        <div class="card shadow-sm border-0 bg-white">
          <div class="card-body p-4">
            <div class="row g-4 align-items-center">
              
              <div class="col-lg-5">
                <h4 class="fw-bold text-dark mb-1">Wydział Ekonomiczno-Socjologiczny (EkSoc)</h4>
                <h5 class="text-muted mb-4">Uniwersytet Łódzki</h5>
                
                <p class="mb-3 lead fs-6">
                  <strong>Adres:</strong><br>
                  ul. Polskiej Organizacji Wojskowej 3/5<br>
                  90-255 Łódź
                </p>
                
                <p class="text-muted small mb-0">
                  Nasze główne spotkania oraz duże turnieje odbywają się zazwyczaj na terenie wydziału EkSoc UŁ. 
                  Dokładne numery sal podajemy w ogłoszeniach przed konkretnym wydarzeniem. 
                  Wydział jest świetnie skomunikowany, znajduje się blisko dworca Łódź Fabryczna.
                </p>
              </div>

              <div class="col-lg-7">
                <div class="ratio ratio-16x9 rounded overflow-hidden shadow-sm border">
                  <iframe 
                    src="https://maps.google.com/maps?q=Wydzia%C5%82+Ekonomiczno-Socjologiczny+Uniwersytetu+%C5%81%C3%B3dzkiego&t=&z=15&ie=UTF8&iwloc=&output=embed" 
                    style="border:0; width: 100%; height: 100%;" 
                    allowfullscreen="true" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                  </iframe>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>