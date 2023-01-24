import requests
from bs4 import BeautifulSoup

URL = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/"
VACCINES_AND_MEDICINES_HTML_ID = "vaccines-and-medicines"
CLINICIAN_DISEASES_HTML_CLASS_NAME = "clinician-disease"

def getListOfVaccines(country: str) -> list:
    page = requests.get(URL + country)
    soup = BeautifulSoup(page.content, "html.parser")
    # Find the "Vaccines and Medicines" table
    vaccinesAndMedicinesTable = soup.find(id=VACCINES_AND_MEDICINES_HTML_ID)
    # Find each entry for "Vaccine for disease" in the table
    clinicianDiseases = vaccinesAndMedicinesTable.find_all("td", class_=CLINICIAN_DISEASES_HTML_CLASS_NAME)

    # Find the disease name within each table cell
    for clinicianDisease in clinicianDiseases:
        diseaseName = clinicianDisease.find("a").text
        print(diseaseName)



getListOfVaccines("south-korea")