'''
Write a function to sort a list of elements using pancake sort.
'''

def pancake_sort(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):
        max_index = lst.index(max(lst[:i+1]))
        lst = lst[:max_index+1][::-1] + lst[max_index+1:]
        lst = lst[:i+1][::-1] + lst[i+1:]
    return lst


assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
