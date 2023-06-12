<template>
  <RouterView />
  <div id="app">
    <div class="country-dropdown">
      <h2>✈️ Where are you travelling to?</h2>
      <select class="select-country" v-model="selectedCountry" @change="handleCountrySelected">
        <option disabled value="">Please select a country</option>
        <option v-for="destination in destinationList" :value="destination">{{ destination.displayName }}</option>
      </select>
    </div>
    
<div v-if="selectedCountry" class="vaccine-info">
  <h1>💉 Vaccine Information</h1>
  <a :href="vaccineInfoLink" target="_blank">{{ selectedCountry.displayName }} on CDC website</a>
  <ul>
    <li v-for="vaccine in vaccineList" :key="vaccine.id" class="vaccine-item">
      <h2 class="vaccine-disease">Vaccine: {{ vaccine.disease }}</h2>
      <p class="vaccine-recommendations">Recommendations: {{ vaccine.recommendations }}</p>
      <ul class="dosage-list" v-if="vaccine.dosageList.length > 0">
        <div class="dosage-box">
          <li v-for="dosage in vaccine.dosageList" :key="dosage.brand_name" class="dosage-item">
            <p><strong>Brand Name:</strong> {{ dosage.brand_name }}</p>
            <p><strong>Dose:</strong> {{ dosage.dose }}</p>
            <p><strong>Form:</strong> {{ dosage.form }}</p>
            <p><strong>Generic Name:</strong> {{ dosage.generic_name }}</p>
            <p><strong>Number of Doses:</strong> {{ dosage.number_of_doses }}</p>
            <p><strong>Schedule:</strong> {{ dosage.schedule }}</p>
          </li>
        </div>
      </ul>
    </li>
  </ul>
</div>

  </div>
</template>

<script setup>
import {RouterView} from 'vue-router'
</script>
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        selectedCountry: '',
        destinationList: [],
        vaccineInfoLink: '',
        vaccineList: [
            {
                disease: '',
                recommendations: '',
                // TODO: what does this do? Do I need to define everything here?
                dosageList: []
            }
        ],
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
        this.vaccineList.forEach(async (vaccine) => {
            vaccine.dosageList = await this.getDosages(vaccine)
        })
      },
      async getDosages(vaccine) {
        try {
          const response = await axios.get(`/api/vaccines/${vaccine.disease}/dosages`);
          const data = response.data;
          console.log('Got dosage info:', data)
          return data.items
        } catch (error) {
          console.error('Error fetching dosage information:', error);
        }
      },
      async handleCountrySelected() {
          console.log('Selected country:', this.selectedCountry);
          await this.getVaccines();
      },

    },
    created() {
      this.getDestinations();
    },
  };
</script>