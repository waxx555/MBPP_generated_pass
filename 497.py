'''
Write a function to find the surface area of a cone.
'''

import math

def surfacearea_cone(r,h):
    return math.pi*r*(r+math.sqrt(r**2+h**2))


assert surfacearea_cone(5,12)==282.7433388230814
assert surfacearea_cone(10,15)==880.5179353159282
assert surfacearea_cone(19,17)==2655.923961165254
