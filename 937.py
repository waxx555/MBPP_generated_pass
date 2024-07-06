'''
Write a function to count the most common character in a given string.
'''

def max_char(s):
    return max(s, key=s.count)


assert max_char("hello world")==('l')
assert max_char("hello ")==('l')
assert max_char("python pr")==('p')
