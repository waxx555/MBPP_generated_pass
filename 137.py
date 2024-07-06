'''
Write a function to find the ration of zeroes in an array of integers.
'''

def zero_count(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return round(count/len(arr), 2)


assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.15
assert zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.00
assert zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.00
