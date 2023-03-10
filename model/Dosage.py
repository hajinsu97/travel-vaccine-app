from model.Age import Age


class Dosage:
    def __init__(self, minAge: Age, maxAge: Age, schedule: str):
        self.minAge = minAge
        self.maxAge = maxAge
        self.schedule = schedule
