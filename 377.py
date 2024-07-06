'''
Write a python function to remove all occurrences of a character in a given string.
'''

def remove_Char(s,c):
    return s.replace(c,"")


assert remove_Char("aba",'a') == "b"
assert remove_Char("toggle",'g') == "tole"
assert remove_Char("aabbc",'b') == "aac"
