'''
Write a function to calculate the area of a regular polygon.
'''

import math

def area_polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi/n))


assert area_polygon(4,20)==400.00000000000006
assert area_polygon(10,15)==1731.1969896610804
assert area_polygon(9,7)==302.90938549487214
