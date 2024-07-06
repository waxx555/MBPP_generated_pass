'''
Write a function to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.
'''

def sum_difference(n):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        sum1 += i
        sum2 += i ** 2
    return sum1 ** 2 - sum2


assert sum_difference(12)==5434
assert sum_difference(20)==41230
assert sum_difference(54)==2151270
