# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

sum_weight_x = sum([number * weight for number, weight in zip(numbers, weights)])
sum_weights = sum(weights)
weighted_sum = sum_weight_x / sum_weights

print('{:.1f}'.format(weighted_sum))
