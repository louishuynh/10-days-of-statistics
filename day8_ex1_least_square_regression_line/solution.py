from math import sqrt


def calc_pearson_correl(xs, ys) -> tuple:
    """ Calculates the pearson correlation coefficient, the coverance, means and std devs

    :param xs:
    :param ys:
    :return: corr, cov, x_sd, y_sd
    """

    n = len(xs)

    x_mean = sum(xs) / n
    y_mean = sum(ys) / n

    x_diff = [x - x_mean for x in xs]
    y_diff = [y - y_mean for y in ys]

    x_ss = sum([x ** 2 for x in x_diff])
    y_ss = sum([y ** 2 for y in y_diff])

    x_sd = sqrt(x_ss / n)
    y_sd = sqrt(y_ss / n)

    cov = (1 / n) * sum([x_diff[i] * y_diff[i] for i in range(n)])
    corr = cov / (x_sd * y_sd)

    return corr, cov, x_mean, y_mean, x_sd, y_sd


if __name__ == '__main__':

    # numpy is not supported on hacker rank in this exercise
    x = [95, 85, 80, 70, 60]
    y = [85, 95, 70, 65, 70]

    try:
        import numpy as np
        from sklearn import linear_model
        lm = linear_model.LinearRegression()
        reg = lm.fit(x, y)

        print(x)
        x = np.asarray(x).reshape(-1, 1)
        print(x)
        print(y)
        print(reg.score(x, y))
        print(reg.coef_)
        print(reg.intercept_)

        predicted = reg.predict(np.array([[80]]))[0]
    except:
        corr, cov, x_mean, y_mean, x_sd, y_sd = calc_pearson_correl(x, y)
        b = corr * y_sd / x_sd
        a = y_mean - b * x_mean
        predicted = a + b * 80

    print('{:.3f}'.format(predicted))
