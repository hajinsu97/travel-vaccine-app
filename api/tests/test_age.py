import pytest

from model.age import AgeRange, AgeUnit

@pytest.mark.parametrize(
    "age_range,expected_min_age,expected_max_age",
    [
        ("18-30", 18, 30),
        ('≥18', 18, float('inf')),
        ('>18', 19, float('inf')),
        ("≤30", 0, 30),
        ("<30", 0, 29),
    ],
)
def test_create_age_range_from_str(age_range, expected_min_age, expected_max_age):
    # Example usage:
    age_range = AgeRange.create_age_range_from_str(age_range, AgeUnit.YEARS)
    assert expected_min_age == age_range.min_age.value
    assert expected_max_age == age_range.max_age.value
    assert AgeUnit.YEARS == age_range.min_age.unit == age_range.max_age.unit


# error test cases

# test_create_age_range_from_str_both_months_and_years_inputted
