'''
Write a function to check if one tuple is a subset of another tuple.
'''

def check_subset(t1, t2):
    return all(x in t1 for x in t2)


assert check_subset((10, 4, 5, 6), (5, 10)) == True
assert check_subset((1, 2, 3, 4), (5, 6)) == False
assert check_subset((7, 8, 9, 10), (10, 8)) == True
