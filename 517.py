'''
Write a python function to find the largest postive number from the given list.
'''

def largest_pos(arr):
    return max([i for i in arr if i > 0])


assert largest_pos([1,2,3,4,-1]) == 4
assert largest_pos([0,1,2,-5,-1,6]) == 6
assert largest_pos([0,0,1,0]) == 1
