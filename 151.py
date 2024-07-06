'''
Write a python function to check whether the given number is co-prime or not.
'''

def is_coprime(a,b):
    for i in range(2,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            return False
    return True


assert is_coprime(17,13) == True
assert is_coprime(15,21) == False
assert is_coprime(25,45) == False
