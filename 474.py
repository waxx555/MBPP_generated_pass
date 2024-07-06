'''
Write a function to replace characters in a string.
'''

def replace_char(s, a, b):
    return s.replace(a,b)


assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("character",'c','a')==("aharaater")
assert replace_char("python",'l','a')==("python")
