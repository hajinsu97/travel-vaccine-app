<template>
  <RouterView />
  <div id="app">
    <div class="country-dropdown">
      <h3>✈️ Where are you travelling to?</h3>
      <select class="select-country" v-model="selectedCountry" @change="handleCountrySelected">
        <option disabled value="">Please select a country</option>
        <option v-for="destination in destinationList" :value="destination">{{ destination.displayName }}</option>
      </select>
    </div>
    
<div v-if="selectedCountry" class="vaccine-info">
  <h2>💉 Vaccine Information</h2>
  <a :href="vaccineInfoLink" target="_blank">{{ selectedCountry.displayName }} on CDC website</a>
  <ul>
    <li v-for="vaccine in vaccineList" :key="vaccine.id">
      <p class="vaccine-disease">Vaccine: {{ vaccine.disease }}</p>
      <p class="vaccine-recommendations">Recommendations: {{ vaccine.recommendations }}</p>
      <ul class="dosage-list">
        <li v-for="dosage in vaccine.dosages" :key="dosage.brandName">
          <p><strong>Brand Name:</strong> {{ dosage.brandName }}</p>
          <p><strong>Dose:</strong> {{ dosage.dose }}</p>
          <p><strong>Form:</strong> {{ dosage.form }}</p>
          <p><strong>Generic Name:</strong> {{ dosage.genericName }}</p>
          <p><strong>Number of Doses:</strong> {{ dosage.numberOfDoses }}</p>
          <p><strong>Schedule:</strong> {{ dosage.schedule }}</p>
        </li>
      </ul>
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
        destinationList: [],
        vaccineInfoLink: '',
        vaccineList: [],
      };
    },
    methods: {
      getDestinations() {
        const path = '/api/destinations';
        axios.get(path)
          .then((res) => {
            this.destinationList = res.data;
          })
          .catch((error) => {
            console.error('Error fetching destinations list:', error);
          });
      },
      async getVaccines() {
        try {
          const response = await axios.get(`/api/destinations/${this.selectedCountry.id}/vaccines`);
          const data = response.data;
          this.vaccineInfoLink = data.link
          this.vaccineList = data.items
          console.log('Got vaccine info:', data)
        } catch (error) {
          console.error('Error fetching vaccine information:', error);
        }
      },
      handleCountrySelected() {
        console.log('Selected country:', this.selectedCountry);
        this.getVaccines();
        // for vaccine in this.vaccines
      },

    },
    created() {
      this.getDestinations();
    },
  };
</script>