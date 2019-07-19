from itertools import product

die_outcomes = [roll + 1 for roll in range(6)]

sum_six_and_diff = ([1 if (((d1 + d2) == 6) and (d1 != d2)) else 0 for d1, d2 in product(die_outcomes, die_outcomes)])
print(sum(sum_six_and_diff))
print(len(sum_six_and_diff))
# Answer is 4/6
