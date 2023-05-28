<template>
  <RouterView />
  <div id="app">
    <div class="dropdown">
      <select v-model="selectedCountry" @change="handleCountrySelected">
        <option disabled value="">Please select a country</option>
        <option v-for="destination in destinations" :value="destination">{{ destination }}</option>
      </select>
    </div>
    <p>Selected country: {{ selectedCountry }}</p>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        destinations: '',
        selectedCountry: 'Where are you travelling to?'
      };
    },
    methods: {
      getDestinations() {
        const path = '/api/destinations';
        axios.get(path)
          .then((res) => {
            this.destinations = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      handleCountryChange() {
        console.log('Selected country:', this.selectedCountry);
      },
    },
    created() {
      this.getDestinations();
    },
  };
</script>