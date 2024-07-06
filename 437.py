'''
Write a function to remove odd characters in a string.
'''

def remove_odd(s):
    return s[1::2]


assert remove_odd("python")==("yhn")
assert remove_odd("program")==("rga")
assert remove_odd("language")==("agae")
