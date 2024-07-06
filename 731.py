'''
Write a function to find the lateral surface area of a cone.
'''

import math

def lateralsurface_cone(r,h):
    return math.pi*r*math.sqrt(r**2+h**2)


assert lateralsurface_cone(5,12)==204.20352248333654
assert lateralsurface_cone(10,15)==566.3586699569488
assert lateralsurface_cone(19,17)==1521.8090132193388
