'''
Write a function to find common elements in given nested lists. * list item * list item * list item * list item
'''

def common_in_nested_lists(lst):
    return list(set.intersection(*map(set,lst)))
                

assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])==[18, 12]
assert common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])==[5,23]
assert common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]])==[4]
