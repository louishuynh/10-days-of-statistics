# Enter your code here. Read input from STDIN. Print output to STDOUT


def n_choose_k(n, k):
    return_value = 1
    if k > n / 2:
        k = n - k
    for numerator in range(n - k + 1, n + 1):
        return_value *= numerator
    for denominator in range(1, k + 1):
        return_value /= denominator
    return return_value


def pmf(x, n, p):
    binom_coef = n_choose_k(n, x)
    pdf = binom_coef * (p ** x) * ((1 - p) ** (n - x))
    return pdf


probs = [pmf(x, 6, 1.09 / 2.09) for x in range(3, 7)]


print('{:.3f}'.format(sum(probs)))
