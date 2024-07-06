'''
Write a function to find all pairs in an integer array whose sum is equal to a given number.
'''

def get_pairs_count(arr, n, k):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                count += 1
    return count


assert get_pairs_count([1, 5, 7, -1, 5], 5, 6) == 3
assert get_pairs_count([1, 5, 7, -1], 4, 6) == 2
assert get_pairs_count([1, 1, 1, 1], 4, 2) == 6
