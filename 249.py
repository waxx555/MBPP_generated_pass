'''
Write a function to find the intersection of two arrays using lambda function.
'''

def intersection_array(arr1, arr2):
    return list(filter(lambda x: x in arr1, arr2))


assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]
