'''
Write a python function to count numeric values in a given string.
'''

def number_ctr(s):
    return len(list(filter(lambda x: x.isdigit(), s)))

assert number_ctr('program2bedone') == 1
assert number_ctr('3wonders') ==1
assert number_ctr('123') == 3
