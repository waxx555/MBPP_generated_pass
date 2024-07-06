'''
Write a function to remove even characters in a string.
'''

def remove_even(s):
    return s[::2]


assert remove_even("python")==("pto")
assert remove_even("program")==("porm")
assert remove_even("language")==("lnug")
