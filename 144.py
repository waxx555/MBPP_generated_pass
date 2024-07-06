'''
Write a python function to find the sum of absolute differences in all pairs of the given array.
'''

def sum_Pairs(arr, n):
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum += abs(arr[i]-arr[j])
    return sum


assert sum_Pairs([1,8,9,15,16],5) == 74
assert sum_Pairs([1,2,3,4],4) == 10
assert sum_Pairs([1,2,3,4,5,7,9,11,14],9) == 188
