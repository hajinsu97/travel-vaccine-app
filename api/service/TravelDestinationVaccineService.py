from typing import List
import requests
from bs4 import BeautifulSoup
from flask import abort
from model.Destination import Destination
from model.Vaccine import Vaccine
from model.VaccineList import VaccineList

DESTINATIONS_LIST_URL = "https://wwwnc.cdc.gov/travel/destinations/list"
DESTINATIONS_SELECT_LIST_ID = "thlrdssl-traveler"


# TODO: Unit test for getDestinations()
def get_destinations() -> List[str]:
    page = requests.get(DESTINATIONS_LIST_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    country_list = []

    # Find all <ul> elements containing the countries
    ul_elements = soup.find_all("ul", class_="list-bullet")
    for ul_element in ul_elements:
        # Find all <li> elements within the <ul>
        li_elements = ul_element.find_all("li")

        # Extract the country names from the <a> elements within the <li> elements
        for li in li_elements:
            destination_url_path = li.find("a").get("href")
            country_id = destination_url_path.split("/")[-1]
            country_name = li.find("a").text
            country_list.append(
                Destination(id=country_id, display_name=country_name).__dict__
            )

    return country_list


# TODO: Unit test for getVaccines() (1) Existing country (2) Non-existing country
DESTINATIONS_URL_PREFIX = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/"
VACCINES_AND_MEDICINES_HTML_ID = "vaccines-and-medicines"
CLINICIAN_DISEASES_HTML_CLASS_NAME = "clinician-disease"
CLINICIAN_RECOMMENDATIONS_HTML_CLASS_NAME = "clinician-recomendations"


def get_vaccines(country: str) -> VaccineList:
    destination_url = DESTINATIONS_URL_PREFIX + country
    page = requests.get(destination_url)

    if page.status_code == 404:
        abort(404, f"Country with the name {country} could not be found.")

    # Find the "Vaccines and Medicines" table
    soup = BeautifulSoup(page.content, "html.parser")
    vaccines_and_medicines_table = soup.find(id=VACCINES_AND_MEDICINES_HTML_ID)

    # Get a list of each entry under "Vaccine for disease" in the table
    clinician_diseases = vaccines_and_medicines_table.find_all(
        "td", class_=CLINICIAN_DISEASES_HTML_CLASS_NAME
    )

    # Get a list of each entry under "Recommendations" in the table
    clinician_recommendations = vaccines_and_medicines_table.find_all(
        "td", class_=CLINICIAN_RECOMMENDATIONS_HTML_CLASS_NAME
    )

    # Find the disease name within each table cell
    vaccines_list = []
    for x in range(len(clinician_diseases)):
        disease_name = clinician_diseases[x].text.strip()
        # TODO: For each <p> concatenate and set as recommendation
        recommendation = clinician_recommendations[x].text.strip()

        vaccines_list.append(Vaccine(disease_name, recommendation).__dict__)
    # TODO: Missing Yellow fever recommendation
    return VaccineList(link=destination_url, items=vaccines_list).__dict__
