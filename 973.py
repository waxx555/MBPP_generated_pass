'''
Write a python function to left rotate the string.
'''

def left_rotate(s,n):
    return s[n:] + s[:n]


assert left_rotate("python",2) == "thonpy"   
assert left_rotate("bigdata",3 ) == "databig" 
assert left_rotate("hadoop",1 ) == "adooph" 
