import pytest

from service.VaccineDosageService import get_dosages

TEST_VACCINATION_LOGIC_TABLE_CSV_FILE = "tests/fixtures/Test_Vaccination_Logic_table.csv"

def _get_dosages(disease):
    """
    Helper method for calling the VaccineDosageService.get_dosage method with the test vaccine logic table CSV file
    """
    return get_dosages(disease, csv_file_name=TEST_VACCINATION_LOGIC_TABLE_CSV_FILE)

def test_get_dosages_invalid_disease_name_returns_empty_list():
    non_existent_disease = "non existent disease"
    dosages = _get_dosages(non_existent_disease)
    assert non_existent_disease == dosages["disease"]
    assert [] == dosages["items"]
