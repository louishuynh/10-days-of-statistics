"""
The CLT states that for large enough sample (n), the distribution of the sample mean will approach
normal distribution. This holds for a sample of independent rv from any distribution with a finite
standard deviation.

Let {X1, X2, ..., Xn} bea  random data set of size n (i.e a sequence of iid) rv drawn from various

"""


from math import erf, sqrt


def norm_cdf(x, mu, sigma):
    z = (x - mu) / sigma
    return 0.5 * (1 + erf(z / sqrt(2)))


if __name__ == '__main__':

    n_tickets_available = float(input())
    n_buyers = float(input())
    mu_per_buyer = float(input())
    sigma_per_buyer = float(input())

    mu_sum = n_buyers * mu_per_buyer
    sigma_sum = sqrt(n_buyers) * sigma_per_buyer

    def fprint(x):
        print('{:.4f}'.format(x))

    fprint(norm_cdf(n_tickets_available, mu_sum, sigma_sum))
