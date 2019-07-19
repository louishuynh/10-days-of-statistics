# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# STEP 1: READ STDIN
# 2 lines
# 1st line is number of elements, n
# 2nd line is a list of n elements separated by spaces

str_n, str_numbers = sys.stdin
# numbers will look something like [3, 7, 8, 5, 12, 14, 21, 13, 18]
n = int(str_n)
numbers = [int(x) for x in str_numbers.split(' ')]

# STEP 2: CALCULATE QUARTILES

# sort numbers
numbers.sort()


def calculate_median(sorted_list):
    """ returns the median, lower half and upper half of a sorted list """

    n_sorted = len(sorted_list)

    # calculate median
    if n_sorted % 2:
        # if n_sorted odd then median element is n // 2 + 1
        # python indexing starts at 0 so index is element - 1
        index_median = n_sorted // 2
        median = sorted_list[index_median]

        lower_half = sorted_list[:index_median]
        upper_half = sorted_list[index_median + 1:]

        # for debugging
        # print('list: {}. n:{}. median index:{}. median:{}. lower:{}. upper:{}'.format(sorted_list, n_sorted, index_median, median, lower_half, upper_half))

    else:
        # if n_sorted even then median is average elements at n // 2 and n // 2 + 1
        # python indexing starts at 0 so index is element - 1

        index_median_left = n_sorted // 2 - 1
        index_median_right = index_median_left + 1

        median_left = sorted_list[index_median_left]
        median_right = sorted_list[index_median_right]
        # we are guaranteed that median is an integer
        median = int((median_left + median_right) / 2)

        lower_half = sorted_list[:index_median_left + 1]
        upper_half = sorted_list[index_median_right:]

        # for debugging
        # print('list: {}. n:{}. index median left:{}. index median right: {} median left{}. : median right: {}. median:{}. lower:{}. upper:{}'.format(sorted_list, n_sorted, index_median_left, index_median_right, median_left, median_right, median, lower_half, upper_half))

    return median, lower_half, upper_half
