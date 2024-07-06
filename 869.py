'''
Write a function to remove sublists from a given list of lists, which are outside a given range.
'''

def remove_list_range(lst, start, end):
    return [i for i in lst if i[0]>=start and i[-1]<=end]


assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]
