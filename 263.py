'''
Write a function to merge two dictionaries.
'''

def merge_dict(dict1, dict2):
    return {**dict2, **dict1}


assert merge_dict({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}
assert merge_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}
assert merge_dict({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}
