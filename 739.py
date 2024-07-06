'''
Write a python function to find the index of smallest triangular number with n digits.
'''

def find_Index(n):
    index = 1
    triangular = 1
    while True:
        if len(str(triangular)) == n:
            return index
        index += 1
        triangular += index
        

assert find_Index(2) == 4
assert find_Index(3) == 14
assert find_Index(4) == 45
