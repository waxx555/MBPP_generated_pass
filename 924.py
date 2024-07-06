'''
Write a function to find maximum of two numbers.
'''

def max_of_two(a,b):
    if a>b:
        return a
    return b


assert max_of_two(10,20)==20
assert max_of_two(19,15)==19
assert max_of_two(-10,-20)==-10
