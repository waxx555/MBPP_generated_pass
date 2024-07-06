'''
Write a function to find the longest bitonic subsequence for the given array.
'''

def lbs(arr):
    n = len(arr)
    lis = [1 for _ in range(n)]
    lds = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    max_val = lis[0] + lds[0] - 1
    for i in range(1, n):
        max_val = max(max_val, lis[i] + lds[i] - 1)
    return max_val


assert lbs([0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]) == 7
assert lbs([1, 11, 2, 10, 4, 5, 2, 1]) == 6
assert lbs([80, 60, 30, 40, 20, 10]) == 5
