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


def prob_no_more_than_n_rejects(n):
    probs = [pmf(x, 10, 0.12) for x in range(0, n + 1)]
    return sum(probs)


print('{:.3f}'.format(prob_no_more_than_n_rejects(2)))

print('{:.3f}'.format(1 - prob_no_more_than_n_rejects(1)))
