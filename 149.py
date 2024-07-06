'''
Write a function to find the longest subsequence such that the difference between adjacents is one for the given array.
'''

def longest_subseq_with_diff_one(arr, n):
    dp = [0]*n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if (abs(arr[i]-arr[j]) == 1):
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7
