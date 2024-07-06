'''
Write a python function to count the number of digits in factorial of a given number.
'''

import math
def find_Digits(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    digits = 0
    for i in range(2, n+1):
        digits += math.log10(i)
    return math.floor(digits) + 1


assert find_Digits(7) == 4
assert find_Digits(5) == 3
assert find_Digits(4) == 2
