'''
Write a python function to capitalize first and last letters of each word of a given string.
'''

def capitalize_first_last_letters(s):
    return ' '.join([i[:-1].capitalize() + i[-1].upper() for i in s.split()])


assert capitalize_first_last_letters("python") == "PythoN"
assert capitalize_first_last_letters("bigdata") == "BigdatA"
assert capitalize_first_last_letters("Hadoop") == "HadooP"
