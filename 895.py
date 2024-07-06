'''
Write a function to find the maximum sum of subsequences of given array with no adjacent elements.
'''

def max_sum_subseq(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    return dp[-1]


assert max_sum_subseq([1, 2, 9, 4, 5, 0, 4, 11, 6]) == 26
assert max_sum_subseq([1, 2, 9, 5, 6, 0, 5, 12, 7]) == 28
assert max_sum_subseq([1, 3, 10, 5, 6, 0, 6, 14, 21]) == 44
