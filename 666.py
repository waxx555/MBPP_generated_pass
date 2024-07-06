'''
Write a function to count occurrence of a character in a string.
'''

def count_char(s, c):
    return s.count(c)


assert count_char("Python",'o')==1
assert count_char("little",'t')==2
assert count_char("assert",'s')==2
