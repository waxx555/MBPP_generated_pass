'''
Write a function to access dictionary key’s element by index.
'''

def access_key(dict, index):
    return list(dict.keys())[index]


assert access_key({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'
assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'
assert access_key({'program':15,'computer':45},1)== 'computer'
