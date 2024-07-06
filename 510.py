'''
Write a function to find the number of subsequences having product smaller than k for the given non negative array.
'''

def no_of_subsequences(arr, k):
    n = len(arr)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j and arr[i-1] > 0:
                dp[i][j] += 1 + dp[i-1][j//arr[i-1]]
    return dp[n][k]


assert no_of_subsequences([1,2,3,4], 10) == 11
assert no_of_subsequences([4,8,7,2], 50) == 9
assert no_of_subsequences([5,6,7,8], 15) == 4
