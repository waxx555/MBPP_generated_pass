'''
Write a function to count the number of sublists containing a particular element.
'''

def count_element_in_list(lst,ele):
    return sum([1 for i in lst if ele in i])


assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1
