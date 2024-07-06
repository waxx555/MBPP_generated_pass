'''
Write a python function to check whether the frequency of each digit is less than or equal to the digit itself.
'''

def validate(n):
    for i in str(n):
        if str(n).count(i) > int(i):
            return False
    return True


assert validate(1234) == True
assert validate(51241) == False
assert validate(321) == True
