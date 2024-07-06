'''
Write a function to add two numbers and print number of digits of sum.
'''

def count_digits(a,b):
    return len(str(a+b))


assert count_digits(9875,10)==(4)
assert count_digits(98759853034,100)==(11)
assert count_digits(1234567,500)==(7)
