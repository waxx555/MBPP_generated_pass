'''
Write a function to find a path with the maximum average over all existing paths for the given square matrix of size n*n.
'''

def maxAverageOfPath(matrix, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[n-1][n-1] / (2 * n - 1)


assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3) == 5.2
assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]], 3) == 6.2
assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]], 3) == 7.2 
