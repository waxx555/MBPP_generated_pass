'''
Write a python function to count inversions in an array.
'''

def get_Inv_Count(arr,n):
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                result += 1
    return result


assert get_Inv_Count([1,20,6,4,5],5) == 5
assert get_Inv_Count([1,2,1],3) == 1
assert get_Inv_Count([1,2,5,6,1],5) == 3
