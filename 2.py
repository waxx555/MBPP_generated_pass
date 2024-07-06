'''
Write a function to find the similar elements from the given two tuple lists.
'''

def similar_elements(t1, t2):
    return tuple(sorted(set(t1) & set(t2)))



assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
assert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
assert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)
