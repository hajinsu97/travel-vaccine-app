from model.Age import Age
from model.Dose import Dose


class Dosage:
    def __init__(self, genericName: str, brandName: str, dose: Dose, numberOfDoses: int, schedule: str):
        self.genericName = genericName
        self.brandName = brandName
        # self.minAge = minAge
        # self.maxAge = maxAge
        self.dose = dose
        self.numberOfDoses = numberOfDoses
        self.schedule = schedule
