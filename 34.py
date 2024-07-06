'''
Write a python function to find the missing number in a sorted array.
'''

def find_missing(arr,n):
    for i in range(n-1):
        if arr[i+1]-arr[i]!=1:
            return arr[i]+1
    return -1




assert find_missing([1,2,3,5],4) == 4
assert find_missing([1,3,4,5],4) == 2
assert find_missing([1,2,3,5,6,7],5) == 4
