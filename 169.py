'''
Write a function to calculate the nth pell number.
'''

def get_pell(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * get_pell(n-1) + get_pell(n-2)


assert get_pell(4) == 12
assert get_pell(7) == 169
assert get_pell(8) == 408
