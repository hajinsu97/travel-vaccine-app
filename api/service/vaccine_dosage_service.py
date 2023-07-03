import csv

from flask import abort
from model.age import Age, AgeUnit, AgeRange
from model.dosage import Dosage
from model.dosage_list import DosageList

VACCINE_LOGIC_TABLE_FILE_NAME = "Vaccination Logic table.csv"
DISEASE_COLUMN_HEADER = "Disease/Illness"
BRAND_NAME_COLUMN_HEADER = "Brand"
FORM_COLUMN_HEADER = "Form"
DOSE_COLUMN_HEADER = "Dose"
GENERIC_NAME_COLUMN_HEADER = "Generic"
NUMBER_OF_DOSES_COLUMN_HEADER = "Number of Doses"
SCHEDULE_COLUMN_HEADER = "Schedule (months)"
AGE_YEARS_COLUMN_HEADER = "Age (years)"
AGE_MONTHS_COLUMN_HEADER = "Age (months)"


def get_dosages(disease: str, csv_file_name=VACCINE_LOGIC_TABLE_FILE_NAME) -> DosageList:
    """
    Return a list of all Dosages for a given disease.

    :param disease: Name of the disease
    :return: List of Dosage object
    """
    dosage_list = []
    with open(csv_file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            current_disease = row[DISEASE_COLUMN_HEADER]
            if disease.lower().replace(" ", "-") == current_disease.lower().replace(" ", "-"):
                age_range = AgeRange.create_age_range_from_str(row[AGE_YEARS_COLUMN_HEADER], row[AGE_MONTHS_COLUMN_HEADER])
                # min_age, max_age = Age()
                dosage = Dosage(
                    generic_name=row[GENERIC_NAME_COLUMN_HEADER],
                    brand_name=row[BRAND_NAME_COLUMN_HEADER],
                    form=row[FORM_COLUMN_HEADER],
                    dose=row[DOSE_COLUMN_HEADER],
                    number_of_doses = 0 if not row[NUMBER_OF_DOSES_COLUMN_HEADER] else int(row[NUMBER_OF_DOSES_COLUMN_HEADER]),
                    schedule=row[SCHEDULE_COLUMN_HEADER],
                    age_range=age_range,
                )
                dosage_list.append(dosage.__dict__)
    return DosageList(disease=disease, items=dosage_list).__dict__


def search_dosages(disease: str) -> DosageList:
    """
    Return a list of Dosages for a given disease filtered on the given parameters.
    
    :param disease: Name of the disease
    :return: List of Dosage object
    """
    return get_dosages(disease)
