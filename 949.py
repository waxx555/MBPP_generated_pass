'''
Write a function to sort the given tuple list basis the total digits in tuple.
'''

def sort_list(tup):
    return str(sorted(tup, key=lambda x: sum(map(lambda y: len(str(y)), x))))

assert sort_list([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)] ) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'
assert sort_list([(3, 4, 8), (1, 2), (1234335,), (1345, 234, 334)] ) == '[(1, 2), (3, 4, 8), (1234335,), (1345, 234, 334)]'
assert sort_list([(34, 4, 61, 723), (1, 2), (145,), (134, 23)] ) == '[(1, 2), (145,), (134, 23), (34, 4, 61, 723)]'
