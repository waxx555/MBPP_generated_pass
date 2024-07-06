'''
Write a python function to find the last digit in factorial of a given number.
'''

def last_Digit_Factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num % 10


assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(21) == 0
assert last_Digit_Factorial(30) == 0
