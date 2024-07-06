'''
Write a python function to check whether the given string is made up of two alternating characters or not.
'''

def is_Two_Alter(s):
    return len(set(s)) == 2


assert is_Two_Alter("abab") == True
assert is_Two_Alter("aaaa") == False
assert is_Two_Alter("xyz") == False
