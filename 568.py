'''
Write a function to create a list of empty dictionaries.
'''

def empty_list(n):
    return [{} for i in range(n)]


assert empty_list(5)==[{},{},{},{},{}]
assert empty_list(6)==[{},{},{},{},{},{}]
assert empty_list(7)==[{},{},{},{},{},{},{}]
