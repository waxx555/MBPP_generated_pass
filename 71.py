'''
Write a function to sort a list of elements using comb sort.
'''

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap/shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr


assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]
