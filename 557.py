'''
Write a function to toggle characters case in a string.
'''

def toggle_string(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])


assert toggle_string("Python")==("pYTHON")
assert toggle_string("Pangram")==("pANGRAM")
assert toggle_string("LIttLE")==("liTTle")
