'''
Write a function to check whether the given number is undulating or not.
'''

def is_undulating(n):
    n = str(n)
    if len(n) < 3:
        return False
    for i in range(1, len(n)-1):
        if n[i] == n[i-1] or n[i] == n[i+1]:
            return False
    return True


assert is_undulating("1212121") == True
assert is_undulating("1991") == False
assert is_undulating("121") == True
