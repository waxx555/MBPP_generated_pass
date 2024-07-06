'''
Write a function to locate the left insertion point for a specified value in sorted order.
'''

def left_insertion(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


assert left_insertion([1,2,4,5],6)==4
assert left_insertion([1,2,4,5],3)==2
assert left_insertion([1,2,4,5],7)==4
