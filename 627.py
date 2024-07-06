'''
Write a python function to find the smallest missing number from the given array.
'''

def find_First_Missing(arr, start, end):
    if start > end:
        return end + 1
    if start != arr[start]:
        return start
    mid = int((start + end) / 2)
    if arr[mid] > mid:
        return find_First_Missing(arr, start, mid)
    return find_First_Missing(arr, mid+1, end)


assert find_First_Missing([0,1,2,3],0,3) == 4
assert find_First_Missing([0,1,2,6,9],0,4) == 3
assert find_First_Missing([2,3,5,8,9],0,4) == 0
