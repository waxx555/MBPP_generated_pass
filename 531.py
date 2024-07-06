'''
Write a function to find minimum number of coins that make a given value.
'''

def min_coins(coins,n,value):
    if value == 0:
        return 0
    res = float('inf')
    for i in range(n):
        if coins[i] <= value:
            sub_res = min_coins(coins,n,value-coins[i])
            if sub_res != float('inf') and sub_res + 1 < res:
                res = sub_res + 1
    return res


assert min_coins([9, 6, 5, 1] ,4,11)==2
assert min_coins([4,5,6,7,8,9],6,9)==1
assert min_coins([1, 2, 3],3,4)==2
