'''
Write a function to find the smallest missing element in a sorted array.
'''

def smallest_missing(arr, start, end):
    if start > end:
        return end + 1
    if start != arr[start]:
        return start
    mid = (start + end) // 2
    if arr[mid] == mid:
        return smallest_missing(arr, mid + 1, end)
    return smallest_missing(arr, start, mid)


assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
assert smallest_missing([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
assert smallest_missing([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0
