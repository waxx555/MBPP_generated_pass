'''
Write a function to find the longest chain which can be formed from the given set of pairs.
'''

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def max_chain_length(arr, n):
    arr.sort(key=lambda x: x.b)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i].a > arr[j].b:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


assert max_chain_length([Pair(5, 24), Pair(15, 25),Pair(27, 40), Pair(50, 60)], 4) == 3
assert max_chain_length([Pair(1, 2), Pair(3, 4),Pair(5, 6), Pair(7, 8)], 4) == 4
assert max_chain_length([Pair(19, 10), Pair(11, 12),Pair(13, 14), Pair(15, 16), Pair(31, 54)], 5) == 5
