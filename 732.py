'''
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
'''

def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')


assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')
