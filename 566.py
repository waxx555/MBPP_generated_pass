'''
Write a function to get the sum of a non-negative integer.
'''

def sum_digits(n):
    return sum(int(digit) for digit in str(n))


assert sum_digits(345)==12
assert sum_digits(12)==3
assert sum_digits(97)==16
