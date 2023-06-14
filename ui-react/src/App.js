import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const [selectedDestination, setSelectedDestination] = useState({});
  const [destinationList, setDestinationList] = useState([]);
  const [vaccineInfoLink, setVaccineInfoLink] = useState('');
  const [vaccineList, setVaccineList] = useState([])

  useEffect(() => {
    const fetchDestination = () => {
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
    
    fetchDestination();
  }, []);

  useEffect(() => {
    const fetchVaccines = async () => {
      try {
        const response = await axios.get(`/api/destinations/${selectedDestination.id}/vaccines`);
        const data = response.data;
        setVaccineInfoLink(data.link);
        setVaccineList(data.items);
        console.log('Got vaccine info:', data);
      } catch (error) {
        console.error('Error fetching vaccine information:', error);
      }
    };

    console.info('Selected destination:', selectedDestination);
    fetchVaccines();
    // fetchVaccineDosages();
  },[selectedDestination])

  useEffect(() => {
    const fetchVaccineDosages = async () => {
      try {
        const requests = vaccineList.map(vaccine =>
          axios.get(`/api/vaccines/${vaccine.disease}/dosages`)
        );
        const responses = await Promise.all(requests);
  
        // Adds dosageList as a field in vaccine
        const updatedVaccineList = vaccineList.map((vaccine, index) => ({
          ...vaccine,
          dosageList: responses[index].data.items
        }));
  
        setVaccineList(updatedVaccineList);
      } catch (error) {
        console.error('Error fetching vaccine dosages:', error);
      }
    };

    fetchVaccineDosages();
  },[vaccineInfoLink])

  const handleDestinationSelected = async (event) => {
    const selectedDestinationId = event.target.value;
    const selectedDestination = destinationList.find((destination) => destination.id === selectedDestinationId);
    setSelectedDestination(selectedDestination);
  };

  return (
    <div id="app">
      <div className="destination-dropdown">
        <h2>✈️ Where are you travelling to?</h2>
        <select className="select-destination" value={selectedDestination.id} onChange={handleDestinationSelected}>
          <option disabled value="">
            Please select a country
          </option>
          {destinationList.map((destination) => (
            <option key={destination.id} value={destination.id}>
              {destination.display_name}
            </option>
          ))}
        </select>
      </div>

      {selectedDestination && vaccineList.length > 0 && (
        <div className="vaccine-info">
          <h1>💉 Vaccine Information</h1>
          <a href={vaccineInfoLink} target="_blank" rel="noopener noreferrer">
            {selectedDestination.display_name} on CDC website
          </a>
          <ul>
            {vaccineList.map((vaccine) => (
              <li key={vaccine.disease} className="vaccine-item">
                <h2 className="vaccine-disease">Vaccine: {vaccine.disease}</h2>
                <p className="vaccine-recommendations">Recommendations: {vaccine.recommendations}</p>
                {vaccine.dosageList && vaccine.dosageList.length > 0 && (
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
