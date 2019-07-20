from math import factorial, exp


def poisson_dis(k, lam):
    """

    :param k: the actual number of successes that occur in a specified region.
    :param lam: the average number of successes that occur in a specified regino
    :return: probability of getting exactly k successes when the average number of successes is poisson_lambda

    Calculates poisson distribution.

    Many problems can be broken down into terms of n, x and p. But if we don't know p(x)? We use the Poisson RV.

    Poisson Experiment
    A Poisson experiment is a statistical experiment that has the following properties:
    - The outcome of each trial is either success or failure.
    - The average number of successes  that occurs in a specified region is known.
    - The probability that a success will occur is proportional to the size of the region.
    - The probability that a success will occur in an extremely small region is virtually zero.

    Poisson Distribution
    A Poisson random variable is the number of successes that result from a Poisson experiment.
    The probability distribution of a Poisson random variable is called a Poisson distribution:

    P(k, lambda) = (lambda ** k)(e ** -lambda) / k!

    Here,
    e = 2.71828
    lambda is the average number of successes that occur in a specified region.
    k is the actual number of successes that occur in a specified region.
    P(k, lambda) is the Poisson probability, which is the probability of getting exactly
    k successes when the average number of successes is lambda.

    """

    prob = exp(-lam) * (lam ** k) / factorial(k)
    return prob


if __name__ == '__main__':
    # STEP 1: READ STDIN
    # 2 lines
    # 1st line contains X's means
    # 2nd line contains the probability with which the random variable X is equal to

    # method 1 (doesn't seem to work on hacker rank)
    # numbers will look something like [2.5]
    # poisson_lambda_str, k_str = sys.stdin
    # poisson_lambda = float(poisson_lambda_str)
    # k = int(k_str)

    # method 2
    lam = float(input())
    k = int(input())

    result = poisson_dis(k=k, lam=lam)
    print('{:.3f}'.format(result))
