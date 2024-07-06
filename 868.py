'''
Write a python function to find the length of the last word in a given string.
'''

def length_Of_Last_Word(s):
    if s == "":
        return 0
    else:
        return len(s.split()[-1])
    

assert length_Of_Last_Word("python language") == 8
assert length_Of_Last_Word("PHP") == 3
assert length_Of_Last_Word("") == 0
