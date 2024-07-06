'''
Write a function to calculate the number of digits and letters in a string.
'''

def dig_let(s):
    d=l=0
    for i in s:
        if i.isdigit():
            d+=1
        elif i.isalpha():
            l+=1
    return l,d


assert dig_let("python")==(6,0)
assert dig_let("program")==(7,0)
assert dig_let("python3.0")==(6,2)
