from itertools import product

die_outcomes = [roll + 1 for roll in range(6)]

at_most_nine = ([1 if ((d1 + d2) <= 9) else 0 for d1, d2 in product(die_outcomes, die_outcomes)])
print(sum(at_most_nine))
print(len(at_most_nine))
# Answer is 30/36 or 5/6
