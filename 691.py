'''
Write a function to group the 1st elements on the basis of 2nd elements in the given tuple list.
'''

def group_element(t):
    d = {}
    for i in t:
        if i[1] in d:
            d[i[1]].append(i[0])
        else:
            d[i[1]] = [i[0]]
    return d


assert group_element([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}
assert group_element([(7, 6), (3, 8), (3, 6), (9, 8), (10, 9), (4, 8)]) == {6: [7, 3], 8: [3, 9, 4], 9: [10]}
assert group_element([(8, 7), (4, 9), (4, 7), (10, 9), (11, 10), (5, 9)]) == {7: [8, 4], 9: [4, 10, 5], 10: [11]}
