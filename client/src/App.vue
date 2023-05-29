<template>
  <RouterView />
  <div id="app">
    <div class="country-dropdown">
      <select class="select-country" v-model="selectedCountry" @change="handleCountrySelected">
        <option disabled value="">Please select a country</option>
        <option v-for="destination in destinations" :value="destination">{{ destination }}</option>
      </select>
    </div>
    <p>Selected country: {{ selectedCountry }}</p>
    
    <div v-if="selectedCountry" class="vaccine-info">
      <h2>Vaccine Information</h2>
      <a :href="vaccineInfo.link" target="_blank">Vaccine information for {{ selectedCountry }} on CDC website</a>
      <ul>
        <li v-for="vaccine in vaccineInfo.vaccines" :key="vaccine.id">
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
        selectedCountry: 'Where are you travelling to?',
        destinations: [],
        vaccineInfo: {},
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
            console.error('Error fetching destinations list:', error);
          });
      },
      async getVaccines() {
        try {
          const response = await axios.get(`/api/destinations/${this.selectedCountry}/vaccines`);
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