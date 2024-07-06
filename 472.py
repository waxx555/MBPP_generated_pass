'''
Write a python function to check whether the given list contains consecutive numbers or not.
'''

def check_Consecutive(arr):
    return sorted(arr) == list(range(min(arr),max(arr)+1))


assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5,6]) == False
assert check_Consecutive([1,2,1]) == False
