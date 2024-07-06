'''
Write a function to push all values into a heap and then pop off the smallest values one at a time.
'''

def heap_sort(lst):
    import heapq
    heapq.heapify(lst)
    return [heapq.heappop(lst) for i in range(len(lst))]


assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]