'''
Write a function to sort the given array by using counting sort.
'''

def counting_sort(arr):
    max_num = max(arr)
    count = [0] * (max_num + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i in range(len(count)):
        result += [i] * count[i]
    return result


assert counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
assert counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
assert counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]
