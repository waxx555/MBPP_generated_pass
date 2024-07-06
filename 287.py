'''
Write a python function to find the sum of squares of first n even natural numbers.
'''

def square_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (2 * i) ** 2
    return sum


assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 120
