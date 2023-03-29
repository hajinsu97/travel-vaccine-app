import csv
from model.Dosage import Dosage
from model.Dose import Dose

def getDosages(vaccine: str, dateOfBirth: str) -> list[Dosage]:
    dosageList = []
    with open('Vaccination Logic table_03_26_2023.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            dose = convertStringToDose(row["Dose"])
            dosageList.append(Dosage(row["Generic"], row["Brand"], dose, row["Number of Doses"], row["Schedule (months)"]).__dict__)
    return dosageList

# Return a Dose given a string representing a dose e.g., "1.5 ml"
def convertStringToDose(dose: str) -> Dose:
    amount = None
    unit = None
    split = dose.split()

    if (len(split) > 0):
        amount = split[0]
    if (len(split) > 1):
        unit = split[1]

    return Dose(amount, unit).__dict__