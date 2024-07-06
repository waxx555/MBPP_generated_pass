'''
Write a function to find the nested list elements which are present in another list.
'''

def intersection_nested_lists(lst1, lst2):
    return [[i for i in lst if i in lst1] for lst in lst2]



assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]
assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]])==[[], []]
assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]
