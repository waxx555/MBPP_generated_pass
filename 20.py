'''
Write a function to check if the given number is woodball or not.
'''
def is_woodall(n):
    i = 1
    while True:
        woodall = i * 2 ** i - 1
        if woodall == n:
            return True
        elif woodall > n:
            return False
        i += 1

        


assert is_woodall(383) == True
assert is_woodall(254) == False
assert is_woodall(200) == False
