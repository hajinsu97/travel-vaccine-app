<template>
  <RouterView />
  <div id="app">
    <div class="country-dropdown">
      <h3>✈️ Where are you travelling to?</h3>
      <select class="select-country" v-model="selectedCountry" @change="handleCountrySelected">
        <option disabled value="">Please select a country</option>
        <option v-for="destination in destinations" :value="destination">{{ destination.displayName }}</option>
      </select>
    </div>
    
    <div v-if="selectedCountry" class="vaccine-info">
      <h2>💉 Vaccine Information</h2>
      <a :href="vaccineInfo.link" target="_blank">{{ selectedCountry.displayName }} on CDC website</a>
      <ul>
        <li v-for="vaccine in vaccineInfo.items" :key="vaccine.id">
          <p class="vaccine-disease">Vaccine: {{ vaccine.disease }}</p>
          <p class="vaccine-recommendations">Recommendations: {{ vaccine.recommendations }}</p>
        </li>
      </ul>
    </div>
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
        selectedCountry: '',
        destinations: [],
        vaccineInfo: {},
      };
    },
    methods: {
      getDestinations() {
        console.log(import.meta.env.VITE_API_PROXY_TARGET)
        const path = '/api/destinations';
        axios.get(path)
          .then((res) => {
            this.destinations = res.data;
          })
          .catch((error) => {
            console.error('Error fetching destinations list:', error);
          });
      },
      async getVaccines() {
        try {
          const response = await axios.get(`/api/destinations/${this.selectedCountry.id}/vaccines`);
          this.vaccineInfo = response.data;
          console.log('Got vaccine info:', this.vaccineInfo)
        } catch (error) {
          console.error('Error fetching vaccine information:', error);
        }
      },
      handleCountrySelected() {
        console.log('Selected country:', this.selectedCountry);
        this.getVaccines()
      },

    },
    created() {
      this.getDestinations();
    },
  };
</script>