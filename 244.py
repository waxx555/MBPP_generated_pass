'''
Write a python function to find the next perfect square greater than a given number.
'''

def next_Perfect_Square(n):
    i = 1
    while True:
        if i*i > n:
            return i*i
        i += 1
        

assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16
