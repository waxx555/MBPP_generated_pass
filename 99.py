'''
Write a function to convert the given decimal number to its binary equivalent.
'''

def decimal_to_binary(n):
    return bin(n)[2:]


assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(18) == '10010'
assert decimal_to_binary(7) == '111' 
