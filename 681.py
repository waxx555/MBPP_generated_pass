'''
Write a python function to find the smallest prime divisor of a number.
'''

def smallest_Divisor(n):
    if n == 1:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


assert smallest_Divisor(10) == 2
assert smallest_Divisor(25) == 5
assert smallest_Divisor(31) == 31
