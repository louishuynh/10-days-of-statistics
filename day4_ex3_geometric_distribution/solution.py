# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys


def geometric_dist_pmf(n, p):
    """
    g(n, p) = q^(n-1) * p

    where q = 1 - p

    :param n: total number of trials
    :param p: the pr trial is p
    :return: the number of Bernoulli trials requirobability of success of 1ed to get a success
    """

    return (1 - p) ** (n - 1) * p


if __name__ == '__main__':
    # STEP 1: READ STDIN
    # 3 lines
    # 1st line contains respective space-separated numerator and denominator for the probability of defect
    # 2nd line contains the inspection we want the probability for being the first defect for

    prob_defect_str, first_inspection = sys.stdin
    # numbers will look something like [1, 2]
    prob_defect_list = [int(x) for x in prob_defect_str.split(' ')]
    prob_defect = prob_defect_list[0] / prob_defect_list[1]
    n = int(first_inspection)

    print('{:.3f}'.format(geometric_dist_pmf(n=n, p=prob_defect)))
