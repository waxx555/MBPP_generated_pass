'''
Write a python function to find the cube sum of first n natural numbers.
'''

def sum_Of_Series(n):
    return (n*(n+1)/2)**2


assert sum_Of_Series(5) == 225
assert sum_Of_Series(2) == 9
assert sum_Of_Series(3) == 36
