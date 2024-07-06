'''
Write a python function to find the sum of common divisors of two given numbers.
'''

def sum(a, b):
    sum = 0
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            sum += i
    return sum


assert sum(10,15) == 6
assert sum(100,150) == 93
assert sum(4,6) == 3
