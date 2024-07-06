'''
Write a function to combine two given sorted lists using heapq module.
'''

import heapq

def combine_lists(l1, l2):
    return list(heapq.merge(l1, l2))


assert combine_lists([1, 3, 5, 7, 9, 11],[0, 2, 4, 6, 8, 10])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert combine_lists([1, 3, 5, 6, 8, 9], [2, 5, 7, 11])==[1,2,3,5,5,6,7,8,9,11]
assert combine_lists([1,3,7],[2,4,6])==[1,2,3,4,6,7]
