'''
Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].
'''

def min_cost(cost, m, n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(min_cost(cost, m-1, n-1), min_cost(cost, m-1, n), min_cost(cost, m, n-1))
    


assert min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8
assert min_cost([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12
assert min_cost([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16
