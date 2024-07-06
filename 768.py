'''
Write a python function to check for odd parity of a given number.
'''

def check_Odd_Parity(n):
    return bin(n).count('1') % 2 != 0


assert check_Odd_Parity(13) == True
assert check_Odd_Parity(21) == True
assert check_Odd_Parity(18) == False
