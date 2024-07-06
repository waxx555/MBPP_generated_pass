'''
Write a function to count coin change.
'''

def coin_change(coins, m, n):
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(coins[i],n+1):
            table[j] += table[j-coins[i]]
    return table[n]


assert coin_change([1, 2, 3],3,4)==4
assert coin_change([4,5,6,7,8,9],6,9)==2
assert coin_change([4,5,6,7,8,9],6,4)==1
