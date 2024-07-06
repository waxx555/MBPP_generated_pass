'''
Write a python function to check whether all the characters in a given string are unique.
'''

def unique_Characters(s):
    return len(set(s)) == len(s)


assert unique_Characters('aba') == False
assert unique_Characters('abc') == True
assert unique_Characters('abab') == False
