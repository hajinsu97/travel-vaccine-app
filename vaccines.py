import requests
from bs4 import BeautifulSoup
from flask import abort

URL = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/"
VACCINES_AND_MEDICINES_HTML_ID = "vaccines-and-medicines"
CLINICIAN_DISEASES_HTML_CLASS_NAME = "clinician-disease"


def getVaccines(country: str) -> list[str]:
    # TODO: Add check if country is valid and abort if not
    page = requests.get(URL + country)
    soup = BeautifulSoup(page.content, "html.parser")
    # Find the "Vaccines and Medicines" table
    vaccinesAndMedicinesTable = soup.find(id=VACCINES_AND_MEDICINES_HTML_ID)
    # Find each entry for "Vaccine for disease" in the table
    clinicianDiseases = vaccinesAndMedicinesTable.find_all(
        "td", class_=CLINICIAN_DISEASES_HTML_CLASS_NAME
    )

    diseaseNames = []
    # Find the disease name within each table cell
    for clinicianDisease in clinicianDiseases:
        diseaseName = clinicianDisease.find("a").text
        diseaseNames.append(diseaseName)
    return diseaseNames
