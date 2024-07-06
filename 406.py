'''
Write a python function to find the parity of a given number.
'''

def find_Parity(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return "Even Parity" if count % 2 == 0 else "Odd Parity"


assert find_Parity(12) == "Even Parity"
assert find_Parity(7) == "Odd Parity"
assert find_Parity(10) == "Even Parity"
