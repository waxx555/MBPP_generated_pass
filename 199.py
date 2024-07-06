'''
Write a python function to find highest power of 2 less than or equal to given number.
'''

def highest_Power_of_2(n):
    res = 0
    for i in range(0,n):
        if 2**i <= n:
            res = 2**i
    return res


assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32
