# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


def calculate_standard_deviation(n: int, numbers: list) -> float:
    """

    :param n: int. number of elements provided
    :param numbers: list[int]. elements
    :return: float
    """
    mean = sum(numbers) / n
    sum_squares = sum([(number - mean) ** 2 for number in numbers])
    std_dev = (sum_squares / n) ** (1/2)
    return std_dev


if __name__ == '__main__':
    # STEP 1: READ STDIN
    # 3 lines
    # 1st line is number of elements, n
    # 2nd line is a list of unique elements
    # 3rd line is the frequency at which element occurs

    str_n, str_numbers = sys.stdin
    # numbers will look something like [3, 7, 8, 5, 12, 14, 21, 13, 18]
    n = int(str_n)
    numbers = [int(x) for x in str_numbers.split(' ')]

    std_dev = calculate_standard_deviation(n, numbers)
    print('{:.1f}'.format(std_dev))
