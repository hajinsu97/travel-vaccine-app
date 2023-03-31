from model.Age import Age
from model.Dose import Dose


# TODO: Use a Builder Pattern?
class Dosage:
    def __init__(self, disease: str, genericName: str, brandName: str, form: str, dose: Dose, numberOfDoses: int, schedule: str):
        self.disease = disease
        self.genericName = genericName
        self.brandName = brandName
        self.form = form
        # self.minAge = minAge
        # self.maxAge = maxAge
        self.dose = dose
        self.numberOfDoses = numberOfDoses
        self.schedule = schedule
