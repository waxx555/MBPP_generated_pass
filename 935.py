'''
Write a function to calculate the sum of series 1²+2²+3²+….+n².
'''

def series_sum(n):
    return n*(n+1)*(2*n+1)//6


assert series_sum(6)==91
assert series_sum(7)==140
assert series_sum(12)==650
