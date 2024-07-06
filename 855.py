'''
Write a python function to check for even parity of a given number.
'''

def check_Even_Parity(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count % 2 == 0


assert check_Even_Parity(10) == True
assert check_Even_Parity(11) == False
assert check_Even_Parity(18) == True
