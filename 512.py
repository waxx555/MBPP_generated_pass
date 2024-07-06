'''
Write a function to count the element frequency in the mixed nested tuple.
'''

def count_element_freq(t):
    d = {}
    for i in t:
        if isinstance(i, tuple):
            for j in i:
                d[j] = d.get(j, 0) + 1
        else:
            d[i] = d.get(i, 0) + 1
    return d


assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
assert count_element_freq((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}
assert count_element_freq((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}
