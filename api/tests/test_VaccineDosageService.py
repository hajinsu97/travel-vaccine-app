import pytest

from service.VaccineDosageService import get_dosages

TEST_VACCINATION_LOGIC_TABLE_CSV_FILE = "tests/fixtures/Test_Vaccination_Logic_table.csv"

def _get_dosages(disease):
    """
    Helper method for calling the VaccineDosageService.get_dosage method with the test vaccine logic table CSV file
    """
    return get_dosages(disease, csv_file_name=TEST_VACCINATION_LOGIC_TABLE_CSV_FILE)

def test_get_dosages_non_existent_disease_returns_dosage_list_with_empty_items():
    non_existent_disease = "non existent disease"
    dosages = _get_dosages(non_existent_disease)
    assert dosages["disease"] == non_existent_disease
    assert dosages["items"] == []

def test_get_dosages_valid_disease_name_returns_correct_dosage_list():
    valid_disease_name = "Hepatitis A"
    dosages = _get_dosages(valid_disease_name)
    assert valid_disease_name == dosages["disease"]
    assert len(dosages["items"]) == 2

    dosage_1 = dosages["items"][0]
    assert dosage_1["generic_name"] == "Hepatitis A vaccine, inactivated"
    assert dosage_1["brand_name"] == "Avaxim"
    assert dosage_1["form"] == "Injectable"
    assert dosage_1["dose"] == "0.5 mL"
    assert dosage_1["number_of_doses"] == 2
    assert dosage_1["schedule"] == "0, 3-36"

    dosage_2 = dosages["items"][1]
    assert dosage_2["generic_name"] == "Hepatitis A vaccine, inactivated"
    assert dosage_2["brand_name"] == "Havrix"
    assert dosage_2["form"] == "Injectable"
    assert dosage_2["dose"] == "1 mL"
    assert dosage_2["number_of_doses"] == 2
    assert dosage_2["schedule"] == "0, 6-12"




