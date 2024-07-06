'''
Write a function to find the maximum sum of bi-tonic sub-sequence for the given array.
'''

def max_sum(arr, n):
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]
    for i in range(1, n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + arr[i])
    for i in range(n-2, -1, -1):
        dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + arr[i])
    max_sum = inc[0] + dec[0] - arr[0]
    for i in range(1, n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])
    return max_sum


assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
assert max_sum([80, 60, 30, 40, 20, 10], 6) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138
