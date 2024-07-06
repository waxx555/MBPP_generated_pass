'''
Write a function to find the length of the shortest string that has both str1 and str2 as subsequences.
'''

def super_seq(str1, str2, m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


assert super_seq("AGGTAB", "GXTXAYB", 6, 7) == 9
assert super_seq("feek", "eke", 4, 3) == 5
assert super_seq("PARRT", "RTA", 5, 3) == 6
