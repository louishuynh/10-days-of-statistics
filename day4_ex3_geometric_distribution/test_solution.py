import pytest


from day4_ex3_geometric_distribution.solution import *


def test_geometric_dist_pmf():
    test = geometric_dist_pmf(n=5, p=0.7)
    base = 0.00567
    assert pytest.approx(test, 0.001) == base
