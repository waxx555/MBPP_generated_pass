'''
Write a function to find the longest common subsequence for the given two sequences.
'''

def longest_common_subsequence(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m-1] == s2[n-1]:
        return 1 + longest_common_subsequence(s1, s2, m-1, n-1)
    else:
        return max(longest_common_subsequence(s1, s2, m, n-1), longest_common_subsequence(s1, s2, m-1, n))
    


assert longest_common_subsequence("AGGTAB" , "GXTXAYB", 6, 7) == 4
assert longest_common_subsequence("ABCDGH" , "AEDFHR", 6, 6) == 3
assert longest_common_subsequence("AXYT" , "AYZX", 4, 4) == 2
