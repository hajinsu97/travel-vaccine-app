from enum import Enum

class AgeUnit(Enum):
    YEARS = "years"
    MONTHS = "months"

class Age:
    def __init__(self, value: str, unit: AgeUnit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit.value}"
