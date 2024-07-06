'''
Write a function to find the triplet with sum of the given array
'''

def check_triplet(arr, n, x, y):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == x:
                    return True
                if arr[i] + arr[j] + arr[k] == y:
                    return True
    return False


assert check_triplet([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True
assert check_triplet([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0) == False
assert check_triplet([10, 4, 2, 3, 5], 5, 15, 0) == True
