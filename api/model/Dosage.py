from model.age import Age

class Dosage:
    def __init__(
        self,
        generic_name: str,
        brand_name: str,
        form: str,
        dose: str,
        number_of_doses: int,
        schedule: str,
        min_age: Age,
        max_age: Age,
    ):
        self.generic_name = generic_name
        self.brand_name = brand_name
        self.form = form
        self.dose = dose
        self.number_of_doses = number_of_doses
        self.schedule = schedule
        self.min_age = min_age
        self.max_age = max_age
