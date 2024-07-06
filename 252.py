'''
Write a python function to convert complex numbers to polar coordinates.
'''

import cmath

def convert(n):
    return cmath.polar(n)


assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0)
