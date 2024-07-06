'''
Write a function to extract only the rear index element of each string in the given tuple.
'''

def extract_rear(t):
    return [i[-1] for i in t]


assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']
