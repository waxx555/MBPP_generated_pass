'''
Write a function to find the largest possible value of k such that k modulo x is y.
'''

def find_max_val(k, x, y):
    while k % x != y:
        k -= 1
    return k


assert find_max_val(15, 10, 5) == 15
assert find_max_val(187, 10, 5) == 185
assert find_max_val(16, 11, 1) == 12
