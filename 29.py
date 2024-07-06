'''
Write a python function to find the element occurring odd number of times.
'''

def get_Odd_Occurrence(arr,n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i]==arr[j]:
                count += 1
        if count%2!=0:
            return arr[i]
    return -1




assert get_Odd_Occurrence([1,2,3,1,2,3,1],7) == 1
assert get_Odd_Occurrence([1,2,3,2,3,1,3],7) == 3
assert get_Odd_Occurrence([2,3,5,4,5,2,4,3,5,2,4,4,2],13) == 5
