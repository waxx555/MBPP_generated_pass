'''
Write a python function to find the difference between highest and least frequencies in a given array.
'''

def find_Diff(arr, n):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return max(freq.values()) - min(freq.values())


assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2
assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3
assert find_Diff([1,2,1,2],4) == 0
