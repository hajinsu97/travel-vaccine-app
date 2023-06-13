import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const [selectedCountry, setSelectedCountry] = useState('');
  const [destinationList, setDestinationList] = useState([]);
  const [vaccineInfoLink, setVaccineInfoLink] = useState('');
  const [vaccineList, setVaccineList] = useState([
    {
      disease: '',
      recommendations: '',
      dosageList: []
    }
  ]);

  useEffect(() => {
    getDestinations();
  }, []);

  const getDestinations = () => {
    const path = '/api/destinations';
    axios
      .get(path)
      .then((res) => {
        setDestinationList(res.data);
      })
      .catch((error) => {
        console.error('Error fetching destinations list:', error);
      });
  };

  const getVaccines = async () => {
    try {
      const response = await axios.get(`/api/destinations/${selectedCountry.id}/vaccines`);
      const data = response.data;
      setVaccineInfoLink(data.link);
      setVaccineList(data.items);
      console.log('Got vaccine info:', data);
    } catch (error) {
      console.error('Error fetching vaccine information:', error);
    }

    vaccineList.forEach((vaccine) => {
      vaccine.dosageList = getDosages(vaccine);
    });
  };

  const getDosages = async (vaccine) => {
    try {
      const response = await axios.get(`/api/vaccines/${vaccine.disease}/dosages`);
      const data = response.data;
      console.log('Got dosage info:', data);
      return data.items;
    } catch (error) {
      console.error('Error fetching dosage information:', error);
    }
  };

  useEffect(() => {
    console.log(selectedCountry, '- Has changed')
    getVaccines();
  },[getVaccines, selectedCountry])


  // const handleCountrySelected = async (event) => {
  //   const selectedValue = event.target.value;
  //   const selectedDestination = destinationList.find((destination) => destination.id === selectedValue);
  //   await setSelectedCountry(selectedDestination);
  //   console.info('Selected country:', selectedDestination);
  //   getVaccines();
  // };

  return (
    <div id="app">
      <div className="country-dropdown">
        <h2>✈️ Where are you travelling to?</h2>
        <select className="select-country" value={selectedCountry.id} onChange={setSelectedCountry}>
          <option disabled value="">
            Please select a country
          </option>
          {destinationList.map((destination) => (
            <option key={destination.id} value={destination.id}>
              {destination.displayName}
            </option>
          ))}
        </select>
      </div>

      {selectedCountry && (
        <div className="vaccine-info">
          <h1>💉 Vaccine Information</h1>
          <a href={vaccineInfoLink} target="_blank" rel="noopener noreferrer">
            {selectedCountry.displayName} on CDC website
          </a>
          <ul>
            {vaccineList.map((vaccine) => (
              <li key={vaccine.id} className="vaccine-item">
                <h2 className="vaccine-disease">Vaccine: {vaccine.disease}</h2>
                <p className="vaccine-recommendations">Recommendations: {vaccine.recommendations}</p>
                {vaccine.dosageList.length > 0 && (
                  <ul className="dosage-list">
                    {vaccine.dosageList.map((dosage) => (
                      <div key={dosage.brandName} className="dosage-box">
                        <li className="dosage-item">
                          <p>
                            <strong>Brand Name:</strong> {dosage.brand_name}
                          </p>
                          <p>
                            <strong>Dose:</strong> {dosage.dose}
                          </p>
                          <p>
                            <strong>Form:</strong> {dosage.form}
                          </p>
                          <p>
                            <strong>Generic Name:</strong> {dosage.generic_name}
                          </p>
                          <p>
                            <strong>Number of Doses:</strong> {dosage.number_of_doses}
                          </p>
                          <p>
                            <strong>Schedule:</strong> {dosage.schedule}
                          </p>
                        </li>
                      </div>
                    ))}
                  </ul>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
