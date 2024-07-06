'''
Write a python function to convert octal number to decimal number.
'''

def octal_To_Decimal(n):
    return int(str(n),8)


assert octal_To_Decimal(25) == 21
assert octal_To_Decimal(30) == 24
assert octal_To_Decimal(40) == 32
