'''
Write a function to drop empty items from a given dictionary.
'''

def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}


assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}
