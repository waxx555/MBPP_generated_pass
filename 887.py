'''
Write a python function to check whether the given number is odd or not using bitwise operator.
'''

def is_odd(n):
    return n & 1


assert is_odd(5) == True
assert is_odd(6) == False
assert is_odd(7) == True
