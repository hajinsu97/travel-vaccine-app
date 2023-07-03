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


class InvalidAgeRangeFormat(Exception):
    pass


INVALID_AGE_RANGE_FORMAT = "Must be a string containing one of the following formats: '<9', '≤9', '>9', '≥9', '1-9'"
AGE_MUST_BE_INTEGER = "Age values must be integers"
MIN_AGE_CANNOT_BE_GREATER_THAN_MAX_AGE = (
    "Minimum age cannot be greater than maximum age"
)


class AgeRange:
    def __init__(self, min_age: Age, max_age: Age):
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return f"{str(self.min_age)} - {str(self.max_age)}"

    def __eq__(self, other):
        return self.min_age == other.min_age and self.max_age == other.max_age

    @classmethod
    def create_age_range_from_str(self, age_range: str, units: AgeUnit):
        """
        Return a min and max age based on a inputted age ranges which can be in one of
        the following formats: '<9', '≤9', '>9', '≥9', '1-9'

        :param age_range: Age range string in years
        :return AgeRange containing the minimum and maximum age values.
        """

        min_age = 0
        max_age = float("inf")

        try:
            if "-" in age_range:  # 1-20 means including 1 and 20
                age_array = age_range.split("-")
                min_age = int(age_array[0])
                max_age = int(age_array[1])
            elif age_range.startswith("≤"):  # ≤20 means up to 21 years old
                age_array = age_range.split("≤")
                max_age = int(age_array[1].strip())
            elif age_range.startswith("<"):  # <20 means excluding 20 years old
                age_array = age_range.split("<")
                max_age = int(age_array[1].strip()) - 1
            elif age_range.startswith("≥"):  # ≥20 means above 20 years old
                age_array = age_range.split("≥")
                min_age = int(age_array[1].strip())
            elif age_range.startswith(">"):  # >20 means excluding 20 years old
                age_array = age_range.split(">")
                min_age = int(age_array[1].strip()) + 1
            else:
                raise InvalidAgeRangeFormat(INVALID_AGE_RANGE_FORMAT)
        except ValueError:
            raise InvalidAgeRangeFormat(AGE_MUST_BE_INTEGER)

        if min_age > max_age:
            raise InvalidAgeRangeFormat(MIN_AGE_CANNOT_BE_GREATER_THAN_MAX_AGE)

        return AgeRange(Age(min_age, units), Age(max_age, units))
