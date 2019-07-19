from day1_ex2_interquartile_range.solution import *


def test_calculate_interquartile_range():
    elements = [6, 12, 8, 10, 20, 16]
    frequencies = [5, 4, 3, 2, 1, 5]
    return_value = calculate_interquartile_range(elements, frequencies)
    print(return_value)


def test_median_odd_numbers():
    test = return_median_lower_upper_half([1, 2, 3, 4, 5])
    base = 3, [1, 2], [4, 5]
    assert test == base


def test_median_even_numbers():
    test = return_median_lower_upper_half([1, 2, 3, 4, 5, 6])
    base = 3.5, [1, 2, 3], [4, 5, 6]
    assert test == base

