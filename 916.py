'''
Write a function to find if there is a triplet in the array whose sum is equal to a given value.
'''

def find_triplet_array(arr, n, x):
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == x:
                    return (arr[i], arr[j], arr[k])
    return None


assert find_triplet_array([1, 4, 45, 6, 10, 8], 6, 22) == (4, 10, 8)
assert find_triplet_array([12, 3, 5, 2, 6, 9], 6, 24) == (12, 3, 9)
assert find_triplet_array([1, 2, 3, 4, 5], 5, 9) == (1, 3, 5)
