'''
Write a function to calculate the sum of series 1³+2³+3³+….+n³.
'''

def sum_series(n):
    return (n*(n+1)//2)**2


assert sum_series(7)==784
assert sum_series(5)==225
assert sum_series(15)==14400
