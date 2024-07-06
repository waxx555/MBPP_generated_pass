'''
Write a python function to find the last two digits in factorial of a given number.
'''

def last_Two_Digits(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact % 100


assert last_Two_Digits(7) == 40
assert last_Two_Digits(5) == 20
assert last_Two_Digits(2) == 2
