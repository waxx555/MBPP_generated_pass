'''
Write a function to find the ration of negative numbers in an array of integers.
'''

def negative_count(arr):
    return round(len([i for i in arr if i < 0])/len(arr), 2)


assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.31
assert negative_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.31
assert negative_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.44
