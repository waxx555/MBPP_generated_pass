'''
Write a python function to find the sum of squares of binomial co-efficients.
'''
def nCr(n, r):
    if r == 0:
        return 1
    if r > n:
        return 0
    return nCr(n-1, r-1) + nCr(n-1, r)

def sum_of_square(n):
    res = 0
    for i in range(n+1):
        res += (nCr(n, i))**2
    return res


assert sum_of_square(4) == 70
assert sum_of_square(5) == 252
assert sum_of_square(2) == 6
