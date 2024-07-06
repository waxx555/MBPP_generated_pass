'''
Write a function to find the smallest integers from a given list of numbers using heap queue algorithm.
'''

import heapq

def heap_queue_smallest(arr, k):
    return heapq.nsmallest(k, arr)


assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],3)==[14, 22, 25] 
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],2)==[14, 22]
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[14, 22, 22, 25, 35]
