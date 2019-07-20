from math import erf, sqrt


def norm_cdf(x, mu, sigma):
    z = (x - mu) / (sigma * sqrt(2))
    return (1 / 2) * (1 + erf(z))


if __name__ == '__main__':
    # input will be three lines
    # line one is the mean and stdev
    mu_str, sigma_str = input().split(' ')
    mu, sigma = float(mu_str), float(sigma_str)

    # line 2 is x
    x = float(input())

    # line 3 is x1, x2 (eg between 20 and 22 hours)
    x1_str, x2_str = input().split(' ')
    x1, x2 = float(x1_str), float(x2_str)

    print('{:.3f}'.format(norm_cdf(x, mu, sigma)))
    print('{:.3f}'.format(norm_cdf(x2, mu, sigma) - norm_cdf(x1, mu, sigma)))
