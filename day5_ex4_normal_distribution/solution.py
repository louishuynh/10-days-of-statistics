from math import erf, sqrt


def norm_cdf(x, mu, sigma):
    z = (x - mu) / (sigma * sqrt(2))
    return (1 / 2) * (1 + erf(z))


if __name__ == '__main__':
    # input will be three lines
    # line one is the mean and stdev
    mu_str, sigma_str = input().split(' ')
    mu, sigma = float(mu_str), float(sigma_str)

    x1 = float(input())

    x2 = float(input())

    def fprint(x):
        """ The format required by this hacker rank tutorial is inconsistent compared to others. """
        print('{:.2f}'.format(100 * x))

    fprint(1 - norm_cdf(x1, mu, sigma))
    fprint(1 - norm_cdf(x2, mu, sigma))
    fprint(norm_cdf(x2, mu, sigma))
