'''
Write a function to find sum and average of first n natural numbers.
'''

def sum_average(n):
    return n*(n+1)//2, (n+1)/2


assert sum_average(10)==(55, 5.5)
assert sum_average(15)==(120, 8.0)
assert sum_average(20)==(210, 10.5)
