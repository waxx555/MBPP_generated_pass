'''
Write a function to find three closest elements from three sorted arrays.
'''

def find_closet(arr1, arr2, arr3, n1, n2, n3):
    i, j, k = 0, 0, 0
    diff = float('inf')
    res = ()
    while i < n1 and j < n2 and k < n3:
        minimum = min(arr1[i], arr2[j], arr3[k])
        maximum = max(arr1[i], arr2[j], arr3[k])
        if maximum - minimum < diff:
            diff = maximum - minimum
            res = (arr1[i], arr2[j], arr3[k])
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1
    return res


assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)
assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)
assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)
