'''
Write a function to add the k elements to each element in the tuple.
'''

def add_K_element(t, k):
    return [(i[0]+k, i[1]+k, i[2]+k) for i in t]


assert add_K_element([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
assert add_K_element([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8) == [(9, 10, 11), (12, 13, 14), (15, 16, 17)]
assert add_K_element([(11, 12, 13), (14, 15, 16), (17, 18, 19)], 9) == [(20, 21, 22), (23, 24, 25), (26, 27, 28)]
