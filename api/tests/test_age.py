import pytest

from model.age import *


@pytest.mark.parametrize(
    "age_range,unit,expected_min_age,expected_max_age",
    [
        ("18-30", AgeUnit.YEARS, 18, 30),
        ("≥18", AgeUnit.YEARS, 18, float("inf")),
        (">18", AgeUnit.YEARS, 19, float("inf")),
        ("≤30", AgeUnit.MONTHS, 0, 30),
        ("<30", AgeUnit.MONTHS, 0, 29),
    ],
)
def test_create_age_range_from_str(age_range, unit, expected_min_age, expected_max_age):
    # Example usage:
    age_range = AgeRange.create_age_range_from_str(age_range, unit)
    assert expected_min_age == age_range.min_age.value
    assert expected_max_age == age_range.max_age.value
    assert unit == age_range.min_age.unit == age_range.max_age.unit


def test_create_age_range_from_str_age_range_invalid_format_raises_error():
    with pytest.raises(InvalidAgeRangeFormat) as excinfo:
        AgeRange.create_age_range_from_str("18", AgeUnit.YEARS)
    assert INVALID_AGE_RANGE_FORMAT in str(excinfo.value)


def test_create_age_range_from_str_age_range_age_not_integer_raises_error():
    with pytest.raises(InvalidAgeRangeFormat) as excinfo:
        AgeRange.create_age_range_from_str("a-b", AgeUnit.YEARS)
    assert AGE_MUST_BE_INTEGER in str(excinfo.value)


def test_create_age_range_from_str_age_range_min_age_greater_than_max_age_raises_error():
    with pytest.raises(InvalidAgeRangeFormat) as excinfo:
        AgeRange.create_age_range_from_str("10-5", AgeUnit.YEARS)
    assert MIN_AGE_CANNOT_BE_GREATER_THAN_MAX_AGE in str(excinfo.value)
