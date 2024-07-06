'''
Write a python function to split the array and add the first part to the end.
'''

def split_Arr(arr, n, k):
    return arr[k:] + arr[:k]


assert split_Arr([12,10,5,6,52,36],6,2) == [5,6,52,36,12,10]
assert split_Arr([1,2,3,4],4,1) == [2,3,4,1]
assert split_Arr([0,1,2,3,4,5,6,7],8,3) == [3,4,5,6,7,0,1,2]
