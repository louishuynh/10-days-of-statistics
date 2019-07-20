import pytest

from day5_ex1_poisson_distribution.solution import *


def test_poisson_dist_1():
    test = poisson_dis(k=3, lam=2)
    base = 0.180
    assert pytest.approx(test, 0.005) == base


def test_poisson_dist_2():
    test = sum([poisson_dis(k=x, lam=5) for x in range(0, 4)])
    base = 0.2650
    assert pytest.approx(test, 0.001) == base


def test_poisson_dist_3():
    test = poisson_dis(k=5, lam=2.5)
    base = 0.067
    assert test == base
    # assert pytest.approx(test, 0.001) == base
