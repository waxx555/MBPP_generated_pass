'''
Write a python function to check whether the given number is even or not using bitwise operator.
'''

def is_Even(n):
    return n & 1 == 0


assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(3) == False
