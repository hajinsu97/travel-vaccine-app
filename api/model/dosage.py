from model.age import Age, AgeRange

class Dosage:
    def __init__(
        self,
        generic_name: str,
        brand_name: str,
        form: str,
        dose: str,
        number_of_doses: int,
        schedule: str,
        age_range: AgeRange,
    ):
        self.generic_name = generic_name
        self.brand_name = brand_name
        self.form = form
        self.dose = dose
        self.number_of_doses = number_of_doses
        self.schedule = schedule
        self.age_range = age_range
