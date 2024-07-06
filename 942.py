'''
Write a function to check if any list element is present in the given list.
'''

def check_element(tup, lst):
    return any(i in lst for i in tup)


assert check_element((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True
assert check_element((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True
assert check_element((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False
