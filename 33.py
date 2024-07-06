'''
Write a python function to convert a decimal number to binary number.
'''

def decimal_To_Binary(n):
    return int(bin(n).replace("0b", ""))




assert decimal_To_Binary(10) == 1010
assert decimal_To_Binary(1) == 1
assert decimal_To_Binary(20) == 10100
