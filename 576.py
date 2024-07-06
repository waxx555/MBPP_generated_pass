'''
Write a python function to check whether an array is subarray of another or not.
'''

def is_Sub_Array(arr1, arr2, n, m):
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if arr1[i + j] != arr2[j]:
                break
            j += 1
        if j == m:
            return True
    return False


assert is_Sub_Array([1,4,3,5],[1,2],4,2) == False
assert is_Sub_Array([1,2,1],[1,2,1],3,3) == True
assert is_Sub_Array([1,0,2,2],[2,2,0],4,3) ==False
