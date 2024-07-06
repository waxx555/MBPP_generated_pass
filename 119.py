'''
Write a python function to find the element that appears only once in a sorted array.
'''

def search(arr,n):
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] if arr[0] != arr[1] else arr[1]
    left = 0
    right = n-1
    while left <= right:
        mid = left + (right - left) // 2
        if mid == 0 and arr[mid] != arr[mid+1]:
            return arr[mid]
        if mid == n-1 and arr[mid] != arr[mid-1]:
            return arr[mid]
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] == arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


assert search([1,1,2,2,3],5) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
assert search([1,2,2,3,3,4,4],7) == 1
