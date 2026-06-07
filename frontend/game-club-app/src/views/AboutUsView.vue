<script setup lang="ts">
import { ref, reactive } from 'vue';

interface NewsletterForm {
  email: string;
  honeypot: string;
}

const formData = reactive<NewsletterForm>({
  email: '',
  honeypot: ''
});

const isSubmitted = ref<boolean>(false);
const errorMessage = ref<string>('');
const isLoading = ref<boolean>(false);

// Walidacja email - regex
const validateEmail = (email: string): boolean => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

// Obsługa wysyłki formularza
const handleSubscribe = async () => {
  errorMessage.value = '';
  isSubmitted.value = false;

  // Ochrona przed botami (Honeypot)
  if (formData.honeypot !== '') {
    isSubmitted.value = true;
    formData.email = '';
    return;
  }

  // Walidacja danych wejściowych
  if (!formData.email.trim()) {
    errorMessage.value = 'Adres e-mail jest wymagany.';
    return;
  }

  if (!validateEmail(formData.email)) {
    errorMessage.value = 'Wprowadzony adres e-mail jest niepoprawny.';
    return;
  }

  isLoading.value = true;

  try {
    
    await new Promise(resolve => setTimeout(resolve, 1000)); 
    
    isSubmitted.value = true;
    formData.email = ''; 
  } catch (error) {
    errorMessage.value = 'Wystąpił błąd podczas zapisu. Spróbuj ponownie później.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      
      <div class="col-lg-8 mb-4">
        <h1 class="fw-bold mb-3 text-dark text-center">O nas</h1>
        <p class="lead text-muted">
          Jesteśmy społecznością pasjonatów, która powstała z miłości do nowoczesnych gier planszowych. 
          Naszym celem jest łączenie ludzi przy stole, niezależnie od ich wieku czy doświadczenia.
        </p>
        <p class="text-body">
          W naszej kolekcji posiadamy dziesiątki tytułów – od prostych, szybkich gier imprezowych, 
          przez angażujące gry rodzinne, aż po ciężkie, wielogodzinne strategie ekonomiczne. Organizujemy 
          regularne spotkania, turnieje z nagrodami oraz wieczory z tłumaczeniem zasad dla początkujących. 
          Wierzymy, że planszówki to najlepszy sposób na spędzenie czasu wolnego offline, rozwijanie strategicznego 
          myślenia i przede wszystkim – świetną zabawę w gronie znajomych.
        </p>
      </div>

      <div class="col-lg-8">
        <div class="card p-4 shadow-sm border-0 welcomer-bg text-light rounded-4">
          <div class="card-body">
            <h3 class="card-title fw-bold mb-2">Bądź na bieżąco!</h3>
            <p class="card-text opacity-75 mb-4">
              Zapisz się do naszego newslettera, aby otrzymywać informacje o nadchodzących turniejach, 
              nowościach w naszej kolekcji gier oraz relacjach ze spotkań.
            </p>

            <div v-if="isSubmitted" class="alert alert-success bg-transparent border-success text-success" role="alert">
              Dziękujemy! Twój adres został pomyślnie zapisany do bazy newslettera.
            </div>

            <form v-else @submit.prevent="handleSubscribe" novalidate>
              
              <div class="visually-hidden">
                <label for="honeypot">Zostaw to pole puste</label>
                <input 
                  type="text" 
                  id="honeypot" 
                  v-model="formData.honeypot" 
                  autocomplete="off"
                />
              </div>

              <div class="mb-3">
                <label for="newsletter_email" class="form-label fw-semibold">Adres e-mail</label>
                <div class="input-group">
                  <input 
                    type="email" 
                    id="newsletter_email" 
                    class="form-control form-control-lg bg-secondary text-light border-secondary custom-placeholder" 
                    :class="{ 'is-invalid': errorMessage }"
                    placeholder="np. jan.kowalski@example.com"
                    v-model="formData.email"
                    :disabled="isLoading"
                    required
                  />
                  <button 
                    type="submit" 
                    class="btn btn-light px-4 text-dark fw-bold"
                    :disabled="isLoading"
                  >
                    <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status"></span>
                    Zapisz się
                  </button>
                </div>
                
                <div v-if="errorMessage" class="invalid-feedback d-block mt-2 text-warning">
                  {{ errorMessage }}
                </div>
              </div>

              <small class="d-block mt-3 opacity-50">
                Szanujemy Twoją prywatność. Twój adres e-mail zostanie użyty wyłącznie do celów wysyłki newslettera i nie zostanie przekazany osobom trzecim.
              </small>
            </form>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.welcomer-bg {
  background-color: rgba(0, 0, 0, 0.75); 
}

.custom-placeholder::placeholder {
  color: #adb5bd;
  opacity: 1;
}

.form-control:focus {
  background-color: #6c757d;
  color: #fff;
  border-color: #fff;
  box-shadow: 0 0 0 0.25rem rgba(255, 255, 255, 0.25);
}
</style>