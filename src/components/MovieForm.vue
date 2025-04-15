<template>
    <div>
      <div v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
      </div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
      <form id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3">
          <label for="title">Movie Title</label>
          <input type="text" name="title" class="form-control" />
        </div>
        <div class="form-group mb-3">
          <label for="description">Description</label>
          <input type="text" name="description" class="form-control" />
        </div>
        <div class="form-group mb-3">
          <label for="poster">Movie Poster</label>
          <input type="file" name="poster" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let csrf_token = ref("");
  let successMessage = ref("");
  let errors = ref([]);
  
  function getCsrfToken() {
    fetch("/api/v1/csrf-token")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      });
  }
  
  onMounted(() => {
    getCsrfToken();
  });
  
  function saveMovie() {
    let movieForm = document.getElementById("movieForm");
    let form_data = new FormData(movieForm);
  
    fetch("/api/v1/movies", {
      method: "POST",
      body: form_data,
      headers: {
        "X-CSRFToken": csrf_token.value,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.errors) {
          errors.value = data.errors;
          successMessage.value = "";
        } else {
          successMessage.value = data.message;
          errors.value = [];
          movieForm.reset();
          getCsrfToken(); // Refresh CSRF token after submit
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
  </script>
  