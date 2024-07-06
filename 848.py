'''
Write a function to find the area of a trapezium.
'''

def area_trapezium(a,b,h):
    return (a+b)*h/2


assert area_trapezium(6,9,4)==30
assert area_trapezium(10,20,30)==450
assert area_trapezium(15,25,35)==700
