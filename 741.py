'''
Write a python function to check whether all the characters are same or not.
'''

def all_Characters_Same(s):
    return len(set(s)) == 1


assert all_Characters_Same("python") == False
assert all_Characters_Same("aaa") == True
assert all_Characters_Same("data") == False
