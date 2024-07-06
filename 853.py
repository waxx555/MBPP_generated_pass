'''
Write a python function to find sum of odd factors of a number.
'''

def sum_of_odd_Factors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            sum += i
    return sum


assert sum_of_odd_Factors(30) == 24
assert sum_of_odd_Factors(18) == 13
assert sum_of_odd_Factors(2) == 1
