'''
Write a python function to find the first digit in factorial of a given number.
'''

def first_Digit(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return int(str(fact)[0])


assert first_Digit(5) == 1
assert first_Digit(10) == 3
assert first_Digit(7) == 5
