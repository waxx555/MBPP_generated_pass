'''
Write a function to find the length of the longest increasing subsequence of the given sequence.
'''

def longest_increasing_subsequence(lst):
    n = len(lst)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
assert longest_increasing_subsequence([3, 10, 2, 1, 20]) == 3
assert longest_increasing_subsequence([50, 3, 10, 7, 40, 80]) == 4 
