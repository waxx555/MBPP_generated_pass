'''
Write a function to check if two lists of tuples are identical or not.
'''

def check_identical(tup1, tup2):
    return tup1 == tup2


assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True
assert check_identical([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False
assert check_identical([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True
