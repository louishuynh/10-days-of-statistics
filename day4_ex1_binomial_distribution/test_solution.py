import pytest

from scipy.stats import binom

from day4_ex1_binomial_distribution.solution import *


def test_pmf():
    x = 1
    test = pmf(x, 6, 0.5)
    base = binom.pmf(x, 6, 0.5)
    assert pytest.approx(test, 0.001) == base


def test_submission():
    cdf = {x + 1: 1 - binom.cdf(x, 6, 1.09 / 2.09) for x in range(7)}
    test = sum([pmf(x, 6, 1.09 / 2.09) for x in range(3, 7)])
    base = cdf[3]
    assert pytest.approx(test, 0.001) == base
