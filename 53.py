'''
Write a python function to check whether the first and last characters of a given string are equal or not.
'''

def check_Equality(string):
    return "Equal" if string[0] == string[-1] else "Not Equal"


assert check_Equality("abcda") == "Equal"
assert check_Equality("ab") == "Not Equal"
assert check_Equality("mad") == "Not Equal"
