'''
Write a function to check if the given tuples contain the k or not.
'''

def check_K(tup, k):
    return k in tup


assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((1, 2, 3, 4, 5, 6), 7) == False
assert check_K((7, 8, 9, 44, 11, 12), 11) == True
