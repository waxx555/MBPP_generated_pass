'''
Write a function to zip the two given tuples.
'''

def zip_tuples(t1, t2):
    return [(t1[i], t2[i%len(t2)]) for i in range(len(t1))]


assert zip_tuples((7, 8, 4, 5, 9, 10),(1, 5, 6) ) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
assert zip_tuples((8, 9, 5, 6, 10, 11),(2, 6, 7) ) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
assert zip_tuples((9, 10, 6, 7, 11, 12),(3, 7, 8) ) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]
