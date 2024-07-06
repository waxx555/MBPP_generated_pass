'''
Write a python function to find the maximum occurring character in a given string.
'''

def get_max_occuring_char(s):
    return max(s,key=s.count)


assert get_max_occuring_char("data") == "a"
assert get_max_occuring_char("create") == "e"
assert get_max_occuring_char("brilliant girl") == "i"
