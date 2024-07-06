'''
Write a function to check if a nested list is a subset of another nested list.
'''

def check_subset(lst1, lst2):
    for i in lst2:
        if i not in lst1:
            return False
    return True


assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False
