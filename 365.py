'''
Write a python function to count the number of digits of a given number.
'''

def count_Digit(n):
    return len(str(n))


assert count_Digit(12345) == 5
assert count_Digit(11223305) == 8
assert count_Digit(4123459) == 7
