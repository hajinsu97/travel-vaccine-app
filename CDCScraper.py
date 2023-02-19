import requests
from bs4 import BeautifulSoup
from flask import abort

URL = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/"
VACCINES_AND_MEDICINES_HTML_ID = "vaccines-and-medicines"
CLINICIAN_DISEASES_HTML_CLASS_NAME = "clinician-disease"


def getVaccines(country: str) -> list[str]:
    page = requests.get(URL + country)

    if (page.status_code == 404) {
        abort(404, response=f"Country with the name {country} could not be found.")
    }

    # Find the "Vaccines and Medicines" table
    soup = BeautifulSoup(page.content, "html.parser")
    vaccinesAndMedicinesTable = soup.find(id=VACCINES_AND_MEDICINES_HTML_ID)

    # Find each entry for "Vaccine for disease" in the table
    clinicianDiseases = vaccinesAndMedicinesTable.find_all(
        "td", class_=CLINICIAN_DISEASES_HTML_CLASS_NAME
    )

    # Find the disease name within each table cell
    diseaseNames = []
    for clinicianDisease in clinicianDiseases:
        diseaseName = clinicianDisease.find("a").text
        diseaseNames.append({"vaccine": diseaseName})
    return diseaseNames
