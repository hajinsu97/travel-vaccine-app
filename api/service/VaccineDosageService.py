import csv
from model.Dosage import Dosage
from model.DosageList import DosageList

VACCINE_LOGIC_TABLE_FILE_NAME = "Vaccination Logic table.csv"
DISEASE_COLUMN_HEADER = "Disease/Illness"
BRAND_NAME_COLUMN_HEADER = "Brand"
FORM_COLUMN_HEADER = "Form"
DOSE_COLUMN_HEADER = "Dose"
GENERIC_NAME_COLUMN_HEADER = "Generic"
NUMBER_OF_DOSES_COLUMN_HEADER = "Number of Doses"
SCHEDULE_COLUMN_HEADER = "Schedule (months)"


def get_dosages(disease: str, date_of_birth: str = None) -> DosageList:
    dosage_list = []
    with open(VACCINE_LOGIC_TABLE_FILE_NAME) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            current_disease = row[DISEASE_COLUMN_HEADER]
            if disease.lower().replace(" ", "-") == current_disease.lower().replace(" ", "-"):
                dosage = Dosage(
                    generic_name=row[GENERIC_NAME_COLUMN_HEADER],
                    brand_name=row[BRAND_NAME_COLUMN_HEADER],
                    form=row[FORM_COLUMN_HEADER],
                    dose=row[DOSE_COLUMN_HEADER],
                    number_of_doses = 0 if row[NUMBER_OF_DOSES_COLUMN_HEADER] == '' else int(row[NUMBER_OF_DOSES_COLUMN_HEADER]),
                    schedule=row[SCHEDULE_COLUMN_HEADER],
                )
                dosage_list.append(dosage.__dict__)
    return DosageList(disease=disease, items=dosage_list).__dict__
