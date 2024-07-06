'''
Write a python function to remove spaces from a given string.
'''

def remove_spaces(s):
    return s.replace(" ", "")


assert remove_spaces("a b c") == "abc"
assert remove_spaces("1 2 3") == "123"
assert remove_spaces(" b c") == "bc"
