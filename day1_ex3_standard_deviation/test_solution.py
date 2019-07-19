import pytest
from day1_ex3_standard_deviation.solution import calculate_standard_deviation


def test_calculate_standard_deviation():
    test = calculate_standard_deviation(5, [10, 40, 30, 50, 20])
    base = 14.14
    assert pytest.approx(test, 0.001) == base
