'''
Write a function to remove all elements from a given list present in another list.
'''

def remove_elements(arr1,arr2):
    return [i for i in arr1 if i not in arr2]


assert remove_elements([1,2,3,4,5,6,7,8,9,10],[2,4,6,8])==[1, 3, 5, 7, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7])==[2, 4, 6, 8, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7])==[1, 2, 3, 4, 6, 8, 9, 10]
