'''
Write a function to find the largest subset where each pair is divisible.
'''

def largest_subset(arr, n):
    arr.sort()
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


assert largest_subset([ 1, 3, 6, 13, 17, 18 ], 6) == 4
assert largest_subset([10, 5, 3, 15, 20], 5) == 3
assert largest_subset([18, 1, 3, 6, 13, 17], 6) == 4
