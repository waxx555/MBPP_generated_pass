'''
Write a function to solve gold mine problem.
'''

def get_maxgold(gold,m,n):
    dp = [[0 for i in range(m)] for j in range(n)]
    for col in range(m-1,-1,-1):
        for row in range(n):
            right = 0 if col==m-1 else dp[row][col+1]
            right_up = 0 if col==m-1 or row==0 else dp[row-1][col+1]
            right_down = 0 if col==m-1 or row==n-1 else dp[row+1][col+1]
            dp[row][col] = gold[row][col] + max(right,right_up,right_down)
    res = dp[0][0]
    for i in range(1,n):
        res = max(res,dp[i][0])
    return res


assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16
assert get_maxgold([[10,20],[30,40]],2,2)==70
assert get_maxgold([[4,9],[3,7]],2,2)==13
