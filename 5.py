'''
Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board.
'''

def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]
    return dp[n]


assert count_ways(2) == 3
assert count_ways(8) == 153
assert count_ways(12) == 2131
