'''
Write a python function to count equal element pairs from the given array.
'''

def count_Pairs(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1
    return count


assert count_Pairs([1,1,1,1],4) == 6
assert count_Pairs([1,5,1],3) == 1
assert count_Pairs([3,2,1,7,8,9],6) == 0
