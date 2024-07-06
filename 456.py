'''
Write a function to reverse strings in a given list of string values.
'''

def reverse_string_list(lst):
    return [i[::-1] for i in lst]


assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']
