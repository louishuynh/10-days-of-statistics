# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# STEP 1: READ STDIN
# 3 lines
# 1st line is number of elements, n
# 2nd line is a list of unique elements
# 3rd line is the frequency at which element occurs

str_n, str_numbers, str_freq = sys.stdin
# numbers will look something like [3, 7, 8, 5, 12, 14, 21, 13, 18]
n = int(str_n)
numbers = [int(x) for x in str_numbers.split(' ')]
freq = [int(x) for x in str_freq.split(' ')]


def return_sorted_list(elements, frequencies):

    return_value = []

    for element, frequency in zip(elements, frequencies):
        return_value.extend([element] * frequency)

    return_value.sort()

    return return_value


def return_median_lower_upper_half(sorted_list):

    n_sorted = len(sorted_list)

    # calculate median
    if n_sorted % 2:
        # if n_sorted odd then median element is n // 2 + 1
        # python indexing starts at 0 so index is element - 1
        index_median = n_sorted // 2
        median = sorted_list[index_median]

        lower_half = sorted_list[:index_median]
        upper_half = sorted_list[index_median + 1:]

    else:
        # if n_sorted even then median is average elements at n // 2 and n // 2 + 1
        # python indexing starts at 0 so index is element - 1
        index_median_left = n_sorted // 2 - 1
        index_median_right = index_median_left + 1

        median_left = sorted_list[index_median_left]
        median_right = sorted_list[index_median_right]

        median = (median_left + median_right) / 2

        lower_half = sorted_list[:index_median_left + 1]
        upper_half = sorted_list[index_median_right:]

    return median, lower_half, upper_half


def calculate_interquartile_range(elements, frequencies):
    sorted_list = return_sorted_list(elements, frequencies)
    median, lower_half, upper_half = return_median_lower_upper_half(sorted_list)
    q_1, _, _ = return_median_lower_upper_half(lower_half)
    q_3, _, _ = return_median_lower_upper_half(upper_half )
    return_value = q_3 - q_1
    return return_value


inter_quart_range = calculate_interquartile_range(elements=numbers, frequencies=freq)
print('{:.1f}'.format(inter_quart_range))
