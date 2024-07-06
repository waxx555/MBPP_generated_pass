'''
Write a python function to check if a given number is one less than twice its reverse.
'''

def check(n):
    return n == 2 * int(str(n)[::-1]) - 1


assert check(70) == False
assert check(23) == False
assert check(73) == True
