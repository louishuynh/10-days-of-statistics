"""
Calculate the pearson correlation coefficient.

sum (x_i - x_mean)(y_i - y_mean) / (n)(x_sd)(y_sd)

"""

from math import sqrt


if __name__ == '__main__':

    n = int(input())
    # xs = [float(x) for x in input().split(' ')]
    # ys = [float(y) for y in input().split(' ')]

    x_input = input()
    xs = []
    for e in x_input.split(' '):
        # we do this because the test input also includes a new line character
        try:
            xs.append(float(e))
        except:
            pass


    y_input = input()
    ys = []
    for e in y_input.split(' '):
        # we do this because the test input also includes a new line character
        try:
            ys.append(float(e))
        except:
            pass

    # n = 10
    # xs = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
    # ys = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

    x_mean = sum(xs) / n
    y_mean = sum(ys) / n

    x_err = [x - x_mean for x in xs]
    y_err = [y - y_mean for y in ys]

    x_ss = sum([x ** 2 for x in x_err])
    y_ss = sum([y ** 2 for y in y_err])

    x_sd = sqrt(x_ss / n)
    y_sd = sqrt(y_ss / n)

    cov = (1/n) * sum([x_err[i] * y_err[i] for i in range(n)])

    corr = cov / (x_sd * y_sd)


    def fprint(x):
        print('{:.3f}'.format(x))

    fprint(corr)
