import csv
from model.Dosage import Dosage

VACCINE_LOGIC_TABLE_FILE_NAME = "Vaccination Logic table.csv"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_DISEASE = "Disease/Illness"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_BRAND_NAME = "Brand"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_FORM = "Form"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_DOSE = "Dose"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_GENERIC_NAME = "Generic"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_NUMBER_OF_DOSES = "Number of Doses"
VACCINE_LOGIC_TABLE_COLUMN_HEADER_SCHEDULE_IN_MONTHS = "Schedule (months)"

def getDosages(vaccine: str, dateOfBirth: str) -> list[Dosage]:
    dosageList = []
    with open(VACCINE_LOGIC_TABLE_FILE_NAME) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # TODO: Make constants file?
            dosage = Dosage(row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_DISEASE],
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_GENERIC_NAME], 
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_BRAND_NAME], 
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_FORM],
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_DOSE], 
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_NUMBER_OF_DOSES], 
                            row[VACCINE_LOGIC_TABLE_COLUMN_HEADER_SCHEDULE_IN_MONTHS])
            dosageList.append(dosage.__dict__)
    return dosageList
