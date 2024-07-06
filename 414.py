'''
Write a python function to check whether the value exists in a sequence or not.
'''

def overlapping(arr1,arr2):
    return len(set(arr1).intersection(arr2)) > 0


assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3],[4,5,6]) == False
assert overlapping([1,4,5],[1,4,5]) == True
