'''
Write a python function to find the sum of xor of all pairs of numbers in the given array.
'''

def pair_OR_Sum(lst, n):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res += lst[i] ^ lst[j]
    return res


assert pair_OR_Sum([5,9,7,6],4) == 47
assert pair_OR_Sum([7,3,5],3) == 12
assert pair_OR_Sum([7,3],2) == 4
