import pytest

from service.VaccineDosageService import get_dosages

TEST_VACCINATION_LOGIC_TABLE_CSV_FILE = "tests/fixtures/Test_Vaccination_Logic_table.csv"
DISEASE = "disease"
ITEMS = "items"
GENERIC_NAME = "generic_name"
BRAND_NAME = "brand_name"
FORM = "form"
DOSE = "dose"
NUMBER_OF_DOSES = "number_of_doses"
SCHEDULE = "schedule"


def _get_dosages(disease):
    """
    Helper method for calling the VaccineDosageService.get_dosage method with the test vaccine logic table CSV file
    """
    return get_dosages(disease, csv_file_name=TEST_VACCINATION_LOGIC_TABLE_CSV_FILE)

def test_get_dosages_non_existent_disease_returns_0_dosages():
    non_existent_disease = "non existent disease"
    dosages = _get_dosages(non_existent_disease)
    assert dosages[DISEASE] == non_existent_disease
    assert dosages[ITEMS] == []

def test_get_dosages_valid_disease_name_returns_correct_dosages():
    valid_disease_name = "Hepatitis A"
    dosages = _get_dosages(valid_disease_name)
    assert valid_disease_name == dosages[DISEASE]
    assert len(dosages[ITEMS]) == 2

    dosage_1 = dosages[ITEMS][0]
    assert dosage_1[GENERIC_NAME] == "Hepatitis A vaccine, inactivated"
    assert dosage_1[BRAND_NAME] == "Avaxim"
    assert dosage_1[FORM] == "Injectable"
    assert dosage_1[DOSE] == "0.5 mL"
    assert dosage_1[NUMBER_OF_DOSES] == 2
    assert dosage_1[SCHEDULE] == "0, 3-36"

    dosage_2 = dosages[ITEMS][1]
    assert dosage_2[GENERIC_NAME] == "Hepatitis A vaccine, inactivated"
    assert dosage_2[BRAND_NAME] == "Havrix"
    assert dosage_2[FORM] == "Injectable"
    assert dosage_2[DOSE] == "1 mL"
    assert dosage_2[NUMBER_OF_DOSES] == 2
    assert dosage_2[SCHEDULE] == "0, 6-12"

def test_get_dosages_disease_name_is_case_insensitive():
    assert _get_dosages("hepatitis b")[ITEMS] == _get_dosages("HEPATITIS B")[ITEMS]

def test_get_dosages_pass_disease_name_in_snake_case_returns_dosages():
    disease_name = 'hepatitis-b'
    dosages = _get_dosages(disease_name)
    assert dosages[DISEASE] == disease_name
    assert len(dosages[ITEMS]) == 1

def test_get_dosages_for_vaccine_with_empty_number_of_doses_returns_0_doses():
    dosages = _get_dosages('hepatitis b')
    assert dosages[ITEMS][0][NUMBER_OF_DOSES] == 0
