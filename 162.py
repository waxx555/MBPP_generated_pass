'''
Write a function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
'''

def sum_series(n):
    return sum(range(n,0,-2))


assert sum_series(6)==12
assert sum_series(10)==30
assert sum_series(9)==25
