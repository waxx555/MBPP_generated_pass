'''
Write a function to caluclate the area of a tetrahedron.
'''

import math

def area_tetrahedron(a):
    return math.sqrt(3) * a ** 2


assert area_tetrahedron(3)==15.588457268119894
assert area_tetrahedron(20)==692.8203230275509
assert area_tetrahedron(10)==173.20508075688772
